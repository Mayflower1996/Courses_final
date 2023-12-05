USER_GET_VALID_RESPONSE_SCHEMA = {
  "type": "array",
  "items": {
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
}

RESPONSE_SCHEMA_ERROR = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "message": {"type": "string"}
    },
    "required": ["code", "message"]
}
