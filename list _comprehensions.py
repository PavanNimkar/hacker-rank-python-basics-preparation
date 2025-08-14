import itertools

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    nums = [x, y, z]
    x_permutation = []
    y_permutation = []
    z_permutation = []

    all_permutation = []
    x_permutation = [i for i in range(0, x + 1)]
    y_permutation = [i for i in range(0, y + 1)]
    z_permutation = [i for i in range(0, z + 1)]

    combined = [x_permutation, y_permutation, z_permutation]

    all_permutation = [
        list(combo_tuple) for combo_tuple in itertools.product(*combined)
    ]
    # got all permutations
    # print(all_permutation, type(all_permutation), len(all_permutation))
    # permutations in conditions

    output = [i for i in all_permutation if sum(i) != n]

    print(output)
