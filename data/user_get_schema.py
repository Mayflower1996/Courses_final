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

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "type": {"type": "string"},
        "code": {"type": "integer"},
        "message": {"type": "string"}
    },
    "required": ["code", "type", "message"]
}
