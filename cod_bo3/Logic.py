from .Names import ItemName
from ..AutoWorld import LogicMixin


class CODBO3Logic(LogicMixin):
    def bo3_the_giant_animaltesting_unlocked(self, player):
        return self.has(ItemName.TheGiant_AnimalTesting, player)
    def bo3_the_giant_garage_unlocked(self, player):
        return self.has(ItemName.TheGiant_Garage, player)
    def bo3_the_giant_power_room_unlocked(self, player):
        return self.has(ItemName.TheGiant_PowerRoom, player)
    def bo3_the_giant_teleporter1_unlocked(self, player):
        return self.has(ItemName.TheGiant_Teleporter1, player)
    def bo3_the_giant_teleporter2_unlocked(self, player):
        return self.has(ItemName.TheGiant_Teleporter2, player)
    def bo3_the_giant_teleporter3_unlocked(self, player):
        return self.has(ItemName.TheGiant_Teleporter3, player)