class Polynomial:
    __coefficients: list[float]

    def __init__(self, *_coefficients):
        self.current = 0
        if isinstance(_coefficients[0], float) or isinstance(_coefficients[0], int):
            self.__coefficients = Polynomial.remove_trailing_zeros(list(_coefficients))
        elif isinstance(_coefficients[0], list):
            self.__coefficients = Polynomial.remove_trailing_zeros(_coefficients[0])
        elif isinstance(_coefficients[0], dict):
            self.__coefficients = Polynomial.remove_trailing_zeros(
                [_coefficients[0][key] if key in _coefficients[0].keys() else 0 for key
                 in range(max(list(_coefficients[0].keys())) + 1)])
        elif isinstance(_coefficients[0], Polynomial):
            self.__coefficients = _coefficients[0].get_coefficients_as_list()

    def __repr__(self):
        return f"Polynomial{self.__coefficients}"

    def __str__(self):
        reversed_coefficient = self.__coefficients[::-1]

        def x_expr(_degree):
            if _degree == 0:
                result = ""
            elif _degree == 1:
                result = "x"
            else:
                result = "x^" + str(_degree)
            return result

        degree = len(self.__coefficients) - 1
        res = ""

        for i in range(0, degree + 1):
            _coefficient = reversed_coefficient[i]

            if abs(_coefficient) == 1 and i < degree:
                res += f"{'+' if _coefficient > 0 else '-'}{x_expr(degree - i)}"
            elif _coefficient != 0:
                res += f"{_coefficient:+g}{x_expr(degree - i)}"

        return res.lstrip('+')

    def __eq__(self, other):
        return self.__coefficients == other.get_coefficients_as_list()

    def __add__(self, other):
        if isinstance(other, Polynomial):
            result_list = [0] * max(len(self.__coefficients), len(other.__coefficients))
            for i in range(len(self.__coefficients)):
                result_list[i] += self.__coefficients[i]
            for i in range(len(other.__coefficients)):
                result_list[i] += other.__coefficients[i]
        elif isinstance(other, int) or isinstance(other, float):
            result_list = self.__coefficients
            result_list[0] += other
        else:
            return NotImplemented
        return Polynomial(result_list)

    def __radd__(self, other):
        return Polynomial.__add__(other, self)

    def __iadd__(self, other):
        self.__coefficients = Polynomial.__add__(self, other).get_coefficients_as_list()
        return self

    def __neg__(self):
        return Polynomial(self * -1)

    def __sub__(self, other):
        return Polynomial.__add__(self, -other)

    def __rsub__(self, other):
        return Polynomial.__add__(other, -self)

    def __isub__(self, other):
        self.__coefficients = Polynomial.__sub__(self, other).get_coefficients_as_list()
        return self

    def __call__(self, x):
        result_sum = self.__coefficients[0]
        for i in range(1, len(self.__coefficients)):
            result_sum += self.__coefficients[i] * (x ** i)
        return result_sum

    def degree(self) -> int:
        return len(self.__coefficients) - 1

    def der(self, d=1):
        if not d:
            return self
        if d > 0:
            result_list = [self.__coefficients[i] * i for i in range(1, len(self.__coefficients))]
            for i in range(1, d):
                result_list = [result_list[i] * i for i in range(1, len(result_list))]
            return Polynomial(result_list)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result_list = [0] * (len(other.__coefficients) + len(self.__coefficients))
            for i in range(len(other.__coefficients)):
                for j in range(len(self.__coefficients)):
                    result_list[i + j] += other.__coefficients[i] * self.__coefficients[j]

        elif isinstance(other, int) or isinstance(other, float):
            result_list = [0] * len(self.__coefficients)
            for i in range(len(self.__coefficients)):
                result_list[i] += self.__coefficients[i] * other
        else:
            return NotImplemented

        return Polynomial(result_list)

    def __rmul__(self, other):
        return Polynomial.__mul__(other, self)

    def __imul__(self, other):
        self.__coefficients = Polynomial.__mul__(self, other).get_coefficients_as_list()
        return self

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self.__coefficients):
            raise StopIteration
        value = self.__coefficients[self.current]
        self.current += 1
        return self.current-1, value

    def get_coefficients_as_list(self) -> list:
        return self.__coefficients

    @staticmethod
    def remove_trailing_zeros(lst: list) -> list:
        if not lst:
            return lst
        elif lst[-1] == 0:
            return Polynomial.remove_trailing_zeros(lst[:-1])
        else:
            return lst
