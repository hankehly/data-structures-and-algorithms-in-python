def R_2_01():
    """
    3 examples of life-critical software applications are
      1. remote surgery software that moves robotic arms
      2. automated rocket ignition and trajectory adjustment software in space flight
      3. pacemakers
    """
    pass


def R_2_02():
    """
    An example of a software application where adaptability makes the difference between
    continued sales and bankruptcy is a data-analysis app. To be marketable to a wide
    audience, it must scale to different amounts of input. If the system was written in
    a way that assumes a maximum of N data-points, sales may be unable to target certain
    clients, or the company may lose its existing customers to competitors with more
    scalable systems.
    """
    pass


def R_2_03():
    """
    An example text-editor GUI may encapsulate behavior to process key-strokes, save a
    text file, print a text file, or pass a text file to the python interpreter to run
    as a program.
    """
    pass


def R_2_04():
    class Flower:
        def __init__(self, name: str = "iris", n_petals: int = 5, price: float = 0.99):
            self._name = name
            self._n_petals = n_petals
            self._price = price

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @property
        def n_petals(self):
            return self._n_petals

        @n_petals.setter
        def n_petals(self, value):
            self._n_petals = value

        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, value):
            if value < 0:
                raise ValueError("price must be positive")
            self._price = value

    f = Flower()
    assert f.name == "iris"
    f.name = "foo"
    assert f.name == "foo"

    try:
        f.price = -1
    except ValueError:
        assert True
    else:
        assert False


def R_2_05():
    class CreditCard:
        def charge(self, price):
            if not isinstance(price, (int, float)):
                raise TypeError("price must be numeric")


def R_2_06():
    class CreditCard:
        def make_payment(self, amount):
            if not isinstance(amount, (int, float)):
                raise TypeError("amount must be numeric")
            elif amount < 0:
                raise ValueError("amount cannot be negative")


def R_2_07():
    class CreditCard:
        def __init__(self, customer, bank, acnt, limit, balance=0):
            self._customer = customer
            self._bank = bank
            self._account = acnt
            self._limit = limit
            self._balance = balance


def R_2_08():
    class CreditCard:
        def __init__(self, customer, bank, acnt, limit, balance=0):
            self._customer = customer
            self._bank = bank
            self._account = acnt
            self._limit = limit
            self._balance = balance

        @property
        def bank(self):
            return self._bank

        @property
        def balance(self):
            return self._balance

        def charge(self, price):
            if self._balance + price > self._limit:
                return False
            else:
                self._balance += price
                return True

    def run():
        wallet = [
            CreditCard("John Archer", "KS Savings", "1234 5678 9101 1121", 2500),
            CreditCard("John Archer", "KS Federal", "4321 5678 9101 1121", 3500),
            CreditCard("John Archer", "KS Finance", "2413 5678 9101 1121", 5000),
        ]

        for i in range(1, 100):
            for j, card in enumerate(wallet, start=1):
                price = i * j
                if not card.charge(price):
                    print(f"{card.bank} (i={i}, balance={card.balance}, price={price})")
                    return

    # run()


def R_2_09():
    class Vector:
        def __init__(self, d):
            self._coords = [0] * d

        def __len__(self):
            return len(self._coords)

        def __getitem__(self, item):
            return self._coords[item]

        def __setitem__(self, key, value):
            self._coords[key] = value

        def __sub__(self, other):
            if len(other) != len(self):
                raise ValueError("dimensions must agree")
            result = Vector(len(other))
            for i in range(len(result)):
                result[i] = self[i] - other[i]
            return result

    u = Vector(3)
    u[0] = 3
    u[1] = 3
    u[2] = 3
    v = Vector(3)
    v[0] = 4
    v[1] = 1
    v[2] = 3
    r = u - v
    assert r[0] == -1
    assert r[1] == 2
    assert r[2] == 0


def R_2_10():
    class Vector:
        def __init__(self, d):
            self._coords = [0] * d

        def __len__(self):
            return len(self._coords)

        def __getitem__(self, item):
            return self._coords[item]

        def __setitem__(self, key, value):
            self._coords[key] = value

        def __neg__(self):
            result = Vector(len(self))
            for i in range(len(result)):
                result[i] = -self[i]
            return result

    v = Vector(3)
    v[0] = 1
    v[1] = 0
    v[2] = -1
    r = -v
    assert r[0] == -1
    assert r[1] == 0
    assert r[2] == 1


if __name__ == "__main__":
    R_2_01()
    R_2_02()
    R_2_03()
    R_2_04()
    R_2_05()
    R_2_06()
    R_2_07()
    R_2_08()
    R_2_09()
    R_2_10()
