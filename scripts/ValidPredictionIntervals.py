# %% [markdown]
# This notebook contains some code to show how to run the Python files containing the model code.

# %%
import math, os

from src.Code.Data import *
from src.Code.Load import *
from src.Code.CP import *
from src.Code.QualityMeasures import *

import numpy as np
from tqdm.notebook import tqdm

# %%
data = "residential"

# %%
def summary(data, model, CP = True, folder = FOLDER):
    folder = FOLDER + "/" + data + "/results/"
    files = os.listdir(folder)
    cp = "-CP-" if CP else ""
    filtered = [file for file in files if (model+cp in file)]
    
    data = np.zeros((len(filtered), 3))
    
    for i, f in enumerate(filtered):
        with open(folder + f, "r") as file:
            parts = file.read().splitlines()[0].split("\t")
            data[i, 0] = float(parts[0])
            data[i, 1] = float(parts[1])
            data[i, 2] = float(parts[2])
            
    return {"cov": np.mean(data[:, 0]), "width": np.mean(data[:, 1]), "r2": np.mean(data[:, 2]), \
           "cov_std": np.std(data[:, 0]), "width_std": np.std(data[:, 1]), "r2_std": np.std(data[:, 2])}

# %%
import RunNNCP as NN

for s in tqdm(SEEDS):
    NN.run(data, s)
    
summary(data, "NN")

# %%
import RunKG as KG

for s in tqdm(SEEDS):
    KG.run(data, s, num = 50, drop = np.arange(0.05, 0.55, 0.05), l = 0)
    
summary(data, "KG")

# %%
import RunQR as QR

for s in tqdm(SEEDS):
    QR.run(data, s)
    
summary(data, "QR")

# %%
import RunRFCP as RFCP

for s in tqdm(SEEDS):
    RFCP.run(data, s)
    
summary(data, "QR")

# %%
