import pytest
from assertpy import assert_that, soft_assertions

from libs.data.data_feed import DataClass


@pytest.mark.usefixtures("data")
@pytest.mark.parametrize("data",
                         [
                             DataClass.dict_1,
                             DataClass.dict_2,
                             DataClass.dict_3,
                             DataClass.dict_4,
                         ],
                         indirect=True)
class TestDataFeed:

    def test_01_use_values(self, data):
        print(f"User: {data['first_name']} {data['last_name']}")
        print(f"Phone {data['phone']}")
        print(f"Credit Card data: {data['cc_name']} , {data['cc_address']}, {data['cc_zip']}, "
              f"{data['cc_number']}, {data['cc_exp']}, {data['cc_cvv']},")
        with soft_assertions():
            assert_that(data['first_name']).is_instance_of(str)
            assert_that(data['last_name']).is_instance_of(str)
            assert_that(data['phone']).is_instance_of(str)
            assert_that(data['cc_name']).is_instance_of(str)
            assert_that(data['cc_address']).is_instance_of(str)
            assert_that(data['cc_zip']).is_instance_of(str)
            assert_that(data['cc_number']).is_instance_of(int)
            assert_that(data['cc_exp']).is_instance_of(str)
            assert_that(data['cc_cvv']).is_instance_of(int)
