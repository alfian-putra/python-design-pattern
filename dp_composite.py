#! /usr/bin/python3

from collections.abc import Iterable
from abc import ABC


class SingleValue:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value

class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for c in self:
            for i in c:
                result += i
        return result

class ManyValues(list, ValueContainer):
    pass

single_value = SingleValue(11)
other_values = ManyValues()
other_values.append(22)
other_values.append(33)

print("Single value : ")
print(single_value.value)

print("add all component of other_values :")
print(other_values)


