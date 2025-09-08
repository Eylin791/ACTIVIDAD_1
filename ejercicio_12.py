#Ejercicio 12

class Calculos:

  @staticmethod
  def calcular_salario_bruto(horas_laboradas, valor_hora):
    salario_bruto = horas_laboradas * valor_hora
    return salario_bruto

  @staticmethod
  def calcular_porcentaje_retencion(retencion):
    porcentaje_retencion = retencion/100
    return porcentaje_retencion

  @staticmethod
  def calcular_valor_retencion_fuente(salario_bruto, porcentaje_retencion):
    valor_retencion_fuente = salario_bruto * porcentaje_retencion
    return valor_retencion_fuente

  @staticmethod
  def calcular_salario_neto(salario_bruto, valor_retencion_fuente):
    salario_neto = salario_bruto - valor_retencion_fuente
    return salario_neto


  def main(self):

    horas_trabajadas = float(input("Ingrese un número para horas trabajadas: "))
    valor_hora = float(input("Ingrese un número para valor hora:" ))
    retencion = float(input("Ingrese un número para retención: "))

    salario_bruto = Calculos.calcular_salario_bruto(horas_trabajadas, valor_hora)
    porcentaje_retencion = Calculos.calcular_porcentaje_retencion(retencion)
    valor_retencion_fuente = Calculos.calcular_valor_retencion_fuente(salario_bruto, porcentaje_retencion)
    salario_neto = Calculos.calcular_salario_neto(salario_bruto, valor_retencion_fuente)

    print("Salario bruto: ", salario_bruto)
    print("Valor retención fuente: ", valor_retencion_fuente)
    print("Salario neto: ", salario_neto)
    


if __name__ == "__main__":
  calculos = Calculos()
  calculos.main()






