from enum import Enum

from chromatic import ChromaticScale


class Intervals(Enum):
    """Standard intervals in western music in number of half-steps"""
    P1 = 0  # perfect unison
    m2 = 3  # minor second
    M2 = 4  # major second
    m3 = 3  # minor third
    M3 = 4  # major third
    P4 = 5  # perfect fourth
    TT = 6  # tritone
    d5 = 6  # diminished fifth
    P5 = 7  # perfect fifth
    m6 = 8  # minor sixth
    M6 = 9  # major sixth
    A5 = 8   # augmented 5
    m7 = 10  # minor seventh
    M7 = 11  # major seventh
    P8 = 12  # octave
    M9 = 14 # Major ninth
    
    

class ChordFormula(Enum):
    major = Intervals.P1.value, Intervals.M3.value, Intervals.P5.value
    minor = Intervals.P1.value, Intervals.m3.value, Intervals.P5.value
    aug = Intervals.P1.value, Intervals.m3.value, Intervals.A5.value
    dim = Intervals.P1.value, Intervals.m3.value, Intervals.d5.value
    sus4 = Intervals.P1.value, Intervals.P4.value, Intervals.P5.value
    sus2 = Intervals.P1.value, Intervals.M2.value, Intervals.P5.value
    major7 = Intervals.P1.value, Intervals.M3.value, Intervals.P5.value, Intervals.M7.value
    dom7 = Intervals.P1.value, Intervals.M3.value, Intervals.P5.value, Intervals.m7.value
    minor7 = Intervals.P1.value, Intervals.m3.value, Intervals.P5.value, Intervals.m7.value
    minor7_flat5 = Intervals.P1.value, Intervals.m3.value, Intervals.d5.value, Intervals.m7.value
    dim7 = Intervals.P1.value, Intervals.m3.value, Intervals.d5.value, Intervals.M6.value
    major9 = Intervals.P1.value, Intervals.M3.value, Intervals.P5.value, Intervals.M7.value, Intervals.M9.value
    dom9 = Intervals.P1.value, Intervals.M3.value, Intervals.P5.value, Intervals.m7.value, Intervals.M9.value
    

class Chords:    
    def __init__(self, key: str, quality: str) -> None:
        self.key = key
        self.quality = quality
        s = ChromaticScale(key)
        self.scale: dict[str, int] = s.scale
    
    @property
    def notes(self):
        ranges = ChordFormula.__getitem__(self.quality).value        
        return [k for k, v in self.scale.items() if v in ranges]
        
        
if __name__ == '__main__':
    print(ChordFormula.__getitem__('minor').value)
    c = Chords('A', 'sus4')
    print(c.notes)