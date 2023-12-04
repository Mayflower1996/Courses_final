USER_GET_VALID_RESPONSE_SCHEMA = {
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
    "required": ["id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"]}

RESPONSE_SCHEMA = {
        "type": "object",
        "properties": {
            "code": {"type": "integer"},
            "type": {"type": "string"},
            "message": {"type": "string"}
        },
        "required": ["code", "type", "message"]
}
