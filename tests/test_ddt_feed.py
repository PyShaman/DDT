import unittest

from assertpy import assert_that, soft_assertions
from ddt import ddt, file_data, data


def give_data():
    a = 1
    b = 2
    c = 0
    d = -1
    return a, b, c, d


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

    @data(give_data()[0], give_data()[1], give_data()[2], give_data()[3])
    def test_02(self, a):
        assert_that(a).is_greater_than_or_equal_to(1)
