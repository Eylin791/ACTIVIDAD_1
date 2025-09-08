#Ejercicio 5

class Calculos:
  
  @staticmethod
  def calcular_suma(suma, x):
    suma = suma + x
    return suma

  @staticmethod
  def calcular_x(x, y):
    resultado_x = x + y**2
    return resultado_x



  def main(self):

    suma = float(input("Ingrese un número para suma: "))
    x = float(input("Ingrese un número para x: "))
    y = float(input("Ingrese un número para y: "))
  

    suma = Calculos.calcular_suma(suma, x)
    x = Calculos.calcular_x(x, y)
    
    suma = suma + (x/y)
    
    print(" El valor de la suma es: ", suma)
    


if __name__ == "__main__":
  calculos = Calculos()
  calculos.main()




  

   