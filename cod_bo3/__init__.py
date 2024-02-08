import string

from BaseClasses import MultiWorld, Region, Item, ItemClassification

from worlds.AutoWorld import World

from . import Regions, Locations, Items, Options
from .Names import ItemName, LocationName, RegionName

from .Logic import CODBO3Logic

class BO3ZombiesWorld(World):
    """
    TODO: Game Description
    """
    game: str = "Black Ops 3 - Zombies"

    options_dataclass = Options.BO3ZombiesOptions
    options = Options.BO3ZombiesOptions

    topology_present = True
    # Game's SteamID
    base_id = 311210
    item_name_to_id = Items.BO3ZombiesItem.get_name_to_id(base_id)
    location_name_to_id = Locations.BO3ZombiesLocation.get_name_to_id(base_id)

    # Full Remote Items
    items_handling = 0b111

    enabled_location_names = []
    victory_items = []
    # Options
    the_giant_enabled = False
    victory_round = 1

    def generate_early(self) -> None:
        # read player settings to world instance
        self.the_giant_enabled = self.options.the_giant_enabled
        self.victory_round = self.options.victory_round
        if self.the_giant_enabled:
            #This only works if round are first, eventually replace this with a list of JUST round locations
            for i in range(0, self.victory_round):
                self.enabled_location_names.append(Locations.TheGiant_Locations[i].name)

    def create_regions(self):
        menu_region = self.create_region(self.multiworld, self.player, self.enabled_location_names, 'Menu', None)

        the_giant_courtyard_locations = [
            LocationName.TheGiant_Round1,
            LocationName.TheGiant_Round2,
            LocationName.TheGiant_Round3,
        ]
        # Default Balancing, Make sure you get to every region
        # TODO: Randomize this a bit/weight it

        the_giant_animal_testing_locations = [
            LocationName.TheGiant_Round4,
            LocationName.TheGiant_Round5,
            LocationName.TheGiant_Round6,
        ]
        the_giant_garage_locations = [
            LocationName.TheGiant_Round7,
            LocationName.TheGiant_Round8,
            LocationName.TheGiant_Round9,
        ]
        the_giant_power_room_locations = [
            LocationName.TheGiant_Round10,
            LocationName.TheGiant_Round11,
            LocationName.TheGiant_Round12,
            LocationName.TheGiant_Round13,
        ]
        the_giant_teleporter1_locations = [

        ]
        the_giant_teleporter2_locations = [
            LocationName.TheGiant_Round14,
            LocationName.TheGiant_Round15,
            LocationName.TheGiant_Round16,
            LocationName.TheGiant_Round17,
            LocationName.TheGiant_Round18,
            LocationName.TheGiant_Round19,
            LocationName.TheGiant_Round20,
        ]
        the_giant_teleporter3_locations = [
            LocationName.TheGiant_Round21,
            LocationName.TheGiant_Round22,
            LocationName.TheGiant_Round23,
            LocationName.TheGiant_Round24,
            LocationName.TheGiant_Round25,
            LocationName.TheGiant_Round26,
            LocationName.TheGiant_Round27,
            LocationName.TheGiant_Round28,
            LocationName.TheGiant_Round29,
            LocationName.TheGiant_Round30
        ]

        the_giant_courtyard_region = self.create_region(self.multiworld, self.player, self.enabled_location_names,
                                                        RegionName.TheGiant_Courtyard,
                                                        the_giant_courtyard_locations)
        
        the_giant_animal_testing_region = self.create_region(self.multiworld,self.player,self.enabled_location_names,RegionName.TheGiant_AnimalTesting,the_giant_animal_testing_locations)
        the_giant_garage_region = self.create_region(self.multiworld,self.player,self.enabled_location_names,RegionName.TheGiant_Garage,the_giant_garage_locations)
        the_giant_power_room_region = self.create_region(self.multiworld,self.player,self.enabled_location_names,RegionName.TheGiant_PowerRoom,the_giant_power_room_locations)
        the_giant_teleporter1_region = self.create_region(self.multiworld,self.player,self.enabled_location_names,RegionName.TheGiant_Teleporter1,the_giant_teleporter1_locations)
        the_giant_teleporter2_region = self.create_region(self.multiworld,self.player,self.enabled_location_names,RegionName.TheGiant_Teleporter2,the_giant_teleporter2_locations)
        the_giant_teleporter3_region = self.create_region(self.multiworld,self.player,self.enabled_location_names,RegionName.TheGiant_Teleporter3,the_giant_teleporter3_locations)


        self.multiworld.regions.extend([
            menu_region,

            the_giant_courtyard_region,
            the_giant_animal_testing_region,
            the_giant_garage_region,
            the_giant_power_room_region,
            the_giant_teleporter1_region,
            the_giant_teleporter2_region,
            the_giant_teleporter3_region,
        ])
        Regions.connect_regions(self.multiworld, self.player)

    def create_region(self, world: MultiWorld, player: int, active_location_names: list, name: str, locations=None):
        ret = Region(name, player, world)
        if locations:
            for location in locations:
                if location in active_location_names:
                    location = Locations.BO3ZombiesLocation(player, location, self.location_name_to_id[location], ret)
                    ret.locations.append(location)

        return ret

    def create_item(self, name: str) -> Item:
        useful_categories = {
        }

        # TODO: do a getProgressiveItems list instead
        progression_categories = {
            Items.BO3ZombiesItemCategory.WEAPONS,
            Items.BO3ZombiesItemCategory.BLOCKER,
            Items.BO3ZombiesItemCategory.MACHINE,
            Items.BO3ZombiesItemCategory.POWER,
            Items.BO3ZombiesItemCategory.EASTER_EGG,
            Items.BO3ZombiesItemCategory.VICTORY
        }
        data = self.item_name_to_id[name]

        if Items.all_items_dict[name].category in progression_categories:
            item_classification = ItemClassification.progression
        elif Items.all_items_dict[name].category in useful_categories:
            item_classification = ItemClassification.useful
        else:
            item_classification = ItemClassification.filler

        return Items.BO3ZombiesItem(name, item_classification, data, self.player)

    def create_filler(self) -> Item:
        # TODO make a proper filler item
        return self.create_item(ItemName.Points50)

    def create_items(self) -> None:

        enabled_items = Items.base_items

        if self.the_giant_enabled:
            enabled_items += Items.The_Giant_Items
        enabled_items_dict = {item_data.name: item_data for item_data in enabled_items}

        victory_round = self.victory_round.value

        if self.the_giant_enabled:
            self.victory_items.append(ItemName.TheGiant_Victory)
            victory_location = self.get_round_location_string("The Giant", victory_round)
            self.multiworld.get_location(victory_location, self.player).place_locked_item(
                self.create_item(ItemName.TheGiant_Victory))

        filler_count = len(self.enabled_location_names)
        exclude = [item for item in self.multiworld.precollected_items[self.player]]

        filler_count -= len(exclude)

        for item in map(self.create_item, enabled_items_dict):
            if (Items.all_items_dict[item.name] not in self.victory_items) and (item not in exclude):
                self.multiworld.itempool.append(item)
                filler_count -= 1

        # Creates filler in remaining slots
        self.multiworld.itempool.extend([self.create_filler() for _ in range(filler_count)])

    def generate_basic(self) -> None:
        # for debugging purposes, you may want to visualize the layout of your world. Uncomment the following code to
        # write a PlantUML diagram to the file "my_world.puml" that can help you see whether your regions and locations
        # are connected and placed as desired
        #from Utils import visualize_regions
        #visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
        pass

    def set_rules(self) -> None:
        # Collect all Victory Items for Victory
        self.multiworld.completion_condition[self.player] = lambda state: state.has_all(self.victory_items, self.player)

    def fill_slot_data(self) -> dict:
        slot_data = {
            'seed': "".join(
                self.multiworld.per_slot_randoms[self.player].choice(string.ascii_letters) for _ in range(16)),
            'base_id': str(self.base_id),
            "slot": self.multiworld.player_name[self.player]
        }
        for option_name in Options.bo3_zombies_options:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value
        return slot_data

    @staticmethod
    def get_round_location_string(map_name: str, victory_round: int):
        # TODO Make this nicer/more extendable
        if map_name == "The Giant":
            return Locations.TheGiant_Locations[victory_round - 1].name
        return ""
