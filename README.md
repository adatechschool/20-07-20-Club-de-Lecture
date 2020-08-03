# API (master == back-end)

## Add User
### https://clublecture.herokuapp.com/api/users

  format:

     {
     "user_name": "", STRING
     "email": "", STRING
     "password": "", STRING
     "avatar": "", STRING
     }

filtrage:

    /users?user_name=

## Add Post
### https://clublecture.herokuapp.com/api/posts

  format:
  
      {
      "user": 1, INT
      "creation_date": "2000-10-23T04:05:06Z", DATETIME
      "description": "hey" STRING
      }

filtrage:  

    /posts?user_name=
    /posts?description=  

## Change the user password
### https://clublecture.herokuapp.com/api/(user_name)/settings/password

format:

     {
    "user_name": "", STRING
    "email": "", STRING
    "password": "", STRING !! New Password
    "avatar": "", STRING
     }
