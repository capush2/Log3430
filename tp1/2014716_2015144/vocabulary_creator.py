import json  # pragma: no cover
from text_cleaner import TextCleaning  # pragma: no cover


class VocabularyCreator:
    """Class for creating vocabulary of spam and non-spam messages"""

    def __init__(self):
        self.train_set = "train_set.json"
        self.cleaning = TextCleaning()
        self.vocabulary = "vocabulary.json"
        self.voc_data = {}

    def compute_proba(self, data, total, min_occ):
        '''
        Description: calcul la probabilité de chaque mot du dictionnaire basé sur
        sa fréquence d'occurence
        Sortie: le dictionnaire des probabilité pour chaque mot
        '''
        proba_dict = {}
        # Création d'une copie pour itérer, ensuite on vérifie que la condition minimale d'occurence est remplie.
        # Si elle n l'est pas, on diminue le total et on retire l'entrée de la map.
        copy = data.copy()
        for wd in copy:
            nb_occ = copy[wd]
            if nb_occ < min_occ:
                data.pop(wd)
                total -= nb_occ

        # Le reste du calcul s'effectue sur la map raccourcie
        for wd in data:
            proba_dict[wd] = data[wd] / total

        return proba_dict

    def create_vocab(self, min_occ=1, clean_option=0):
        '''
        Description: fonction pour creer le vocabulaire des mots presents
        dans les e-mails spam et ham et le sauvegarder dans le fichier
        vocabulary.json selon le format specifie dans la description de lab
        Sortie: bool, 'True' pour succes, 'False' dans le cas de failure.
        '''
        print("Creating vocabulary")

        dataset = self.load_dict()

        occ_spam_sub = {}
        occ_spam_bod = {}
        occ_ham_sub = {}
        occ_ham_bod = {}

        total_occ_spam_sub = 0
        total_occ_ham_sub = 0
        total_occ_spam_bod = 0
        total_occ_ham_bod = 0

        email_count = len(dataset["dataset"])
        i = 0

        # Analyze each email
        for email in dataset["dataset"]:
            i += 1
            print("\rEmail " + str(i) + "/" + str(email_count), end="")

            # Get data
            data = email["mail"]
            subject = data["Subject"]
            body = data["Body"]
            is_spam = False

            # Update the number of spams / hams  
            if data["Spam"] == "true":
                is_spam = True

            # Analyze the subject 
            subject = self.clean_text(subject, clean_option)
            if is_spam:
                for wd in subject:
                    total_occ_spam_sub += 1
                    # Add the word to the dictionary or update its occurence count
                    if wd not in occ_spam_sub:
                        occ_spam_sub[wd] = 1
                    else:
                        occ_spam_sub[wd] += 1
            else:
                for wd in subject:
                    total_occ_ham_sub += 1
                    # Add the word to the dictionary or update its occurence count
                    if wd not in occ_ham_sub:
                        occ_ham_sub[wd] = 1
                    else:
                        occ_ham_sub[wd] += 1

            # Analyze the body
            body = self.clean_text(body, clean_option)
            if is_spam:
                for wd in body:
                    total_occ_spam_bod += 1
                    # Add the word to the dictionary or update its occurence count
                    if wd not in occ_spam_bod:
                        occ_spam_bod[wd] = 1
                    else:
                        occ_spam_bod[wd] += 1
            else:
                for wd in body:
                    total_occ_ham_bod += 1
                    # Add the word to the dictionary or update its occurence count
                    if wd not in occ_ham_bod:
                        occ_ham_bod[wd] = 1
                    else:
                        occ_ham_bod[wd] += 1

        # Create the data dictionary
        p_sub_spam = self.compute_proba(occ_spam_sub, total_occ_spam_sub, min_occ)
        p_sub_ham = self.compute_proba(occ_ham_sub, total_occ_ham_sub, min_occ)
        p_body_spam = self.compute_proba(occ_spam_bod, total_occ_spam_bod, min_occ)
        p_body_ham = self.compute_proba(occ_ham_bod, total_occ_ham_bod, min_occ)

        self.voc_data = {
            "p_sub_spam": p_sub_spam,
            "p_sub_ham": p_sub_ham,
            "p_body_spam": p_body_spam,
            "p_body_ham": p_body_ham
        }

        # Save data
        with open(self.vocabulary, "w") as outfile:
            json.dump(self.voc_data, outfile, indent=4)

        print("\n")
        return True

    def load_dict(self):
        with open(self.train_set) as json_data:
            data_dict = json.load(json_data)
        return data_dict

    def write_data_to_vocab_file(self, vocab):
        try:
            with open(self.vocabulary, "w") as outfile:
                json.dump(vocab, outfile)
                print("Vocab created")
                return True
        except:
            return False

    def clean_text(self, text, clean_option):
        return self.cleaning.clean_text(text, clean_option)
