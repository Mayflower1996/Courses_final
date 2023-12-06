PET_GET_VALID_RESPONSE_SCHEMA = {
    "type": "object",
    "properties":
    {
        "id": {"type": "integer"},
        "category": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "name": {"type": "string"},
        "photoUrls": {"type": "string"},
        "tags": [
            {
                "id": {"type": "integer"},
                "name": {"type": "string"}
            }
        ],
        "status": {"type": "string"},
        "required": ["id", "name", "photoUrls"]}
}
