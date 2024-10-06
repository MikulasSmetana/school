class Classroom:
    def __init__(self, name, sclass, floor, pavilion):
        self.name = name
        self.sclass = sclass
        self.floor = floor
        self.pavilion = pavilion
        self.pupils = 0
    def arrive(self, increase):
        self.pupils += increase
        print(f"Ve třídě je nyní {self.pupils} žáků.")
    def leave(self, decrease):
        if(decrease > self.pupils):
            self.pupils = 0
            print(f"Ve třídě je nyní {self.pupils} žáků.")
        else:
            self.pupils -= decrease
            print(f"Ve třídě je nyní {self.pupils} žáků.")


class1 = Classroom("Č1","3.A","1.","nový")
print(f"Ve třídě {class1.name} se nachází třída {class1.sclass}. Tato třída je v pavilonu {class1.pavilion} v {class1.floor} patře.")

class1.arrive(20)
class1.leave(8)