from dataclasses import dataclass, field
from itertools import count
from typing import Iterable, List, Optional, Tuple, get_args

from BaseClasses import Location, LocationProgressType, Region

class TTGrindWorksLocation(Location):
    game = "Toontown: The Grindworks"
    
