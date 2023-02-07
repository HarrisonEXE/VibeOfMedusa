from abc import ABC, abstractmethod


class IDemo(ABC):
    def __init__(self):
        self.running = False
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def announceStart(self):
        pass
