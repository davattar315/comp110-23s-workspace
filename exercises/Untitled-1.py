x: int = 1
y: float = .1
z =  (((0.9*y) + (0.3(y**1/3)))/1.05)*x/x
while x >= 50:
    print(z)
    y = z 