#Universidad del Valle de Guatemala 
#Gabriela Paola Contreras Guerra 20213
#Libreria Matematica a utilizar 

def normalize(v):
    length = pow(((v[0])**2 +(v[1])**2 +(v[2])**2 ),0.5)
    return length

def normalized(v):
    temp= []
    for i in range (len(v)):
        norm = v[i]/ normalize(v)
        temp.append(norm)
    return temp

def dot(a,b):
    dotproduct =0
    for a,b in zip(a,b):
        dotproduct = dotproduct + a * b
    return dotproduct

def subtract(a, b):
    result = [a[i] - b[i] for i in range(min(len(a), len(b)))]
    return result

def add (a, b):
    result = [a[i] + b[i] for i in range(min(len(a), len(b)))]
    return result
