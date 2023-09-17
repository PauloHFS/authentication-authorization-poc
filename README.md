# authentication-authorization-poc

Proof of concept to test how to work with Authentication and Authorizantion on a Web Server

## Checkpoints

- [ ] create a authentication flow
  - [ ] sign-up endpoint
  - [ ] sign-in endpoint
  - [ ] implements a JWT token
  - [ ] implements a refresh token
  - [ ] handle the sessions on the server
  - [ ] set the cookies on the client
  - [ ] use redis to store the refresh tokens
- [ ] create a authorization flow
  - [ ] create a middleware to check if the user is authorized
  - [ ] create a autorization flow (roles and permissions)
