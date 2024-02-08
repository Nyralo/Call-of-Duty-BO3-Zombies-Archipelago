import typing
from enum import IntEnum
from BaseClasses import Item
from .Names import ItemName


class BO3ZombiesItemCategory(IntEnum):
    BLOCKER = 5
    WEAPONS = 6
    POWER = 7
    EASTER_EGG = 8
    MACHINE = 9
    MISC = 10
    VICTORY = 11


class ItemData(typing.NamedTuple):
    name: str
    category: BO3ZombiesItemCategory


class BO3ZombiesItem(Item):
    game: str = "Black Ops 3 - Zombies"

    @staticmethod
    def get_name_to_id(base_id) -> dict:
        return {item_data.name: id for id, item_data in enumerate(all_items, base_id)}


# The Giant Items
The_Giant_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.TheGiant_Juggernog, BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_QuickRevive, BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_DoubleTap, BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_SpeedCola,BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_MuleKick, BO3ZombiesItemCategory.MACHINE),
    #(ItemName.TheGiant_RandomMachine,BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_Wallbuys, BO3ZombiesItemCategory.WEAPONS),
    
    (ItemName.TheGiant_AnimalTesting,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_Garage,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_PowerRoom,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_Teleporter1,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_Teleporter2,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_Teleporter3,BO3ZombiesItemCategory.BLOCKER),
]]

# Point Drop Items
Points_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points500, BO3ZombiesItemCategory.MISC)

]]

# Victory
Victory_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.TheGiant_Victory, BO3ZombiesItemCategory.VICTORY)
]]

# Misc/Filler Items
Misc_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points50, BO3ZombiesItemCategory.MISC)
]]

base_items = Points_Items

all_items = Points_Items + Victory_Items + Misc_Items + The_Giant_Items

all_items_dict = {item_data.name: item_data for item_data in all_items}
