from sql_builder.processors.base_processor import BaseProcessor
from sql_builder.services.registry import register_processor


@register_processor("test")
class TestProcessor(BaseProcessor):
    def process(self, name: str, params: dict):
        print(f"[TEST] {name} -> {params}")
