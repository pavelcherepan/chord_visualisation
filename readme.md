# Chord visualizer

Use to create a diagram of all variations of a guitar chord from a given string.

# Requirements
- Python 3.9 or higher
- External library dependencies: **scikit-learn**, **NumPy**, **matplotlib**

# Installation
Clone or download the code repository. To install the dependencies run:
```
python -m pip install matplotlib scikit-learn numpy
```

# Usage

Run `main` function in the `main.py` and provide a string of a chord to be displayed
and a `plot` argument of how different variants should be displayed.

Possible values for `plot` argument:
  * integer - if an integer is provided then only the plot with that integer index will be displayed. 
  * **"all"** - then all variants will be shown on a large plot. 
  * **'save-all'** - the script will save plots in the *export* subfolder or selected folder.
