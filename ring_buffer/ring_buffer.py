# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.data = [None]*capacity

    def append(self, item):
        self.data[self.current] = item  # adds item to ring
        if self.current < self.capacity - 1:  # if the items in ring are less than capacity
            self.current += 1  # increment to ring
        else:
            self.current = 0  # otherwise reset capacity to 0

    def get(self):
        # Return raw list instead of placeholder "None" initiated by self.data on line 25
        return [item for item in self.data if item != None]
