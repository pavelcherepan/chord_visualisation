from chromatic import ChromaticScale

class FretboardNotes:
    chromatic_scale = ChromaticScale.notes
    
    def __init__(
        self, 
        tuning: tuple[str, ...] = ('E', 'B', 'G', 'D', 'A', 'E'),
        max_frets: int = 13
        ) -> None:        
        self._tuning = tuning
        self._max_frets = max_frets
        self._populate_all_strings()
        
    def _populate_all_strings(self):
        string_notes: dict[str, list[str]] = {}
        for open_note in self._tuning:
            string_notes[open_note] = []
            for fret in range(self._max_frets + 1):
                string_notes[open_note].append(
                    self.chromatic_scale[(self.chromatic_scale.index(open_note) + fret) % 12])
        self.string_notes = string_notes
            
    def get_note(self, string: int, fret: int) -> str:
        open_note = self._tuning[string - 1]
        return self.chromatic_scale[(self.chromatic_scale.index(open_note) + fret) % 12]
    
    def get_fret_position_from_note(self, note: str):
        positions: list[tuple[int, int]] = []
        for string_no, open_note in enumerate(self.string_notes.keys()):
            frets = [idx for idx, i in enumerate(self.string_notes[open_note]) if i == note]
            positions.extend([(string_no + 1, f) for f in frets])
            if string_no == 0:
                positions.extend([(6, f) for f in frets])
        return positions
        

if __name__ == "__main__":
    f = FretboardNotes()
    print(f.get_fret_position_from_note('E'))
    
        
    
        
        