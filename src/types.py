from abc import ABC, abstractmethod


################### Abstract Types ###################
class Point(ABC):
  """
  Abstract Vector of coordinates representing a point
  """
  def __init__(self, coordinates=[]):
    self._coords = coordinates
    self.n = len(self._coords)
  
  def __len__(self):
    return len(self._coords)

  def __repr__(self):
    coords_str = " ".join([str(e) for e in self._coords])
    return f"Point {self.n}D: {coords_str}"

  def __str__(self):
    return self.__repr__()

class Poly(ABC):
  """
  Abstract Vector of coordinates representing a multidimensional Polygon
  """
  def __init__(self, points=[]):
    self._pts = points
    self.check_input(points)
    self.n = len(points)
  
  def check_input(self, points):
    if len(points)>0:
      for p in points: 
        if not isinstance(p, Point): 
          raise ValueError("input must be a list of Point objects")
          return

  def __len__(self):
    return len(self._pts)

  def __repr__(self):
    return "Polygon: \n" + "".join([" "+str(e)+"\n" for e in self._pts])

  def __str__(self):
    return self.__repr__()

class Body(ABC):
  """
  Abstract Vector of polygons representing a geometry body
  """
  def __init__(self, points=[]):
    self._pts = points
    self.check_input(points)
    self.n = len(points)
  
  def check_input(self, points):
    if len(points)>0:
      for p in points: 
        if not isinstance(p, Point): 
          raise ValueError("input must be a list of Point objects")
          return

  def __len__(self):
    return len(self._pts)

  def __repr__(self):
    return "Polygon: " + " ".join(["\t"+str(e) for e in self._pts])

  def __str__(self):
    return self.__repr__()

################### Special Types ###################

class Point2(Point):
  """
  Vector of 2d coordinates
  """
  def __init__(self, x=0, y=0):
    super().__init__([x,y])

class Point3(Point):
  """
  Vector of 3d coordinates
  """
  def __init__(self, x=0, y=0, z=0):
    super().__init__([x,y,z])

class Poly3(Poly):
  """
  Vector of 2d coordinates
  """
  def __init__(self, p1, p2, p3):
    super().__init__([p1, p2, p3])

class Poly4(Poly):
  """
  Vector of 3d coordinates
  """
  def __init__(self, p1, p2, p3, p4):
    super().__init__([p1, p2, p3, p4])

class meshbody(Body):
  """
  collection of faces forming a mesh body
  """
  def __init__(self, p1, p2, p3, p4):
    super().__init__([p1, p2, p3, p4])


################### Factory of Types ###################

class Factory_Primitives:
  """
  Factory methods for creating different geometries
  """
  @staticmethod
  def make_a_point(coordsList):
    """
    single 2 or 3 dimension point factory
      in: x, y, z , ...
      out: Point object
        example: make_a_point(2, 5, 7) --> Point3 object
    """
    if len(coordsList)==2: return Point2(*coordsList)
    elif len(coordsList)==3: return Point3(*coordsList)
    else: raise ValueError("number of input elements != 2,3")
  
  @staticmethod
  def make_a_poly(pointsList):
    """
    a single 3 or 4 vertice polygon factory
      in: p1, p2, p3 , ...
      out: Point object
        p1, p2, p3 = Point(0,2,3), Point(2,7,5), Point(5,2,7)
        example: make_a_poly(p1, p2, p3) --> Poly3 object
    """
    if len(pointsList)==3: return Poly3(*pointsList)
    elif len(pointsList)==4: return Poly4(*pointsList)
    else: raise ValueError("number of input elements != 2,3")





if __name__ == "__main__":
  import random
  for el in range(100):
    i = [random.randint(1,1000)]*3
    C = Factory_Primitives.make_a_point(i)
    print(C)

  for el in range(100):
    i1 = [random.randint(1,1000)]*3
    i2 = [random.randint(1,1000)]*3
    i3 = [random.randint(1,1000)]*3
    C = Factory_Primitives.make_a_poly(
      [Factory_Primitives.make_a_point(i1), 
      Factory_Primitives.make_a_point(i2), 
      Factory_Primitives.make_a_point(i3)])
    print(C)


