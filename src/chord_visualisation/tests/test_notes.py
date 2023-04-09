import pytest

from core.notes import ChromaticNotes, MusicalNote


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (ChromaticNotes.get_note_by_standard_notation("A"), MusicalNote("A", "A", 27.5, None)),
        (ChromaticNotes.get_note_by_standard_notation("A#"), MusicalNote("A#", "Bb", 29.14, None)),
        (ChromaticNotes.get_note_by_standard_notation("B"), MusicalNote("B", "B", 30.87, None)),
        (ChromaticNotes.get_note_by_standard_notation("C"), MusicalNote("C", "C", 32.7, None)),
        (ChromaticNotes.get_note_by_standard_notation("C#"), MusicalNote("C#", "Db", 34.65, None)),
        (ChromaticNotes.get_note_by_standard_notation("D"), MusicalNote("D", "D", 36.71, None)),
        (ChromaticNotes.get_note_by_standard_notation("D#"), MusicalNote("D#", "Eb", 38.89, None)),
        (ChromaticNotes.get_note_by_standard_notation("E"), MusicalNote("E", "E", 41.2, None)),
        (ChromaticNotes.get_note_by_standard_notation("F"), MusicalNote("F", "F", 43.65, None)),
        (ChromaticNotes.get_note_by_standard_notation("F#"), MusicalNote("F#", "Gb", 46.25, None)),
        (ChromaticNotes.get_note_by_standard_notation("G"), MusicalNote("G", "G", 49, None)),
        (ChromaticNotes.get_note_by_standard_notation("G#"), MusicalNote("G#", "Ab", 51.91, None)),
    ],
)
def test_get_note_by_standard_notation(test_input, expected):
    assert test_input == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (ChromaticNotes.get_note_by_alternative_notation("A"), MusicalNote("A", "A", 27.5, None)),
        (ChromaticNotes.get_note_by_alternative_notation("Bb"), MusicalNote("A#", "Bb", 29.14, None)),
        (ChromaticNotes.get_note_by_alternative_notation("B"), MusicalNote("B", "B", 30.87, None)),
        (ChromaticNotes.get_note_by_alternative_notation("C"), MusicalNote("C", "C", 32.7, None)),
        (ChromaticNotes.get_note_by_alternative_notation("Db"), MusicalNote("C#", "Db", 34.65, None)),
        (ChromaticNotes.get_note_by_alternative_notation("D"), MusicalNote("D", "D", 36.71, None)),
        (ChromaticNotes.get_note_by_alternative_notation("Eb"), MusicalNote("D#", "Eb", 38.89, None)),
        (ChromaticNotes.get_note_by_alternative_notation("E"), MusicalNote("E", "E", 41.2, None)),
        (ChromaticNotes.get_note_by_alternative_notation("F"), MusicalNote("F", "F", 43.65, None)),
        (ChromaticNotes.get_note_by_alternative_notation("Gb"), MusicalNote("F#", "Gb", 46.25, None)),
        (ChromaticNotes.get_note_by_alternative_notation("G"), MusicalNote("G", "G", 49, None)),
        (ChromaticNotes.get_note_by_alternative_notation("Ab"), MusicalNote("G#", "Ab", 51.91, None)),
    ],
)
def test_get_note_by_alternative_notation(test_input, expected):
    assert test_input == expected
