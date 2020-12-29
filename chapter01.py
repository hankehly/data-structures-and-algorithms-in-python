def R_1_01():
    """
    R-1.1
    -----
    Write a short Python function, is_multiple(n, m), that takes two integer values and
    returns True if n is a multiple of m, that is, n = mi for some integer i, and False
    otherwise.
    """

    def is_multiple(n, m):
        return n % m == 0

    assert is_multiple(10, 5)
    assert is_multiple(7, 3) is False


def R_1_02():
    """
    R-1.2
    -----
    Write a short Python function, is_even(k), that takes an integer value and returns
    True if k is even, and False otherwise. However, your function cannot use the
    multiplication, modulo, or division operators.
    """

    def is_even(k):
        _, rem = divmod(k, 2)
        return rem == 0

    assert is_even(4)
    assert is_even(5) is False


def R_1_03():
    """
    R-1.3
    -----
    Write a short Python function, minmax(data), that takes a sequence of one or more
    numbers, and returns the smallest and largest numbers, in the form of a tuple of
    length two. Do not use the built-in functions min or max in implementing your
    solution.
    """

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
    """
    R-1.4
    -----
    Write a short Python function that takes a positive integer n and returns the sum of
    the squares of all the positive integers smaller than n.
    """

    def f(n):
        assert n > 0, "input value must be greater than zero"
        return sum([i ** 2 for i in range(n)])

    result = f(10)
    assert result == 285, f"result: {result}"


def R_1_05():
    """
    R-1.5
    -----
    Give a single command that computes the sum from Exercise R-1.4, relying on Python's
    comprehension syntax and the built-in sum function.
    """
    pass  # completed in R-1.4


def R_1_06():
    """
    R-1.6
    -----
    Write a short Python function that takes a positive integer n and returns the sum of
    the squares of all the odd positive integers smaller than n.
    """

    def f(n):
        assert isinstance(n, int) and n > 0, "input value must be a positive integer"
        return sum([i ** 2 for i in range(1, n, 2)])

    assert f(10) == 165
    assert f(7) == 35


def R_1_07():
    """
    R-1.7
    -----
    Give a single command that computes the sum from Exercise R-1.6, relying on Python's
    comprehension syntax and the built-in sum function.
    """
    pass  # completed in R-1.6


def R_1_08():
    """
    R-1.8
    -----
    Python allows negative integers to be used as indices into a sequence, such as a
    string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0,
    what is the equivalent index j ≥ 0 such that s[j] references the same element?
    """
    s = "telephone"
    k = -5
    # to get the equivalent value of s[k] using j ≥ 0
    # we would flip the sign and subtract 1, because
    # indexing with positive integers starts at zero
    # whereas indexing with negative integers starts at -1
    j = -k - 1
    assert s[k] == s[j]


def R_1_09():
    """
    R-1.9
    -----
    What parameters should be sent to the range constructor, to produce a range with
    values 50, 60, 70, 80?
    """
    assert list(range(50, 80 + 1, 10)) == [50, 60, 70, 80]


def R_1_10():
    """
    R-1.10
    ------
    What parameters should be sent to the range constructor, to produce a range with
    values 8, 6, 4, 2, 0, −2, −4, −6, −8?
    """
    assert list(range(8, -8 - 1, -2)) == [8, 6, 4, 2, 0, -2, -4, -6, -8]


def R_1_11():
    """
    R-1.11
    ------
    Demonstrate how to use Python's list comprehension syntax to produce the list
    [1, 2, 4, 8, 16, 32, 64, 128, 256].
    """
    exp = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    assert [2 ** i for i in range(len(exp))] == exp


def R_1_12():
    """
    R-1.12
    ------
    Python's random module includes a function choice(data) that returns a random
    element from a non-empty sequence. The random module includes a more basic function
    randrange, with parameterization similar to the built-in range function, that
    returns a random choice from the given range. Using only the randrange function,
    implement your own version of the choice function.
    """
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

    for _ in range(50):
        choices.add(choice(exp))

    assert choices == set(exp), f"\n\texp: {set(exp)}\n\tact: {choices}"


def C_1_13():
    """
    C-1.13
    ------
    Write a pseudo-code description of a function that reverses a list of n integers, so
    that the numbers are listed in the opposite order than they were before, and compare
    this method to an equivalent Python function for doing the same thing.
    """
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
