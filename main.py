import json
import requests

def dish_fetch(num): # Función requerida en el Readme
    
    # 1. Hacemos la solicitud GET a la API
    response = requests.get("https://api-colombia.com/api/v1/TypicalDish/" + num) # Se agrega en num
    
    # 2. Convertimos el contenido JSON en un diccionario de Python
    plato = json.loads(response.content)
    
    # 3. Retornamos el diccionario
    return plato

def main():
    # El bucle while True repetirá el menú continuamente
    while True:
        print("\n=== 🇨🇴 MENÚ DE PLATOS TÍPICOS DE COLOMBIA 🇨🇴 ===")
        print("1. Consultar plato por ID")
        print("2. Salir")
        
        opcion = input("\nSelecciona una opción (1 o 2): ")
        
        if opcion == "1":
            num = input("Ingresa el ID del plato típico (ej. 1, 2, 3): ")
            
            # Llamamos a la función dish_fetch para obtener la información del plato
            plato = dish_fetch(num)
            
            # Mostramos el resultado
            print("\n----------------------------------------")
            print("Nombre: " + plato["name"])
            print("Descripción: " + plato["description"])
            print("Ingredientes: " + plato["ingredients"])
            print("----------------------------------------")
            
        elif opcion == "2":
            print("\n¡Gracias por consultar el menú! ¡Hasta pronto! 👋")
            break  # Detiene el bucle while True y finaliza el programa
            
        else:
            print("\n⚠️ Opción no válida. Por favor digita 1 o 2.")

if __name__ == "__main__":
    main()