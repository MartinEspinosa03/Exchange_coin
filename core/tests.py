from django.test import TestCase
from .forms import CustomUserCreationForm

# Create your tests here.
class FormularioTestCase(TestCase):
    def test_formulario_valido(self):
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