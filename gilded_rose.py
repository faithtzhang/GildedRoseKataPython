# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC


# Helper function to check for invalid quality
def validate_quality(item):
    if item.quality > 50 or item.quality < 0:
        raise ValueError(f"Invalid quality for item {item.name}: {item.quality}")


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Use strategy pattern to update quality
class ItemUpdateStrategy(ABC):
    @abstractmethod
    def update_quality(self, item: "Item"):
        pass


# update for normal items
class NormalItemUpdate(ItemUpdateStrategy):
    def update_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:  # past sell in, degrade twice as fast.
            item.quality -= 1
        validate_quality(item)


# update for "Aged Brie"
class AgedBrieUpdate(ItemUpdateStrategy):
    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
        validate_quality(item)


# update for "Backstage passes to a TAFKAL80ETC concert"
class BackstagePassesUpdate(ItemUpdateStrategy):
    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11:
                item.quality += 1
            if item.sell_in < 6:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        validate_quality(item)


# update for "Sulfuras, Hand of Ragnaros"
class SulfurasUpdate(ItemUpdateStrategy):
    def update_quality(self, item: Item):
        validate_quality(item)
        pass  # Sulfuras does not change


class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

        self.updateMethods = {
            "Aged Brie": AgedBrieUpdate(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdate(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdate(),
        }

    def update_quality(self):
        for item in self.items:
            try:
                updater = self.updateMethods.get(item.name, NormalItemUpdate())
                updater.update_quality(item)
            except ValueError as e:
                print(f"Error updating quality for {item.name}: {e}")
