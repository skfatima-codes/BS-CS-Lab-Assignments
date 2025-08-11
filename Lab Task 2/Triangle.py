class Triangle:
    def __init__(self, *args):
        if len(args) == 0:  # Default constructor
            self.sideA = 1.0
            self.sideB = 1.0
            self.sideC = 1.0
        elif len(args) == 1:  # Equilateral triangle
            side = args[0]
            self.sideA = self.sideB = self.sideC = side
        elif len(args) == 2:  # Isosceles triangle (x, x, y)
            x, y = args
            self.sideA = self.sideB = x
            self.sideC = y
        elif len(args) == 3:  # Arbitrary triangle (x, y, z)
            self.sideA, self.sideB, self.sideC = args
        else:
            raise ValueError("Invalid number of arguments")

    def clone_triangle(self):
        return Triangle(self.sideA, self.sideB, self.sideC)

    # Getter and Setter methods
    def get_sideA(self):
        return self.sideA

    def set_sideA(self, sideA):
        self.sideA = sideA

    def get_sideB(self):
        return self.sideB

    def set_sideB(self, sideB):
        self.sideB = sideB

    def get_sideC(self):
        return self.sideC

    def set_sideC(self, sideC):
        self.sideC = sideC