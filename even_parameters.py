def even_parameters(func):
    def wrapper(*args):
        try:
            even_nums = tuple(x for x in args if x % 2 == 0)
            if even_nums == args:
                return func(*args)
            else:
                raise TypeError
        except TypeError:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


@even_parameters
def func(*args):
    return sum(args)

result = func(4, 4, 4)
if result == 12:
    print(True)
else:
    print(False)

@even_parameters
def func(*args):
    return sum(args)

result = func(4, 5, 4)
if result == "Please use only even numbers!":
    print(True)
else:
    print(False)
#
#    def test_with_non_integer_params(self):
#        @even_parameters
#        def func(*args):
#            return sum(args)
#
#        result = func(4, "4", 4)
#        self.assertEqual(result, "Please use only even numbers!")
#
#    def test_with_no_params(self):
#        @even_parameters
#        def func():
#            return "hi"
#
#        result = func()
#        self.assertEqual(result, "hi")
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#