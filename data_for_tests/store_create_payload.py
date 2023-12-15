class StorePayload:
    VALID_ONE_PET_PAYLOAD = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-12-10T08:14:40.759Z",
        "status": "placed",
        "complete": False
    }

    # should return 500 (expected fail)
    INVALID_TWO_PETS_PAYLOAD = [{
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-12-10T08:14:40.759Z",
        "status": "placed",
        "complete": False
    },
        {
            "id": 2,
            "petId": 2,
            "quantity": 2,
            "shipDate": "2023-12-10T08:14:40.759Z",
            "status": "placed",
            "complete": False
        }]

    INVALID_ORDER_PAYLOAD_EMPTY_FIELDS = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "",
        "status": "",
        "complete": 0
    }

    INVALID_ORDER_PAYLOAD_LARGE_PETID = {
        "id": 1,
        "petId": 9999999999999999999,
        "quantity": 1,
        "shipDate": "2023-12-10T08:14:40.759Z",
        "status": "placed",
        "complete": False
    }

    INVALID_ORDER_PAYLOAD_LARGE_ID = {
        "id": 9999999999999999999,
        "petId": 2,
        "quantity": 1,
        "shipDate": "2023-12-10T08:14:40.759Z",
        "status": "placed",
        "complete": False
    }

    INVALID_ORDER_PAYLOAD_LARGE_QUANTITY = {
        "id": 3,
        "petId": 2,
        "quantity": 9999999999,
        "shipDate": "2023-12-10T08:14:40.759Z",
        "status": "placed",
        "complete": False
    }

    INVALID_ORDER_PAYLOADS = [("Invalid order payload with large ID", INVALID_ORDER_PAYLOAD_LARGE_ID),
                              ("Invalid order payload with large petID", INVALID_ORDER_PAYLOAD_LARGE_PETID),
                              ("Invalid order payload with large quantity", INVALID_ORDER_PAYLOAD_LARGE_QUANTITY),
                              ("Invalid order payload with empty fields", INVALID_ORDER_PAYLOAD_EMPTY_FIELDS)]

    PET_INVENTORY_TEST_STATUS = {
        "id": 9,
        "category": {"id": 9, "name": "inventory_test"},
        "name": "indoggie",
        "photoUrls": ["https://media.tenor.com/pOS38tUuVnQAAAAd/cat-meme.gif"],
        "tags": [{"id": 9, "name": "inv_test"}],
        "status": "inv_test"
    }
