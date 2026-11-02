from fleet import (
    FleetAnalytics,
    FuelVehicle,
    EVehicle,
    MaintenanceRequiredError,
    InvalidMileageError,
)

if __name__ == "__main__":
    analytics = FleetAnalytics()

    v1 = FuelVehicle("D-PK 101", 12000.0, 0.0, 7.5, 1.75)
    v2 = FuelVehicle("D-PK 202", 58000.0, 40000.0, 9.0, 1.80)
    e1 = EVehicle("D-EV 303", 25000.0, 20000.0, 18.0, 0.35)
    e2 = EVehicle("D-EV 404", 62000.0, 60000.0, 15.0, 0.30)

    analytics.add_vehicle(v1)
    analytics.add_vehicle(v2)
    analytics.add_vehicle(e1)
    analytics.add_vehicle(e2)

    print("FLEET MANAGER SIMULATION\n")

    print("Fahrzeuge, die zur Wartung müssen:")
    service_needed = analytics.filter_vehicles(lambda v: v.needs_service())
    for v in service_needed:
        print(f" * {v.license_plate} (KM: {v.mileage:.1f})")
    print()

    print("Fahrzeuge mit mehr als 50.000 KM:")
    high_mileage = analytics.filter_vehicles(lambda v: v.mileage > 50000.0)
    for v in high_mileage:
        print(f" * {v.license_plate} (KM: {v.mileage:.1f})")
    print()

    test_distance = 250.0
    print(f"Fahrtkosten für eine Teststrecke von {test_distance} km:")
    for v in analytics.vehicles:
        cost = v.calculate_trip_cost(test_distance)
        print(f" * {v.license_plate}: {cost:.2f} €")
    print()

    cheapest = min(
        analytics.vehicles,
        key=lambda v: v.calculate_trip_cost(test_distance)
    )
    cheapest_cost = cheapest.calculate_trip_cost(test_distance)
    print(f"Günstigstes Fahrzeug: {cheapest.license_plate} mit {cheapest_cost:.2f} €")
    print()

    print("Test der Zusatzaufgabe:")
    try:
        print(f"Fahre 11.000 km mit {e1.license_plate}...")
        e1.drive(11000.0)
    except MaintenanceRequiredError as e:
        print(f"Erfolg: {e}")