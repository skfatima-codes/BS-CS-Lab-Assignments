from Triangle import Triangle

t1 = Triangle()
print("Triangle t1:", t1.get_sideA(), t1.get_sideB(), t1.get_sideC())

t2 = Triangle(5.5)
print("Triangle t2:", t2.get_sideA(), t2.get_sideB(), t2.get_sideC())

t3 = Triangle(4.0, 6.0)
print("Triangle t3:", t3.get_sideA(), t3.get_sideB(), t3.get_sideC())

t4 = Triangle(3.0, 4.0, 5.0)
print("Triangle t4:", t4.get_sideA(), t4.get_sideB(), t4.get_sideC())

t5 = t4.clone_triangle()
print("Triangle t5 (clone of t4):", t5.get_sideA(), t5.get_sideB(), t5.get_sideC())
