class Cylinder:
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()
        
    def get_surface_area(self):         # surface area = (2 * pi * radius * height) + (2 * pi * radius ** 2)
        self.surface_area = (2 * 3.142 * self.radius * self.height) + (2 * 3.142 * self.radius ** 2)
        return round(self.surface_area, 2)
        
    def get_volume(self):
        self.volume = 3.142 * self.height * (self.radius ** 2)
        return round(self.volume, 2)
    
cyl1 = Cylinder(21)

print(cyl1.get_surface_area())
print(cyl1.get_volume())
