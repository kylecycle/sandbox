from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    @abstractmethod
    def process(self, name: str, params: dict):
        """Execute processing logic for a given entry."""
        pass


# EOF
