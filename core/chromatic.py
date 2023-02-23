
class ChromaticScale:
    notes = ('A', 'A#', 'B', 'C', 'C#', 'D', 
             'D#', 'E', 'F', 'F#', 'G', 'G#')
    
    def __init__(self, root_note: str):
        self.root_note = root_note
    
    @property
    def scale(self) -> dict[str, int]:
        """Generate a scale for a specific key."""
               
        starting_idx = list(self.notes).index(self.root_note)
        notes: list[str] = []

        for idx in range(len(self.notes)):
            new_index = (starting_idx + idx) % len(self.notes)
            notes.append(self.notes[new_index])

        return dict(zip(notes, list(range(len(notes)))))
    
 
        
if __name__ == '__main__':
    print(ChromaticScale("E").scale)