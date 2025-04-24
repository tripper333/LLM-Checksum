import numpy as np
import torch
import tiktoken
from openai import OpenAI

client = OpenAI()

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    resp = client.embeddings.create(input=[text], model=model)
    return torch.tensor(resp.data[0].embedding)

def compute_variance(embedding):
    if embedding.numel() == 0 or torch.isnan(embedding).any():
        return np.nan
    return embedding.var().item()

def compute_token_entropy(text, model="cl100k_base"):
    enc = tiktoken.get_encoding(model)
    tokens = enc.encode(text)
    if not tokens:
        return 0.0
    counts = np.bincount(tokens)
    probs = counts / counts.sum()
    entropy = -np.sum([p * np.log2(p + 1e-9) for p in probs if p > 0])
    num = len(tokens)
    return float(entropy / np.log2(num)) if num > 1 else 0.0

def compute_mu(variance, entropy, kv=50.0, ke=1.0):
    if np.isnan(variance) or np.isnan(entropy):
        return np.nan
    decay = kv * variance + ke * entropy
    return float(np.exp(-decay))

def generate_field(mu, entropy, var, grid_size=40):
    if np.isnan(mu) or np.isnan(entropy) or np.isnan(var):
        x = np.linspace(-2, 2, grid_size)
        y = np.linspace(-2, 2, grid_size)
        X, Y = np.meshgrid(x, y)
        return X, Y, np.full_like(X, np.nan)
    x = np.linspace(-2, 2, grid_size)
    y = np.linspace(-2, 2, grid_size)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    Z = 1 / (1 + np.exp(
        -(np.sin(3*R) + np.cos(2*X)*np.sin(2*Y))
        + 4 * (mu - 0.5)
        + 2 * (entropy - 0.5)
        + 3 * (var - 0.1)
    ))
    return X, Y, Z
