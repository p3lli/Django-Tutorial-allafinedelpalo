# Tutorial Django per il sito allafinedelpalo.it

Il repository contiene un semplice esempio di applicazione web creata utilizzando il framework python Django

## Inizializzazione

Dopo aver clonato il repository, eseguite i seguenti comandi:
1) per installare Django
```
pip install -U -r requirements.txt
```
2) per creare il database sqlite
```
python ./manage.py makemigrations
python ./manage.py migrate
```
3) per popolare il database
```
python ./manage.py shell
```
una volta aperta la shell, digitate i seguenti comandi python:
```
from ecommerce.models import Prodotto, Casa
Casa.objects.create(nome='Sony', email='info@sony.com')
Casa.objects.create(nome='Nintendo', email='info@nitendo.com')
sony = Casa.objects.filter(nome='Sony')
nintendo = Casa.objects.filter(nome='Nintendo')
Prodotto.objects.create(nome='GameBoy', prezzo=150.00, dimensione='P', casa=nintendo[0])
Prodotto.objects.create(nome='SNES', prezzo=249.99, dimensione='M', casa=nintendo[0])
Prodotto.objects.create(nome='PSP', prezzo=170.00, dimensione='P', casa=sony[0])
Prodotto.objects.create(nome='PlayStation', prezzo=349.99, dimensione='M', casa=sony[0])
```
4) per creare un superuser

```
python manage.py createsuperuser
```

## Articoli di riferimento

Introduzione: http://www.allafinedelpalo.it/python-django-introduzione/

Parte 1: http://www.allafinedelpalo.it/python-django-1-settings-url-modello/

Parte 2: http://www.allafinedelpalo.it/python-django-2-view-e-template

Parte 3: coming soon...

Parte 4: coming soon...


