import os
from unittest import TestCase

from tests.unit.dbt_test_utils import *


class TestHashCheckMacro(TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        macro_type = 'internal'

        cls.dbt_test = DBTTestUtils(model_directory=f'{macro_type}/hash_check')

        os.chdir(TESTS_DBT_ROOT)

        cls.model = 'test_hash_check'

    def setUp(self) -> None:

        self.dbt_test.clean_target()

    # HASH_CHECK

    def test_hash_check_with_md5_setting(self):

        var_dict = {
            'hash': 'MD5'}

        process_logs = self.dbt_test.run_model(model=self.model, model_vars=var_dict)

        actual_sql = self.dbt_test.retrieve_compiled_model(self.model)

        expected_sql = "MD5_BINARY('^^')"

        self.assertIn('Done', process_logs)

        self.assertEqual(expected_sql, actual_sql)

    def test_hash_check_with_sha_setting(self):

        var_dict = {
            'hash': 'SHA'}

        process_logs = self.dbt_test.run_model(model=self.model, model_vars=var_dict)

        actual_sql = self.dbt_test.retrieve_compiled_model(self.model)

        expected_sql = "SHA2_BINARY('^^')"

        self.assertIn('Done', process_logs)

        self.assertEqual(expected_sql, actual_sql)

    def test_hash_check_with_default_setting(self):

        process_logs = self.dbt_test.run_model(model=self.model)

        actual_sql = self.dbt_test.retrieve_compiled_model(self.model)

        expected_sql = "MD5_BINARY('^^')"

        self.assertIn('Done', process_logs)

        self.assertEqual(expected_sql, actual_sql)
