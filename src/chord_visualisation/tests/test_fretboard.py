import pytest
from core.fretboard import FretboardNotes


@pytest.fixture
def fretboard():
    return FretboardNotes()


def test_get_note_from_fretboard_position(fretboard):
    assert fretboard.get_note(3, 3) == "A#"


def test_get_fret_position_from_note(fretboard):
    assert fretboard.get_fret_position_from_note("E") == [
        (1, 0),
        (1, 12),
        (6, 0),
        (6, 12),
        (2, 5),
        (3, 9),
        (4, 2),
        (5, 7),
    ]


def test_get_root_note_string_from_chord_shape(fretboard):
    assert fretboard.get_root_note_string_from_chord_shape([(1, 2), (2, 3), (3, 2)], "D") == 4
