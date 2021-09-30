from vocabulary_creator import VocabularyCreator# pragma: no cover
import unittest# pragma: no cover
from unittest.mock import patch# pragma: no cover


class TestVocabularyCreator(unittest.TestCase):
    def setUp(self):
        self.mails = {"dataset": [
            {
                "mail": {
                    "Subject": "sub",
                    "Body": "body",
                    "Spam": "true",
                }
            },
            {
                "mail": {
                    "Subject": "sub",
                    "Body": "body",
                    "Spam": "false",
                }
            },
        ]}  # données pour mocker "return_value" du "load_dict"  # données pour mocker "return_value" du "load_dict"
        self.clean_subject_spam = ["not", "spam", "not", "not"]  # données pour mocker "return_value" du "clean_text"
        self.clean_body_spam = ["spam", "spam"]  # données pour mocker "return_value" du "clean_text"
        self.clean_subject_ham = ["not", "spam"]  # données pour mocker "return_value" du "clean_text"
        self.clean_body_ham = ["not", "not"]  # données pour mocker "return_value" du "clean_text"
        self.vocab_expected = {
            'p_body_ham': {
                'not': 0.75,
                'spam': 0.25
            },
            'p_body_spam': {
                'not': 0.5,
                'spam': 0.5
            },
            'p_sub_ham': {
                'spam': 1.0
            },
            'p_sub_spam': {
                'not': 1.0
            }
        }  # vocabulaire avec les valuers de la probabilité calculées correctement

    def tearDown(self):
        pass

    @patch("vocabulary_creator.VocabularyCreator.load_dict")
    @patch("vocabulary_creator.VocabularyCreator.clean_text")
    def test_create_vocab_spam_Returns_vocabulary_with_correct_values(
            self, mock_clean_text, mock_load_dict
    ):
        side_effect_arr = [self.clean_subject_spam, self.clean_body_spam, self.clean_subject_ham, self.clean_body_ham]

        def side_effect(arg1):
            return side_effect_arr.pop()

        mock_load_dict.return_value = self.mails
        mock_clean_text.side_effect = side_effect
        vocabulary_creator = VocabularyCreator()
        vocabulary_creator.create_vocab()
        self.assertEqual(vocabulary_creator.voc_data, self.vocab_expected)

        """Description: Tester qu'un vocabulaire avec les probabilités calculées
        correctement va être retourné. Il faut mocker les fonctions "load dict"
         (utiliser self.mails comme un return value simulé),"clean text"
         (cette fonction va être appelé quelques fois, pour chaque appel on
         va simuler la return_value different, pour cela il faut utiliser
         side_effect (vois l'exemple dans l'énonce)) et
         "write_data_to_vocab_file" qui va simuler "return True" au lieu
         d'écrire au fichier "vocabulary.json".
         if faut utiliser self.assertEqual(appele_a_create_vocab(), self.vocab_expected)
        """
        pass

    ###########################################
    #               CUSTOM TEST               #
    ###########################################
