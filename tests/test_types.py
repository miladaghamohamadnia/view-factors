from src.types import *
import random


def test_points():
  for el in range(100):
    i = [random.randint(1,1000)]*3
    C = Factory_Primitives.make_a_point(i)
    print(C)

def test_polygons():
  for el in range(100):
    i1 = [random.randint(1,1000)]*3
    i2 = [random.randint(1,1000)]*3
    i3 = [random.randint(1,1000)]*3
    C = Factory_Primitives.make_a_poly(
        [Factory_Primitives.make_a_point(i1), 
        Factory_Primitives.make_a_point(i2), 
        Factory_Primitives.make_a_point(i3)])
    print(C)
