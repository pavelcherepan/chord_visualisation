from major_scale import MajorScale


class Chords:
    
    def __init__(self, root_note: str) -> None:
        self.root_note = root_note
        s = MajorScale(root_note)
        self.scale: list[str] = s.scale
        
    @property
    def major(self):
        """Get notes for 1-3-5 formula"""
        return [i for idx, i in enumerate(self.scale) if idx in [0, 2, 4]]
    
    @property
    def augmented(self):
        """Get notes for 1-3-5# chord formula"""
        return [f'{i}#' if idx == 4 else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4]]
    
    @property
    def minor(self):
        """Get notes for 1-3♭-5 chord formula"""
        return [f'{i}♭' if idx == 2 else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4]]
    
    @property
    def diminished(self):
        """Get notes for 1-♭3-♭5 chord formula"""
        return [f'{i}♭' if idx in [2, 4] else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4]]
    
    @property
    def suspended_4(self):
        """Get notes for 1-4-5 chord formula"""
        return [i for idx, i in enumerate(self.scale) if idx in [0, 3, 4]]
    
    @property
    def suspended_2(self):
        """Get notes for 1-2-5 chord formula"""
        return [i for idx, i in enumerate(self.scale) if idx in [0, 1, 4]]
    
    @property
    def major_7(self):
        """Get notes for 1-3-5-7 chord formula"""
        return [i for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6]]
    
    @property
    def dominant_7(self):
        """Get notes for 1-3-5-♭7 chord formula"""
        return [f'{i}♭' if idx == 6 else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6]]
    
    @property
    def minor_7(self):
        """Get notes for 1-♭3-5-♭7 chord formula"""
        return [f'{i}♭' if idx in [2, 6] else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6]]
    
    @property
    def minor_7_flat_5(self):
        """Get notes for 1-♭3-♭5-♭7 chord formula"""
        return [f'{i}♭' if idx != 0 else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6]]
    
    @property
    def diminished_7(self):
        """Get notes for 1-♭3-♭5-♭♭7(6) chord formula"""
        return [i if idx == 0 else f'{i}♭♭' if idx == 6 else f'{i}♭' 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6]]
        
    @property
    def major_9(self):
        """Get notes for 1-3-5-7-9 chord formula"""
        return [i for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6, 8]]
    
    @property
    def dominant_9(self):
        """Get notes for 1-3-5-♭7-9 chord formula"""
        return [f'{i}♭' if idx == 6 else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6, 8]]
        
    @property
    def dominant_11(self):
        """Get notes for 1-3-5-♭7-9 chord formula"""
        return [f'{i}♭' if idx == 6 else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6, 8, 10]]
    
    @property
    def dominant_13(self):
        """Get notes for 1-3-5-♭7-9 chord formula"""
        return [f'{i}♭' if idx == 6 else i 
                for idx, i in enumerate(self.scale) if idx in [0, 2, 4, 6, 8, 10, 12]]
        
        
if __name__ == '__main__':
    c = Chords('A#')
    print(c.minor)