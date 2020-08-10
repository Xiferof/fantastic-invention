import unittest
import src.quiz as quiz


class TestUserMethods(unittest.TestCase):
    def test_quiz_is_unique(self):
        template = quiz.generate_random_backround_list()
        print(template)
        self.assertGreater(len(template), 5) # more than 5 colours?
        self.assertEqual(len(template), len(set(template)))