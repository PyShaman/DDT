from dataclasses import asdict, dataclass, field


@dataclass
class DataclassFeed1:

    first_name: str = field(default="John 1")
    last_name: str = field(default="Doe 1")
    phone: str = field(default="+48 665-778-111")
    cc_name: str = field(default="John Doe 1")
    cc_address: str = field(default="Secret 1")
    cc_zip: str = field(default="64-111")
    cc_number: str = field(default="4916981102414485")
    cc_exp: str = field(default="01/11")
    cc_cvv: str = field(default="111")

    def return_data_1(self):
        return asdict(self)


@dataclass
class DataclassFeed2:

    first_name: str = field(default="John 2")
    last_name: str = field(default="Doe 2")
    phone: str = field(default="+48 665-778-222")
    cc_name: str = field(default="John Doe 2")
    cc_address: str = field(default="Secret 2")
    cc_zip: str = field(default="64-222")
    cc_number: str = field(default="4929563524610349")
    cc_exp: str = field(default="02/22")
    cc_cvv: str = field(default="222")

    def return_data_2(self):
        return asdict(self)


@dataclass
class DataclassFeed3:

    first_name: str = field(default="John 3")
    last_name: str = field(default="Doe 3")
    phone: str = field(default="+48 665-778-333")
    cc_name: str = field(default="John Doe 3")
    cc_address: str = field(default="Secret 3")
    cc_zip: str = field(default="64-333")
    cc_number: str = field(default="375171031014166")
    cc_exp: str = field(default="03/33")
    cc_cvv: str = field(default="333")

    def return_data_3(self):
        return asdict(self)


@dataclass
class DataclassFeed4:

    first_name: str = field(default="John 4")
    last_name: str = field(default="Doe 4")
    phone: str = field(default="+48 665-778-444")
    cc_name: str = field(default="John Doe 4")
    cc_address: str = field(default="Secret 4")
    cc_zip: str = field(default="64-444")
    cc_number: str = field(default="6387317915618621")
    cc_exp: str = field(default="04/44")
    cc_cvv: str = field(default="444")

    def return_data_4(self):
        return asdict(self)
