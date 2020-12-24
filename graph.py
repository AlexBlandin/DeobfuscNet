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
  df = pd.DataFrame(models)
  df.insert(0,"",[f"Epoch {i}" for i in range(10)])
  try:
    df.to_csv(f"acc{spec}.csv",index=False)
  except PermissionError:
    pass
  except Exception as e:
    raise e
  ndiff = {}
  for model in models:
    nmodel = f"N{model}"
    if nmodel in models:
      ndiff[model] = (models[nmodel].sum()-models[model].sum())/10 # +ve means norm. helped, -ve reverse
  ndf = pd.DataFrame({"model":ndiff.keys(),"diff":ndiff.values()})
  try:
    ndf.to_csv(f"ndiff{spec}.csv",index=False)
  except PermissionError:
    pass
  except Exception as e:
    raise e

# Overall
# - Validation Accuracy over Ten Epochs for All Models (Jitter+Confusables)
# - Validation Accuracy over Ten Epochs for CNN Models (Jitter+Confusables)
# - Validation Accuracy over Ten Epochs for Dense Models (Jitter+Confusables)
# - Relative Impact of Normalisation (Jitter+Confusables)

# Confusables Only
# - Validation Accuracy over Ten Epochs for All Models (Confusables)
# - Validation Accuracy over Ten Epochs for CNN Models (Confusables)
# - Validation Accuracy over Ten Epochs for Dense Models (Confusables)
# - Relative Impact of Normalisation (Confusables)

# Jitter Only
# - Validation Accuracy over Ten Epochs for All Models (Jitter)
# - Validation Accuracy over Ten Epochs for CNN Models (Jitter)
# - Validation Accuracy over Ten Epochs for Dense Models (Jitter)
# - Relative Impact of Normalisation (Jitter)
