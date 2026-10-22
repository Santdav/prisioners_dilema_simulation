from abc import ABC, abstractmethod

from moves import Move


class Strategy(ABC):
    name: str = "unnamed"

    @abstractmethod
    def choose(self, my_history: list[Move], opp_history: list[Move]) -> Move:
        ...

    def reset(self) -> None:
        """Clear internal state between matches."""
        pass