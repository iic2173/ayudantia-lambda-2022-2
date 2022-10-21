SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Sample schema",
    "description": "The root schema comprises the entire JSON document.",
    "examples": [{"key": "gasto", "value": "765"}],
    "required": ["key", "value"],
    "properties": {
        "key": {
            "$id": "#/properties/key",
            "type": "string",
            "title": "The key",
            "examples": ["gasto"],
            "maxLength": 20,
        },
        "value": {
            "$id": "#/properties/value",
            "type": "string",
            "title": "The value",
            "examples": ["765"],
            "maxLength": 30,
        },
    },
}

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.validation import SchemaValidationError, validate

def lambda_handler(event, context: LambdaContext) -> dict:
  try:

    # using standalone function to validate input data only
    validate(event=event, schema=SCHEMA)

    # in this example the body can be of any type because we are not validating the OUTPUT
    return {"body": "Data validated", "statusCode": 200}
  except SchemaValidationError as exception:
    # SchemaValidationError indicates where a data mismatch is
    print("Schema Validation Error")
    return {"body": str(exception), "statusCode": 400}
