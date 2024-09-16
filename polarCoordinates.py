from cmath import phase
comp_number = input()
angle = phase(complex(comp_number))
r = abs(complex(comp_number))
print(r)
print(angle)