from ..base_processor import BaseProcessor
from ..registry import register_processor


@register_processor("test")
class TestProcessor(BaseProcessor):
    def process(self, name: str, params: dict):
        print(f"[TEST] {name} -> {params}")
