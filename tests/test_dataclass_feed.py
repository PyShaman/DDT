import pytest
from assertpy import assert_that, soft_assertions


@pytest.mark.usefixtures("dc_1", "dc_2", "dc_3", "dc_4")
class TestDataclassFeed:

    def test_01_check_dataclass_1_dict(self, dc_1):
        with soft_assertions():
            assert_that(dc_1["first_name"]).contains("John 1")
            assert_that(dc_1["last_name"]).contains("Doe 1")
            assert_that(dc_1["phone"]).contains("+48 665-778-111")
            assert_that(dc_1["cc_name"]).contains("John Doe 1")
            assert_that(dc_1["cc_address"]).contains("Secret 1")
            assert_that(dc_1["cc_zip"]).contains("64-111")
            assert_that(dc_1["cc_number"]).is_equal_to(4916981102414485)
            assert_that(dc_1["cc_exp"]).contains("01/11")
            assert_that(dc_1["cc_cvv"]).is_equal_to(111)

    def test_01_check_dataclass_2_dict(self, dc_2):
        with soft_assertions():
            assert_that(dc_2["first_name"]).contains("John 2")
            assert_that(dc_2["last_name"]).contains("Doe 2")
            assert_that(dc_2["phone"]).contains("+48 665-778-222")
            assert_that(dc_2["cc_name"]).contains("John Doe 2")
            assert_that(dc_2["cc_address"]).contains("Secret 2")
            assert_that(dc_2["cc_zip"]).contains("64-222")
            assert_that(dc_2["cc_number"]).is_equal_to(4929563524610349)
            assert_that(dc_2["cc_exp"]).contains("02/22")
            assert_that(dc_2["cc_cvv"]).is_equal_to(222)

    def test_01_check_dataclass_3_dict(self, dc_3):
        with soft_assertions():
            assert_that(dc_3["first_name"]).contains("John 3")
            assert_that(dc_3["last_name"]).contains("Doe 3")
            assert_that(dc_3["phone"]).contains("+48 665-778-333")
            assert_that(dc_3["cc_name"]).contains("John Doe 3")
            assert_that(dc_3["cc_address"]).contains("Secret 3")
            assert_that(dc_3["cc_zip"]).contains("64-333")
            assert_that(dc_3["cc_number"]).is_equal_to(375171031014166)
            assert_that(dc_3["cc_exp"]).contains("03/33")
            assert_that(dc_3["cc_cvv"]).is_equal_to(333)

    def test_01_check_dataclass_4_dict(self, dc_4):
        with soft_assertions():
            assert_that(dc_4["first_name"]).contains("John 4")
            assert_that(dc_4["last_name"]).contains("Doe 4")
            assert_that(dc_4["phone"]).contains("+48 665-778-444")
            assert_that(dc_4["cc_name"]).contains("John Doe 4")
            assert_that(dc_4["cc_address"]).contains("Secret 4")
            assert_that(dc_4["cc_zip"]).contains("64-444")
            assert_that(dc_4["cc_number"]).is_equal_to(6387317915618621)
            assert_that(dc_4["cc_exp"]).contains("04/44")
            assert_that(dc_4["cc_cvv"]).is_equal_to(444)
