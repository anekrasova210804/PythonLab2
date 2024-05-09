from polynomial import Polynomial

poly_list = [Polynomial(0), Polynomial({0: -3, 2: 1, 5: 4}),
             Polynomial(1, 2, 3, 0, 0, 0, 5, 0, 0), Polynomial([1, 2, 3, 0, 0, 0, 5])]
for i in poly_list:
    print("REPR:", repr(i), "STR:", i, "DEGREE:", i.degree())

print()
print(f"{poly_list[0]} is {"not " if poly_list[0] != poly_list[1] else ""}equal to {poly_list[1]}")
print(f"{poly_list[2]} is {"not " if poly_list[2] != poly_list[3] else ""}equal to {poly_list[3]}\n")

print(f"({poly_list[1]}) + 3 = {poly_list[1] + 3}")
print(f"({poly_list[2]}) + ({poly_list[3]}) = {poly_list[2] + poly_list[3]}")
print(f"2*({poly_list[2]}) = {2 * poly_list[2]}")
print(f"({poly_list[2]}) * ({poly_list[1]}) = {poly_list[2] * poly_list[1]}\n")
# FROM GOOGLE:  (20x^11+5x^8+12x^7-7x^6+4x^5+3x^4+2x^3-8x^2-6x-3
print(f"-({poly_list[3]}) = {-poly_list[3]}")
print(f"({poly_list[2]}) - ({poly_list[3]}) = {poly_list[2] - poly_list[3]}")
print(f"({poly_list[3]}) - ({poly_list[1]}) = {poly_list[3] - poly_list[1]}\n")

print(f"({poly_list[2]}) from 0 = {poly_list[2](0)}")
print(f"({poly_list[1]}) from 1 = {poly_list[1](1)}\n")

for i in range(poly_list[2].degree() + 2):
    print("DER", i, "IS", poly_list[2].der(i))

print()

for i in poly_list[2]:
    print(i)
