import unittest
from unittest.mock import patch


class TestCRUD(unittest.TestCase):
    def setUp(self):
        self.cum = "CUMMM" #Placeholder
    def tearDown(self):
        pass


    @patch("crud.CRUD.read_users_file")
    @patch("crud.CRUD.modify_groups_file")
    @patch("crud.CRUD.modify_users_file")
    def test_property1(
        self, mock_modify_users_file, mock_modify_groups_file, mock_read_users_file
    ):
        #Sample
        pass