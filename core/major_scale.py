
class MajorScale:
    major_scale = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    def __init__(self, root_note: str) -> None:
        self.root_note = root_note
        self._init_scale()    
        
    def _init_scale(self):
        start_idx = self.major_scale.index(self.root_note)
        self.scale: list[str] = [self.major_scale[i % 7] 
                                 for i in range(start_idx, start_idx + 14)]
    
    
    
if __name__ == '__main__':
    m = MajorScale('C')
    print(m.scale)