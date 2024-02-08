# Options.py
from dataclasses import dataclass
import typing
from Options import Option, DefaultOnToggle, Toggle, PerGameCommonOptions, Range


class TheGiantEnabled(DefaultOnToggle):
    """Enables Map: \"The Giant\"."""
    display_name = "\"The Giant\" map enabled?: "


class SpecialRoundsEnabled(Toggle):
    """Enables Special Rounds (Dogs, Monkeys, ect.)."""
    display_name = "Special Rounds Enabled?: "


class VictoryRound(Range):
    """Round to award Map Victory."""
    display_name = "Victory Round: "
    range_start = 1
    range_end = 99
    default = 20


@dataclass
class BO3ZombiesOptions(PerGameCommonOptions):
    the_giant_enabled: TheGiantEnabled
    #special_rounds_enabled: SpecialRoundsEnabled
    victory_round: VictoryRound


bo3_zombies_options: typing.Dict[str, type(Option)] = {
    "the_giant_enabled": TheGiantEnabled,
    #"special_rounds_enabled": SpecialRoundsEnabled,
    "victory_round": VictoryRound
}
