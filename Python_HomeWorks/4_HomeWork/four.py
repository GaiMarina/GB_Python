
# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
#    (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#    Пример:
#    k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Задана натуральная степень k. # Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. # Пример: # k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 # Pn(x)=аnхn+an-1xn-1+аn-2хn-2+....+а2х2+a1х+а0, from random import randint def create_list(k, m, n): # создание списка случайных чисел указанного диапазона в соответствии с указанной степенью уравнения return [randint(m, n) for i in range(k + 1)]

def create_polynomial(input_list): # создание и форматирование многочлена на основании списка чисел polynomial_list = [] for i in range(len(input_list)): if input_list[-1 - i] != 0: polynomial_list.insert(0, str(input_list[-1 -i]) + "*x^" + str(i)) polynomial_str = " + ".join(polynomial_list) polynomial_str += " = 0" polynomial_str = polynomial_str.replace(" 1*", " ") polynomial_str = polynomial_str.replace("^1", "") polynomial_str = polynomial_str.replace("x^0", "1") polynomial_str = polynomial_str.replace("*1", "") if polynomial_str[0] == "1" and polynomial_str[1] == "*": n = 2 polynomial_str = polynomial_str[n:] return polynomial_str  
    
    k = int(input("Введите степень уравнения: ")) m = int(input("Введите нижнюю границу чисел: ")) n = int(input("Введите верхнюю границу чисел: ")) input_list = create_list(k, m, n) polynomial_list = create_polynomial(input_list) print(input_list) print(create_polynomial(input_list)) # with open('D:\\Обучение\\Практика\\Python\\Home_task4\\Polynomial_task004.txt', 'a') as data: # data.write(f"\n{create_polynomial(input_list)}") 
    
    def get_coeffs(digits): digits = digits.strip().strip(' = 0') digits = digits.split(' + ') coeffs = {} for i in digits: a, *b = i.split(' * x ** ') if b: coeffs[int(b[0])] = int(a) else: if i.endswith('x'): a, *b = i.split(' * x') coeffs[1] = int(a) else: coeffs[0] = int(i) return coeffs def sum_coeffs(d, coeffs): for key in d: if not key in coeffs: coeffs[key] = 0 coeffs[key] += d[key] return coeffs with open('res.txt') as f: digits1 = f.read() digits2 = digits1[:] coeffs1 = get_coeffs(digits1) coeffs2 = get_coeffs(digits2) coeffs = {} coeffs = sum_coeffs(coeffs1, coeffs) coeffs = sum_coeffs(coeffs2, coeffs) res = '' max_num = max(coeffs.keys()) for i, j in coeffs.items(): res += str(j) if i != 0 and j != 0 and i != 1: res += ' * x ** ' res += str(i) res += ' + ' elif j == 0: continue eli 
    
    elif i == 1: res += ' * x + ' else: res += ' = 0' print(res) 