CORRECT_ONE_PET_PAYLOAD = {
  "id": 22,
  "category": {
    "id": 1,
    "name": "Cats"
  },
  "name": "Pushistik",
  "photoUrls": [
    "https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg"
  ],
  "tags": [
    {
      "id": 708,
      "name": "Catsforsale"
    }
  ],
  "status": "available"
}
CORRECT_TWO_PET_PAYLOAD = [{
  "id": 24,
  "category": {
    "id": 2,
    "name": "Dogs"
  },
  "name": "Gabriel",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 709,
      "name": "Dogsforsale"
    }
  ],
  "status": "pending"
}
    ]
CORRECT_THREE_PET_PAYLOAD = {
        "id": 2502,
        "category": {
            "id": 1,
            "name": "Cats"
        },
        "name": "Chernysh",
        "photoUrls": [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Blackcat-Lilith.jpg/440px-Blackcat-Lilith.jpg"
        ],
        "tags": [
            {
                "id": 708,
                "name": "Catsforsale"
            }
        ],
        "status": "sold"
    }
PET_PAYLOAD_EMPTY_FIELDS = {
        "id": 27,
        "category": {
            "id": 27,
            "name": ""
        },
        "name": "",
        "photoUrls": [
            ""
        ],
        "tags": [
            {
                "id": 27,
                "name": ""
            }
        ],
        "status": ""
    }
INCORRECT_STATUS_PET_PAYLOAD = {
        "id": 345,
        "category": {
            "id": 1,
            "name": "Cats"
        },
        "name": "Chery",
        "photoUrls": [
            ""
        ],
        "tags": [
            {
                "id": 708,
                "name": "Catsforsale"
            }
        ],
        "status": "nostatus"
    }
