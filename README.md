# DeobfuscNet

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WnkB7pCg2EyWleeZI0cccyeTW6I0Oe6o)

A project by Alex Blandin - 953274@swansea.ac.uk / a.j.blandin@swansea.ac.uk

Full Repository at https://github.com/AlexBlandin/DeobfuscNet

### Installation (Colab)

[Open in Colab](https://colab.research.google.com/drive/1WnkB7pCg2EyWleeZI0cccyeTW6I0Oe6o). Click the "Copy to Drive" button in the tool tray at the top. Done.

### Installation (Local)

Good luck:

- Colab-specific syntax is used (`!wget`, `!pip`, etc.), these can be removed if the required files are present in the local directory, or replaced with python code that downloads the given file to the local directory
- DOWNLOAD options should "fail gracefully" outside of Colab
- Ensure Tensorflow2 is installed alongside all other required modules
  - py-ulid
  - tqdm
  - numpy
  - sklearn
  - skimage
  - matplotlib
- Ensure Weasyprint is installed with all requirements as per its [installation requirements](https://weasyprint.readthedocs.io/en/stable/install.html)

### Running (Colab)

In Colab, select Runtime -> Run All (Ctrl+F9).

Changing parameters using the drop-down menus is preferred. Use Runtime -> Run After (Ctrl+F10) from that cell, as the project is designed to be run linearly from a given point to the very end.

### Running (Local)

If in a notebook/Jupyter setting, similar to **Running (Colab)**, otherwise it would need to be completely run as a script.

### Summary Plots

Run `$python3 graph.py` to prep the `results/` directory into accuracy listings (`acc-jitter.csv` etc.) and average difference from normalising (`ndiff-confuse.csv` etc.). These can be plugged into the corresponding `.xlsx` files, which should update the graphs. Examples from the given dataset are available in the `graphs/` directory.

> Copyright © 2020