import pkgutil
import importlib
from sql_builder.services.registry import get_processor_class


class SqlFactory:

    _loaded = False

    @classmethod
    def _load_processors(cls):
        if cls._loaded:
            return
        # valid relative import form inside a package
        import sql_builder.processors as pkg
        for _, module_name, _ in pkgutil.iter_modules(pkg.__path__):
            importlib.import_module(f"{pkg.__name__}.{module_name}")
        cls._loaded = True

    @classmethod
    def get_processor(cls, type_name: str):
        cls._load_processors()  # ensure all plugins loaded
        processor_cls = get_processor_class(type_name)
        if not processor_cls:
            raise ValueError(f"No processor found for type '{type_name}'")
        return processor_cls()
