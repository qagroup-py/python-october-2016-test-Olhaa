# coding: utf-8

"""
Implement class structure/hierarchy for following classes:

Basil  (базилік)
Beetroor  (буряк)
Blueberry  (чорниця)
Cabbage  (капуста)
Carrot  (морква)
Concorde (pear)  (груша "Конкорд")
Dill  (кріп)
Domestic strawberry  (полуниця)
Golden delicious (apple)  (яблуко "Голден")
Granny Smith (apple)  (яблуко "Гренні Сміт")
Onion  (цибуля)
Potato  (картопля)
Red globe (grapes)  (виноград "Ред Глоб")
Victoria (grapes)  (виногдар "Вікторія")
Wild strawberry  (суниця)
"""

class Food:
    def __init__(self, name):
        self.name = name
    
class Berries(Food):
    pass

Blueberry = Berries 
Domestic_strawberry = Berries
Wild_strawberry = Berries

class Fruits(Food):
    pass

Concorde_Pear = Fruits
Golden_delicious_apple = Fruits
Granny_Smith_apple = Fruits
Red_globe_grapes = Fruits
Victoria_grapes = Fruits

class Greens(Food):
    pass

Basil = Greens
Dill = Greens 

class Vegetables(Food):
    pass


Beetroor = Vegetables
Cabbage = Vegetables
Carrot = Vegetables 
Onion = Vegetables
Potato = Vegetables



