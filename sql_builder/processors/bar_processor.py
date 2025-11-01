from sql_builder.processors.base_processor import BaseProcessor
from sql_builder.services.registry import register_processor


@register_processor("bar")
class BarProcessor(BaseProcessor):
    def process(self, name: str, params: dict):
        print(f"[BAR] {name} -> {params}")
