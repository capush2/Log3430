# TODO Test stuff baby
import copy

from crud import CRUD
import unittest
from unittest.mock import patch


class TestCRUDMadum(unittest.TestCase):
    def setUp(self):

        # 0 -> toRemove
        # 1 -> toUpdate
        # 2 -> toRmGroup
        # 3 -> toAdd
        self.users_data_init = {
            "0": {
                "name": "removeName@gmail.com",
                "Trust": 100,
                "SpamN": 0,
                "HamN": 20,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": ["default"],
            },
            "1": {
                "name": "updateName@gmail.com",
                "Trust": 100,
                "SpamN": 0,
                "HamN": 20,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": ["default"],
            },
            "2": {
                "name": "rmGroupName@gmail.com",
                "Trust": 100,
                "SpamN": 0,
                "HamN": 20,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": ["default"],
            },
        }

        self.users_data_add = {
            "name": "addName@gmail.com",
            "Trust": 50,
            "SpamN": 0,
            "HamN": 0,
            "Date_of_first_seen_message": 1596844800.0,
            "Date_of_last_seen_message": 1596844800.0,
            "Groups": ["default"],
        }

        self.oracle = [
            {
                "field": "name",
                "in": "updated@gmail.com",
                "new": "updated@gmail.com",
            },
            {
                "field": "Trust",
                "in": 50,
                "new": 50,
            },
            {
                "field": "SpamN",
                "in": 50,
                "new": 50,
            },
            {
                "field": "Date_of_last_seen_message",
                "in": "2020-08-09",
                "new": 1596931200,
            },
            {
                "field": "Date_of_first_seen_message",
                "in": "2020-08-07",
                "new": 1596758400,
            },
            {
                "field": "Groups",
                "in": ["group2"],
                "new": ["group2"],
            },
        ]

    def tearDown(self):
        pass

    # On a crée un Getter get_users_data pour faciliter les tests. On va donc le tester aussi

    # ************Rapporteurs*****************
    @patch("crud.CRUD.read_users_file")
    def test_get_users_data(self, mock_read_users_file):
        mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
        crud = CRUD()
        self.assertEqual(crud.get_users_data(), self.users_data_init)

    # ************Constructeur*****************
    @patch("crud.CRUD.read_users_file")
    def test_init(self, mock_read_users_file):
        mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
        crud = CRUD()
        self.assertEqual(crud.get_users_data(), self.users_data_init)

    # *************Transformateurs*************
    # Pour simplifier l'écrire des test cases on a abbrévié les noms des méthodes,
    # On test les 4 transformateurs add_new_user, update_users, remove_user, remove_user_group dans tous les ordres
    # 4! = 24 test cases

    # A -> add_new_users
    # U -> update_users
    # R -> remove_users
    # G -> remove_user_group

    def a(self, crud, oracle):
        if "0" not in oracle:
            oracle["0"] = copy.deepcopy(self.users_data_add)
        else:
            oracle["3"] = copy.deepcopy(self.users_data_add)
        self.assertEqual(crud.add_new_user(self.users_data_add["name"], "2020-08-08"), oracle)

    def u(self, crud, oracle, i):
        oracle["1"][self.oracle[i]["field"]] = self.oracle[i]["new"]
        self.assertEqual(crud.update_users("1", self.oracle[i]["field"], self.oracle[i]["in"]), oracle)

    def r(self, crud, oracle):
        oracle.pop("0")
        self.assertEqual(crud.remove_user("0"), oracle)

    def g(self, crud, oracle):
        oracle["2"]["Groups"] = []
        self.assertEqual(crud.remove_user_group("2", "default"), oracle)

    # A en first

    @patch("crud.CRUD.read_users_file")
    def test_AURG(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.a(crud, updated_user)

            self.u(crud, updated_user, i)

            self.r(crud, updated_user)

            self.g(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_AUGR(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.a(crud, updated_user)

            self.u(crud, updated_user, i)

            self.g(crud, updated_user)

            self.r(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_ARUG(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.a(crud, updated_user)

            self.r(crud, updated_user)

            self.u(crud, updated_user, i)

            self.g(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_ARGU(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.a(crud, updated_user)

            self.r(crud, updated_user)

            self.g(crud, updated_user)

            self.u(crud, updated_user, i)

    @patch("crud.CRUD.read_users_file")
    def test_AGUR(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.a(crud, updated_user)

            self.g(crud, updated_user)

            self.u(crud, updated_user, i)

            self.r(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_AGRU(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.a(crud, updated_user)

            self.g(crud, updated_user)

            self.r(crud, updated_user)

            self.u(crud, updated_user, i)

    # G en first
    @patch("crud.CRUD.read_users_file")
    def test_GURA(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.g(crud, updated_user)

            self.u(crud, updated_user, i)

            self.r(crud, updated_user)

            self.a(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_GUAR(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.g(crud, updated_user)

            self.u(crud, updated_user, i)

            self.a(crud, updated_user)

            self.r(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_GRUA(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.g(crud, updated_user)

            self.r(crud, updated_user)

            self.u(crud, updated_user, i)

            self.a(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_GRAU(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.g(crud, updated_user)

            self.r(crud, updated_user)

            self.a(crud, updated_user)

            self.u(crud, updated_user, i)

    @patch("crud.CRUD.read_users_file")
    def test_GAUR(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.g(crud, updated_user)

            self.a(crud, updated_user)

            self.u(crud, updated_user, i)

            self.r(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_GARU(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.g(crud, updated_user)

            self.a(crud, updated_user)

            self.r(crud, updated_user)

            self.u(crud, updated_user, i)

    # U en first
    @patch("crud.CRUD.read_users_file")
    def test_UARG(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.u(crud, updated_user, i)

            self.a(crud, updated_user)

            self.r(crud, updated_user)

            self.g(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_UAGR(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.u(crud, updated_user, i)

            self.a(crud, updated_user)

            self.g(crud, updated_user)

            self.r(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_URAG(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.u(crud, updated_user, i)

            self.r(crud, updated_user)

            self.a(crud, updated_user)

            self.g(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_URGA(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.u(crud, updated_user, i)

            self.r(crud, updated_user)

            self.g(crud, updated_user)

            self.a(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_UGAR(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.u(crud, updated_user, i)

            self.g(crud, updated_user)

            self.a(crud, updated_user)

            self.r(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_UGRA(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.u(crud, updated_user, i)

            self.g(crud, updated_user)

            self.r(crud, updated_user)

            self.a(crud, updated_user)

    # R en first
    @patch("crud.CRUD.read_users_file")
    def test_RUAG(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.r(crud, updated_user)

            self.u(crud, updated_user, i)

            self.a(crud, updated_user)

            self.g(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_RUGA(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.r(crud, updated_user)

            self.u(crud, updated_user, i)

            self.g(crud, updated_user)

            self.a(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_RAUG(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.r(crud, updated_user)

            self.a(crud, updated_user)

            self.u(crud, updated_user, i)

            self.g(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_RAGU(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.r(crud, updated_user)

            self.a(crud, updated_user)

            self.g(crud, updated_user)

            self.u(crud, updated_user, i)

    @patch("crud.CRUD.read_users_file")
    def test_RGUA(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.r(crud, updated_user)

            self.g(crud, updated_user)

            self.u(crud, updated_user, i)

            self.a(crud, updated_user)

    @patch("crud.CRUD.read_users_file")
    def test_RGAU(self, mock_read_users_file):

        for i in range(6):
            mock_read_users_file.return_value = copy.deepcopy(self.users_data_init)
            crud = CRUD()
            crud.add_new_group("group2", 75, [])

            updated_user = copy.deepcopy(self.users_data_init)

            self.r(crud, updated_user)

            self.g(crud, updated_user)

            self.a(crud, updated_user)

            self.u(crud, updated_user, i)

    # ************Autres*****************
    # Il n'y a pas de méthodes autres à tester
