#Ejercicio 4
class Calculos:
  
  @staticmethod
  def Calcular_edad_alberto(self, edad_juan):
    edad_alberto = (2/3)* edad_juan
    return edad_alberto

  @staticmethod
  def Calcular_edad_ana(self, edad_juan):
    edad_ana = (4/3) *edad_juan
    return edad_ana

  @staticmethod
  def Calcular_edad_mama(self, edad_juan, edad_ana, edad_alberto):
    edad_mama =  edad_juan + edad_ana + edad_alberto
    return edad_mama

  def main(self):

    edad_juan = 9
    edad_alberto = Calculos.Calcular_edad_alberto(self, edad_juan)
    edad_ana = Calculos.Calcular_edad_ana(self, edad_juan)
    edad_mama = Calculos.Calcular_edad_mama(self, edad_juan, edad_ana, edad_alberto)
    print(" Las edades son: ")
    print("Juan = ", edad_juan)
    print("Ana = ", edad_ana)
    print("Alberto = ", edad_alberto)
    print("Mama = ", edad_mama)

if __name__ == "__main__":
  calculos = Calculos()
  calculos.main()


