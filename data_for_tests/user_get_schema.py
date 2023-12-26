class UserSchema:
    USER_GET_VALID_RESPONSE_SCHEMA = {
        "type": "object",
        "properties": {
            "email": {"type": "string", "format": "email"},
            "firstName": {"type": "string"},
            "id": {"type": "integer"},
            "lastName": {"type": "string"},
            "password": {"type": "string"},
            "phone": {"type": "string"},
            "userStatus": {"type": "integer"},
            "username": {"type": "string"}
        },
    }
