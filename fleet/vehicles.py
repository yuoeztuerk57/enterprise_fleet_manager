from abc import ABC, abstractmethod
from .exceptions import MaintenanceRequiredError, InvalidMileageError

class Vehicle(ABC):
    def __init__(self, license_plate: str, mileage: float, last_service_km: float):
        if mileage < 0 or last_service_km < 0 or last_service_km > mileage:
            raise InvalidMileageError("Ungültiger Kilometerstand")
        self.license_plate = license_plate
        self.mileage = mileage
        self.last_service_km = last_service_km

    def needs_service(self) -> bool:
        return (self.mileage - self.last_service_km) > 15000.0

    def drive(self, distance: float):
        if distance < 0:
            raise InvalidMileageError("Distanz darf nicht negativ sein")
        self.mileage += distance
        if self.needs_service():
            raise MaintenanceRequiredError(
                f"Wartung erforderlich für {self.license_plate}"
            )

    @abstractmethod
    def calculate_trip_cost(self, distance: float) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.license_plate} (KM: {self.mileage:.1f})"

class FuelVehicle(Vehicle):
    def __init__(
        self,
        license_plate: str,
        mileage: float,
        last_service_km: float,
        fuel_consumption_per_100km: float,
        fuel_price_per_liter: float,
    ):
        super().__init__(license_plate, mileage, last_service_km)
        self.fuel_consumption_per_100km = fuel_consumption_per_100km
        self.fuel_price_per_liter = fuel_price_per_liter

    def calculate_trip_cost(self, distance: float) -> float:
        liters = (distance / 100.0) * self.fuel_consumption_per_100km
        cost = liters * self.fuel_price_per_liter
        return round(cost, 2)

class EVehicle(Vehicle):
    def __init__(
        self,
        license_plate: str,
        mileage: float,
        last_service_km: float,
        kwh_per_100km: float,
        electricity_price_per_kwh: float,
    ):
        super().__init__(license_plate, mileage, last_service_km)
        self.kwh_per_100km = kwh_per_100km
        self.electricity_price_per_kwh = electricity_price_per_kwh

    def calculate_trip_cost(self, distance: float) -> float:
        kwh = (distance / 100.0) * self.kwh_per_100km
        cost = kwh * self.electricity_price_per_kwh
        return round(cost, 2)