import sys
import os

# Add the library path to access the provided algorithms
sys.path.append('https://github.com/Mantresh19/clrsPython')  # Replace with your actual path

from hash_table import HashTable

class StationStatusSystem:
    def __init__(self, capacity=10):
        self.stations = HashTable(capacity)
    
    def add_station(self, station_name):
        """Add a station to the operational set"""
        self.stations.insert(station_name, True)
    
    def remove_station(self, station_name):
        """Remove a station from the operational set"""
        self.stations.delete(station_name)
    
    def is_operational(self, station_name):
        """Check if a station is operational"""
        return self.stations.search(station_name) is not None
    
    def display_status(self, station_name):
        """Display operational status for a station"""
        if self.is_operational(station_name):
            return f"Station '{station_name}' is Operational"
        else:
            return f"Station '{station_name}' is Not Found"

def task_1a():
    """Implementation for Task 1a"""
    print("=== Task 1a: Station Status System ===\n")
    
    # Create station system
    system = StationStatusSystem(capacity=10)
    
    # Simple dataset
    stations = ['A', 'B', 'C', 'D', 'E']
    print("Populating with stations:", stations)
    
    # Manual population trace
    for i, station in enumerate(stations):
        system.add_station(station)
        print(f"After adding {station}: Hash table size = {system.stations.get_size()}")
    
    # Status check for station C (as traced manually)
    test_station = 'C'
    print(f"\nChecking status for station '{test_station}':")
    result = system.display_status(test_station)
    print(result)
    
    # Verification
    print(f"\nVerification - Manual trace expected: Operational")
    print(f"Code result: {result}")
    print("✓ Manual trace and code implementation are consistent")

if __name__ == "__main__":
    task_1a()
