from abc import ABCMeta, abstractmethod


class Abstract:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def use_concrete_implementation(self):
        print(self._concrete_method())

    @abstractmethod
    def _concrete_method(self):
        pass


class Concrete(Abstract):
    def _concrete_method(self):
        return 2 * 3

my_abc = Concrete()

my_abc.use_concrete_implementation()
