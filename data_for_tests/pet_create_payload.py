class PetPayload:
    CORRECT_ONE_PET_PAYLOAD = {
        "id": 229802,
        "category": {
            "id": 1,
            "name": "Cats"
        },
        "name": "Pushistik",
        "photoUrls": [
        ],
        "tags": [
            {
                "id": 708,
                "name": "Catsforsale"
            }
        ],
        "status": "available"
    }
    CORRECT_TWO_PET_PAYLOAD = {
        "id": 24905,
        "category": {
            "id": 2,
            "name": "Dogs"
        },
        "name": "Gabriel",
        "photoUrls": [
            ""
        ],
        "tags": [
            {
                "id": 709,
                "name": "Dogsforsale"
            }
        ],
        "status": "pending"
    }
    # such pet already exists
    CORRECT_THREE_PET_PAYLOAD = {
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
    CORRECT_FOUR_PET_PAYLOAD = {
        "id": 299993,
        "category": {
            "id": 2,
            "name": "Dogs"
        },
        "name": "Tom",
        "photoUrls": [
            ""
        ],
        "tags": [
            {
                "id": 709,
                "name": "Dogsforsale"
            }
        ],
        "status": "available"
    }

    # for updating pet tests
    UPDATE_PET = {
        "id": 299993,
        "category": {"id": 13, "name": "hamsters"},
        "name": "Booba",
        "photoUrls": ["data/cat.gif"],
        "tags": [{"id": 432, "name": "Bad"}, {"id": 43, "name": "Health_issues"}],
        "status": "pending"
    }

    PET_PAYLOAD_EMPTY_FIELDS = {
    }
    REQUIRED_FIELDS_EMPTY_PET_PAYLOAD = {
        "id": 345,
        "category": {
            "id": 1,
            "name": "Cats"
        },
        "name": "",
        "photoUrls": [
            ""
        ],
        "tags": [
            {
                "id": 708,
                "name": "Catsforsale"
            }
        ],
        "status": "pending"
    }
    INCORRECT_STATUS_PET_PAYLOAD = {
        "id": 294,
        "category": {
            "id": 2,
            "name": "Dogs"
        },
        "name": "Terry",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 709,
                "name": "Dogsforsale"
            }
        ],
        "status": "nostatus"
    }

    INCORRECT_ID1_PET_PAYLOAD = {
        "id": -42294,
        "category": {
            "id": 2,
            "name": "Dogs"
        },
        "name": "Tor",
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
    LONG_ID_PET_PAYLOAD = {
        "id": 2945345689345678250671,
        "category": {
            "id": 2,
            "name": "Dogs"
        },
        "name": "Don",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 709,
                "name": "Dogsforsale"
            }
        ],
        "status": "available"
    }
    INCORRECT_ID_PET_PAYLOAD = {
        "id": "id",
        "category": {
            "id": 2,
            "name": "Dogs"
        },
        "name": "Donna",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 709,
                "name": "Dogsforsale"
            }
        ],
        "status": "available"
    }
    # For tests updating pet with formData (name and status)
    UPDATE_PET_DATA_RESP = CORRECT_ONE_PET_PAYLOAD
    UPDATE_PET_DATA_RESP_INVALID = CORRECT_ONE_PET_PAYLOAD
    UPDATE_PET_DATA_RESP_NAME = CORRECT_ONE_PET_PAYLOAD
    UPDATE_PET_DATA_RESP["name"] = "Tesla"
    UPDATE_PET_DATA_RESP["status"] = "pending"
    UPDATE_PET_DATA_RESP_INVALID["status"] = "nostatus"
    UPDATE_PET_DATA_RESP_NAME["name"] = "-"
