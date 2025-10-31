# sql_processor/registry.py
_processor_registry = {}


def register_processor(type_name: str):
    def decorator(cls):
        _processor_registry[type_name] = cls
        return cls
    return decorator


def get_processor_class(type_name: str):
    return _processor_registry.get(type_name)
