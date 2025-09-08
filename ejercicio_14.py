#Ejercicio 14

import sys
import math

class Calculos:


  @staticmethod
  def calcular_cuadrado(número):
    cuadrado = math.pow(número, 2)
    return cuadrado


  @staticmethod
  def calcular_cubo(número):
    cubo = math.pow(número, 3)
    return cubo

  def main(self):

    número= float(input("Ingrese un número: "))

    cuadrado = Calculos.calcular_cuadrado(número)
    cubo = Calculos.calcular_cubo(número)

    print("El cuadrado del número es: ", cuadrado)
    print("El cubo del número es: ", cubo)  

if __name__ == "__main__":
  calculos = Calculos()
  calculos.main()




  