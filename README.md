# API (master == back-end)

## Comment tester le backend en local

Attention, c'est spécifique à cette branche du dépôt, qui est faite pour
simplifier les tests avant de porter les modifications dans la branche déployée
en production. En particulier, elle utilise une base de données SQLite plutôt
que PostgreSQL.

On commence par créer et activer un environnement virtuel Python3 :

    virtualenv3 ~/clublecture
    . ~/clublecture/bin/activate

Ensuite on installe les paquets python nécessaires au backend :

    pip install -r requirements.txt

Ensuite on doit pouvoir lancer le serveur 

    ./manage.py runserver

Il est possible qu'il manque une ou deux commandes à faire avant le `runserver`,
à tester.

## Documentation de l'API

### Add User
#### https://clublecture.herokuapp.com/api/users

  format:

     {
     "user_name": "", STRING
     "email": "", STRING
     "password": "", STRING
     "avatar": "", STRING !! Optional
     }

filtrage:

    /users?user_name=

### Add Post
#### https://clublecture.herokuapp.com/api/posts

  format:

      {
      "user_name": "lol", CHAR
      "description": "hey" STRING
      }

filtrage:  

    /posts?user_name=
    /posts?description=

### Change Post
#### https://clublecture.herokuapp.com/api/posts/(user_name)/(post_id)

  format:

      {
      "user_name": "lol", CHAR
      "description": "hey" STRING
      }

### Change the user password
#### https://clublecture.herokuapp.com/api/(user_name)/settings/password

format:

     {
    "user_name": "", STRING
    "email": "", STRING
    "password": "", STRING !! New Password
    "avatar": "", STRING
     }
