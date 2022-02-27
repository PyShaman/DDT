import pytest

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
