
concert = "Backstage passes to a TAFKAL80ETC concert"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != concert:
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                self.manage_concert_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            self.manage_out_of_date_items(item)

    def manage_out_of_date_items(self, item):
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != concert:
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = 0
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

    def manage_concert_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == concert:
                if item.sell_in < 11 and item.quality <50:
                        item.quality = item.quality + 1
                if item.sell_in < 6 and item.quality <50:
                        item.quality = item.quality + 1
