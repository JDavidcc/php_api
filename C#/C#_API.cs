using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        Console.WriteLine("Calculadora de Suma");
        
        Console.Write("Ingrese el primer número: ");
        double numero1 = double.Parse(Console.ReadLine());
        
        Console.Write("Ingrese el segundo número: ");
        double numero2 = double.Parse(Console.ReadLine());

        var apiUrl = "http://tudominio.com/api.php"; // Reemplaza con la URL de tu API

        using (var client = new HttpClient())
        {
            var parametros = new FormUrlEncodedContent(new[]
            {
                new KeyValuePair<string, string>("numero1", numero1.ToString()),
                new KeyValuePair<string, string>("numero2", numero2.ToString())
            });

            HttpResponseMessage response;

            try
            {
                response = await client.PostAsync(apiUrl, parametros);
            }
            catch (HttpRequestException)
            {
                Console.WriteLine("Error al conectar con el API.");
                return;
            }

            if (response.IsSuccessStatusCode)
            {
                var contenido = await response.Content.ReadAsStringAsync();
                Console.WriteLine($"Resultado de la suma: {contenido}");
            }
            else
            {
                Console.WriteLine("Error en la solicitud al API.");
            }
        }
    }
}
