"""
A circular buffer is a collection of objects stored in a buffer that is treated
as though it is connected end-to-end in a circle. When an object is added to
this circular buffer, it is added to the position that immediately follows the
most recently added object, while removing an object always removes the object
that has been in the buffer the longest.

This works as long as there are empty spots in the buffer. If the buffer becomes
full, adding a new object to the buffer requires getting rid of an existing
object; with a circular buffer, the object that has been in the buffer the
longest is discarded and replaced by the new object.

Assuming we have a circular buffer with room for 3 objects, write a
CircularBuffer class in Python that implements a circular buffer for arbitrary
objects. The class should be initialized with the buffer size and provide the
following methods:

put: Add an object to the buffer

get: Remove (and return) the oldest object in the buffer. Return None if the
buffer is empty.

You may assume that none of the values stored in the buffer are
None (however, None may be used to designate empty spots in the buffer).

put method:
-Inputs: any object
-Output: None

Explicit Rules:
- function adds object to the buffer in the spot after the last added object
- if the buffer is empty, object is added to the first spot in the buffer
- if the buffer is full, the oldest added object is removed and the passed
  object is added in its place

from start of program:
- put = 1, oldest is 0, cur_idx is 0
- put = 2, oldest is 0, cur_idx is 1
- put = 3, oldest is 0, cur_idx is 2
- put = 4, oldest is (put % 3), cur_idx is oldest - 1
- put = 5, oldest is (put % 3), cur_idx is oldest - 1
- put = 6, oldest is (put % 3), cur_idx is oldest - 1
"""

"""
dict approach

bufferdict = dict()
put_key = 1
spaces = 3

def remove_oldest(buffer):
    remove_key = list(buffer.keys())[0]
    return buffer.pop[remove_key]

# put 1
bufferdict[put_key] = "obj1"  # put_key is 1
put_key += 1
if len(bufferdict) > spaces:
    remove_oldest(buffer_dict)
# result: bufferdict is { 1: "obj1" }, put_key is 2

# put 2
bufferdict[put_key] = "obj2"  # put_key is 2
put_key += 1
if len(bufferdict) > spaces:
    remove_oldest(buffer_dict)
# result: bufferdict is { 1: "obj1", 2: "obj2" }, put_key is 3

# get
return remove_oldest(buffer_dict)
# result: bufferdict is { 2: "obj 2" }, put_key is still 3

# put 3
bufferdict[put_key] = "obj3"  # put_key is 3
put_key += 1
if len(bufferdict) > spaces:
    remove_oldest(buffer_dict)
# result: bufferdict is { 2: "obj2", 3: "obj3" }, put_key is 4

# put 4
bufferdict[put_key] = "obj4"  # put_key is 4
put_key += 1
if len(bufferdict) > spaces:
    remove_oldest(buffer_dict)
# result: bufferdict is { 2: "obj2", 3: "obj3", 4: "obj4" }, put_key is 5

# get
return remove_oldest(buffer_dict)
# result: bufferdict is { 3: "obj3", 4: "obj4" }, put_key is still 5

# put 5
bufferdict[put_key] = "obj5"  # put_key is 5
put_key += 1
if len(bufferdict) > spaces:
    remove_oldest(buffer_dict)
# result: bufferdict is { 3: "obj3", 4: "obj4", 5: "obj5" }, put_key is 6

# put 6
bufferdict[put_key] = "obj5"  # put_key is 6
put_key += 1
if len(bufferdict) > spaces:
    remove_oldest(buffer_dict)
# result: bufferdict is { 3: "obj3", 4: "obj4", 5: "obj5" }, put_key is 7

# put 7
bufferdict[put_key] = "obj5"  # put_key is 7
put_key += 1
if len(bufferdict) > spaces:
    remove_oldest(buffer_dict)
# result: bufferdict is { 3: "obj3", 4: "obj4", 5: "obj5" }, put_key is 8
"""


# dictionary implementation
class CircularBuffer_dict:
    def __init__(self, spaces):
        self._spaces = spaces
        self._buffer = dict()
        self._put_key = 0

    def _increment_put_key(self):
        self._put_key = (self._put_key + 1) % self._spaces

    def _pop_oldest(self):
        if self._buffer:
            oldest_key = list(self._buffer)[0]
            return self._buffer.pop(oldest_key)
        return None

    def put(self, object):
        if len(self._buffer) + 1 > self._spaces:
            self._pop_oldest()
        self._buffer[self._put_key] = object
        self._increment_put_key()

    def get(self):
        return self._pop_oldest()


# single unordered list implementation:
class CircularBuffer_1list:
    def __init__(self, spaces):
        self._spaces = spaces
        self._buffer = []

    def put(self, object):
        self._buffer.append(object)
        if len(self._buffer) > self._spaces:
            del self._buffer[0]

    def get(self):
        if self._buffer:
            return self._buffer.pop(0)
        return None


# ordered object list + filled indices list implementation
class CircularBuffer_2lists:
    def __init__(self, spaces):
        self._spaces = spaces
        self._buffer = [None] * spaces
        self._filled_idxs = []
        self._insert_idx = 0

    def put(self, object):
        self._buffer[self._insert_idx] = object  # _insert_idx = 0 on first put

        self._filled_idxs.append(self._insert_idx)
        if len(self._filled_idxs) > self._spaces:
            del self._filled_idxs[0]
        # [0], [0, 1], [1], [1, 2], [1, 2, 0], [2, 0], [2, 0, 1], [0, 1, 2]

        self._insert_idx = (self._insert_idx + 1) % self._spaces
        # _insert_idx = 1, 2, 0, 1, 2, 0

    def get(self):
        if self._filled_idxs:
            oldest_idx = self._filled_idxs[0]
            oldest_obj = self._buffer[oldest_idx]
            self._buffer[oldest_idx] = None
            return oldest_obj
        return None


# Launch School solution (single ordered list implementation):
class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.next = 0
        self.oldest = 0

    def put(self, obj):
        next_item = (self.next + 1) % len(self.buffer)

        if self.buffer[self.next] is not None:
            self.oldest = next_item

        self.buffer[self.next] = obj
        self.next = next_item

    def get(self):
        value = self.buffer[self.oldest]
        self.buffer[self.oldest] = None
        if value is not None:
            self.oldest += 1
            self.oldest %= len(self.buffer)

        return value


buffer = CircularBuffer(3)

print(buffer.get() is None)  # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)  # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)  # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)  # True
print(buffer.get() == 6)  # True
print(buffer.get() == 7)  # True
print(buffer.get() is None)  # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)  # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)  # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)  # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)  # True
print(buffer2.get() == 5)  # True
print(buffer2.get() == 6)  # True
print(buffer2.get() == 7)  # True
print(buffer2.get() is None)  # True
