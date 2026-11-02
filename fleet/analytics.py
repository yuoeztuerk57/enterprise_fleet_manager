from typing import Callable
from .vehicles import Vehicle

class FleetAnalytics:
    def __init__(self, vehicles: list[Vehicle] | None = None):
        self.vehicles: list[Vehicle] = vehicles if vehicles is not None else []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def filter_vehicles(self, predicate_fn: Callable[[Vehicle], bool]) -> list[Vehicle]:
        return list(filter(predicate_fn, self.vehicles))

    def sort_vehicles(
        self, key_fn: Callable[[Vehicle], float | str], reverse: bool = False
    ) -> list[Vehicle]:
        return sorted(self.vehicles, key=key_fn, reverse=reverse)