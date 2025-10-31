from ..base_processor import BaseProcessor
from ..registry import register_processor


@register_processor("barb")
class BarbProcessor(BaseProcessor):
    def process(self, name: str, params: dict):
        print(f"[BARB] {name} -> {params}")
