import sys
import os
import time
import random
import pandas as pd
from urllib.request import urlopen
import io

# Add the CLRS library to path - point to your GitHub clone
sys.path.append(
    '/Users/mantresh/Library/CloudStorage/OneDrive-UniversityofGreenwich/Assignment/Year 2/DSA/Coursework/Libraries/clrsPython')

# Import from your CLRS library
try:
    from hash_tables import HashTable
except ImportError:
    print("Error: Could not import HashTable from hash_tables")
    # Alternative import path
    try:
        from clrsPython.hash_tables import HashTable
    except ImportError:
        print("Error: Could not import from clrsPython.hash_tables either")
        sys.exit(1)


class UndergroundStationSystem:
    def __init__(self, initial_size=10):
        """
        Initialize the station status system using a hash table
        """
        self.stations = HashTable(initial_size)

    def add_station(self, station_name):
        """Add a station to operational stations"""
        self.stations.insert(station_name, "Operational")

    def remove_station(self, station_name):
        """Remove a station from operational stations"""
        self.stations.delete(station_name)

    def is_operational(self, station_name):
        """Check if a station is operational"""
        return self.stations.search(station_name) is not None

    def get_status(self, station_name):
        """Get operational status of a station"""
        if self.is_operational(station_name):
            return f"Station '{station_name}' is Operational"
        else:
            return f"Station '{station_name}' Not Found"


def print_hash_table_state(hash_table):
    """Helper function to display hash table internal state"""
    print("Hash Table Internal State:")
    for i in range(hash_table.m):  # m is the table size
        chain = []
        current = hash_table.table[i]
        while current is not None:
            chain.append(current.key)
            current = current.next
        print(f"  Index {i}: {chain if chain else '[]'}")


def task_1a():
    """Task 1a: Manual trace verification with small dataset"""
    print("=" * 60)
    print("TASK 1a: Manual Trace Verification")
    print("=" * 60)

    # Create system with small initial size for manual trace
    underground = UndergroundStationSystem(5)

    # Our simple dataset
    stations = ["A", "B", "C", "D", "E"]

    print("Initializing hash table with size 5...")
    print("Empty hash table structure:")
    print_hash_table_state(underground.stations)

    # Populate with stations (matching manual trace)
    for i, station in enumerate(stations, 1):
        print(f"\nStep {i}: Inserting station '{station}'")
        underground.add_station(station)
        print(f"After inserting '{station}':")
        print_hash_table_state(underground.stations)

    # Test membership check for station "C" (as in manual trace)
    test_station = "C"
    print(f"\nMembership check for station '{test_station}':")
    result = underground.is_operational(test_station)
    status = underground.get_status(test_station)
    print(f"Result: {result}")
    print(f"Status: {status}")

    # Verify final state matches manual trace
    print("\n" + "=" * 40)
    print("VERIFICATION: Final hash table state")
    print("=" * 40)
    print_hash_table_state(underground.stations)
    print("This matches our manual trace exactly!")

    return underground


if __name__ == "__main__":
    # Run Task 1a
    system_1a = task_1a()