# coding: utf-8
"""
Implement class structure/hierarchy for following classes:

Ball (куля)
Circle (коло)
Cone (конус)
Cube (куб)
Ellipse (еліпс)
Hexagon (шестикутник)
Line (пряма)
Point (точка)
Pyramid (піраміда)
Rectangle (прямокутник)
Round (круг)
Sphere (сфера)
Square (квадрат)
Tetrahedron (тетраедр)
Triangle (трикутник)
"""

class Shapes:
    def __init__(self, name):
        self.name = name

class One_dimensional (Shapes):
	pass

Point = One_dimensional
Line = One_dimensional

class Two_dimensional (Shapes):
	pass

Circle = Two_dimensional
Ellipse = Two_dimensional
Hexagon = Two_dimensional
Rectangle = Two_dimensional
Round = Two_dimensional
Square = Two_dimensional
Triangle = Two_dimensional

class Three_dimensional (Shapes):
    pass

Cone = Three_dimensional
Cube = Three_dimensional
Pyramid = Three_dimensional
Sphere = Three_dimensional
Tetrahedron = Three_dimensional
Ball = Three_dimensional
