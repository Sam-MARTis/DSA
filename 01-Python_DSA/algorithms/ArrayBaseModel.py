class ArrayModel:
    def __init__(self, a: list = []) -> None:
        self.vals = a[:]
        pass
    def add(self, a) -> None:
        self.vals.append(a)
    def adds(self, a) -> None:
        for i in a:
            self.vals.append(i)

    def get_values(self) -> list:
        return self.vals
    
    def set_values(self, vals):
        self.vals = vals