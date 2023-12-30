from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class UserProfile(models.Model):
    
    STATUS = (
        ('online', 'online'),
        ('offline', 'offline'),
        ('do not disturb', 'do not disturb'),
    )
    
    avatar = models.URLField(
        _("avatar"),
        blank=True
    )
    
    first_name = models.CharField(
        _("first name"),
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150, 
        blank=True
    )
    
    email = models.EmailField(_("email address"), blank=True)
    
   
    
    desc = models.TextField(
        max_length=300,
        blank=True,
    )
    
    status = models.CharField(
        _('status'), 
        choices=STATUS,
        max_length=18,
        default='online',
    )
    
    user_id = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

class Posts(models.Model):
    
    post = models.TextField(
        max_length = 1000
    )

    user_id = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )