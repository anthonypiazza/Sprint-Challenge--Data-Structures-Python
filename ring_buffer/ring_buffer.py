from math import remainder

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # print(item)
    # print(f"Self Capacity: {self.capacity}, Current Size: {self.current}, Modulo: {remainder(self.current, 5)}")
    if self.current >= self.capacity:
      if self.current == 5:
        del self.storage[0]
        self.storage.insert(0, item)
        self.current = 6
      elif self.current == 6:
        del self.storage[1]
        self.storage.insert(1, item)
        self.current = 7
      elif self.current == 7:
        del self.storage[2]
        self.storage.insert(2, item)
        self.current = 8
      elif self.current == 8:
        del self.storage[3]
        self.storage.insert(3, item)
        self.current = 9
      elif self.current == 9:
        del self.storage[4]
        self.storage.insert(4, item)
        self.current = 5
    else:
      self.current+=1
      del self.storage[0]
      self.storage.insert(4, item)
    # print(self.current)
    

  def get(self):
    # print([i for i in self.storage if i is not None])
    return [i for i in self.storage if i is not None]