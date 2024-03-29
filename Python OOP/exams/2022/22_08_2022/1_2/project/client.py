class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0

        self.orders_dict = {}
        
    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, value: str):
        if not value.isdigit() or value[0] != "0" or len(value) < 10:
            raise ValueError("Invalid phone number!")

        self.__phone_number = value

