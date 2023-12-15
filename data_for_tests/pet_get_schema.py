class PetSchema:
    PET_GET_VALID_RESPONSE_SCHEMA = {
        "type": "object",
        "properties": {
            "id": {"type": "integer", "format": "int64"},
            "category": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "format": "int64"},
                    "name": {"type": "string"}
                }
            },
            "name": {"type": "string"},
            "photoUrls": {"type": "array", "items": {"type": "string"}},
            "tags": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "format": "int64"},
                        "name": {"type": "string"}
                    },
                }
            },
            "status": {"type": "string", "enum": ["available", "pending", "sold"]}
        },
        "required": ["id", "name", "photoUrls"]
    }
