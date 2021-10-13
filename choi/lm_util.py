import os
import sys
import torch
import logging

# os.environ["CUDA_VISIBLE_DEVICES"]="2"

from transformers.modeling_bert import BertConfig, BertModel
#from KoBERT_Transformers.kobert_transformers.tokenization_kobert import KoBertTokenizer

from transformers.modeling_electra import ElectraModel, ElectraConfig
from transformers.tokenization_electra import ElectraTokenizer

def dot_product_scores(x, y):
    return torch.matmul(x,torch.transpose(y, 0, 1))

def cosine(x,y):
    return torch.nn.CosineSimilarity(dim=1, eps=1e-6)(x,y)