import math_lib as ml 
import numpy as np

DIR_LIGHT = 0
POINT_LIGHT = 1
AMBIENT_LIGHT = 2

def reflectVector(normal, direction):
    reflect = 2 * ml.dot(normal, direction)
    temp=[]
    for i in range(len(normal)):
        value = reflect * normal[i]
        temp.append(value)
    reflect = temp
    reflect = ml.subtract(reflect, direction)
    reflect = ml.normalized(reflect)
    return reflect

def refractVector(normal, direction, ior):
    #Snell´s law
    pass

def fresnel (normal, direction, ior):
    #Fresnel Equation
    pass


class DirectionalLight(object):
    def __init__(self, direction = (0,-1,0), intensity = 1, color = (1,1,1)):
        self.direction = ml.normalized(direction)
        self.intensity = intensity
        self.color = color
        self.lightType = DIR_LIGHT

    def getDiffuseColor(self, intersect, raytracer):
        light_dir = self.direction * -1
        intensity = ml.dot(intersect.normal, light_dir) * self.intensity
        intensity = float(max(0, intensity))            
                                                        
        diffuseColor = [intensity * self.color[0],
                        intensity * self.color[1],
                        intensity * self.color[2]]

        return diffuseColor

    def getSpecColor(self, intersect, raytracer):
        temp3 = []
        for i in range(len(self.direction)):
            number = self.direction[i] * -1
            temp3.append(number)

        light_dir = temp3
        reflect = reflectVector(intersect.normal, light_dir)

        view_dir = ml.subtract( raytracer.camPosition, intersect.point)
        view_dir = ml.normalized(view_dir)

        spec_intensity = self.intensity * max(0,ml.dot(view_dir, reflect)) ** intersect.sceneObj.material.spec
        specColor = [spec_intensity * self.color[0],
                     spec_intensity * self.color[1],
                     spec_intensity * self.color[2]]

        return specColor

    def getShadowIntensity(self, intersect, raytracer):
        temp4 = []
        for i in range(len(self.direction)):
            number = self.direction[i] * -1
            temp4.append(number)

        light_dir = temp4

        shadow_intensity = 0
        shadow_intersect = raytracer.scene_intersect(intersect.point, light_dir, intersect.sceneObj)
        if shadow_intersect:
            shadow_intensity = 1

        return shadow_intensity


class PointLight(object):
    def __init__(self, point, constant = 1.0, linear = 0.1, quad = 0.05, color = (1,1,1)):
        self.point = point
        self.constant = constant
        self.linear = linear
        self.quad = quad
        self.color = color
        self.lightType = POINT_LIGHT

    def getDiffuseColor(self, intersect, raytracer):
        light_dir = ml.subtract(self.point, intersect.point)
        light_dir = ml.normalized(light_dir)

       
        attenuation = 1.0
        intensity = ml.dot(intersect.normal, light_dir) * attenuation
        intensity = float(max(0, intensity))            
                                                        
        diffuseColor = [intensity * self.color[0],
                        intensity * self.color[1],
                        intensity * self.color[2]]

        return diffuseColor

    def getSpecColor(self, intersect, raytracer):
        light_dir = ml.subtract(self.point, intersect.point)
        light_dir = ml.normalized(light_dir)
        

        reflect = reflectVector(intersect.normal, light_dir)

        view_dir = ml.subtract( raytracer.camPosition, intersect.point)
        view_dir = ml.normalized(view_dir)

        attenuation = 1.0

        spec_intensity = attenuation * max(0,ml.dot(view_dir, reflect)) ** intersect.sceneObj.material.spec
        specColor = [spec_intensity * self.color[0],
                     spec_intensity * self.color[1],
                     spec_intensity * self.color[2]]

        return specColor

    def getShadowIntensity(self, intersect, raytracer):
        light_dir = ml.subtract(self.point, intersect.point)
        light_dir = ml.normalized(light_dir)

        shadow_intensity = 0
        shadow_intersect = raytracer.scene_intersect(intersect.point, light_dir, intersect.sceneObj)
        if shadow_intersect:
            shadow_intensity = 1

        return shadow_intensity


class AmbientLight(object):
    def __init__(self, intensity = 0.1, color = (1,1,1)):
        self.intensity = intensity
        self.color = color
        self.lightType = AMBIENT_LIGHT

    def getDiffuseColor(self, intersect, raytracer):
        temp =[]
        for i in range(len(self.color)):
            val = self.color[i] * self.intensity
            temp.append(val)
        return temp

    def getSpecColor(self, intersect, raytracer):
        return [0,0,0]

    def getShadowIntensity(self, intersect, raytracer):
        return 0
