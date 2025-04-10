class Validator:
    @staticmethod
    def validate(json_obj):
        if isinstance(json_obj, dict):
            keys = set()
            for key, value in json_obj.items():
                if key in keys:
                    raise ValueError(f"Duplicate key: {key}")
                keys.add(key)
                Validator.validate(value)
        elif isinstance(json_obj, list):
            for item in json_obj:
                Validator.validate(item)