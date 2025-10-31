from exceptions import UnknownProcessorType
from processors.bar_processor import BarProcessor
from processors.barb_processor import BarbProcessor


class SqlFactory:
    _registry = {
        "bar": BarProcessor,
        "barb": BarbProcessor,
    }

    @classmethod
    def get_processor(cls, type_name: str):
        try:
            return cls._registry[type_name]()
        except KeyError:
            raise UnknownProcessorType(f"Unknown type: {type_name}")
