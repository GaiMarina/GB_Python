
# сложить два числа.

x = 0
y = 0

def init(a, b):     # этот метод отвечает за инициализацию x и y
    global x        # global - для того, чтобы x существовал не только в контексте метода.
    global y
    x = a
    y = b

def sum(): 
    return x + y