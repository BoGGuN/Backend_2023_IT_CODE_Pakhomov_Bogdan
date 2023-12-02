class Counter:
    def __init__(self, initial_value):
        self.value = initial_value

    def inc(self):
        self.value += 1
        return self.value

    def dec(self):
        self.value -= 1
        return self.value


class ReverseCounter(Counter):
    """Наследование класса Count с измененными модулями"""
    def inc(self):
        self.value -= 1
        return self.value

    def dec(self):
        self.value += 1
        return self.value


def get_counter(number):
    if number >= 0:
        return Counter(number)
    else:
        return ReverseCounter(number)


counter = get_counter(5)
a = counter.inc()
b = counter.inc()
c = counter.inc()
d = counter.dec()
print(a, b, c, d)
counter = get_counter(-1)
a = counter.inc()
b = counter.inc()
c = counter.inc()
d = counter.dec()
print(a, b, c, d)
counter = get_counter(0)
a = counter.inc()
b = counter.inc()
c = counter.inc()
d = counter.dec()
print(a, b, c, d)
