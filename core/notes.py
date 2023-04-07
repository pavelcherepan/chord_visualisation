from attrs import define
import enum


@define
class MusicalNote:
    standard_notation: str
    alternative_notation: str
    base_frequency: float
    octave: int | None = None


class ChromaticNotes(enum.Enum):
    A = MusicalNote("A", "A", 27.5, None)
    A_sharp = MusicalNote("A#", "Bb", 29.14, None)
    B = MusicalNote("B", "B", 30.87, None)
    C = MusicalNote("C", "C", 32.7, None)
    C_sharp = MusicalNote("C#", "Db", 34.65, None)
    D = MusicalNote("D", "D", 36.71, None)
    D_sharp = MusicalNote("D#", "Eb", 38.89, None)
    E = MusicalNote("E", "E", 41.2, None)
    F = MusicalNote("F", "F", 43.65, None)
    F_sharp = MusicalNote("F#", "Gb", 46.25, None)
    G = MusicalNote("G", "G", 49, None)
    G_sharp = MusicalNote("G#", "Ab", 51.91, None)

    @classmethod
    def get_note_by_standard_notation(cls, standard_notation: str) -> MusicalNote:
        return cls.__getitem__(standard_notation).value

    @classmethod
    def get_note_by_alternative_notation(cls, alternative_notation: str) -> MusicalNote:
        for note in cls:
            if note.value.alternative_notation == alternative_notation:
                return note.value

    @classmethod
    def get_full_octave_from_starting_note(cls, starting_note: str) -> list[MusicalNote]:
        n = cls.get_note_by_standard_notation(starting_note)
        starting_note_index = list(cls).index(cls.__getitem__(n.standard_notation))
        return list(cls)[starting_note_index:] + list(cls)[:starting_note_index]

    @classmethod
    def get_full_octave_of_notes_and_distance_from_starting_note(cls, starting_note: str) -> dict[str, int]:
        n = cls.get_note_by_standard_notation(starting_note)
        return {
            note.value.standard_notation: distance
            for distance, note in enumerate(cls.get_full_octave_from_starting_note(n))
        }


if __name__ == "__main__":
    print(ChromaticNotes.get_full_octave_of_notes_and_distance_from_starting_note(ChromaticNotes.E.value))
