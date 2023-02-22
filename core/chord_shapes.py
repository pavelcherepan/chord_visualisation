
from itertools import product

from chords import Chords
from fretboard import FretboardNotes


note_translator = {
    'B♭': 'A#',
    'D♭': 'C#',
    'E♭': 'D#',
    'G♭': 'F#',
    'A♭': 'G#',
    'C♭': 'C',
    'F♭': 'F'
}


class ChordShapes:    
    def __init__(
        self, 
        tuning: tuple[str, ...] = ('E', 'B', 'G', 'D', 'A', 'E'),
        ) -> None:  
        self.fretboard = FretboardNotes(tuning)  

    def get_chord_name(self, chord_string: str):
        root_note = chord_string[0]   # assuming standard chord notation
        
        if (len(chord_string) == 1) or ('major' in chord_string):
            chord_quality = 'major'
        elif (('minor' in chord_string) or 
              (len(chord_string) == 2 and chord_string[1] == 'm')):
            chord_quality = 'minor'
        elif 'sus4' in chord_string:
            chord_quality = 'suspended_4'
        elif 'sus2' in chord_string:
            chord_quality = 'suspended_2'
        return root_note, chord_quality
    
    def get_chord_notes(self, root_note: str, quality: str):
        c = Chords(root_note)
        return c.__getattribute__(quality)
        
    def get_shapes(self, chord_string: str) -> list[list[tuple[int, int]]]:
        root, qual = self.get_chord_name(chord_string)

        # get chord notes translate flats to alternative names
        notes = [note_translator.get(n) or n 
                 for n in self.get_chord_notes(root, qual)]
        chord_notes: dict[int, list[tuple[int, int]]] = {
            idx: self.fretboard.get_fret_position_from_note(n)
            for idx, n in enumerate(notes)
        }
        # now get all possible combinations
        comb = list(product(*chord_notes.values()))
        
        # filter the resulting combinations such that:
        #  - notes of a chord are no more than 3 frets apart
        #  - all notes have to be on separate strings
        unplayable_idx: list[int] = []
        fret_ranges = list(map(lambda x: 
            max(f[1] for f in x) - min(f[1] for f in x), comb))
        unplayable_idx = [idx for idx, i 
                          in enumerate(fret_ranges) if i >= 3]

        # identify combinations where different 
        # notes are played on the same string
        different_strings = [
            idx for idx, i in enumerate(comb) 
            if len({x[0] for x in i}) != len(i)
        ]
        unplayable_idx.extend(different_strings)

        comb_filtered = [i for idx, i in enumerate(comb) 
                         if idx not in unplayable_idx]
        # sort results in the order of strings
        comb_filtered = [sorted(i, key=lambda x: x[0]) 
                         for i in comb_filtered]
        return comb_filtered        
        

if __name__ == '__main__':
    c = ChordShapes()
    c.get_shapes('D')

            
        