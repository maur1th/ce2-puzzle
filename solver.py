# puzzle solver
import re
import itertools


permutations = [x for x in itertools.permutations(range(1,10))]
eq = "x+13*x/x+x+12*x-x-11+x*x/x-10-66"


# class Variable:
#     all_values = set(x for x in range(1,10))
#     count = itertools.count()

#     def __init__(self):
#         self.possible_values = [x for x in range(1,10)]
#         self.value = None
#         next(self.__class__.count)

#     def __repr__(self):
#         return str(self.value)


# def get_variables(eq):
#     var, counter = dict(), 0
#     for c in eq:
#         if c.isalpha():
#             key = "var" + str(counter)
#             var[key] = Variable()
#             counter += 1
#     return var


def evaluate(eq, variables):
    for v in variables:
        eq = re.sub(r'[a-z]', str(v), eq, 1)
    return eval(eq)


def solve(eq, permutations):
    for permutation in permutations:
        try:
            result = evaluate(eq, permutation)
        except ZeroDivisionError:
            result = None
        if result == 0:
            return permutation


solution = solve(eq, permutations)
print(solution)

# var = get_variables(eq)
