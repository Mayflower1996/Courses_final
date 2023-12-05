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
  "required": [
    "id",
    "username",
    "firstName",
    "lastName",
    "email",
    "password",
    "phone",
    "userStatus"
  ]
}

RESPONSE_SCHEMA_ERROR = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "message": {"type": "string"}
    },
    "required": ["code", "message"]
}
