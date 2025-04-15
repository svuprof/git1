class ElectricCar:
    def __init__(self, brand, model, battery_kwh, range_miles, has_autopilot):
        self.brand = brand
        self.model = model
        self.battery_kwh = battery_kwh
        self.range_miles = range_miles
        self.has_autopilot = has_autopilot

    def display_specs(self):
        print(f"{self.brand} {self.model} | Battery: {self.battery_kwh}kWh | Range: {self.range_miles} miles")
        if self.has_autopilot:
            print("This car has autopilot.")
        else:
            print("This car does not have autopilot.")

    def charge_status(self):
        print(f"Charging {self.brand} {self.model}...")
        print(f"Estimated full charge range: {self.range_miles} miles with a {self.battery_kwh}kWh battery.")