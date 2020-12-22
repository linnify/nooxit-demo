# Nooxit Project

### Project structure

#### Technologies

- For the API part we used FastAPI framework
- The web client was written in React
- For the OpenID Provider we used Ory Hydra
- Custom Auth Provider

#### Run the project

In order to start the project you need to run the following command
```
docker-compose up -d
```

The Auth system has 2 users with different groups

```
email: vlad.rusu@linnify.com
password: test1234
groups: users and members
```

and

```
email: razvan.bretoiu@linnify.com
password: test1234
groups: users
```

#### Web
The WEB Application has 2 pages: one for the users and another one for the members.

You need to be logged in into the system to have access to those pages.

To see the users you need to be in the `users` group and to see the members you need to
be in the `members` group

#### Backend
The backend part was developed in FastAPI and it has the following endpoints

- /auth/login -> Return the authorized URL for the SSO page where the user can login
- /auth/callback -> Callback URL used for OAuth2 flow. 
- /auth/profile -> Return the current user based on the access token
- /users -> Return the users dummy data only if the user belongs to the "users" group
- /members -> Return the members dummy data only if the user belongs to the "members" group

#### Authorization Flow

- We used the Code Flow for OAuth which is the most secure and used flow in OAuth.
- To login into the system, you need to get an authorization URL from the API
- To get the authorization URL the client needs to pass a redirect page, so the API will
redirect the user to that page after the authorization flow is completed
- We ask for the following scopes: openid, email, mail and groups




