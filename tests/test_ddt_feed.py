import unittest

from assertpy import assert_that, soft_assertions
from ddt import ddt, file_data, data


@ddt
class TestDDTFeed(unittest.TestCase):

    @file_data("../libs/data/ddt_feed.json")
    def test_01(self, first_name, last_name, phone, cc_name, cc_address, cc_zip, cc_number, cc_exp, cc_cvv):
        print(f"""
        {first_name}
        {last_name}
        {phone}
        {cc_name}
        {cc_address}
        {cc_zip}
        {cc_number}
        {cc_exp}
        {cc_cvv}
        """)
        with soft_assertions():
            assert_that(first_name).is_instance_of(str)
            assert_that(last_name).is_instance_of(str)
            assert_that(phone).is_instance_of(str)
            assert_that(cc_name).is_instance_of(str)
            assert_that(cc_address).is_instance_of(str)
            assert_that(cc_zip).is_instance_of(str)
            assert_that(cc_number).is_instance_of(int)
            assert_that(cc_exp).is_instance_of(str)
            assert_that(cc_cvv).is_instance_of(int)
