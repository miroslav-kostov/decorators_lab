from itertools import permutations
from math import inf


def find_current_sequence(num):
    return [x for x in range(1, num + 1)]


def possible_permutations(n):
    for el in permutations(n):
        yield list(el)


def permutation_results(all_possible_permutations, custom_res):
    for permutation in all_possible_permutations:
        current_case = list.copy(permutation)
        length = len(current_case)
        done = []
        res = 0
        for i in range(length - 1):
            min_no = inf
            min_idx = 0
            for x in range(len(current_case)):
                if current_case[x] < min_no:
                    min_idx = x
                    min_no = current_case[x]
            current_case = list(reversed(current_case[:min_idx + 1])) + current_case[min_idx + 1:]
            res += min_idx + 1
            done.append(current_case.pop(0))
        if res == custom_res:
            return list(permutation)


amount_of_tests = int(input())

for test_no in range(1, amount_of_tests + 1):
    current_test = input().split()
    size_of_wanted_list = int(current_test[0])
    desired_cost = int(current_test[1])
    the_current_sequence = find_current_sequence(size_of_wanted_list)
    all_permutations = list(possible_permutations(the_current_sequence))
    results_of_reversorting = permutation_results(all_permutations, desired_cost)
    try:
        print(f"Case #{test_no}: {' '.join([str(x) for x in results_of_reversorting])}")
    except:
        print(f"Case #{test_no}: IMPOSSIBLE")

