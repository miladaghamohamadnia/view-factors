from abc import ABC, abstractmethod

class Point(ABC):
  """
  Abstract Vector of coordinates representing a point
  """
  def __init__(self, elements=[]):
    self._elems = elements
    self.n = len(self._elems)
  
  def __len__(self):
    return len(self._elems)

  def __repr__(self):
    return "Point: " + " ".join([str(e) for e in self._elems])


class Coord:
  """
  coordinate data type
  """
  def __init__(self, val=0.0):
    self._val = val

  @property
  def val(self):
    return self._val
  
  @val.setter
  def val(self, val_s):
    self._val = val_s
  
  def __repr__(self):
    return f"val: {self._val}"
  

class Point2(Point):
  """
  Vector of 2d coordinates
  """
  def __init__(self, elements=[0, 0]):
    super().__init__(elements)


class Point3(Point):
  """
  Vector of 3d coordinates
  """
  def __init__(self, elements=[0, 0, 0]):
    super().__init__(elements)


def make_p(elements):
  """
  single point factory
  """
  if len(elements)==2:
    return Point2(elements)
  elif len(elements)==3:
    return Point3(elements)
  else:
    raise ValueError("number of input elements != 2,3")






if __name__ == "__main__":
  import random
  for el in range(100):
    C = make_p([random.randint(1,1000)]*3)
    print(C)


