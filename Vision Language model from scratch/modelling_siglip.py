from typing import Optional, Tuple
import torch 
import torch.nn as nn

class silipvisionConfig:

    def __init__(self,
                 hidden_size= 786,
                 intermediate_size= 3072,
                 num_hidden_layers = 12,
                 num_attention_heads= 12,
                 num_channels= 3,
                 image_size= 224,
                 patch_size= 16,
                 layer_norm_eps= 1e-6,
                 attention_dropput= 0.0,
                 num_image_tokens: int= None,
                    *kwargs

                 
                 ):
        pass