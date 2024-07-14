user_post = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "createdAt",
        "job",
        "name"
    ],
    "additionalProperties": False,
}

user_get = {
    "type": "object",
    "properties": {
        "page": {
            "type": "integer"
        },
        "per_page": {
            "type": "integer"
        },
        "total": {
            "type": "integer"
        },
        "total_pages": {
            "type": "integer"
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "email": {
                        "type": "string"
                    },
                    "first_name": {
                        "type": "string"
                    },
                    "last_name": {
                        "type": "string"
                    },
                    "avatar": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "email",
                    "first_name",
                    "last_name",
                    "avatar"],
                "additionalProperties": False
            }
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            },
            "required": [
                "url",
                "text"
            ],
            "additionalProperties": False
        }
    },
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "data",
        "support"],
    "additionalProperties": False
}

user_patch = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        }
    },
    "required": [
        "name",
        "job",
        "updatedAt"
    ],
    "additionalProperties": False
}

user_positive = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "email": {
            "type": "string"
        },
        "first_name": {
            "type": "string"
        },
        "last_name": {
            "type": "string"
        },
        "avatar": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "email",
        "first_name",
        "last_name",
        "avatar"],
    "additionalProperties": False
}

