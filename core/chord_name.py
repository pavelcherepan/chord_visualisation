import sys
from pathlib import Path

sys.path.insert(0, str(Path().parent.resolve()))

from core.fretboard import FretboardNotes
from core.chord_shapes import ChordDiagram

from functools import reduce


class ChordNameGenerator:
    """
    Class tasked with generating a name of a chord
    based on the input chord diagram.
    """
    
    def __init__(self, 
                 tuning: tuple[str, ...] = ('E', 'B', 'G', 'D', 'A', 'E')
                 ) -> None:
        self._tuning = tuning
        self.fretboard = FretboardNotes(tuning)
        
    def identify_root_note(self, diagram: ChordDiagram) -> tuple[tuple[int, int], str]:
        """Get root note from a given chord diagram.
        Here we simply identify the lowest (register-wise) string
        that is either fretted or played open and consider the
        base note to be the root of the chord. 
        

        Args:
            diagram (ChordDiagram): A ChordDiagram object showing the
                position of fingers and also open/muted strings.

        Returns:
            tuple[tuple[int, int], str]: A tuple of finger position 
                (string, fret) and a string of root note name.
        """
        # we first extend the shape member with the values of open strings
        # giving them 0th fret.
        open_strings = [(i, 0) for i in diagram.open_strings]
        all_strings = diagram.shape + open_strings
        max_string: tuple[int, int] = reduce(lambda x, y: x if x[0] > y[0] else y, all_strings)
        return max_string, self.fretboard.get_note(string=max_string[0], fret=max_string[1])
    
    
if __name__ == '__main__':
    cng = ChordNameGenerator()
    cd = ChordDiagram(shape=[(1, 2), (2, 3), (3, 2)], open_strings=[4], muted_strings=[])
    print(cng.identify_root_note(cd))
    
        