
def datos_valentina():
    print("Mi nombre es Valentina Vargas, tengo 22 años")

def datos_angelo():
    print("Mi nombre es Angelo ponce, tengo 29 años")

def datos_cris():
    print("Mi nombre es Cristopher Campos, tengo 29 años")
 # Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        datos_valentina()
    elif op == "2":
        datos_cris()
    elif op == "3":
        datos_angelo()
    else:
        print(" Opción inválida.")
