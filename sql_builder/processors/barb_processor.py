from sql_builder.processors.base_processor import BaseProcessor
from sql_builder.services.registry import register_processor


@register_processor("barb")
class BarbProcessor(BaseProcessor):
    def process(self, name: str, params: dict):
        print(f"[BARB] {name} -> {params}")
