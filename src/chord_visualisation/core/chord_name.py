import enum
import itertools
from functools import reduce

from core.chord_shapes import ChordDiagram, FingerPosition
from core.chords import ChordFormula, Intervals
from core.fretboard import FretboardNotes
from core.notes import ChromaticNotes


class ChordNameGenerator:
    """
    Class tasked with generating a name of a chord
    based on the input chord diagram.
    """

    def __init__(self, tuning: tuple[str, ...] = ("E", "B", "G", "D", "A", "E")) -> None:
        self._tuning = tuning
        self.fretboard = FretboardNotes(tuning)

    def identify_root_note(self, diagram: ChordDiagram) -> None:
        """Get root note from a given chord diagram.
        Here we simply identify the lowest (register-wise) string
        that is either fretted or played open and consider the
        base note to be the root of the chord.

        TODO: This algorithm will need to be changed when slash chords are implemented.

        Args:
            diagram (ChordDiagram): A ChordDiagram object showing the
                position of fingers and also open/muted strings.
        """
        # we first extend the shape member with the values of open strings
        # giving them 0th fret.
        open_strings = [FingerPosition(i, 0) for i in diagram.open_strings]
        all_strings: list[FingerPosition] = diagram.shape + open_strings
        # then we reduce the resulting list to find the FingerPosition
        # with the highest string value
        max_string: FingerPosition = reduce(lambda x, y: x if x.string > y.string else y, all_strings)
        self.root_note: FingerPosition = max_string
        # Get the name of root note
        self.root_note_name = self.fretboard.get_note(string=max_string.string, fret=max_string.fret)

    def indentify_chord_quality(self, diagram: ChordDiagram) -> str | None:
        """Identify the chord's quality from the diagram. To do this we
        first need to identify root note, which is done in identify_root_note()
        method. Then counting from the root note, we get the distances in semitones
        for other notes of a triad. Finally, we match the collection of
        Intervals against known chord formulas.

        Args:
            diagram (ChordDiagram): A ChordDiagram object showing the
                position of fingers and also open/muted strings.
        """
        diag_with_open_strings = self._add_open_strings_to_diagram(diagram)
        notes = self._get_all_other_notes(diag_with_open_strings)
        dist = self._calculate_distances(notes)
        intervals = self._create_intervals(self.root_note_name, notes, dist)
        return self._get_chord_quality_from_formula(intervals)

    def _add_open_strings_to_diagram(self, diagram: ChordDiagram) -> ChordDiagram:
        open_strings = [FingerPosition(i, 0) for i in diagram.open_strings]
        diagram.shape += open_strings
        return diagram

    def _create_chromatic_scale(self, root_note: str):
        return ChromaticNotes.get_full_octave_of_notes_and_distance_from_starting_note(root_note)

    def _get_all_other_notes(self, diagram: ChordDiagram):
        # get names of all other notes in the chord
        return [self.fretboard.get_note(pos.string, pos.fret) for pos in diagram.shape]

    def _calculate_distances(self, notes: list[str]) -> list[int]:
        return [
            ChromaticNotes.get_full_octave_of_notes_and_distance_from_starting_note(starting_note=self.root_note_name)[
                i
            ]
            for i in notes
        ]

    def _create_intervals(self, root_note: str, notes: list[str], distances: list[int]):
        intervals_dict: dict[str, list[enum.Enum]] = {}
        for note, dist in zip(notes, distances):
            # add a perfect unison interval which will always be there
            # for the root note
            intervals_dict[root_note] = [Intervals.P1]
            # go through all intervals and if the distance
            # matches what we have available, add it to the list
            valid_intervals = [i[1] for i in Intervals._member_map_.items() if i[1].value == dist]
            intervals_dict[note] = valid_intervals
        return intervals_dict

    def _get_chord_quality_from_formula(self, intervals: dict[str, list[enum.Enum]]) -> str | None:
        # because some intervals can have same semitone ranges and it's important
        # to keep those ranges because they might result in different chords,
        # out intervals dict will have for each of the notes a list of up to
        # two intervals that such note can be from the root.
        #
        # Now we need to find the formula that matches this combination of
        # intervals. Now we go through and create all possible combinations
        # of our list elements and check them against the known formulas.
        comb: list[tuple[Intervals]] = list(itertools.product(*intervals.values()))

        # sort the resulting list according to the interval value
        comb_sorted: list[list[Intervals]] = [sorted(i, key=lambda x: x.value) for i in comb]

        # now go through all the chord formulas and see if any of them match
        for c in comb_sorted:
            for f in ChordFormula._member_map_.items():
                if f[1]._value_ == tuple(c):
                    return f[0]


if __name__ == "__main__":
    cng = ChordNameGenerator()
    # shape=[FingerPosition(1, 2), FingerPosition(2, 3), FingerPosition(3, 2)]
    # shape_2 = [FingerPosition(1, 1), FingerPosition(2, 3), FingerPosition(3, 2)]
    shape_3 = [FingerPosition(1, 3), FingerPosition(5, 2), FingerPosition(6, 3)]

    cd = ChordDiagram(shape=shape_3, open_strings=[2, 3, 4], muted_strings=[])
    cng.identify_root_note(cd)
    quality = cng.indentify_chord_quality(cd)
    print(f"{cng.root_note_name} {quality}")
