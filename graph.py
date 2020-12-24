import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

for spec in ["jitter-confuse", "jitter", "confuse"]:
  for f in Path("results/").glob(f"*-{spec}-0*.csv"):
    df=pd.read_csv(f) # no index_col as epoch is time-series data, not id
    

# Overall
# - Validation Accuracy over Ten Epochs for All Models
# - Validation Accuracy over Ten Epochs for CNN Models
# - Validation Accuracy over Ten Epochs for Dense Models
# - Relative Impact of Normalisation

# Confusables Only
# - Validation Accuracy over Ten Epochs for All Models
# - Validation Accuracy over Ten Epochs for CNN Models
# - Validation Accuracy over Ten Epochs for Dense Models
# - Relative Impact of Normalisation

# Jitter Only
# - Validation Accuracy over Ten Epochs for All Models
# - Validation Accuracy over Ten Epochs for CNN Models
# - Validation Accuracy over Ten Epochs for Dense Models
# - Relative Impact of Normalisation
