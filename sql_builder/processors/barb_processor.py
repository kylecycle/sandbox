from base_processor import BaseProcessor


class BarbProcessor(BaseProcessor):
    def process(self, name: str, params: dict):
        # Processing for type = "barb"
        print(f"[BARB] Processing {name} with params {params}")
