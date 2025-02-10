from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

class FormularioTestCase(TestCase):
    def setUp(self):
        """ Configuración inicial antes de cada prueba """
        self.client = Client()

    def test_formulario_valido(self):
        """ Prueba con datos correctos """
        data = {
            'username': 'MartinDJ',
            'first_name': 'Martin',
            'last_name': 'Ochoa',
            'email': 'correo@gmail.com',
            'password1': 'contraseñaSegura123',
            'password2': 'contraseñaSegura123',
        }
        form = CustomUserCreationForm(data)
        self.assertTrue(form.is_valid())

    def test_formulario_invalido(self):
        """ Prueba con contraseñas que no coinciden """
        data = {
            'username': 'UsuarioInvalido',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'correo@example.com',
            'password1': 'password123',
            'password2': 'password456',
        }
        form = CustomUserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_formulario_email_invalido(self):
        """ Prueba con un correo electrónico inválido """
        data = {
            'username': 'UsuarioPrueba',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'correo-invalido',
            'password1': 'password123',
            'password2': 'password123',
        }
        form = CustomUserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_respuesta_servidor(self):
        """ Verifica que el servidor responda con 200 OK antes de completar el test """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_respuesta_servidor_exchange(self):
        """Verifica que el servidor responda con 200 OK después de iniciar sesión y acceder a la vista exchange"""
        
        # Crear usuario de prueba
        usuario = User.objects.create_user(username="martinO", password="12345")

        # Simular acceso a la página de login
        login_data = {"username": "martinO", "password": "12345"}
        response = self.client.post("/accounts/login/", login_data, follow=True)  # Seguir la redirección

        # Verificar que el login fue exitoso
        self.assertEqual(response.status_code, 200)  # Ahora obtenemos la página final después del login

        # Ahora, acceder a la vista exchange después de estar autenticado
        response = self.client.get("/exchange/")
        
        # Verificar que la respuesta ahora sea 200
        self.assertEqual(response.status_code, 200)
