print ("PROGRAM MENGHITUNG AKAR PERSAMAAN KUADRAT")
print ("Masukkan nilai a, b, dan c dari persamaan kuadrat ax^2 + bx + c = 0")
a = float(input("Masukkan nilai a: "))               
b = float(input("Masukkan nilai b: "))               
c = float(input("Masukkan nilai c: "))   

if a == 0:
    print("Nilai a tidak boleh 0, karena bukan persamaan kuadrat.")     
else:
    D = b**2 - 4*a*c
    if D < 0:
        print("Persamaan kuadrat tidak memiliki akar real.")
    elif D == 0:
        x = -b / (2*a)
        print(f"Persamaan kuadrat memiliki satu akar real: x = {x}")
    else:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print(f"Persamaan kuadrat memiliki dua akar real: x1 = {x1}, x2 = {x2}") 