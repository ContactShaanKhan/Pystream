import functools

class Pystream():

    # Can set if we do inplace by default
    def __init__(self, data, default_in_place=False):
        self.data = data
        self.default_in_place = default_in_place

    def __apply_in_place(self, in_place, new_data):
        if in_place:
            self.data = new_data
            return self

        return Pystream(new_data, default_in_place=self.default_in_place)
              
    # Intermediate
    def map(self, func, in_place=None):
        if in_place is None:
            in_place = self.default_in_place

        _data = map(func, self.data)
        return self.__apply_in_place(in_place, _data)

    # Intermediate
    def filter(self, func, in_place=None):
        if in_place is None:
            in_place = self.default_in_place

        _data = filter(func, self.data)
        return self.__apply_in_place(in_place, _data)

    # Intermediate
    def reduce(self, func, in_place=None):
        if in_place is None:
            in_place = self.default_in_place

        _data = functools.reduce(func, self.data)
        return self.__apply_in_place(in_place, _data)
        
    # Terminal - collects to a list
    def collect(self):
        try:
            return list(self.data)
        except Exception:
            return self.data
