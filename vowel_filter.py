def vowel_filter(function):
    vowels = set('aeoiuyAEOUYI')

    def wrapper():
        res = function()
        return [i for i in res if i in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
