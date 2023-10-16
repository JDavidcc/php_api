import requests

def main():
    print("Calculadora de Suma")
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    # Realizar la solicitud POST al API
    api_url = "http://localhost/php_api/api2.php"  
    parametros = {"numero1": numero1, "numero2": numero2}
    
    try:
        response = requests.post(api_url, data=parametros)
        response_data = response.json()

        if response.status_code == 200:
            resultado = response_data["resultado"]
            print(f"La suma de {numero1} y {numero2} es: {resultado}")
        else:
            print(f"Error: {response_data['error']}")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el API: {e}")

if __name__ == "__main__":
    main()
