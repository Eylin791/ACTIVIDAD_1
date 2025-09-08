#Ejercicio 17

import sys
import math

class Calculos:

  @staticmethod
  def calcular_area_circulo(radio):
    area_circulo = math.pi * math.pow(radio, 2)
    return area_circulo

  @staticmethod
  def calcular_longitud_circunferencia(radio):
    longitud_circunferencia = 2 * math.pi * radio
    return longitud_circunferencia


  def main(self):

    radio = float(input("Ingrese un número para el radio: "))

    area_circulo = Calculos.calcular_area_circulo(radio)
    longitud_circunferencia = Calculos.calcular_longitud_circunferencia(radio)

    print("El área del circulo es: ", area_circulo)
    print("La longitud de la circunferencia es: ", longitud_circunferencia)  

if __name__ == "__main__":
  calculos = Calculos()
  calculos.main()
