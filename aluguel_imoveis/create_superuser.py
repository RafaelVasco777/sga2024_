# create_superuser.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aluguel_imoveis.settings')
django.setup()

from django.contrib.auth.models import User

username = 'rafael'
email = 'rafael@henriques.com'
password = 'vasco2024'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superusuário "{username}" criado com sucesso.')
else:
    print(f'Superusuário "{username}" já existe.')
