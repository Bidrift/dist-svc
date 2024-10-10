# Twitter-like application
This application is a part of Software Architecture assignment implementing a twitter-like service using distributed services patterns using Python, Flask and JWT. This app features the following:

- User Service: Manages user registration, authentication, and user existence validation.

- Message Service: Allows users to post messages and fetch the latest message feed.

- Like Service: Allows users to like messages and increments the like count of the message.

The architecture is to separate each service on a different container and uses Docker to deploy on the following ports:

- User: localhost:5000
- Messages: localhost:5001
- Like: localhost:5002

# Demo

Here is the demo of the application, that also includes the featured API requests: [Demo](https://drive.google.com/file/d/1cGDtSB1v74gZ5sBVXilBZEQTjBshCj8J/view?usp=sharing)

# Running the App

To run the application, first you need to make sure you have Docker installed.

1. Copy the repository using the green "Code" button above

2. Build and Start the Services using the following command in the repository folder

```sh
docker-compose up --build
```
3. Test the API on the ports mentioned above in your local network

Some examples

- Register (gives token)
```
POST http://localhost:5000/register
{
  "username": "john_doe"
}
```

- Login (gives token)
```
POST http://localhost:5000/login
{
  "username": "john_doe"
}
```

- Sending a message
```
POST http://localhost:5001/send
Authorization: Bearer <TOKEN>
{
  "message": "Your message"
}
```

- Like a message
```
POST http://localhost:5002/like
Authorization: Bearer <JWT_TOKEN>
{
  "message_id": "<MESSAGE_ID>"
}
```

- Feed
```
GET http://localhost:5001/feed
```

4. Stopping the App
```sh
docker-compose down
```

5. Contributing
Feel free to contribute by opening issues or submitting pull requests for improvements or bug fixes.

6. License
This project is licensed under the MIT License.