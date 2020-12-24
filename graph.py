import pandas as pd
from pathlib import Path

specs = ["-jitter-confuse", "-jitter", "-confuse"]
for spec in specs:
  models = {}
  for f in Path("results/").glob(f"*{spec}-0*.csv"):
    if spec == specs[0] or (spec != specs[0] and (specs[1] not in f.name or specs[2] not in f.name)): # so we don't duplicate      
      model = f.name.split(spec)[0]
      df = pd.read_csv(f)
      acc = df["val_categorical_accuracy"] # the only one we care about
      if model not in models or (model in models and acc[9] > models[model][9]): # since we're only plotting 10 epochs worth
        models[model] = acc[:10]
  df = pd.DataFrame({"epochs":list(range(10)), **models})
  df.to_csv(f"acc{spec}.csv",index=False)

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
