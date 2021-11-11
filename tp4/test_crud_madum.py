# TODO Test stuff baby
import unittest
from unittest.mock import patch


class TestCRUDMadum(unittest.TestCase):
    def setUp(self):
        # c'est un exemple de données "mock" à utiliser comme "return value" de read_users_file
        self.users_data = {
            "1": {
                "name": "alex@gmail.com",
                "Trust": 100,
                "SpamN": 0,
                "HamN": 20,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": ["default"],
            },
        }

    def tearDown(self):
        pass

    # On a crée un Getter get_users_data pour faciliter les tests. On va donc le tester aussi

    # ************Rapporteurs*****************
    def test_get_users_data(self):
        pass

    # ************Constructeur*****************
    def test_init(self):
        pass

    # *************Transformateurs*************
    # Pour simplifier l'écrire des test cases on a abbrévié les noms des méthodes,
    # On test les 4 transformateurs add_new_user, update_users, remove_user, remove_user_group dans tous les ordres
    # 4! = 24 test cases

    # A -> add_new_users
    # U -> update_users
    # R -> remove_users
    # G -> remove_user_group

    # A en first

    def test_AURG(self):
        pass

    def test_AUGR(self):
        pass

    def test_ARUG(self):
        pass

    def test_ARGU(self):
        pass

    def test_AGUR(self):
        pass

    def test_AGRU(self):
        pass

    # G en first
    def test_GURA(self):
        pass

    def test_GUAR(self):
        pass

    def test_GRUA(self):
        pass

    def test_GRAU(self):
        pass

    def test_GAUR(self):
        pass

    def test_GARU(self):
        pass

    # U en first
    def test_UARG(self):
        pass

    def test_UAGR(self):
        pass

    def test_URAG(self):
        pass

    def test_URGA(self):
        pass

    def test_UGAR(self):
        pass

    def test_UGRA(self):
        pass

    # R en first
    def test_RUAG(self):
        pass

    def test_RUGA(self):
        pass

    def test_RAUG(self):
        pass

    def test_RAGU(self):
        pass

    def test_RGUA(self):
        pass

    def test_RGAU(self):
        pass

    # ************Autres*****************
    # Il n'y a pas de méthodes autres à tester
