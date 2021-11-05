import csv
import json

from vocabulary_creator import VocabularyCreator
from renege import RENEGE
from email_analyzer import EmailAnalyzer


def evaluate(use_log_prob=False, use_log_combine=False, clean_option=0):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    total = 0
    analyzer = EmailAnalyzer()
    with open("test_set.json") as email_file:
        new_emails = json.load(email_file)

    i = 0
    email_count = len(new_emails["dataset"])

    print("Evaluating emails \n")
    for e_mail in new_emails["dataset"]:
        i += 1
        print("\rEmail " + str(i) + "/" + str(email_count), end="")

        new_email = e_mail["mail"]
        subject = new_email["Subject"]
        body = new_email["Body"]
        spam = new_email["Spam"]

        # Passage des paramètres
        if (analyzer.is_spam(subject, body, use_log_prob, use_log_combine, clean_option)) and (spam == "true"):
            tp += 1
        if (not (analyzer.is_spam(subject, body, use_log_prob, use_log_combine, clean_option))) and (spam == "false"):
            tn += 1
        if (analyzer.is_spam(subject, body, use_log_prob, use_log_combine, clean_option)) and (spam == "false"):
            fp += 1
        if (not (analyzer.is_spam(subject, body, use_log_prob, use_log_combine, clean_option))) and (spam == "true"):
            fn += 1
        total += 1

    print("")
    print("\nAccuracy: ", round((tp + tn) / (tp + tn + fp + fn), 2))
    print("Precision: ", round(tp / (tp + fp), 2))
    print("Recall: ", round(tp / (tp + fn), 2))
    return True


def exec_test_set():
    first_line = True
    # Ouvrir le fichier csv, passer la première ligne et executer une fois par cas de test
    with open('SpamHam3.csv', newline='') as csvfile:
        test_set_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for test_case in test_set_reader:
            if first_line:
                first_line = False
                continue

            print(test_case)
            # 1. Creation de vocabulaire.
            vocab = VocabularyCreator()
            vocab.create_vocab(int(test_case[2]), int(test_case[3]))

            # 2. Classification des emails et initialisation de utilisateurs et groupes.
            renege = RENEGE()
            renege.classify_emails(bool(test_case[0]), bool(test_case[1]), int(test_case[3]))

            # 3. Evaluation de performance du modele avec la fonction evaluate()
            evaluate(bool(test_case[0]), bool(test_case[1]), int(test_case[3]))




if __name__ == "__main__":
    exec_test_set()
