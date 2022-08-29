# Description:
#         Write a Python program that calculates the distance between two 3D points.
#         The points are represented by two lists with three elements. The first element is the x-coordinate. The second element is the y-coordinate. The third element is the z-coordinate.

pointA=[3,4,5]
pointB=[1,3,5]
def distance(pointA,pointB):
    distance = 0
    for i in range(len(pointA)):
         distance += (pointB[i] - pointA[i])**2
    distance = distance**0.5
    return distance
D = distance(pointA,pointB)
print(D)













