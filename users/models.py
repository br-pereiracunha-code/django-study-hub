# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Modelo de usuário customizado.
    
    Herda todas as funcionalidades do AbstractUser padrão do Django.
    Você pode adicionar campos extras aqui no futuro, se precisar.
    """
    
    # Exemplo de campo extra que você pode adicionar depois:
    # phone_number = models.CharField(_('telefone'), max_length=15, blank=True, null=True)
    # date_of_birth = models.DateField(_('data de nascimento'), blank=True, null=True)
    
    # Se você quiser que o email seja único, pode descomentar a linha abaixo
    # email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    
    # Se você quiser que o email seja o campo de login principal, descomente as linhas abaixo:
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username'] # Se você ainda quiser um username, mas não para login
    
    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')
        # Você pode adicionar ordering ou outras opções de Meta aqui
    
    def __str__(self):
        # Por padrão, AbstractUser usa o username.
        # Se você mudar USERNAME_FIELD para 'email', mude aqui também.
        return self.username # Ou self.email, se você mudar USERNAME_FIELD
