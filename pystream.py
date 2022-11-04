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

    # Terminal - Apply this function to all the elements in the pystream
    def foreach(self, func):
        for elem in list(self.data):
            func(elem)

    # Flatten the list by any number of levels
    def flat(self, num_levels=1, in_place=None):
        if in_place is None:
            in_place = self.default_in_place

        def _concat(x, y):
            x_is_list = isinstance(x, list)
            y_is_list = isinstance(y, list)

            if x_is_list and y_is_list:
                return [*x, *y]
            if x_is_list:
                return [*x, y]
            if y_is_list:
                return [x, *y]
            return [x, y]            

        _data = self.data
        for i in range(0, num_levels):
            _data = functools.reduce(_concat, _data)
        
        return self.__apply_in_place(in_place, _data)
        
    def flatmap(self, func, in_place=None):
        if in_place is None:
            in_place = self.default_in_place

        _data = Pystream(self.data, True).map(func).flat().collect()
        return self.__apply_in_place(in_place, _data)

    # Terminal - collects to a list
    def collect(self):
        try:
            return list(self.data)
        except Exception:
            return self.data
