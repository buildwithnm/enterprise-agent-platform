from abc import ABC, abstractmethod


class BaseProcessor(ABC):

    @abstractmethod
    def build(self):
        """
        Returns an LCEL Runnable.

        Every processor in the platform
        must implement this.
        """
        pass