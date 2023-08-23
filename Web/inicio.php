<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <!-- Agrega los enlaces a los estilos de Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

</head>
<body>

<?php require_once 'header.php' ?>

<div class="container mt-5">
    <div class="row">
        <div class="col-md-6">
            <img src="Vicente.png" alt="Imagen" class="img-fluid">
        </div>
        <div class="col-md-6">
            <div class="row">
                <h2>Vicente! Estamos felices de verte de nuevo</h2><br><br>
                <p>Nombre: Vicente</p>
                <p>Apellidos: Gonzalez</p>
                <p>Edad: 21</p>
                <p>Status Actual: Estable</p>
                <p>Futuro Status: Estable</p>
            </div>
            <div class="row">
                <canvas id="canva" width="300" height="600"></canvas>
            </div>
        </div>
    </div>
</div>

<?php require_once 'footer.php' ?>

<script src="./char.js"></script>
</body>
</html>
