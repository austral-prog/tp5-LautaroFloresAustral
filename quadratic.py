# Replace the "ANSWER HERE" for your answer
import math
def roots(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return f'( )'
    elif d == 0:
        x = (-b/(2*a))
        return f'({x})'
    elif d > 0:
        r1 = (-b + math.sqrt(d))/(2*a)
        r2 = (-b - math.sqrt(d))/(2*a)
        return f'({r1}, {r2})'


def value_y(a, b, c, x):
    y = a * (x**2) + b * x + c
    return y


def to_string(a, b, c):
    resultado = 'f(x) ='
    if a != 0:
        resultado += f' {a} * X^2'
    if b != 0:
        if a != 0:
            resultado += f' + {b} * X'
        else:
            resultado += f' {b} * X'
    if c != 0 or (a == 0 and b == 0):
        if a != 0 or b != 0:
            resultado += f' + {c}'
        else:
            resultado += f' {c}'
    return resultado


def derivation(a, b, c):
    resultado = "f'(x) ="

    if a != 0:
        resultado += f" {2*a} * X"
        if b != 0:
            resultado += f" + {b}"
    else:
        if b != 0:
            resultado += f" {b}"
        else:
            resultado += " 0"
    return resultado
