from attrs import define
import enum


@define
class MusicalNote:
    """
    Musical note class.

    Args:
        standard_notation (str): Standard notation of the musical note.
        alternative_notation (str): Alternative notation of the musical note.
        base_frequency (float): The base frequency of the musical note.
        octave (int, optional): Octave for the musical note. Defaults to None.

    """

    standard_notation: str
    alternative_notation: str
    base_frequency: float
    octave: int | None = None


class ChromaticNotes(enum.Enum):
    """ChromaticNotes enum."""

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
        """Get a MusicalNote object by standard notation.

        Args:
            standard_notation (str): Standard notation of the musical note.

        Returns:
            MusicalNote: MusicalNote object.
        """
        return [i.value for i in cls.__members__.values() if i.value.standard_notation == standard_notation][0]

    @classmethod
    def get_note_by_alternative_notation(cls, alternative_notation: str) -> MusicalNote:
        """Get a MusicalNote object by alternative notation.

        Args:
            alternative_notation (str): Alternative notation of the musical note.

        Returns:
            MusicalNote: MusicalNote object.
        """
        for note in cls:
            if note.value.alternative_notation == alternative_notation:
                return note.value

    @classmethod
    def get_full_octave_from_starting_note(cls, starting_note: str) -> list[MusicalNote]:
        """Get a full octave of MusicalNote objects from a starting note.

        Args:
            starting_note (str): Starting note of the octave.

        Raises:
            ValueError: Starting note not in list.

        Returns:
            list[MusicalNote]: List of MusicalNote objects.
        """
        for idx, i in enumerate(cls.__members__.values()):
            if i.value.standard_notation == starting_note:
                starting_note_index = idx
                break
        else:
            raise ValueError("starting note not in list")
        return [i.value for i in cls][starting_note_index:] + [i.value for i in cls][:starting_note_index]

    @classmethod
    def get_full_octave_of_notes_and_distance_from_starting_note(cls, starting_note: str) -> dict[str, int]:
        """Get a full octave of MusicalNote objects and their distance from the starting note.

        Args:
            starting_note (str): Starting note of the octave.

        Returns:
            dict[str, int]: Dictionary of musical note standard notations and their distances from the starting note.
        """
        return {
            note.standard_notation: distance
            for distance, note in enumerate(cls.get_full_octave_from_starting_note(starting_note))
        }

    @classmethod
    def get_standard_notations_for_full_octave_from_starting_note(cls, starting_note: str) -> list[str]:
        """Get a full octave of standard notations from a starting note.

        Args:
            starting_note (str): Starting note of the octave.

        Returns:
            list[str]: List of musical note standard notations.
        """
        return [i.standard_notation for i in cls.get_full_octave_from_starting_note(starting_note)]

    @classmethod
    def get_standard_notation_from_alternative_notation(cls, alternative_notation: str) -> str:
        """
        Get the standard notation of a musical note from its alternative notation.
        In case no such object exists, the alternative notation is returned.

        Args:
            alternative_notation (str): Alternative notation of the musical note.

        Returns:
            str: Standard notation of the musical note.
        """
        try:
            return cls.get_note_by_alternative_notation(alternative_notation).standard_notation
        except AttributeError:
            return alternative_notation


if __name__ == "__main__":
    print(ChromaticNotes.get_standard_notations_for_full_octave_from_starting_note("A"))
