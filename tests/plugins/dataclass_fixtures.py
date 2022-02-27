import pytest

from libs.data.dataclass_feed import DataclassFeed1, DataclassFeed2, DataclassFeed3, DataclassFeed4


@pytest.fixture(scope="function")
def dc_1():
    return DataclassFeed1().return_data_1()


@pytest.fixture(scope="function")
def dc_2():
    return DataclassFeed2().return_data_2()


@pytest.fixture(scope="function")
def dc_3():
    return DataclassFeed3().return_data_3()


@pytest.fixture(scope="function")
def dc_4():
    return DataclassFeed4().return_data_4()
