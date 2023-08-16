
# Note that changing the LOWER or UPPER bounds may also change the conditions for the information obtained from
# the conversation between Polly and Sam. This means that some of the eliminations may not be correct with other bounds.
# If the bounds are changed from 2 and 800 respectively, some of the elimination steps may need to be adjusted as well.
LOWER = 2
UPPER = 800


def problem():
    print("\nPolly and Sam are visited by a friend.\n"
          "The friend, having thought of two numbers between 2 and 800 inclusive,\n"
          "whispers their product to Polly and their sum to Sam.\n"
          "The following dialogue takes place:\n"
          "Polly:     I don’t know the two numbers\n"
          "Sam:       I know, and neither do I\n"
          "Polly:     I know the two numbers\n"
          "Sam:       So do I\n"
          "What are the two numbers?")


def number_of_pairs():
    pairs = [(x, y) for x in range(LOWER, UPPER + 1) for y in range(LOWER, UPPER + 1)]
    print(f'Total number of possible pairs, (x,y): '
          f'{(UPPER - LOWER + 1)} * {(UPPER - LOWER + 1)} = '
          f'{(UPPER - LOWER + 1) * (UPPER - LOWER + 1)}  ({len(pairs)})')


def redundant_pair_elimination():
    print(f'\nRedundant pairs are eliminated since (x,y) = (y,x)')
    print(f'Eliminated number of pairs: '
          f'{(UPPER - LOWER + 1) * (UPPER - LOWER + 1) - (UPPER - LOWER + 1) * (UPPER - LOWER + 2) // 2}')
    pairs = [(x, y) for x in range(LOWER, UPPER + 1) for y in range(x, UPPER + 1)]
    print(f'Remaining number of pairs: {(UPPER - LOWER + 1) * (UPPER - LOWER + 2) // 2}  ({len(pairs)})')
    return pairs


def prime_pair_elimination(pairs: list, primes: list):
    new_pairs = []
    print(f'\nEliminating prime pairs')
    num_pairs = len(pairs)
    for pair in pairs:
        if (pair[0] not in primes) or (pair[1] not in primes):
            new_pairs.append(pair)
    print(f'Eliminated number of pairs: {num_pairs - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return new_pairs


def qube_prime_elimination(pairs: list, primes: list):
    new_pairs = []
    print(f'\nEliminating pairs of the form (p, p^2) where p is a prime number.')
    num_pairs = len(pairs)
    for pair in pairs:
        if not ((pair[0] in primes) and (pair[1] == pair[0] * pair[0])):
            new_pairs.append(pair)
    print(f'Eliminated number of pairs: {num_pairs - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return new_pairs


def eliminating_even_sums(pairs):
    new_pairs = []
    print(f"\nEliminating pairs that have an even sum (Goldbach's conjecture)")
    num_pairs = len(pairs)
    for pair in pairs:
        if (pair[0] + pair[1]) % 2 == 1:
            new_pairs.append(pair)
    print(f'Eliminated number of pairs: {num_pairs - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return new_pairs


def eliminating_primes_plus_two_sums(pairs, primes):
    new_pairs = []
    primes_plus_2 = [p + 2 for p in primes]
    print(f"\nEliminating pairs that have a sum that is a prime plus 2")
    num_pairs = len(pairs)
    for pair in pairs:
        if (pair[0] + pair[1]) not in primes_plus_2:
            new_pairs.append(pair)
    print(f'Eliminated number of pairs: {num_pairs - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return new_pairs


def eliminating_pairs_with_sum_over_401(pairs):
    new_pairs = []
    print(f"\nEliminating pairs that have a sum greater than 401")
    num_pairs = len(pairs)
    for pair in pairs:
        if pair[0] + pair[1] < 402:
            new_pairs.append(pair)
    print(f'Eliminated number of pairs: {num_pairs - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return new_pairs


def eliminating_multiple_factorizations(pairs: list):
    print(f"\nEliminating pairs that have a product that can be factored in more than one way")
    num_pairs = len(pairs)
    factorizations = {}
    for pair in pairs:
        if pair[0] * pair[1] in factorizations.keys():
            factorizations[pair[0] * pair[1]].append(pair)
        else:
            factorizations[pair[0] * pair[1]] = [pair]
    new_pairs = []
    for num_f in factorizations.values():
        if len(num_f) == 1:
            new_pairs.append(num_f[0])
    print(f'Eliminated number of pairs: {num_pairs - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return new_pairs


def eliminating_multiple_sums(pairs: list):
    print(f"\nEliminating pairs that have a sum that can be produced in more than one way")
    num_pairs = len(pairs)
    summations = {}
    for pair in pairs:
        if pair[0] + pair[1] in summations.keys():
            summations[pair[0] + pair[1]].append(pair)
        else:
            summations[pair[0] + pair[1]] = [pair]
    new_pairs = []
    for num_s in summations.values():
        if len(num_s) == 1:
            new_pairs.append(num_s[0])
    print(f'Eliminated number of pairs: {num_pairs - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return new_pairs


def prime_list(limit):
    if limit < 2:
        return []
    else:
        primes = [2]
        for test_number in range(3, limit + 1, 2):
            is_prime = True
            for prime in primes:
                if test_number % prime == 0:
                    is_prime = False
                    break
                if prime * prime > test_number:
                    break
            if is_prime:
                primes.append(test_number)
    return primes


def main():
    primes = prime_list(800)
    problem()
    print("\n\nSOLUTION\n========")
    number_of_pairs()
    pairs = redundant_pair_elimination()
    pairs = prime_pair_elimination(pairs, primes)
    pairs = qube_prime_elimination(pairs, primes)
    pairs = eliminating_even_sums(pairs)
    pairs = eliminating_primes_plus_two_sums(pairs, primes)
    pairs = eliminating_pairs_with_sum_over_401(pairs)
    pairs = eliminating_multiple_factorizations(pairs)
    pairs = eliminating_multiple_sums(pairs)
    print(f'\nThe two number are: {pairs[0]}')


if __name__ == "__main__":
    main()
