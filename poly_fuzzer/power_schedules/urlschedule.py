from poly_fuzzer.power_schedules.abstract_power_schedule import AbstractPowerSchedule
from poly_fuzzer.common.abstract_seed import AbstractSeed
from cgi_decode import cgi_decode
from urllib.parse import urlparse
from html.parser import HTMLParser


class PowerSchedule(AbstractPowerSchedule):

    def __init__(self) -> None:
        super().__init__()
    
        
    def _assign_energy(self, seeds: list[AbstractSeed]) -> None:
        """Assigns each seed the same energy"""
        for seed in seeds:
            seed_length = len(seed.data)
            energy = 1 / seed_length
            seed.energy = energy
        return seeds    


class UrlPowerSchedule(AbstractPowerSchedule):

    def __init__(self) -> None:
        super().__init__()

    def _assign_energy(self, seeds: list[AbstractSeed]) -> None:
        """Assigns each seed the same energy"""
        for seed in seeds:
            print(seed.data)
            seed.energy = 1 / (len(urlparse(seed.data).path) + 0.5)
        return seeds
    
class HtmlPowerSchedule(AbstractPowerSchedule):

    def __init__(self) -> None:
        super().__init__()

    def _assign_energy(self, seeds: list[AbstractSeed]) -> None:
        """Assigns each seed the same energy"""
        for seed in seeds:
            print(seed.data)
            seed.energy = 1 / (len(seed.data) + 0.5)
        return seeds