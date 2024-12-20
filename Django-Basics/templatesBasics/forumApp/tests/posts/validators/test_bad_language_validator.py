from unittest import TestCase
from django.core.exceptions import ValidationError
from forumApp.posts.validators import BadLanguageValidator


class TestBadLanguageValidator(TestCase):

    def test__bad_words_included__raises_validation_error(self):
        validator = BadLanguageValidator()

        with self.assertRaises(ValidationError) as ve:
            validator("bad_word2")

        self.assertEqual(
            "['The text contains bad words!']",
            str(ve.exception)
        )
