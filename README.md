# API (master == back-end)

## Add User
### https://clublecture.herokuapp.com/api/users

  format:

     {
     "user_name": "", STRING
     "email": "", STRING
     "password": "", STRING
     "avatar": "", STRING !! Optional
     }

filtrage:

    /users?user_name=

## Add Post
### https://clublecture.herokuapp.com/api/posts

  format:

      {
      "user_name": "lol", CHAR
      "description": "hey" STRING
      }

filtrage:  

    /posts?user_name=
    /posts?description=

## Change Post
### https://clublecture.herokuapp.com/api/posts/(user_name)/(post_id)

  format:

      {
      "user_name": "lol", CHAR
      "description": "hey" STRING
      }

## Change the user password
### https://clublecture.herokuapp.com/api/(user_name)/settings/password

format:

     {
    "user_name": "", STRING
    "email": "", STRING
    "password": "", STRING !! New Password
    "avatar": "", STRING
     }
