LOW = 2
HIGH = 800
PROBLEM = f"""
Polly and Sam are visited by a friend.
The friend, having thought of two numbers between {LOW} and {HIGH} inclusive, 
whispers their product to Polly and their sum to Sam.
The following dialogue takes place:
Polly:     I don’t know the two numbers
Sam:       I know, and neither do I
Polly:     I know the two numbers
Sam:       So do I

What are the two numbers?"""


def initial_condition(low: int, high: int):
    pairs = [(x, y) for x in range(low, high + 1) for y in range(low, high + 1)]
    print(f'Total number of possible pairs, (x,y): '
          f'{(high - low + 1)} * {(high - low + 1)} = '
          f'{(high - low + 1) * (high - low + 1)}  ({len(pairs)})')


def redundant_pair_elimination(low: int, high: int) -> list:
    print(f'\nRedundant pairs are eliminated since (x,y) = (y,x)')
    print(f'Eliminated number of pairs: '
          f'{(high - low + 1) * (high - low + 1) - (high - low + 1) * (high - low + 2) // 2}')
    pairs = [(x, y) for x in range(low, high + 1) for y in range(x, high + 1)]
    print(f'Remaining number of pairs: {(high - low + 1) * (high - low + 2) // 2}  ({len(pairs)})')
    return pairs


def polly_does_not_know_the_numbers(pairs: list) -> list:
    print(f"\nPolly doesn't know the two numbers from the product she is told.")
    print(f"Eliminating pairs that have a product that can be produced in only one way")
    products = {}
    for pair in pairs:
        if pair[0] * pair[1] in products.keys():
            products[pair[0] * pair[1]].append(pair)
        else:
            products[pair[0] * pair[1]] = [pair]
    new_pairs = set()
    for num_p in products.values():
        if len(num_p) != 1:
            for new_pair in num_p:
                new_pairs.add(new_pair)
    print(f'Eliminated number of pairs: {len(pairs) - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return list(new_pairs)


def sam_knows_that_polly_does_not_know_the_numbers(pairs: list, original_pairs: list) -> list:
    new_pairs = []
    print(f"\nSam knows from the sum that he is told that Polly doesn't know the two numbers.")
    print(f"Eliminating pairs that have a sum of any of the removed pairs in the previous step.")
    removed_pairs = list(set(original_pairs) - set(pairs))
    forbidden_sums = set()
    for r_pair in removed_pairs:
        forbidden_sums.add(r_pair[0] + r_pair[1])
    for pair in pairs:
        if pair[0] + pair[1] not in forbidden_sums:
            new_pairs.append(pair)
    print(f'Eliminated number of pairs: {len(pairs) - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return list(new_pairs)


def sam_does_not_know_the_numbers(pairs: list) -> list:
    print(f"\nSam doesn't know the two numbers from the sum he is told and the remaining pairs.")
    print(f"Eliminating pairs that have a sum that can be produced in only one way")
    num_pairs = len(pairs)
    summations = {}
    for pair in pairs:
        if pair[0] + pair[1] in summations.keys():
            summations[pair[0] + pair[1]].append(pair)
        else:
            summations[pair[0] + pair[1]] = [pair]
    new_pairs = set()
    for num_s in summations.values():
        if len(num_s) != 1:
            for new_pair in num_s:
                new_pairs.add(new_pair)
    print(f'Eliminated number of pairs: {num_pairs - len(new_pairs)}')
    print(f'Remaining number of pairs: {len(new_pairs)}')
    return list(new_pairs)


def polly_knows_the_two_numbers(pairs: list) -> list:
    print(f"\nPolly knows what the two numbers are based on the product she has and the remaining pairs.")
    print(f"Her product can therefore only be factored in one way from the remaining pairs.")
    print(f"Eliminating pairs that have a product that can be factored in more than one way")
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


def sam_knows_the_two_numbers(pairs: list) -> list:
    print(f"\nSam knows what the two numbers are based on the sum he has and the remaining pairs.")
    print(f"His sum can therefore only be produced in one way from the remaining pairs.")
    print(f"Eliminating pairs that have a sum that can be produced in more than one way")
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


def main():
    print(PROBLEM)
    print("\n\nSOLUTION\n========")
    initial_condition(LOW, HIGH)
    original_pairs = redundant_pair_elimination(LOW, HIGH)
    pairs = polly_does_not_know_the_numbers(original_pairs)
    pairs = sam_knows_that_polly_does_not_know_the_numbers(pairs, original_pairs)
    pairs = sam_does_not_know_the_numbers(pairs)
    pairs = polly_knows_the_two_numbers(pairs)
    pairs = sam_knows_the_two_numbers(pairs)
    print(f'\nThe solution is: {pairs}')


if __name__ == "__main__":
    main()
