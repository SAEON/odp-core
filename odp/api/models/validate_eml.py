

import json
import jsonschema
from jsonschema import validate
import os

# Paths to your schema and instance files
SCHEMA_PATH = "/home/g.zhou/odp-core/odp/schema/metadata/saeon/eml.json"
INSTANCE_PATH = "/home/g.zhou/odp-core/odp/schema/metadata/saeon/eml-template.json"

def load_json(filepath):
    """Load a JSON file from disk."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_eml_metadata(schema_path, instance_path):
    """Validate a JSON instance against the EML schema."""
    try:
        schema = load_json(schema_path)
        instance = load_json(instance_path)

        validate(instance=instance, schema=schema)
        print("✅ Validation successful! The metadata conforms to the EML schema.")
    except jsonschema.exceptions.ValidationError as ve:
        print("❌ Validation error:", ve.message)
        print("At path:", list(ve.path))
    except Exception as e:
        print("⚠️ General error:", str(e))

if __name__ == "__main__":
    if os.path.exists(SCHEMA_PATH) and os.path.exists(INSTANCE_PATH):
        validate_eml_metadata(SCHEMA_PATH, INSTANCE_PATH)
    else:
        print("❌ One or both JSON files not found. Please check paths.")
