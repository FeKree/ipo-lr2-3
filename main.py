import math
V = float(input("Введите объем сферы "))
if V < 0:
    print("введите корректные значения")
else:
    R = (3 * V ** (1/3)) / (4 * math.pi)
    print(f"Радиус сферы равен {R}")
