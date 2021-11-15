# TODO Test stuff baby
import unittest
from unittest.mock import patch

from crud import CRUD


class TestCRUDMadum(unittest.TestCase):
    def setUp(self):
        self.crud = CRUD()
        # c'est un exemple de données "mock" à utiliser comme "return value" de read_users_file        
        self.toAdd = {
            "name": "addName@gmail.com",
            "Trust": 100,
            "SpamN": 0,
            "HamN": 20,
            "Date_of_first_seen_message": 1596844800.0,
            "Date_of_last_seen_message": 1596844800.0,
            "Groups": ["default"],
        }
        self.toRemove = {
            "name": "removeName@gmail.com",
            "Trust": 100,
            "SpamN": 0,
            "HamN": 20,
            "Date_of_first_seen_message": 1596844800.0,
            "Date_of_last_seen_message": 1596844800.0,
            "Groups": ["default"],
        }
        self.toUpdate = {
            "name": "updateName@gmail.com",
            "Trust": 100,
            "SpamN": 0,
            "HamN": 20,
            "Date_of_first_seen_message": 1596844800.0,
            "Date_of_last_seen_message": 1596844800.0,
            "Groups": ["default"],
        }
        self.toRmvGroup = {
            "name": "rmvGroup@gmail.com",
            "Trust": 100,
            "SpamN": 0,
            "HamN": 20,
            "Date_of_first_seen_message": 1596844800.0,
            "Date_of_last_seen_message": 1596844800.0,
            "Groups": ["default"],
        }
        self.users_data = {
            "0": self.toRemove,
            "1": self.toUpdate,
            "2": self.toRmvGroup
        }
        self.dates = {
            "old": {
                "dateTime": "2020-08-08",
                "unix": 1596844800.0
            },
            "new": {
                "dateTime": "2020-07-07",
                "unix": 1594094400.0
            }
        }
        self.update_fields = {
            "name": {
                "field": "name",
                "old": "updateName@gmail.com",
                "new": "updatedName@gmail.com"
            },
            "Date_of_last_seen_message": {
                "field": "Date_of_last_seen_message",
                "old": 1596844800.0,
                "new": 1594094400.0
            },
            "Date_of_first_seen_message": {
                "field": "Date_of_first_seen_message",
                "old": 1596844800.0,
                "new": 1594094400.0
            },
            "Trust": {
                "field": "Trust",
                "old": 100,
                "new": 10
            },
            "SpamN": {
                "field": "SpamN",
                "old": 0,
                "new": 30
            },
            "Groups": {
                "field": "Groups",
                "old": ["default"],
                "new": ["default"]
            },
        }

    def tearDown(self):
        pass

    def find_user(self, name, data):
        for iter in data:
            if iter["name"] == name:
                return iter
        return False

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

    # A -> add_new_user
    # U -> update_users
    # R -> remove_users
    # G -> remove_user_group

    # A en first
    @patch("crud.CRUD.read_users_file")
    def test_AURG(self, mock_read_users_file):
        mock_read_users_file.return_value = self.users_data
        crud = CRUD()
        for field in self.update_fields:
            field_name = field["field"]
            self.assertTrue(self.find_user(self.toAdd["name"], crud.add_new_user(self.toAdd["name"], self.dates["old"])))
            crud.update_users("toUpdate", field, self.update_fields[field_name]["new"])
            crud.remove_user()
            crud.remove_user_group()

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
