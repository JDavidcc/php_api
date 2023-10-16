<?php
// Verificar si se han recibido los parámetros 'numero1' y 'numero2' mediante POST
if(isset($_POST['numero1']) && isset($_POST['numero2'])){
    // Obtener los valores de los parámetros
    $numero1 = $_POST['numero1'];
    $numero2 = $_POST['numero2'];

    // Realizar la suma
    $resultado = $numero1 + $numero2;

    // Crear un arreglo asociativo con la respuesta
    $response = array(
        'resultado' => $resultado
    );

    // Convertir el arreglo a formato JSON y enviar como respuesta
    header('Content-Type: application/json');
    echo json_encode($response);
} else {
    // Si no se proporcionaron los parámetros, devolver un mensaje de error
    $response = array(
        'error' => 'Los parámetros "numero1" y "numero2" son obligatorios.'
    );

    // Convertir el arreglo a formato JSON y enviar como respuesta
    header('Content-Type: application/json');
    echo json_encode($response);
}
?>
