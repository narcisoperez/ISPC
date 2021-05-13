# Libraries
from math import tan


# Functions
def geometricShape(number_of_sides):
    """This function deciphers the name of the figure from its sides"""
    if number_of_sides > 7:
        name = str(number_of_sides) + '-gon'
        return name
    else:
        number_of_sides -= 3
        basicForm = ['triangle', 'square', 'pentagon', 'hexagon', 'heptagon']
        name = basicForm[number_of_sides]
        return name


def perimeter(sidesValues):
    """This function calculates the perimeter of the polygon"""
    # Sum of de sides
    c = 0
    for i in sidesValues:
        c += i
    return c


def area(polygon, polygon_perimeter):
    """This function calculates the area of polygon"""
    # Apothem
    a = len(polygon)  # Number of sides
    b = polygon[0]  # Side length

    apothem = b / (2 * tan((180 / a) * 3.14159 / 180))

    # Area
    polygon_area = (polygon_perimeter * apothem) / 2
    return polygon_area


def inputSides(number_of_sides):
    """this function loads the values of the sides of the polygon, entered by the user"""
    polygon = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(number_of_sides)]
    return polygon


# Main block
N_sides = int(input("Enter the number of sides of the polygon: "))  # Number of sides
# Polygon validation
if N_sides < 3:
    print("Error, please try again...")
else:
    polygon = inputSides(N_sides)   # Value of sides
    print("The perimeter and area of the", geometricShape(N_sides),
          "is\nPerimeter: ", perimeter(polygon), "\nArea: %0.2f" % area(polygon, perimeter(polygon)))
