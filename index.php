<!DOCTYPE html>
<html>
<head>
    <title>Calculadora de Suma</title>
</head>
<body>
    <h1>Calculadora de Suma</h1>
    
    <!-- Formulario para ingresar los números -->
    <form method="POST" action="http://localhost/php_api/api2.php"> 
        <label for="numero1">Número 1:</label>
        <input type="number" name="numero1" required>
        <br>
        <label for="numero2">Número 2:</label>
        <input type="number" name="numero2" required>
        <br>
        <input type="submit" value="Calcular Suma">
    </form>

    <?php
    // Mostrar el resultado de la suma si está disponible
    if(isset($_GET['resultado'])){
        $resultado = $_GET['resultado'];
        echo '<p>Resultado de la suma: ' . $resultado . '</p>';
    }
    ?>
</body>
</html>
