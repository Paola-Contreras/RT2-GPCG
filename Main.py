from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1020
height = 1020

# Materiales

solid = Material(diffuse = (0.3, 0.5, 0.3), spec = 16)
solid1 = Material(diffuse = (0, 0, 0.9), spec = 8)


mirror = Material(diffuse = (0.9, 0.3, 0.9), spec = 64, matType = REFLECTIVE)
mirror1 = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)

glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
glass1 = Material(diffuse = (0.7, 0.7, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("po.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))

rtx.scene.append( Sphere(V3(-3, 2,-10), 1, solid1)  )
rtx.scene.append( Sphere(V3(-3,-2,-10), 1, solid)  )

rtx.scene.append( Sphere(V3(0,2,-10), 1, mirror1)  )
rtx.scene.append( Sphere(V3(0,-2,-10), 1, mirror)  )

rtx.scene.append( Sphere(V3(3,2,-10), 1, glass1)  )
rtx.scene.append( Sphere(V3(3,-2,-10), 1, glass)  )


rtx.glRender()

rtx.glFinish("output.bmp")