def vowel_filter(function):

    def wrapper():

        result = function()
        vowels = "aieouy"
        return [x for x in result if x in vowels]

    return wrapper

