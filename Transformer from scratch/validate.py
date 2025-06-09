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


def run_validation(moidel, validation_ds, tokenizer_src, tokenizer_tgt, max_len, device , print_msg, global_state, writer, run_examples):
    model.eval()
    
    count = 0
    source_texts = []

    expected = []
    predicted = []

    #Size of the control Window(Just use a default value)
    console_width = 80

    with torch.no_grad():
        for batch in validation_ds:
