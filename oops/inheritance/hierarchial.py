#             A
#             |
#             |
#      ------ ---------
#      |               |
#      |               |
#      B               C


# Single Parent Class
class Shape:
    def __init__(self, color):
        self.color = color

# Child Class 1 (Inherits from Shape)
class Circle(Shape):
    def draw(self):
        print(f"Drawing a {self.color} circle.")

# Child Class 2 (Also inherits from Shape)
class Square(Shape):
    def draw(self):
        print(f"Drawing a {self.color} square.")

# --- Demonstration ---
c = Circle("red")
s = Square("blue")

c.draw()  # Uses inherited 'color'
s.draw()  # Uses inherited 'color'

                