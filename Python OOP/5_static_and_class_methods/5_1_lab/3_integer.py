class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if type(float_value) != float:
            return "value is not a float"

        num = int(float_value)
        return cls(num)

    @classmethod
    def from_roman(cls, value: str):
        roman_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I':1}
        result = 0
        for i in range(len(value)):
            if roman_nums[value[i]] > roman_nums[value[i-1]] and i != 0:
                result += roman_nums[value[i]] - 2 * roman_nums[value[i-1]]
            else:
                result += roman_nums[value[i]]

        return cls(result)

    @classmethod
    def from_string(cls, value: str):
        if not type(value) == str:
            return "wrong type"

        elif not value.isdigit():
            return "wrong type"

        return cls(int(value))