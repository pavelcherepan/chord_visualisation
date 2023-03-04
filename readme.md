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
The `main.py` provides two convenience functions:

`plot_chord_shapes` -  Plot all possible open chord shapes by providing 
a string of a chord name to be displayed and a `plot` argument of how 
different variants should be displayed.

If an integer is provided then only the plot with that integer index will be displayed. 
If 'all' then all variants will be shown on a large plot. If 'one-by-one'
then the script will display plots one by one in the order of the index.

    Args:
        chord_string (str): A string of chord name
        plot (int | str): Value of how to display plot. 
            If an integer is provided then only the plot with that 
            integer index will be displayed. If 'all' then all 
            variants will be shown on a large plot. If 'save-all'
            then the script will display plots one by one in the 
            order of the index.

`find_chord_name_from_diagram` - Find the name of a chord from finger diagram. 

    Args:
        finger_positions (list[tuple[int, int]]): A list of tuple of finger positions
            on a fretboard in the form (string, fret).
        open_strings (list[int]): A list of integers of strings that are played open.
        muted_strings (list[int]): A list of integers of strings that are muted.

    Returns:
        str | None: A string of the chord name
