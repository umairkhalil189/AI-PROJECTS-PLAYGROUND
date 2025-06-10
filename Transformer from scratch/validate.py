import torch 
import torch.nn as nn

from torch.utils.data import Dataset, DataLoader, random_split

from dataset import BilingualDataset, causal_mask
from model import build_transformer

from config import get_weights_file_path, get_config

from datasets import load_dataset
from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
from tokenizers.pre_tokenizers import Whitespace

from torch.utils.tensorboard import SummaryWriter
import warnings

from tqdm import tqdm

from pathlib import Path

def greedy_decode(model, source, source_mask, tokenizer_src, tokenizer_tgt, max_len, device):
    sos_idx = tokenizer_tgt.token_to_id('[SOS]')
    eos_idx = tokenizer_tgt.token_to_id('[EOS]')

    #Precompute the encoder output and resuese it for every token we get from decoder
    encoder_output = model.encode(source, source_mask)

    #Initialize th edecodr input with sos tokens
    decoder_input= torch.empty(1,1).fill_(sos_idx).type_as(source).to(device)
    while True:
        if decoder_input.size(1) == max_len:
            break

        #Build the mask for the target (Decoder Input)
        decoder_mask = causal_mask(decoder_input.size(1).type_as(source_mask).to(device))
        
        #Calculate the output of the decoder
        out = model.decode(encoder_output, source_mask, decoder_input, decoder_mask)

        #Get the next token
        prob = model.project(out[:, -1])

        #Select the token with the max probability (because it is a greedy search)
        _, next_word =  torch.max(prob, dim=1)
        decoder_input = torch.cat([decoder_input, torch.empty(1,1).type_as(source).fill_(next_word.item()).to(device)], dim=1)

        if next_word == eos_idx:
            break

    return decoder_input.squeeze(0)





def run_validation(model, validation_ds, tokenizer_src, tokenizer_tgt, max_len, device , print_msg, global_state, writer, run_examples):
    model.eval()
    count = 0
    source_texts = []

    expected = []
    predicted = []

    #Size of the control Window(Just use a default value)
    console_width = 80

    with torch.no_grad():
        for batch in validation_ds:
            count +=1
            encoder_input = batch['encoder_input'].to(device)
            encoder_mask = batch['encoder_mask'].to(device)

            assert batch.size(0) == 1, "Batch Size must be 1 for validation"

            model_out= greedy_decode(model, source, encoder_mask, tokenizer_src, tokenizer_tgt, max_len, device)

            source_text = batch['src_text'][0]
            target_text = batch['tgt_text'][0]
            model_out_text = tokenizer_tgt.decode(model_out.detach().cpu().numpy())

            source_texts.append(source_text)
            expected.append(target_text)
            predicted.append(model_out_text)

            #Print to console

            print_msg('-'*console_width)
            print_msg(f'SOURCE: {source_text}')
            print_msg(f'TARGET: {target_text}')
            print_msg(f'PREDICTED: {model_out_text}')

            if count == num_examples:
                break

            

