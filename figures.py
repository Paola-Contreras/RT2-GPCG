import numpy as np
from math import  pi 
import math_lib as ml 

WHITE = (1,1,1)
BLACK = (0,0,0)

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2


class Intersect(object):
    def __init__(self, distance, point, normal, texcoords, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.texcoords = texcoords
        self.sceneObj = sceneObj

class Material(object):
    def __init__(self, diffuse = WHITE, spec = 1.0, ior = 1.0, texture = None, matType = OPAQUE):
        self.diffuse = diffuse
        self.spec = spec
        self.ior = ior
        self.texture = texture
        self.matType = matType


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = ml.subtract(self.center, orig)
        tca = ml.dot(L, dir)
        
        #Magnitud de un vector 
        Sum= (L[0] **2 + L[1]**2 + L[2]**2)**0.5

        d = (Sum ** 2 - tca ** 2) ** 0.5
        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        # P = O + t0 * D
        mul = []
        for j in range(len(dir)):
            res = t0 * dir[j]
            mul.append(res)
        

        P = ml.add(orig, mul)
        normal = ml.subtract(P, self.center)
        normal = ml.normalized(normal)

        u = 1 - ((np.arctan2(normal[2], normal[0]) / (2 * pi)) + 0.5)
        v = np.arccos(-normal[1]) / pi

        uvs = (u,v)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         texcoords = uvs,
                         sceneObj = self)
