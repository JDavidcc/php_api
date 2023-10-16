<?php
    // Para usar el api desde php 
    // http://localhost/Php_API/API.Php?x=83287
    // Esta aplicación PHP es un API REST por lo que no tiene interfaz de usuario
        header("Content-Type: application/json; charset=UTF-8");

    if (!empty($_GET["x"])) {
        $x = $_GET["x"];
        if (empty($x))
        {
            response(100, NULL);
        }
        else{
            //En lugar de hacer la operación, se llama a la base de datos.
            //response(200, $x + $y);
            $servername = "localhost";
            $username = "root";
            $password = "";
            $dbname = "codigo_postales";
            $conn = new mysqli($servername, $username, $password, $dbname);
            if($conn->connect_error){
                response (500, NULL);
            }
            $sql="SELECT colonia * FROM codigo_postales WHERE cp= $x";
            response (200, $sql);
        }
    } else
     {
        response(300, NULL);
    }

    function response($status, $data) {
        header("HTTP/1.1 " . $status);
        $response = array(
            "status" => $status,
            "data" => $data
        );
        echo json_encode($response);
    }
?>