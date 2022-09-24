
# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#    для всех значений предикат. (¬ отрицание, ∧ и, ∨ или)

x = float(input('Enter X: '))
y = float(input('Enter Y: '))
z = float(input('Enter Z: '))

a = not(x or y or z)
b = not x and not y and not z
print(a == b)
