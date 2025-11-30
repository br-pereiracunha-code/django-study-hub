# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User # Importe seu modelo User customizado

# Se você quiser usar formulários customizados para o admin,
# você precisaria criá-los primeiro
# Por enquanto, vamos usar os padrões do Django.
# from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User) # Registra seu modelo User no admin
class UserAdmin(BaseUserAdmin):
    """
    Admin customizado para o modelo User.
    
    Herda de BaseUserAdmin para manter a maioria das funcionalidades padrão,
    mas permite customizar a exibição e os formulários.
    """
    
    # Se fosse utilizar formulários customizados, descomentaria e usaria assim:
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    
    # O modelo que este admin gerencia
    model = User
    
    # Campos a serem exibidos na lista de usuários no admin
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    
    # Campos pelos quais você pode filtrar a lista de usuários
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    
    # Campos pelos quais você pode pesquisar usuários
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    # Ordem padrão da lista de usuários
    ordering = ['email'] # Ou 'username', dependendo da sua preferência
    
    # Define os fieldsets para a página de detalhes/edição do usuário
    # Isso organiza os campos em seções no admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Informações Pessoais'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissões'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Datas Importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Define os fieldsets para a página de adição de novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password2')} # password2 é para confirmação
        ),
    )
    
    # Campos que serão somente leitura no admin
    readonly_fields = ['last_login', 'date_joined']
