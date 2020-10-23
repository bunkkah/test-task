class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area_calculation(self):
        area = abs(0.5 * (self.a[0] * (self.b[1] - self.c[1]) + self.b[0] * (self.c[1] - self.a[1])
                          + self.c[0] * (self.a[1] - self.b[1])))

        return area

    def perimeter_calculation(self):

        dist1 = ((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2) ** (1 / 2)
        dist2 = ((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2) ** (1 / 2)
        dist3 = ((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2) ** (1 / 2)

        perimeter = dist1 + dist2 + dist3

        return perimeter

    def does_exist(self):
        # тут лучше было бы не дублировать формулу из метода area_calculation, но как есть
        s = abs(0.5 * (self.a[0] * (self.b[1] - self.c[1]) + self.b[0] * (self.c[1] - self.a[1])
                       + self.c[0] * (self.a[1] - self.b[1])))
        if s > 0:
            return True
        else:
            return False
