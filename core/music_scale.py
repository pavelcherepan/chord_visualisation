
from enum import Enum

from core.chromatic import ChromaticScale


class ScalePatterns(Enum):
    major = 'W-W-H-W-W-W-H'
    minor = 'W-H-W-W-H-W-W'
    

class MusicScale:
    
    def __init__(self, key: str) -> None:
        self._key = key
        
    @property
    def key(self) -> str:
        return self._key
    
    def _pattern_to_intervals(self, pattern: str) -> list[int]:
        """Generate a list of seminote differences from
        the starting key note for all notes in a music scale
        based on a string of fules.

        Args:
            pattern (str): A String of scale pattern with 
                "W" indicating a full note and "H" indicating
                a half note.

        Returns:
            list[int]: List of integers of scale intervals from
                the key note.
        """
        inter = [1 if i=="H" else 2 for i in pattern.split("-")]
        cumsum: list[int] = [0]   # starting with 0 because key note alway will be in the scale.
        running_sum = 0
        
        for i in inter:
            running_sum += i
            cumsum.append(running_sum)
        
        return cumsum          
        
    def scale(self, pattern: str) -> list[str]:
        """Generate major scale following specific pattern
        
        Args:
            pattern (str): A String of scale pattern with 
                "W" indicating a full note and "H" indicating
                a half note.
        
        """
        chroma = ChromaticScale(self.key)
        intervals = self._pattern_to_intervals(pattern)

        res_scale: list[str] = [
            key for key, value in chroma.scale.items() if value in intervals
        ]
        return res_scale     
        
        
   
if __name__ == '__main__':
    m = MusicScale('D')
    print(m.scale(ScalePatterns.minor.value))