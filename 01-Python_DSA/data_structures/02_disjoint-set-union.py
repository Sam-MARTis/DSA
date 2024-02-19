class DSU:
    def __init__(self) -> None:
        self.sets = []
    
    def make_set(self, x):
        setThis = set()
        setThis.add(x)
        self.sets.append(setThis)
    def combine_set(self, x, y):
        if (x not in self.sets) or (y not in self.sets):
            return ValueError("Elements need to be in the set first")
    def get_sets(self):
        return self.sets
    

myDSU = DSU()
print(myDSU.get_sets())
myDSU.make_set(2)
print(myDSU.get_sets())
myDSU.make_set(3)
print(myDSU.get_sets())