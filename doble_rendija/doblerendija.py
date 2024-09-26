import math

# Función que representa la onda compleja de cada rendija
def onda(amplitud, fase):
    return (amplitud, fase)

# Sumar dos números complejos representados como tuplas (amplitud, fase)
def sumar_ondas(onda1, onda2):
    real1 = onda1[0] * math.cos(onda1[1])
    imag1 = onda1[0] * math.sin(onda1[1])
    real2 = onda2[0] * math.cos(onda2[1])
    imag2 = onda2[0] * math.sin(onda2[1])
    
    real_total = real1 + real2
    imag_total = imag1 + imag2
    
    amplitud_total = math.sqrt(real_total**2 + imag_total**2)
    fase_total = math.atan2(imag_total, real_total)
    
    return (amplitud_total, fase_total)

# Calcular la intensidad de la onda total
def calcular_intensidad(onda_total):
    return onda_total[0] ** 2

# Simulación simple para una posición en la pantalla
onda1 = onda(1, 0)  # Onda desde la primera rendija
onda2 = onda(1, math.pi / 2)  # Onda desde la segunda rendija (fase cambiada)

onda_total = sumar_ondas(onda1, onda2)
intensidad = calcular_intensidad(onda_total)

print(f"Intensidad en el punto: {intensidad}")
