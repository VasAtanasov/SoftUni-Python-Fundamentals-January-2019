class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.right = left + width
        self.top = top
        self.bottom = top - height

    def is_inside(self, rectangle):
        return self.left >= rectangle.left and \
               self.right <= rectangle.right and \
               self.top <= rectangle.top and \
               self.bottom >= rectangle.bottom


r1 = Rectangle(*list(map(int, input().split(" "))))
r2 = Rectangle(*list(map(int, input().split(" "))))

if r1.is_inside(r2):
    print("Inside")
else:
    print("Not inside")
