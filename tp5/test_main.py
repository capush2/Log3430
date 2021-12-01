import json
import math
import random
import re
import unittest
from tp5.main import evaluate
from tp5.renege import RENEGE
from tp5.vocabulary_creator import VocabularyCreator


def create_classify(train_set_name, test_set_name):
    vocab = VocabularyCreator()
    vocab.train_set = train_set_name
    vocab.create_vocab()

    renege = RENEGE()
    renege.email_file = train_set_name
    renege.classify_emails()

    return evaluate(test_set_name)


class TestCRUD(unittest.TestCase):
    original_accuracy = create_classify("train700.json", "test300.json")

    def setUp(self):
        self.fname_train = "train700.json"
        self.fname_test = "test300.json"
        self.fname_words = "words.txt"
        self.fname1 = "train700_mails.json"
        self.fname2 = "test300_mails.json"
        self.fname3 = "train700_words.json"
        self.fname4 = "test300_words.json"
        self.fname5 = "train700x2.json"
        self.fname6 = "test300x2.json"
        self.fname7 = "train700_noise.json"
        self.fname8 = "test300_noise.json"
        self.tolerance = 0.03
        pass

    def tearDown(self):
        print("Original accuracy = " + str(TestCRUD.original_accuracy))
        pass

    def test_property1(self):
        with open(self.fname_train) as train_set:
            mails = json.load(train_set)

        random.shuffle(mails["dataset"])

        with open(self.fname1, 'w') as new_set:
            json.dump(mails, new_set, indent=4)

        accuracy = create_classify(self.fname1, self.fname_test)
        self.assertLessEqual(abs(accuracy - TestCRUD.original_accuracy), self.tolerance)
        pass

    def test_property2(self):
        with open(self.fname_test) as test_set:
            mails = json.load(test_set)

        random.shuffle(mails["dataset"])

        with open(self.fname2, 'w') as new_set:
            json.dump(mails, new_set, indent=4)

        accuracy = create_classify(self.fname_train, self.fname2)
        self.assertLessEqual(abs(accuracy - TestCRUD.original_accuracy), self.tolerance)
        pass

    def test_property3(self):
        with open(self.fname_train) as train_set:
            mails = json.load(train_set)

        for mail in mails["dataset"]:
            subject_words = mail["mail"]["Subject"].split()
            body_words = mail["mail"]["Body"].split()
            random.shuffle(subject_words)
            random.shuffle(body_words)
            mail["mail"]["Subject"] = ' '.join(subject_words)
            mail["mail"]["Body"] = ' '.join(body_words)

        with open(self.fname3, 'w') as new_set:
            json.dump(mails, new_set, indent=4)
        accuracy = create_classify(self.fname3, self.fname_test)
        self.assertLessEqual(abs(accuracy - TestCRUD.original_accuracy), self.tolerance)
        pass

    def test_property4(self):
        with open(self.fname_test) as test_set:
            mails = json.load(test_set)

        for mail in mails["dataset"]:
            subject_words = mail["mail"]["Subject"].split()
            body_words = mail["mail"]["Body"].split()
            random.shuffle(subject_words)
            random.shuffle(body_words)
            mail["mail"]["Subject"] = ' '.join(subject_words)
            mail["mail"]["Body"] = ' '.join(body_words)

        with open(self.fname4, 'w') as new_set:
            json.dump(mails, new_set, indent=4)
        accuracy = create_classify(self.fname_train, self.fname4)
        self.assertLessEqual(abs(accuracy - TestCRUD.original_accuracy), self.tolerance)
        pass

    def test_property5(self):
        with open(self.fname_train) as train_set:
            mails = json.load(train_set)

        mails["dataset"] *= 2

        with open(self.fname5, 'w') as new_set:
            json.dump(mails, new_set, indent=4)
        accuracy = create_classify(self.fname5, self.fname_test)
        self.assertLessEqual(abs(accuracy - TestCRUD.original_accuracy), self.tolerance)
        pass

    def test_property6(self):
        with open(self.fname_test) as test_set:
            mails = json.load(test_set)

        mails["dataset"] *= 2

        with open(self.fname6, 'w') as new_set:
            json.dump(mails, new_set, indent=4)
        accuracy = create_classify(self.fname_train, self.fname6)
        self.assertLessEqual(abs(accuracy - TestCRUD.original_accuracy), self.tolerance)
        pass

    def test_property7(self):
        with open(self.fname_train) as train_set:
            mails = json.load(train_set)

        with open(self.fname_words) as noise_set:
            noise = re.sub('\ |\[|]|\'|\"', '', noise_set.read()).split(',')

        for mail in mails["dataset"]:
            n_sub_words = len(mail["mail"]["Subject"].split())
            n_body_words = len(mail["mail"]["Body"].split())
            sub_rand = random.sample(noise, math.floor(n_sub_words / 10))
            body_rand = random.sample(noise, math.floor(n_body_words / 10))
            mail["mail"]["Subject"] += ' ' + ' '.join(sub_rand)
            mail["mail"]["Body"] += ' ' + ' '.join(body_rand)

        with open(self.fname7, 'w') as new_set:
            json.dump(mails, new_set, indent=4)
        accuracy = create_classify(self.fname7, self.fname_test)
        self.assertLessEqual(abs(accuracy - TestCRUD.original_accuracy), self.tolerance)
        pass

    def test_property8(self):
        with open(self.fname_test) as test_set:
            mails = json.load(test_set)

        with open(self.fname_words) as noise_set:
            noise = re.sub('\ |\[|]|\'|\"', '', noise_set.read()).split(',')

        for mail in mails["dataset"]:
            n_sub_words = len(mail["mail"]["Subject"].split())
            n_body_words = len(mail["mail"]["Body"].split())
            sub_rand = random.sample(noise, math.floor(n_sub_words / 10))
            body_rand = random.sample(noise, math.floor(n_body_words / 10))
            mail["mail"]["Subject"] += ' ' + ' '.join(sub_rand)
            mail["mail"]["Body"] += ' ' + ' '.join(body_rand)

        with open(self.fname8, 'w') as new_set:
            json.dump(mails, new_set, indent=4)
        accuracy = create_classify(self.fname_train, self.fname8)
        self.assertLessEqual(abs(accuracy - TestCRUD.original_accuracy), self.tolerance)
        pass
