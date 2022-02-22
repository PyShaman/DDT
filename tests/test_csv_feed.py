import unittest

from ddt import data, ddt, unpack

from libs.data.data_csv_feed import CSVFeed


@ddt
class TestCSV(unittest.TestCase):
    _data = CSVFeed().return_csv_data()

    @data(_data[0], _data[1], _data[2], _data[3])
    @unpack
    def test_01(self, a, b, c, d, e, f, g, h, i):
        print(f"""
        First Name: {a}
        Last Name: {b}
        phone: {c}
        cc_name: {d}
        cc_address: {e}
        cc_zip: {f}
        cc_number: {g}
        cc_exp: {h}
        cc_cvv: {i}
        """)
