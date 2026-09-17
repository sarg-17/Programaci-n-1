def calculadora():
    while True:
        print("1. Suma")
        print("2. Resta")
        print("3. Salir")
        
        opcion = input("Elige una opción. ")
        if opcion in ["1", "2"]: 
            try:
                num1 = float(input("Primer número: "))
                num2 = float(input("Segundo número: "))
                
                if opcion == "1":
                    resultado = num1 + num2
                    print(f"El resultado de {num1} + {num2} es igual a {resultado}")
                    
                elif opcion == "2":
                    resultado = num1 - num2
                    print(f"El resultado de {num1} - {num2} es igual a {resultado}")
            except ValueError: 
                print("Ingrece únicamente valores numéricos.")        
        elif opcion == "3":
            break
        else:
            print("Opción no valida")
calculadora() 