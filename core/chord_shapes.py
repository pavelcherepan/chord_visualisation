from dataclasses import dataclass
from itertools import product

from chords import Chords
from fretboard import FretboardNotes
from music_scale import MusicScale, ScalePatterns


@dataclass
class ChordDiagram:
    shape: list[tuple[int, int]]
    open_strings: list[int]
    muted_strings: list[int]


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
        self.tuning = tuning
        self.fretboard = FretboardNotes(tuning)  

    def parse_chord_string(self, chord_string: str) -> tuple[str, str]:
        if len(chord_string) == 1:
            return chord_string, "major"
        if chord_string[1] in ["#", "♭", "b"]:
            root_note = chord_string[:2]
            raw_quality = chord_string[2:]
        else:
            root_note = chord_string[0] 
            raw_quality = chord_string[1:] 
        quality = self._parse_quality_string(raw_quality)
        return root_note, quality
        
    def _parse_quality_string(self, raw_quality: str) -> str:
        if raw_quality == 'm':
            return "minor"
        elif raw_quality == 'm7':
            return 'minor7'
        else:
            return raw_quality
    
    def get_chord_notes(self, key: str, quality: str) -> list[str]:
        c = Chords(key, quality)
        return c.notes
    
    def get_chord_diagram(self, chord_string: str):
        key, quality = self.parse_chord_string(chord_string)
        raw_shapes = self._get_shapes(key, quality)
        filtered_shapes = self._filter_shapes(raw_shapes)
        return self._check_open_strings(filtered_shapes, key, quality)     
        
    def _get_shapes(self, root: str, quality: str
                    ) -> list[tuple[tuple[int, int], ...]]:       
        # get chord notes translate flats to alternative names
        notes = [note_translator.get(n) or n 
                 for n in self.get_chord_notes(root, quality)]
        chord_notes: dict[int, list[tuple[int, int]]] = {
            idx: self.fretboard.get_fret_position_from_note(n)
            for idx, n in enumerate(notes)
        }
        # now get all possible combinations
        return list(product(*chord_notes.values()))
    
    def _filter_shapes(self, raw_shapes: list[tuple[tuple[int, int], ...]]):        
        # filter the resulting combinations such that:
        #  - notes of a chord are no more than 3 frets apart
        #  - all notes have to be on separate strings
        unplayable_idx: list[int] = []
        fret_ranges = list(map(lambda x: 
            max(f[1] for f in x) - min(f[1] for f in x), raw_shapes))
        unplayable_idx = [idx for idx, i 
                          in enumerate(fret_ranges) if i >= 3]

        # identify combinations where different 
        # notes are played on the same string
        different_strings = [
            idx for idx, i in enumerate(raw_shapes) 
            if len({x[0] for x in i}) != len(i)
        ]
        unplayable_idx.extend(different_strings)

        comb_filtered = [i for idx, i in enumerate(raw_shapes) 
                         if idx not in unplayable_idx]
        # sort results in the order of strings
        comb_filtered = [sorted(i, key=lambda x: x[0]) 
                         for i in comb_filtered]
        return comb_filtered
    
    def _check_open_strings(
        self, 
        raw_shapes: list[list[tuple[int, int]]],
        root: str,
        quality: str
        ) -> list[ChordDiagram]:
        s = MusicScale(root)   
        scale = s.scale(ScalePatterns.__getitem__(quality).value)
        print(f"{scale=}")
        
        res: list[ChordDiagram] = []
        # for each of the shapes identify which strings are open
        for shape in raw_shapes:
            played_strings: list[int] = [i[0] for i in shape]
            print(f"\n {shape=}, {played_strings=}")
            raw_open_strings: list[int] = [i for i in range(1, 7) 
                                           if i not in played_strings]
            print(f"{raw_open_strings=}")
            # if the open string is lower register than the root note
            # then it will need to get muted
            muted_strings: list[int] = [i for i in raw_open_strings 
                                        if i > max(played_strings)]  
            print(f"{muted_strings=}")          
            # go through tuning and if a note is not depressed and
            # it is still in the correct scale then add it to open_strings
            open_strings = [idx+1 for idx, i in enumerate(self.tuning) 
                            if i in scale 
                            and idx+1 in raw_open_strings 
                            and idx+1 not in muted_strings]
            print(f"{open_strings=}")
            muted_strings = [i for i in raw_open_strings 
                             if i not in open_strings]
            res.append(ChordDiagram(
                shape=shape, 
                open_strings=open_strings, 
                muted_strings=muted_strings
                )
                       )
        return res          
            

if __name__ == '__main__':
    c = ChordShapes()
    c.get_chord_diagram('Dm')

            
        