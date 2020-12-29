import math
import random


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
    def shuffle_v1(data):
        """
        This was my first thought. This implementation keeps track of selected indices
        and explicitly chooses unused indices for selection in subsequent iterations.
        """
        n = len(data)
        indices_used = set()
        sample_index = None
        new_sequence = []
        for i in range(n):
            while sample_index is None or sample_index in indices_used:
                sample_index = random.randint(0, n - 1)
            indices_used.add(sample_index)
            new_sequence.append(data[sample_index])
        return new_sequence

    def shuffle_v2(data):
        """
        This implementation is what the author is probably suggesting. It's much more
        concise and mutates the input just like random.shuffle

        Procedure:
        1. Iterate over data indices (range(len(data)))
        2. At index i, select a random index j from data (random int between 0, n)
        3. Swap data[i] with data[j]
        4. Repeat steps 2, 3 until iteration is complete

        """
        n = len(data)
        for i in range(n):
            j = random.randint(i, n - 1)
            data[i], data[j] = data[j], data[i]
        return data

    # uncomment to check output
    # print(shuffle_v2([1, 2, 3, 4, 5]))


def C_1_21():
    def f():
        lines = []
        while True:
            try:
                text = input("Enter something, or type ctrl-D to continue: ")
                lines.append(text)
            except EOFError:
                break
        n = len(lines)
        # reverse the lines
        for i in range(n // 2):
            j = n - 1 - i
            lines[i], lines[j] = lines[j], lines[i]
        return lines

    # print(f())


def C_1_22():
    def dot_product(a, b):
        """
        The definition of dot product I found says to compute the sum of the products
        of corresponding pairs of values in 2 equal-length sequences; but the exercise
        says to return an array c of length n.

        To compute based on the above definition, just take the sum of c.
        """
        assert len(a) == len(b), "a and b must be the same length"
        n = len(a)
        c = [a[i] * b[i] for i in range(n)]
        return c

    act = dot_product([2, 4, 6], [3, 6, 9])
    exp = [6, 24, 54]
    assert act == exp


def C_1_23():
    def f():
        a = [1, 2, 3]
        try:
            a[99] = 4
        except IndexError:
            print("Don't try buffer overflow attacks in Python")

    # f()


def C_1_24():
    def compute_number_of_vowels(string):
        count = 0
        for char in string:
            if char in "aeiou":
                count += 1
        return count

    assert compute_number_of_vowels("hello world") == 3


def C_1_25():
    def remove_punctuation(s):
        upper = map(chr, range(ord("A"), ord("Z") + 1))
        lower = map(chr, range(ord("a"), ord("z") + 1))
        extra = {" "}
        valid = set(upper) | set(lower) | extra
        cp = ""
        for char in s:
            if char in valid:
                cp += char
        return cp

    assert remove_punctuation("Let's try, Mike.") == "Lets try Mike"


def C_1_26():
    def f(a, b, c):
        """
        The exercise hint says to try a case analysis for each pair of integers and an
        operator, so I check the distributive property.

        If we just want an int check, we could use isinstance or int constructor.
        """
        try:
            a, b, c = int(a), int(b), int(c)
            assert a * (b + c) == a * b + a * c
            return True
        except (TypeError, ValueError):
            return False

    def run():
        resp = input("Enter three numbers, separated by a space: ")
        args = resp.split(" ")
        validity = "valid" if f(*args) else "invalid"
        print(f"The values entered are {validity}")

    # run()


def C_1_27():
    def factors_v1(n):
        """
        This was my first thought – buffer the larger values and replay them later.
        """
        k = 1
        buf = []
        while k * k < n:
            if n % k == 0:
                yield k
                buf.insert(0, n // k)
            k += 1
        if k * k == n:
            yield k
        for val in buf:
            yield val

    def factors_v2(n):
        """
        This was another solution suggesting in the exercise hints. We start from the
        square root and check if n is divisible by i.
        """
        k = 1
        while k * k < n:
            if n % k == 0:
                yield k
            k += 1
        # at this point, k equals the square root of n
        for i in range(k, 0, -1):
            if n % i == 0:
                yield n // i

    n_ = 1000

    v1 = [x for x in factors_v1(n_)]
    v2 = [x for x in factors_v2(n_)]

    assert v1 == v2


def C_1_28():
    def norm(v, p=2):
        s = 0
        for n in v:
            s += n ** p
        return s ** 0.5

    assert norm((4, 3)) == 5
    assert norm((4, 3), p=3) == (4 ** 3 + 3 ** 3) ** 0.5


def P_1_29():
    s = "catdog"

    def v1():
        """
        Stacked for-loops approach
        """
        combos = []
        for a in s:
            for b in s:
                if b in [a]:
                    continue
                for c in s:
                    if c in [a, b]:
                        continue
                    for d in s:
                        if d in [a, b, c]:
                            continue
                        for e in s:
                            if e in [a, b, c, d]:
                                continue
                            for f in s:
                                if f in [a, b, c, d, e]:
                                    continue
                                combos.append(a + b + c + d + e + f)
        return set(combos)

    def v2():
        """
        Brute force approach using random.shuffle with deduplication step
        """
        combos = set()
        s_iter = list(s)
        for i in range(10_000):
            combos.add("".join(s_iter))
            random.shuffle(s_iter)
        return set(combos)

    def v3():
        """
        To be fair, I found this on the internet, and I still can't understand it
        completely.

        https://stackoverflow.com/questions/30281913/printing-all-possible-combinations-using-recursion
        """
        c = set()

        def words(chars, word=""):
            if chars:
                for char in chars:
                    words(chars - {char}, word + char)
            else:
                c.add(word)

        words(set("catdog"))
        return c

    assert v1() == v2() == v3()


def P_1_30():
    def f(v):
        """
        Calculates the number of times one must repeatedly divide v by 2 before getting
        a value less than 2.
        """
        assert v >= 2, "input must be greater than or equal to 2"
        n = 0
        while v >= 2:
            v /= 2
            n += 1
        return n

    # You can divide 3 by 2 once before getting a value lower than 2
    assert f(3) == int(math.log(3, 2)) == 1

    # You can divide 40 by 2 5 times before getting a value lower than 2
    assert f(40) == int(math.log(40, 2)) == 5

    # etc..
    assert f(127) == int(math.log(127, 2)) == 6


def P_1_31():
    """
    Mental notes:
    You buy something that costs $5.23
    You gave the clerk a $100 bill
    Your change is $94.77
    Can we give change with a $100 bill? No
    Can we give change with a $50 bill? Yes, 1. Now the amount due is $44.77
    Can we give change with a $20 bill? Yes, 2. Now the amount due is $4.77
    Can we give change with a $10 bill? No
    Can we give change with a $5 bill? No
    Can we give change with a $1 bill? Yes, 4. Now the amount due is $0.77
    Can we give change with a quarter? Yes, 3. Now the amount due is $0.02
    Can we give change with a dime? No
    Can we give change with a nickel? No
    Can we give change with a penny? Yes, 2. Now the amount due is $0.00
    Done.
    """

    def make_change(*, cost, paid, currency):
        assert cost <= paid

        currency_large_first = sorted(currency.items(), key=lambda x: -x[1])

        change = {}
        total_due = paid - cost

        for name, amount in currency_large_first:
            n, rem = divmod(total_due, amount)
            change[name] = int(n)
            total_due -= n * amount

        return change

    usd = {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.1,
        "quarter": 0.25,
        "one_dollar": 1.0,
        "five_dollar": 5.0,
        "ten_dollar": 10.0,
        "twenty_dollar": 20.0,
        "fifty_dollar": 50.0,
        "hundred_dollar": 100.0,
    }

    # yen = {
    #     "one_yen": 1,
    #     "five_yen": 5,
    #     "ten_yen": 10,
    #     "fifty_yen": 50,
    #     "one_hundred_yen": 100,
    #     "five_hundred_yen": 500,
    #     "one_thousand_yen": 1000,
    #     "five_thousand_yen": 5000,
    #     "ten_thousand_yen": 10_000,
    # }

    exp_usd = {
        "hundred_dollar": 0,
        "fifty_dollar": 1,
        "twenty_dollar": 2,
        "ten_dollar": 0,
        "five_dollar": 0,
        "one_dollar": 4,
        "quarter": 3,
        "dime": 0,
        "nickel": 0,
        "penny": 1,
    }

    act_usd = make_change(cost=5.23, paid=100.0, currency=usd)
    assert exp_usd == act_usd


def P_1_32():
    print("P-1.32 is not implemented")


def P_1_33():
    print("P-1.33 is not implemented")


def P_1_34():
    def run(sentence, *, n_typos=8, n_lines=100):
        n = len(sentence)
        row_iter = range(1, n_lines + 1)
        lines = []
        typo_ix = random.sample(row_iter, n_typos)
        alpha_chars = list(map(chr, range(ord("a"), ord("z") + 1)))
        n_alpha_chars = len(alpha_chars)

        for i in row_iter:
            ln = f"({i:03d}) "
            if i in typo_ix:
                typo_char_ix = random.randint(0, n - 1)
                replace_char_ix = random.randint(0, n_alpha_chars - 1)
                s_temp = list(sentence)
                s_temp[typo_char_ix] = alpha_chars[replace_char_ix]
                string = "".join([ln] + s_temp)
            else:
                string = "".join([ln] + list(sentence))
            lines.append(string)
        return lines

    # for l in run("I will never spam my friends again.", n_typos=40):
    #     print(l)


def P_1_35():
    def f(n):
        # not counting leap years!
        days_per_month = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        freq = {}
        for i in range(n):
            month = random.randint(1, 12)
            day = random.randint(1, days_per_month[month])
            date = str(month).zfill(2) + "-" + str(day).zfill(2)
            if date in freq:
                freq[date] += 1
            else:
                freq[date] = 1

        n_same_birthdays = 0
        for key, val in freq.items():
            if val > 1:
                n_same_birthdays += 1
        # if n > 23:
        #     pass
        return n_same_birthdays

    # for n in range(5, 101, 5):
    #     res = f(n)
        # print(n, res)

    print("P-1.35 is not implemented")


def P_1_36():
    print("P-1.36 is not implemented")


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
    C_1_20()
    C_1_21()
    C_1_22()
    C_1_23()
    C_1_24()
    C_1_25()
    C_1_26()
    C_1_27()
    C_1_28()
    P_1_29()
    P_1_30()
    P_1_31()
    P_1_32()
    P_1_33()
    P_1_34()
    P_1_35()
    P_1_36()
