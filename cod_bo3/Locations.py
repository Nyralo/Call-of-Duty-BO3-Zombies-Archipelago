import typing
from enum import IntEnum
from BaseClasses import Location
from .Names import LocationName


class BO3ZombiesLocationCategory(IntEnum):
    ROUND = 0
    MISC = 10


class LocationData(typing.NamedTuple):
    name: str
    category: BO3ZombiesLocationCategory
    code: int


class BO3ZombiesLocation(Location):
    game: str = "Black Ops 3 - Zombies"

    @staticmethod
    def get_name_to_id(base_id) -> dict:
        return {loc_data.name: loc_data.code + base_id for loc_data in all_locations}


# The Giant Locations
TheGiant_Locations = [LocationData(row[0], row[1], row[2]) for row in [
    # Rounds
    (LocationName.TheGiant_Round1, BO3ZombiesLocationCategory.ROUND, 1),
    (LocationName.TheGiant_Round2, BO3ZombiesLocationCategory.ROUND, 2),
    (LocationName.TheGiant_Round3, BO3ZombiesLocationCategory.ROUND, 3),
    (LocationName.TheGiant_Round4, BO3ZombiesLocationCategory.ROUND, 4),
    (LocationName.TheGiant_Round5, BO3ZombiesLocationCategory.ROUND, 5),
    (LocationName.TheGiant_Round6, BO3ZombiesLocationCategory.ROUND, 6),
    (LocationName.TheGiant_Round7, BO3ZombiesLocationCategory.ROUND, 7),
    (LocationName.TheGiant_Round8, BO3ZombiesLocationCategory.ROUND, 8),
    (LocationName.TheGiant_Round9, BO3ZombiesLocationCategory.ROUND, 9),
    (LocationName.TheGiant_Round10, BO3ZombiesLocationCategory.ROUND, 10),
    (LocationName.TheGiant_Round11, BO3ZombiesLocationCategory.ROUND, 11),
    (LocationName.TheGiant_Round12, BO3ZombiesLocationCategory.ROUND, 12),
    (LocationName.TheGiant_Round13, BO3ZombiesLocationCategory.ROUND, 13),
    (LocationName.TheGiant_Round14, BO3ZombiesLocationCategory.ROUND, 14),
    (LocationName.TheGiant_Round15, BO3ZombiesLocationCategory.ROUND, 15),
    (LocationName.TheGiant_Round16, BO3ZombiesLocationCategory.ROUND, 16),
    (LocationName.TheGiant_Round17, BO3ZombiesLocationCategory.ROUND, 17),
    (LocationName.TheGiant_Round18, BO3ZombiesLocationCategory.ROUND, 18),
    (LocationName.TheGiant_Round19, BO3ZombiesLocationCategory.ROUND, 19),
    (LocationName.TheGiant_Round20, BO3ZombiesLocationCategory.ROUND, 20),
    (LocationName.TheGiant_Round21, BO3ZombiesLocationCategory.ROUND, 21),
    (LocationName.TheGiant_Round22, BO3ZombiesLocationCategory.ROUND, 22),
    (LocationName.TheGiant_Round23, BO3ZombiesLocationCategory.ROUND, 23),
    (LocationName.TheGiant_Round24, BO3ZombiesLocationCategory.ROUND, 24),
    (LocationName.TheGiant_Round25, BO3ZombiesLocationCategory.ROUND, 25),
    (LocationName.TheGiant_Round26, BO3ZombiesLocationCategory.ROUND, 26),
    (LocationName.TheGiant_Round27, BO3ZombiesLocationCategory.ROUND, 27),
    (LocationName.TheGiant_Round28, BO3ZombiesLocationCategory.ROUND, 28),
    (LocationName.TheGiant_Round29, BO3ZombiesLocationCategory.ROUND, 29),
    (LocationName.TheGiant_Round30, BO3ZombiesLocationCategory.ROUND, 30)
]]

all_locations = TheGiant_Locations
