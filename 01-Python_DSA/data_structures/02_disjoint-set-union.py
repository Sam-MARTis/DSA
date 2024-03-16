class DSU:
    def __init__(self) -> None:
        self.sets = []
    
    def make_set(self, *x):
        setThis = set()
        for i in x:
            setThis.add(i)
        self.sets.append(setThis)
    def get_sets(self):
        return self.sets
    def mergse_sets(self, x, y):
        set1 = set()
        set2 = set()
        for i in self.sets:
            if x in i:
                set1 = i
            if y in i:
                set2 = i
        setCombined = set1.union(set2)
        self.sets.remove(set1)
        self.sets.remove(set2)
        self.sets.append(setCombined)
            
    

myDSU = DSU()
print(myDSU.get_sets())
myDSU.make_set(2)
print(myDSU.get_sets())
myDSU.make_set(3, 4, 3, 5)
myDSU.mergse_sets(2, 3)
myDSU.make_set(3, 4, 9)
myDSU.mergse_sets(2, 3)
print(myDSU.get_sets())wi