USER_GET_OK_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string"},
        "phone": {"type": "string"},
        "userStatus": {"type": "integer"}
    },
    "required": ["id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"]
}

USER_GET_BAD_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    }
}
