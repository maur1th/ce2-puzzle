# puzzle solver
import re
import itertools


permutations = [x for x in itertools.permutations(range(1,10))]
eq = "x+13*x/x+x+12*x-x-11+x*x/x-10-66"


def evaluate(eq, variables):
    for v in variables:
        eq = re.sub(r'[a-z]', str(v), eq, 1)
    return eval(eq)


def solve(eq, permutations):
    for permutation in permutations:
        try:
            result = evaluate(eq, permutation)
        except ZeroDivisionError:
            continue
        if result == 0:
            return permutation


solution = solve(eq, permutations)
print(solution)
