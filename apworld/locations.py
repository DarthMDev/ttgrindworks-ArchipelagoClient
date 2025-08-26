from dataclasses import dataclass, field
from itertools import count
from typing import Iterable, List, Optional, Tuple, get_args
from .options import TotalLocations
# from environments, import environment data

from BaseClasses import Location, LocationProgressType, Region

class TTGrindWorksLocation(Location):
    game : str = "Toontown: The Grindworks"


# using classic items ItemPickups check from RoR2 
def get_classic_item_pickups(n: int) -> Dict[str, int]:
    """Get n ItemPickups, capped at the max value for TotalLocations"""
    n = max(n, 0)
    n = min(n, TotalLocations.range_end)
    return {f"ItemPickup{i + 1}": ror2_locations_start_id + i for i in range(n)}

item_pickups = get_classic_item_pickups(TotalLocations.range_end)
location_table = item_pickups

# find environment and location offsets (?)

# find locations within a single environment

# get a dictionary of all locations for the given options

# update location table
