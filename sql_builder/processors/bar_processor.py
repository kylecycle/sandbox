from base_processor import BaseProcessor


class BarProcessor(BaseProcessor):
    def process(self, name: str, params: dict):
        # Processing for type = "bar"
        print(f"[BAR] Processing {name} with params {params}")
