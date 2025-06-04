import torch 
import torch.nn as nn

from torch.utils.data import Dataset, Dataloader, random_split
from datasets import load_dataset
from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers.models import WordLevelTrainer
from tokenizer.pre_tokenizers import Whitespace

from pathlib import Path

def get_all_sentences(ds, lang):
    for item in ds:
        yield[item]


def get_or_build_tokenizer(config, ds, lang):
    #Config['tokenizer.file'] = ../tokenizers/tokenizer_{0}.json
    tokenizer_path = Path(config['tokenizer.file'].format(lang))
    if not Path.exists(tokenizer_path):
        tokenizer = Tokenizer(WordLevel( unk_token ='[UNK]' ))
        tokenizer.pre_tokenizer = Whitespace()
        trainer = WordLevelTrainer(special_tokens("[UnK]", "[PAD]", "[SOS]", "[EOS]", min_frequency = 2))
        tokenizer.train_from_iterator(get_all_sentences(ds, lang), trainer = trainer)
        tokenizer.save(str(tokenizer_path))
    else:
        tokenizer = Tokenizer.from_file(str(tokenizer_path))
    return tokenizer

def get_ds(config):
    ds_raw= load_dataset('opus_books', f'{config["lang_src"]} - {config["lang_tgt"]}' , split = 'train')
    
    #Build Tokenizers

    tokenizer_src = get_or_build_tokenizer(config, ds_raw, config['lang_src'])
    tokenizer_tgt = get_or_build_tokenizer(config, ds_raw, config['lang_tgt'])

    #Keep 90% or training, 10% for validation
    train_ds_size =int(0.9*len(ds_raw))
    val_ds_size = len(ds_size) - len(train_ds_size)

    train_ds_raw, val_ds_raw = random_split(ds_raw, [train_ds_size, val_ds_size])
