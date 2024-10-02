# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_invalid_quality(self):
        items = [Item("item1", 0, 60)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(60, items[0].quality) # invalid number greater than 50

    def test_sell_in_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(0, items[0].sell_in) # expects sell_in 1

    def test_quality_aged_brie(self):
        items = [Item("Aged Brie", 2, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(1, items[0].quality) # expects quality 2


if __name__ == '__main__':
    unittest.main()
