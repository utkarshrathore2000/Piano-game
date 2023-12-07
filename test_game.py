import unittest
from music_theory_game import calculate_semitones, generate_notes


class GameTestCase(unittest.TestCase):

    def test_calculate_semitones(self):
        # Test case where the first note is higher than the second
        note1 = "C#"
        note2 = "F"
        result = calculate_semitones(note1, note2)
        self.assertEqual(result, 4)

        # Test case where the second note is higher than the first
        note1 = "D"
        note2 = "A#"
        result = calculate_semitones(note1, note2)
        self.assertEqual(result, 4)

        # Test case where the notes are the same
        note1 = "E"
        note2 = "E"
        result = calculate_semitones(note1, note2)
        self.assertEqual(result, 0)

    def test_calculate_wrong_semitones(self):
        # Test case where the first note is higher than the second
        note1 = "C#"
        note2 = "F"
        result = calculate_semitones(note1, note2)
        self.assertNotEqual(result, 2)

        # Test case where the second note is higher than the first
        note1 = "D"
        note2 = "A#"
        result = calculate_semitones(note1, note2)
        self.assertNotEqual(result, 2)

        # Test case where the notes are the same
        note1 = "E"
        note2 = "E"
        result = calculate_semitones(note1, note2)
        self.assertNotEqual(result, 1)

    def test_generate_notes(self):
        # Test that two different notes are generated
        notes = generate_notes()
        self.assertNotEqual(notes[0], notes[1])
