<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iniciar Sesión</title>
    <!-- Agrega los enlaces a los estilos de Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="text-center"> <!-- Agrega la clase text-center al body para centrar todo el contenido -->

<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="mb-4">Vital Monitor</h2>
            <h2 class="mb-4">Iniciar Sesión</h2>
            <form id="loginForm">
                <div class="mb-3">
                    <label for="username" class="form-label">Nombre de Usuario</label>
                    <input type="text" class="form-control" id="username" name="username" required>
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Contraseña</label>
                    <input type="password" class="form-control" id="password" name="password" required>
                </div>
                <button type="submit" class="btn btn-primary">Iniciar sesión</button>
            </form>
            <p class="mt-3">¿No tienes una cuenta? <a href="#" id="registerLink">Regístrate</a></p>
        </div>
    </div>
</div>

<!-- Agrega los enlaces a los scripts de Bootstrap y jQuery (necesario para algunas funcionalidades de Bootstrap) -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

<script>
$(document).ready(function() {
    // Validar el formulario al enviar
    $('#loginForm').submit(function(event) {
        var username = $('#username').val();
        var password = $('#password').val();

        if (username === '' || password === '') {
            alert('Por favor, completa todos los campos.');
            event.preventDefault();
        } else {
            // Simulamos una validación exitosa y redirigimos al usuario a la página de inicio
            window.location.href = 'inicio.php';
        }
    });

    // Enlace para registrarse
    $('#registerLink').click(function(event) {
        event.preventDefault();
        // Aquí puedes agregar la lógica para redirigir a la página de registro
    });
});

</script>

</body>
</html>
