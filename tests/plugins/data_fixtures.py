import pytest


@pytest.fixture(scope="class")
def data(request):
    first_name = request.param["first_name"]
    last_name = request.param["last_name"]
    phone = request.param["phone"]
    cc_name = request.param["cc_name"]
    cc_address = request.param["cc_address"]
    cc_zip = request.param["cc_zip"]
    cc_number = request.param["cc_number"]
    cc_exp = request.param["cc_exp"]
    cc_cvv = request.param["cc_cvv"]
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "cc_name": cc_name,
        "cc_address": cc_address,
        "cc_zip": cc_zip,
        "cc_number": cc_number,
        "cc_exp": cc_exp,
        "cc_cvv": cc_cvv,
    }
    yield payload
