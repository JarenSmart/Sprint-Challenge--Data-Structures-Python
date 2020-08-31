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
        return self.data


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.queue = [None]
#         self.tail = -1
#         self.head = 0
#         self.size = 0

#     def append(self, item):
#         if self.size == self.capacity:
#             print("Error : Ring is full")
#         else:
#             self.tail = (self.tail + 1) % self.capacity
#             self.queue[self.tail] = item
#             self.size = self.size + 1

#     def Dequeue(self):
#         if self.size == 0:
#             print("The ring is empty")
#             return
#         else:
#             x = self.queue[self.head]
#             self.head = (self.head + 1) % self.capacity
#         self.size = self.size - 1
#         return x

#     def get(self):
#         if self.size == 0:
#             print("The ring is empty")
#         else:
#             index = self.head

#             for i in range(self.size):
#                 print(self.queue[index])
#                 index = (index + 1) % self.capacity
