from Party.data_utils import append_to_list, slice_list, reverse_list
from Party.math_utils import area_circle, area_triangle, area_rectangle

my_list = [1, 2, 3]
print("Original List:", my_list)
print("After appending 4:", append_to_list(my_list, 4))
print("Sliced List (1 to 3):", slice_list(my_list, 1, 3))
print("Reversed List:", reverse_list(my_list))

print("Area of Circle (radius 5):", area_circle(5))
print("Area of Triangle (base 4, height 3):", area_triangle(4, 3))
print("Area of Rectangle (length 5, width 2):", area_rectangle(5, 2))
