from core.plot_chords import ChordShapePlot



def main(
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
            variants will be shown on a large plot. If 'one-by-one'
            then the script will display plots one by one in the 
            order of the index.
    """
    c = ChordShapePlot(chord_string)
    
    if isinstance(plot, int):
        c.plot_by_idx(plot)
    elif plot == 'all':
        c.plot_all()
    else:
        c.plot_one_by_one()
        
        
if __name__ == '__main__':
    main('Am', 'one-by-one')
    