from enum import Enum

from core.chromatic import ChromaticScale


class Intervals(Enum):
    """Standard intervals in western music in number of half-steps"""
    P1 = 0  # perfect unison
    m2 = 1  # minor second
    M2 = 2  # major second
    m3 = 3  # minor third
    M3 = 4  # major third
    P4 = 5  # perfect fourth
    TT = 6  # tritone
    d5 = 6  # diminished fifth
    P5 = 7  # perfect fifth
    A5 = 8  # augmented fifth
    m6 = 8  # minor sixth
    M6 = 9  # major sixth
    d7 = 9  # diminished seventh
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
    dim7 = Intervals.P1.value, Intervals.m3.value, Intervals.d5.value, Intervals.d7.value
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
    c = Chords('D', 'major')
    print(c.notes)
    
    
    foo = (Intervals.P1.value, Intervals.M3.value, Intervals.P5.value)
    for f in ChordFormula._member_map_.items():
        print(f[1].value)
        if f[1]._value_ == foo:
            print(f[0])
            break
