class Factory:
    def __init__(self,name,color,toy):
        self.name = name
        self.color = color
        self.toy = toy
    def material(self):
        if self.toy == 'animal':
            return 'Buy silk'
        else:
            return 'Buy plastic'
    def creation(self):
        if self.toy == 'animal':
            return 'The toy is being sewn'
        else:
            return 'The toy is poured into the mold'
    def paint(self):
        return 'The toy is painted to {}'.format(self.color)
        
class Bear(Factory):
    def them(self):
        return bear.material(), bear.creation(),bear.paint()
class Cat(Factory):
    def them(self):
        return cat.material(), cat.creation(),cat.paint()

bear = Bear('Bear','gren','animal') 
cat = Cat('Cat','white','plastic')       

print(cat.them())