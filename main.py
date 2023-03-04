from core.plot_chords import ChordShapePlot
from core.chord_shapes import ChordDiagram, FingerPosition
from core.chord_name import ChordNameGenerator



def plot_chord_shapes(
    chord_string: str,
    plot: int | str = 1):
    """Generate a plot of chord diagram.
    
    Usage: Provide a string of chord name and the value for
    plot parameter that determines how plots will be displayed.
    The plot argument accepts either an integer or one of
    strings ['all', 'one-by-one']. 
    Args:
        chord_string (str): A string of chord name
        plot (int | str): Value of how to display plot. 
            If an integer is provided then only the plot with that 
            integer index will be displayed. If 'all' then all 
            variants will be shown on a large plot. If 'save-all'
            then the script will display plots one by one in the 
            order of the index.
    """
    c = ChordShapePlot(chord_string)
    
    if isinstance(plot, int):
        c.plot_by_idx(plot)
    elif plot == 'all':
        c.plot_all()
    else:

        c.save_all_plots()  
        

def find_chord_name_from_diagram(finger_positions: list[tuple[int, int]],
                                 open_strings: list[int],
                                 muted_strings: list[int]
                                 ) -> str | None:
    """Find the name of a chord from finger diagram. 

    Args:
        finger_positions (list[tuple[int, int]]): A list of tuple of finger positions
            on a fretboard in the form (string, fret).
        open_strings (list[int]): A list of integers of strings that are played open.
        muted_strings (list[int]): A list of integers of strings that are muted.

    Returns:
        str | None: A string of the chord name
    """
    shape = [FingerPosition(i[0], i[1]) for i in finger_positions]
    cd = ChordDiagram(shape=shape, open_strings=open_strings, muted_strings=muted_strings)
    cng = ChordNameGenerator()
    cng.identify_root_note(cd)
    quality = cng.indentify_chord_quality(cd)
    return(f"{cng.root_note_name} {quality}")    

               
if __name__ == '__main__':
    # plot_chord_shapes('Am', 'one-by-one')
    
    shape_3 = [(1, 3), (5, 2), (6, 3)]
    open_strings=[2, 3, 4]
    muted_strings=[]

    res = find_chord_name_from_diagram(
        finger_positions=shape_3, open_strings=open_strings, muted_strings=muted_strings)
    print(res)
