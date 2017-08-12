import ctypes

class DynamicArray:
##IN PROGRESS
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)
        

    def make_array(self, c):
        return (c * ctypes.py_object)

    def __len__(self):
        return self.size

    def __getitem__(self, i):
        if not 0 <= i < self.size:
            raise IndexError('invalid index')
        else:
            return self.array[i]

    def __str__(self):
        array_string = self.array[0]
        for i in range(1, self.size):
            array_string += ", " + str(self.array[i])

        return array_string

    def append(self, obj):
        if self.size == self.capacity:
            temp_array = self.make_array(2 * self.capacity)
            for i in range(self.size):
                temp_array[i] = self.array[i]
            self.array = temp_array
            self.array[self.capacity] = obj
            self.size += 1
        
