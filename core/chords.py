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
    major = Intervals.P1, Intervals.M3, Intervals.P5
    minor = Intervals.P1, Intervals.m3, Intervals.P5
    aug = Intervals.P1, Intervals.m3, Intervals.A5
    dim = Intervals.P1, Intervals.m3, Intervals.d5
    sus4 = Intervals.P1, Intervals.P4, Intervals.P5
    sus2 = Intervals.P1, Intervals.M2, Intervals.P5
    major7 = Intervals.P1, Intervals.M3, Intervals.P5, Intervals.M7
    dom7 = Intervals.P1, Intervals.M3, Intervals.P5, Intervals.m7
    minor7 = Intervals.P1, Intervals.m3, Intervals.P5, Intervals.m7
    minor7_flat5 = Intervals.P1, Intervals.m3, Intervals.d5, Intervals.m7
    dim7 = Intervals.P1, Intervals.m3, Intervals.d5, Intervals.d7
    major9 = Intervals.P1, Intervals.M3, Intervals.P5, Intervals.M7, Intervals.M9
    dom9 = Intervals.P1, Intervals.M3, Intervals.P5, Intervals.m7, Intervals.M9
    
    @classmethod
    def get_quality_from_intervals(cls, intervals: tuple[Intervals, ...]) -> str | None:
        """Get a chord quality by providing a tuple of musical intervals"""
        lookup = dict(zip([v.value for v in cls._member_map_.values()], cls._member_map_.keys()))
        return lookup.get(intervals)
    

class Chords:    
    def __init__(self, key: str, quality: str) -> None:
        self.key = key
        self.quality = quality
        s = ChromaticScale(key)
        self.scale: dict[str, int] = s.scale
    
    @property
    def notes(self):
        print(ChordFormula.__getitem__(self.quality))
        ranges: tuple[int, ...] = tuple(i.value for i in ChordFormula.__getitem__(self.quality).value)
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
