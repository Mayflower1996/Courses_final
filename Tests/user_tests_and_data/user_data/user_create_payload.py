CORRECT_ONE_USER_PAYLOAD = {
    "id": 1,
    "username": "testuser1",
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "password": "password1",
    "phone": "1234567890",
    "userStatus": 0
}

CORRECT_TWO_USERS_PAYLOAD = [{
    "id": 1,
    "username": "testuser1",
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "password": "password1",
    "phone": "1234567890",
    "userStatus": 0
},
    {
        "id": 2,
        "username": "testuser2",
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane@example.com",
        "password": "password2",
        "phone": "9876543210",
        "userStatus": 0
    }]

INCORRECT_USER_PAYLOAD_EMPTY_FIELDS = {
    "id": 3,
    "username": "",
    "firstName": "",
    "lastName": "",
    "email": "",
    "password": "",
    "phone": "",
    "userStatus": 0
}

INCORRECT_USER_PAYLOAD_LARGE_STATUS = {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 10000000000
}

USER_PAYLOADS = [("Correct two users payload", CORRECT_TWO_USERS_PAYLOAD),
                 ("Incorrect user payload with large status", INCORRECT_USER_PAYLOAD_LARGE_STATUS),
                 ("Incorrect user payload with empty fields", INCORRECT_USER_PAYLOAD_EMPTY_FIELDS)]
