from datetime import datetime

from crud import CRUD
import unittest
from unittest.mock import patch

import time


class TestCRUD(unittest.TestCase):
    def setUp(self):
        self.new_users_data = {
            "0": {
                "name": "steve@gmail.com",
                "Trust": 50,
                "SpamN": 0,
                "HamN": 0,
                "Date_of_first_seen_message": 1596844800.0,
                "Date_of_last_seen_message": 1596844800.0,
                "Groups": ["default"],
            },
        }
        self.no_mem_groups_data = {
            "0": {
                "name": "default",
                "Trust": 50,
                "List_of_members": [],
            }
        }
        self.filled_groups_data = {
            "0": {
                "name": "default",
                "Trust": 50,
                "List_of_members": ["steve@gmail.com"],
            }
        }

    def tearDown(self):
        pass

    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.modify_users_file")
    def test_add_new_user_Passes_correct_data_to_modify_users_file(
            self, mock_modify_users_file, mock_modify_groups_file, mock_read_users_file
    ):
        mock_read_users_file.return_value = {}
        mock_modify_users_file.return_value = True
        mock_modify_groups_file.return_value = True

        crud = CRUD()
        date = datetime.utcfromtimestamp(self.new_users_data["0"]["Date_of_first_seen_message"])
        crud.add_new_user(self.new_users_data["0"]["name"], date.strftime('%Y-%m-%d'))

        print("Test 1 executed")
        mock_modify_users_file.assert_called_once_with(self.new_users_data)

    @patch("crud.CRUD.read_groups_file")
    @patch("crud.CRUD.modify_groups_file")
    def test_add_new_group_Passes_correct_data_to_modify_groups_file(
            self, mock_modify_groups_file, mock_read_groups_file
    ):
        mock_read_groups_file.return_value = {}
        mock_modify_groups_file.return_value = True

        crud = CRUD()
        crud.add_new_group(self.no_mem_groups_data["0"]["name"], self.no_mem_groups_data["0"]["Trust"],
                           ["alex@gmail.com", "mark@mail.com"])

        print("Test 2 executed")
        mock_modify_groups_file.assert_called_once_with(self.no_mem_groups_data)

    @patch("crud.CRUD.read_users_file")
    def test_get_user_data_Returns_false_for_invalid_id(self, mock_read_users_file):
        mock_read_users_file.return_value = self.new_users_data
        crud = CRUD()

        print("Test 3 executed")
        self.assertFalse(crud.get_user_data("badId", "name"))

    @patch("crud.CRUD.read_users_file")
    def test_get_user_data_Returns_false_for_invalid_field(self, mock_read_users_file):
        mock_read_users_file.return_value = self.new_users_data
        crud = CRUD()

        print("Test 4 executed")
        self.assertFalse(crud.get_user_data("0", "badField"))

    @patch("crud.CRUD.read_users_file")
    def test_get_user_data_Returns_correct_value_if_field_and_id_are_valid(
            self, mock_read_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        crud = CRUD()

        print("Test 5 executed")
        self.assertEqual(crud.get_user_data("0", "name"), self.new_users_data["0"]["name"])

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_data_Returns_false_for_invalid_id(self, mock_read_groups_file):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        crud = CRUD()

        print("Test 6 executed")
        self.assertFalse(crud.get_groups_data("badId", "name"))

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_data_Returns_false_for_invalid_field(
            self, mock_read_groups_file
    ):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        crud = CRUD()

        print("Test 7 executed")
        self.assertFalse(crud.get_groups_data("0", "badField"))

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_data_Returns_correct_value_if_field_and_id_are_valid(
            self, mock_read_groups_file
    ):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        crud = CRUD()

        print("Test 8 executed")
        self.assertEqual(crud.get_groups_data("0", "name"), self.no_mem_groups_data["0"]["name"])

    @patch("crud.CRUD.read_users_file")
    def test_get_user_id_Returns_false_for_invalid_user_name(
            self, mock_read_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        crud = CRUD()

        print("Test 9 executed")
        self.assertFalse(crud.get_user_id("badId"))

    @patch("crud.CRUD.read_users_file")
    def test_get_user_id_Returns_id_for_valid_user_name(self, mock_read_users_file):
        mock_read_users_file.return_value = self.new_users_data
        crud = CRUD()

        print("Test 10 executed")
        self.assertEqual(crud.get_user_id("steve@gmail.com"), "0")

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_id_Returns_false_for_invalid_group_name(
            self, mock_read_groups_file
    ):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        crud = CRUD()

        print("Test 11 executed")
        self.assertFalse(crud.get_user_id("badId"))

    @patch("crud.CRUD.read_groups_file")
    def test_get_group_id_Returns_id_for_valid_group_name(self, mock_read_groups_file):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        crud = CRUD()

        print("Test 12 executed")
        self.assertEqual(crud.get_group_id("default"), "0")

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    # Modify_user_file mock est inutile pour tester False pour update
    def test_update_users_Returns_false_for_invalid_id(
            self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        mock_modify_users_file.return_value = {}
        crud = CRUD()

        print("Test 13 executed")
        self.assertFalse(crud.update_users("badId", "name", "jean-paul.sartre@gmail.com"))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    def test_update_users_Returns_false_for_invalid_field(
            self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        mock_modify_users_file.return_value = {}
        crud = CRUD()

        print("Test 14 executed")
        self.assertFalse(crud.update_users("0", "badField", "jean-paul.sartre@gmail.com"))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    def test_update_users_Passes_correct_data_to_modify_users_file(
            self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        mock_modify_users_file.return_value = {}
        crud = CRUD()

        modified_user = {"0": self.new_users_data["0"].copy()}
        modified_user["0"]["name"] = "new@gmail.com"
        crud.update_users("0", "name", "new@gmail.com")

        print("Test 15 executed")
        mock_modify_users_file.assert_called_once_with(modified_user)

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")
    def test_update_groups_Returns_false_for_invalid_id(
            self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        mock_modify_groups_file.return_value = {}
        crud = CRUD()

        print("Test 16 executed")
        self.assertFalse(crud.update_users("badId", "name", "newGroup"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")
    def test_update_groups_Returns_false_for_invalid_field(
            self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        mock_modify_groups_file.return_value = {}
        crud = CRUD()

        print("Test 16 executed")
        self.assertFalse(crud.update_users("0", "badField", "newGroup"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")
    def test_update_groups_Passes_correct_data_to_modify_groups_file(
            self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        mock_modify_groups_file.return_value = {}
        crud = CRUD()

        modified_group = {"0": self.no_mem_groups_data["0"].copy()}
        modified_group["0"]["name"] = "newGroups"
        crud.update_groups("0", "name", "newGroups")

        print("Test 17 executed")
        mock_modify_groups_file.assert_called_once_with(modified_group)

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    def test_remove_user_Returns_false_for_invalid_id(
            self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        mock_modify_users_file.return_value = {}
        crud = CRUD()

        print("Test 18 executed")
        self.assertFalse(crud.remove_user("badId"))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    def test_remove_user_Passes_correct_value_to_modify_users_file(
            self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        mock_modify_users_file.return_value = {}
        crud = CRUD()

        print("Test 19 executed")
        crud.remove_user("0")
        mock_modify_users_file.assert_called_once_with({})

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    def test_remove_user_group_Returns_false_for_invalid_id(
            self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        mock_modify_users_file.return_value = {}
        crud = CRUD()

        print("Test 20 executed")
        self.assertFalse(crud.remove_user_group("badId", "default"))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    def test_remove_user_group_Returns_false_for_invalid_group(
            self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        mock_modify_users_file.return_value = {}
        crud = CRUD()

        print("Test 21 executed")
        self.assertFalse(crud.remove_user_group("0", "badGroup"))

    @patch("crud.CRUD.modify_users_file")
    @patch("crud.CRUD.read_users_file")
    def test_remove_user_group_Passes_correct_value_to_modify_users_file(
            self, mock_read_users_file, mock_modify_users_file
    ):
        mock_read_users_file.return_value = self.new_users_data
        mock_modify_users_file.return_value = {}
        crud = CRUD()

        modified_user = {"0": self.new_users_data["0"].copy()}
        modified_user["0"]["Groups"] = []

        crud.remove_user_group("0", "default")

        print("Test 22 executed")
        mock_modify_users_file.assert_called_once_with(modified_user)

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")
    def test_remove_group_Returns_false_for_invalid_id(
            self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        mock_modify_groups_file.return_value = {}
        crud = CRUD()

        print("Test 23 executed")
        self.assertFalse(crud.remove_group("badId"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")
    def test_remove_group_Passes_correct_value_to_modify_groups_file(
            self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.no_mem_groups_data
        mock_modify_groups_file.return_value = {}
        crud = CRUD()

        crud.remove_group("0")

        print("Test 24 executed")
        mock_modify_groups_file.assert_called_once_with({})

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")
    def test_remove_group_member_Returns_false_for_invalid_id(
            self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.filled_groups_data
        mock_modify_groups_file.return_value = {}
        crud = CRUD()

        print("Test 25 executed")
        self.assertFalse(crud.remove_group_member("badId", "steve@gmail.com"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")
    def test_remove_group_member_Returns_false_for_invalid_group_member(
            self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.filled_groups_data
        mock_modify_groups_file.return_value = {}
        crud = CRUD()

        print("Test 26 executed")
        self.assertFalse(crud.remove_group_member("0", "badUser"))

    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.read_groups_file")
    def test_remove_group_member_Passes_correct_value_to_modify_groups_file(
            self, mock_read_groups_file, mock_modify_groups_file
    ):
        mock_read_groups_file.return_value = self.filled_groups_data
        mock_modify_groups_file.return_value = {}
        crud = CRUD()

        crud.remove_group_member("0", "steve@gmail.com")

        print("Test 27 executed")
        mock_modify_groups_file.assert_called_once_with(self.no_mem_groups_data)

    ###########################################
    #               CUSTOM TEST               #
    ###########################################

    # TODO Test coverage doit etre > 80 commencer avec test_update_users_specific_case