from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions, OptionGroup

# Using the RoR2 options as a starting point. 
# Thanks to kindasneaki for the options code

class Goal(Choice):
    """
    If we decide to implement different run types, this is where that option is chosen.
    """
    display_name = "Game Mode"
    option_classic = 0
    option_explore = 1
    default = 1


class Victory(Choice):
    """
    Different victory conditions can be added here. 
    """
    display_name = "Victory Condition"
    option_any = 0
    default = 0


class TotalLocations(Range):
    """
    This should affect the total number of checks available in the game.
    Note: the range minimums/maximums should be determined with testing.
    """
    display_name = "Total Locations"
    range_start = 40
    range_end = 250
    default = 40


class ItemPickupStep(Range):
    """
    Number of items to pick up before an AP Check is completed.
    Setting to 1 means every other pickup.
    Setting to 2 means every third pickup. So on...
    """
    display_name = "Item Pickup Step"
    range_start = 0
    range_end = 5
    default = 1


class AllowTrapItems(Toggle):
    """Allows Trap items in the item pool."""
    display_name = "Enable Trap Items"

class ItemWeights(Choice):
    """Set Use Item Weight Presets to yes if you want to use one of these presets.
    Preset choices for determining the weights of the item pool.
    
    """
    display_name = "Item Weights"
    option_default = 0
    option_new = 1


grindworks_option_groups = [
    OptionGroup("Classic Mode Options", [
        TotalLocations,
    ], start_collapsed=True),
    OptionGroup("Weighted Choices", [
        #TO DO: Add in weighted choices once created
    ]),
]


@dataclass
class ROR2Options(PerGameCommonOptions):
    goal: Goal
    victory: Victory
    total_locations: TotalLocations
    chests_per_stage: ChestsPerEnvironment
    item_pickup_step: ItemPickupStep
    enable_trap: AllowTrapItems
    item_weights: ItemWeights
    item_pool_presets: ItemPoolPresetToggle
    # define the weights of the generated item pool.
    # TO DO: define weights once created
