# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_invalid_quality(self):
        items = [Item("item1", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(39, items[0].quality) # quality decreases by 1

    def test_sell_in_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(20, items[0].quality) # quality does not change

    def test_quality_aged_brie(self):
        items = [Item("Aged Brie", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(42, items[0].quality) # quality increases by 2


if __name__ == '__main__':
    unittest.main()
