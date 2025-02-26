import math


class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be greater than 0")
        super().__init__("Square")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


def main():
    try:
        shape_type = input("Enter the shape type (Square/Circle): ").strip().lower()

        if shape_type == "square":
            side_length = float(input("Enter the side length of the square: "))
            shape = Square(side_length)
        elif shape_type == "circle":
            radius = float(input("Enter the radius of the circle: "))
            shape = Circle(radius)
        else:
            raise ValueError("Invalid shape type. Please enter 'Square' or 'Circle'.")

        print(f"The area of the {shape.shape_type} is: {shape.area()}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
