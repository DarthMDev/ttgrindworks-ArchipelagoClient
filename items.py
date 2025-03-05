from dataclasses import dataclass, field
from enum import Enum
from itertools import count
from typing import Dict, List, Set

from BaseClasses import Item, ItemClassification

class TTGrindWorksItem(Enum):
    # laff bosts (useful)
    LAFF_BOOST_1 = "+1 Laff Boost"
    LAFF_BOOST_2 = "+2 Laff Boost"
    LAFF_BOOST_3 = "+3 Laff Boost"
    LAFF_BOOST_4 = "+4 Laff Boost"
    LAFF_BOOST_5 = "+5 Laff Boost"
    LAFF_BOOST_6 = "+6 Laff Boost"
    
    # jellybean types (filler) (red, blue, green, light blue, pink, and yellow
    RED_JELLYBEAN = "Red Jellybean"
    BLUE_JELLYBEAN = "Blue Jellybean"
    GREEN_JELLYBEAN = "Green Jellybean"
    LIGHT_BLUE_JELLYBEAN = "Light Blue Jellybean"
    PINK_JELLYBEAN = "Pink Jellybean"
    YELLOW_JELLYBEAN = "Yellow Jellybean"
    
    # accessories (useful)
    GAG_PACK = "Gag Pack"
    JAMBOREE_PACK = "Jamboree Pack"
    SHARK_FIN = "Shark Fin"
    SMALL_POUCH = "Small Pouch"
    WOOD_SWORD = "Wood Sword"
    CELEBRITY_SHADES = "Celebrity Shades"
    DORKY_GLASSES = "Dorky Glasses"
    GOGGLES = "Goggles"
    MONOCLE = "Monocle"
    SQUARE_FRAMES = "Square Frames"
    CHEF_HAT = "Chef Hat"
    CONDUCTOR_HAT = "Conductor Hat"
    FEDORA = "Fedora"
    PARTY_HAT = "Party Hat"
    COG_PACK = "Cog Pack"
    EYE_PATCH = "Eye Patch"
    MASK = "Mask"
    CROWN = "Crown"
    BAT_WINGS = "Bat Wings"
    ANTI_COG_CONTROL_HAT = "Anti-Cog Control Hat"
    CATEYE_GLASSES = "Cateye Glasses"
    BUG_EYE_GLASSES = "Bug Eye Glasses"
    ARCHER_HAT = "Archer Hat"
    TOYS_BACKPACK = "Toys Backpack"
    TIARA = "Tiara"
    WITCH_HAT = "Witch Hat"
    SUPER_TOON_CAPE = "Super Toon Cape"
    MINI_BLINDS = "Mini Blinds"
    GROUCHO_GLASSES = "Groucho Glasses"
    ANVIL_HAT = "Anvil Hat
    AVIATOR_GLASSES = "Aviator Glasses"
    DRAGON_WINGS = "Dragon Wings"
    FEZ = "Fez"
    PIRATE_HAT = "Pirate Hat"
    GLASSES_3D = "3D Glasses"
    PROPELLER_HAT = "Propeller Hat"
    FRUIT_HAT = "Fruit Hat"
    TOP_HAT = "Top Hat"
    VIKING_HELMET = "Viking Helmet"
    GOLF_HAT = "Golf Hat"
    POLICE_HAT = "Police Hat"
    BOWLER_HAT = "Bowler Hat"
    MINER_HAT = "Miner Hat"
    BASEBALL_CAP = "Baseball Cap"
    SCUBA_TANK = "Scuba Tank"
    BIRD_HAT = "Bird Hat"
    DETECTIVE_HAT = "Detective Hat"
    
    # Candies (useful)
    CANDY_DAMAGE = "Damage Increase"
    CANDY_DEFENSE = "Defense Increase"
    CANDY_HP = "HP Increase"
    CANDY_SPEED = "Speed Increase"
    
    