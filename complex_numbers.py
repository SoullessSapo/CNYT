import math

def suma(a, b):
    """Suma dos números complejos en forma cartesiana."""
    return (a[0] + b[0], a[1] + b[1])

def resta(a, b):
    """Resta dos números complejos en forma cartesiana."""
    return (a[0] - b[0], a[1] - b[1])

def producto(a, b):
    """Multiplica dos números complejos en forma cartesiana."""
    real = a[0] * b[0] - a[1] * b[1]
    imaginaria = a[0] * b[1] + a[1] * b[0]
    return (real, imaginaria)

def division(a, b):
    """Divide dos números complejos en forma cartesiana."""
    divisor = b[0] ** 2 + b[1] ** 2
    real = (a[0] * b[0] + a[1] * b[1]) / divisor
    imaginaria = (a[1] * b[0] - a[0] * b[1]) / divisor
    return (real, imaginaria)

def modulo(a):
    """Calcula el módulo de un número complejo en forma cartesiana."""
    return math.sqrt(a[0] ** 2 + a[1] ** 2)

def conjugado(a):
    """Retorna el conjugado de un número complejo en forma cartesiana."""
    return (a[0], -a[1])

def cartesiano_a_polar(a):
    """Convierte un número complejo de su forma cartesiana a polar."""
    modulo = math.sqrt(a[0] ** 2 + a[1] ** 2)
    angulo = math.atan2(a[1], a[0])
    return (modulo, angulo)

def polar_a_cartesiano(p):
    """Convierte un número complejo de su forma polar a cartesiana."""
    real = p[0] * math.cos(p[1])
    imaginaria = p[0] * math.sin(p[1])
    return (real, imaginaria)

def fase(a):
    """Retorna la fase de un número complejo en forma cartesiana."""
    return math.atan2(a[1], a[0])
