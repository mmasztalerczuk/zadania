def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def call_func_in_given_range(foo, a, b):
    results = []
    for i in range(a, b):
        results.append(foo(i))
    return results


def print_elements_of_list(l):
    for index, element in enumerate(l):
        print(index + 1, element)


if __name__ == "__main__":
    print_elements_of_list(call_func_in_given_range(fizzbuzz, 1, 101))
