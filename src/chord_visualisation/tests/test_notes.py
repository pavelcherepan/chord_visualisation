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


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            ChromaticNotes.get_full_octave_from_starting_note("A"),
            [
                MusicalNote("A", "A", 27.5, None),
                MusicalNote("A#", "Bb", 29.14, None),
                MusicalNote("B", "B", 30.87, None),
                MusicalNote("C", "C", 32.7, None),
                MusicalNote("C#", "Db", 34.65, None),
                MusicalNote("D", "D", 36.71, None),
                MusicalNote("D#", "Eb", 38.89, None),
                MusicalNote("E", "E", 41.2, None),
                MusicalNote("F", "F", 43.65, None),
                MusicalNote("F#", "Gb", 46.25, None),
                MusicalNote("G", "G", 49, None),
                MusicalNote("G#", "Ab", 51.91, None),
            ],
        ),
        (
            ChromaticNotes.get_full_octave_from_starting_note("C"),
            [
                MusicalNote("C", "C", 32.7, None),
                MusicalNote("C#", "Db", 34.65, None),
                MusicalNote("D", "D", 36.71, None),
                MusicalNote("D#", "Eb", 38.89, None),
                MusicalNote("E", "E", 41.2, None),
                MusicalNote("F", "F", 43.65, None),
                MusicalNote("F#", "Gb", 46.25, None),
                MusicalNote("G", "G", 49, None),
                MusicalNote("G#", "Ab", 51.91, None),
                MusicalNote("A", "A", 27.5, None),
                MusicalNote("A#", "Bb", 29.14, None),
                MusicalNote("B", "B", 30.87, None),
            ],
        ),
    ],
)
def test_get_full_octave_from_starting_note(test_input, expected):
    assert test_input == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            ChromaticNotes.get_full_octave_of_notes_and_distance_from_starting_note("A"),
            {"A": 0, "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7, "F": 8, "F#": 9, "G": 10, "G#": 11},
        )
    ],
)
def test_get_full_octave_of_notes_and_distance_from_starting_note(test_input, expected):
    assert test_input == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            ChromaticNotes.get_standard_notations_for_full_octave_from_starting_note("A"),
            ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],
        ),
    ],
)
def test_get_standard_notations_for_full_octave_from_starting_note(test_input, expected):
    assert test_input == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (ChromaticNotes.get_standard_notation_from_alternative_notation("Bb"), "A#"),
        (ChromaticNotes.get_standard_notation_from_alternative_notation("Db"), "C#"),
        (ChromaticNotes.get_standard_notation_from_alternative_notation("Eb"), "D#"),
    ],
)
def test_get_standard_notation_from_alternative_notation(test_input, expected):
    assert test_input == expected
