def R_1_01():
    def is_multiple(n, m):
        return n % m == 0

    assert is_multiple(10, 5)
    assert is_multiple(7, 3) is False


def R_1_02():
    def is_even(k):
        _, rem = divmod(k, 2)
        return rem == 0

    assert is_even(4)
    assert is_even(5) is False


def R_1_03():
    def minmax(data):
        _min = _max = data[0]
        for n in data:
            if n < _min:
                _min = n
            if n > _max:
                _max = n
        return _min, _max

    input_1 = [82, 9, 36, 11, 14, 18, 90, 17, 35, 54]
    input_2 = [100, 6, 79, 100, 59, 89, 2, 90, 7, 95]

    assert minmax(input_1) == (9, 90)
    assert minmax(input_2) == (2, 100)


def R_1_04():
    def f(n):
        assert n > 0, "input value must be greater than zero"
        return sum([i ** 2 for i in range(n)])

    result = f(10)
    assert result == 285, f"result: {result}"


def R_1_05():
    pass  # completed in R-1.4


def R_1_06():
    def f(n):
        assert isinstance(n, int) and n > 0, "input value must be a positive integer"
        return sum([i ** 2 for i in range(1, n, 2)])

    assert f(10) == 165
    assert f(7) == 35


def R_1_07():
    pass  # completed in R-1.6


def R_1_08():
    s = "telephone"
    k = -5
    # to get the equivalent value of s[k] using j ≥ 0
    # we would flip the sign and subtract 1, because
    # indexing with positive integers starts at zero
    # whereas indexing with negative integers starts at -1
    j = -k - 1
    assert s[k] == s[j]


def R_1_09():
    assert list(range(50, 80 + 1, 10)) == [50, 60, 70, 80]


def R_1_10():
    assert list(range(8, -8 - 1, -2)) == [8, 6, 4, 2, 0, -2, -4, -6, -8]


def R_1_11():
    exp = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    assert [2 ** i for i in range(len(exp))] == exp


def R_1_12():
    import random

    def choice(data):
        assert data, "data must be a non-empty sequence"
        range_min, range_max = min(data), max(data) + 1
        c = None
        while c not in data:
            c = random.randrange(range_min, range_max)
        return c

    exp = [82, 9, 36, 11, 14, 18, 90, 17, 35, 54]
    choices = set()

    for _ in range(100):
        choices.add(choice(exp))

    assert choices == set(exp), f"\n\texp: {set(exp)}\n\tact: {choices}"


def C_1_13():
    def reverse(seq):
        n = len(seq)
        a = []
        for i, k in enumerate(range(n - 1, -1, -1)):
            a.append(seq[k])
        return a

    exp = [5, 4, 3, 2, 1]
    act = reverse([1, 2, 3, 4, 5])

    assert list(reversed([1, 2, 3, 4, 5])) == exp
    assert act == exp, f"\n\tact: {act}\n\texp: {exp}"


def C_1_14():
    def f(seq):
        for i in seq:
            for j in seq:
                if i == j:
                    continue
                if i * j % 2 != 0:
                    return True
        return False

    assert f([3, 6, 8, 10]) is False
    assert f([3, 6, 7, 10]) is True


def C_1_15():
    def distinct(seq):
        seen = set()
        for n in seq:
            if n in seen:
                return False
            seen.add(n)
        return True

    assert distinct([1, 2, 3, 4, 5])
    assert distinct([1, 2, 2, 3, 4]) is False


def C_1_16():
    # Scale function from page 25
    def scale(data, factor):
        for j in range(len(data)):
            data[j] *= factor

    seq = [1, 2, 3, 4, 5]
    scale(seq, 2)

    # int objects are immutable, but the list that contains them is mutable.
    # The scale functions mutates the list by replacing each item with a new
    # instance of int.
    assert seq == [2, 4, 6, 8, 10]


def C_1_17():
    def scale(data, factor):
        for val in data:
            val *= factor

    # No, data will stay the same. In the updated scale function, val is assigned to a
    # new int object on each iteration; but this new value is never inserted into data
    # ie. data is never mutated.
    seq = [1, 2, 3, 4, 5]
    scale(seq, 2)
    assert seq == [1, 2, 3, 4, 5]


def C_1_18():
    exp = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
    # the factors of each number are (n, n-1)
    # 1 * 0, 2 * 1, 3 * 2, ...
    act = [n * (n - 1) for n in range(1, 11)]
    assert act == exp


def C_1_19():
    exp = [
        # fmt: off
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        # fmt: on
    ]
    start = ord("a")
    stop = ord("z") + 1
    act = [chr(n) for n in range(start, stop)]
    assert act == exp


def C_1_20():
    pass


if __name__ == "__main__":
    R_1_01()
    R_1_02()
    R_1_03()
    R_1_04()
    R_1_05()
    R_1_06()
    R_1_07()
    R_1_08()
    R_1_09()
    R_1_10()
    R_1_11()
    R_1_12()
    C_1_13()
    C_1_14()
    C_1_15()
    C_1_16()
    C_1_17()
    C_1_18()
    C_1_19()
