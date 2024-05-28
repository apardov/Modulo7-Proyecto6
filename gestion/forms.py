from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, ModelChoiceField
from .models import CustomEmailUser, Pedido, DetallePedido


# definicion de formularios para creacion de usuarios y modificacion de estos
# usando los predefinidos que Django provee
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomEmailUser
        fields = ('email', 'rut', 'nombre_completo')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomEmailUser
        fields = ('email', 'rut', 'nombre_completo')


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class DetallePedidoForm(ModelForm):
    class Meta:
        model = DetallePedido
        fields = '__all__'


class ChangeStatusForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado']


class TakeOrderForm(ModelForm):
    cliente = ModelChoiceField(queryset=CustomEmailUser.objects.all())

    class Meta:
        model = Pedido
        fields = ['cliente', 'numero_pedido', 'direccion_entrega', 'forma_pago']
