from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)

#earth = Material(texture = Texture("earthDay.bmp"))
#marble = Material(diffuse = (0.8,0.8,0.8), texture = Texture("marble.bmp"), spec = 32, matType= REFLECTIVE)

#canica = Material(diffuse = (0.8,0.8,1.0), texture = Texture("whiteMarble.bmp"), spec = 32, ior = 1.5, matType= TRANSPARENT)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)

glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
diamond = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 2.417, matType = TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))

#rtx.scene.append( Sphere(V3(-3,2,-10), 1, earth)  )
rtx.scene.append( Sphere(V3(-3,-2,-10), 1, brick)  )

#rtx.scene.append( Sphere(V3(0,2,-10), 1, marble)  )
rtx.scene.append( Sphere(V3(0,-2,-10), 1, mirror)  )

#rtx.scene.append( Sphere(V3(3,2,-10), 1, canica)  )
rtx.scene.append( Sphere(V3(3,-2,-10), 1, glass)  )

#rtx.scene.append( Sphere(V3(3, 2,-10), 1, stone)  )


rtx.glRender()

rtx.glFinish("output.bmp")