from functools import reduce
import Test


class CoffeeShop:
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders

    def add_order(self, order):
        for item in self.menu:
            if (item['item'] == order):
                self.orders.append(order)
                return "Order added!"
        return "This item is currently unavailable!"

    def fulfill_order(self):
        if (len(self.orders) == 0):
            return "All orders have been fulfilled!"
        return "The {item} is ready!".format(item=self.orders.pop(0))

    def list_orders(self):
        return self.orders

    def due_amount(self):
        due = 0
        for order in self.orders:
            due += list(filter(lambda item: item['item']
                               == order, self.menu))[0]['price']
        return round(due, 2)

    def cheapest_item(self):
        cheapest = {'price': 50000}
        for item in self.menu:
            if (item['price'] < cheapest['price']):
                cheapest = item
        return cheapest['item']

    def drinks_only(self):
        return list(map(lambda item: item['item'], filter(lambda item: item['type'] == 'drink', self.menu)))

    def food_only(self):
        return list(map(lambda item: item['item'], filter(lambda item: item['type'] == 'food', self.menu)))


m1, m2, m3 = [
    ["orange juice", "drink", 2.13], ["lemonade", "drink", 0.85], [
        "cranberry juice", "drink", 3.36],
    ["pineapple juice", "drink", 1.89], ["lemon iced tea",
                                         "drink", 1.28], ["apple iced tea", "drink", 1.28],
    ["vanilla chai latte", "drink", 2.48], ["hot chocolate",
                                            "drink", 0.99], ["iced coffee", "drink", 1.12],
    ["tuna sandwich", "food", 0.95], ["ham and cheese sandwich",
                                      "food", 1.35], ["bacon and egg", "food", 1.15],
    ["steak", "food", 3.28], ["hamburger", "food", 1.05], [
        "cinnamon roll", "food", 1.05]
], [
    ["turkey english muffin", "food", 7.99], ["avocado toast",
                                              "food", 5.05], ["chocolate croissant", "food", 3.00],
    ["espresso", "drink", 2.99], ["iced caramel macchiato",
                                  "drink", 4.50], ["cortado", "drink", 4.00],
    ["nitro cold brew tester", "drink", 8.00]
], [
    ["cheeseburger with fries", "food", 5.44],
    ["cinnamon roll", "food", 4.99],
    ["hot chocolate", "drink", 2.99],
    ["lemon tea", "drink", 2.50],
    ["iced coffee", "drink", 3.00],
    ["vanilla chai latte", "drink", 4.00]
]
menu1 = [{'item': x[0], 'type': x[1], 'price': x[2]} for x in m1]
menu2 = [{'item': x[0], 'type': x[1], 'price': x[2]} for x in m2]
menu3 = [{'item': x[0], 'type': x[1], 'price': x[2]} for x in m3]

shopx = CoffeeShop("Xavier's", menu1, list())
Test.assert_equals(shopx.add_order('cinnamon roll'), 'Order added!')
Test.assert_equals(shopx.add_order('iced coffee'), 'Order added!')
Test.assert_equals(shopx.list_orders(), ['cinnamon roll', 'iced coffee'])
Test.assert_equals(shopx.due_amount(), 2.17)
Test.assert_equals(shopx.fulfill_order(), 'The cinnamon roll is ready!')
Test.assert_equals(shopx.fulfill_order(), 'The iced coffee is ready!')
Test.assert_equals(shopx.fulfill_order(), 'All orders have been fulfilled!')
Test.assert_equals(shopx.add_order('hot cocoa'),
                   'This item is currently unavailable!')
Test.assert_equals(shopx.add_order('iced tea'),
                   'This item is currently unavailable!')
Test.assert_equals(shopx.list_orders(), [])
Test.assert_equals(shopx.due_amount(), 0)
Test.assert_equals(shopx.cheapest_item(), 'lemonade')
Test.assert_equals(shopx.drinks_only(), ['orange juice', 'lemonade', 'cranberry juice', 'pineapple juice',
                   'lemon iced tea', 'apple iced tea', 'vanilla chai latte', 'hot chocolate', 'iced coffee'])
Test.assert_equals(shopx.food_only(), [
                   'tuna sandwich', 'ham and cheese sandwich', 'bacon and egg', 'steak', 'hamburger', 'cinnamon roll'])

shopy = CoffeeShop('Deep Into Coffee', menu2, list())
Test.assert_equals(shopy.add_order("cortado"), "Order added!")
Test.assert_equals(shopy.fulfill_order(), "The cortado is ready!")
Test.assert_equals(shopy.fulfill_order(), "All orders have been fulfilled!")
Test.assert_equals(shopy.add_order("avocado toast"), "Order added!")
Test.assert_equals(shopy.list_orders(), ["avocado toast"])
Test.assert_equals(shopy.due_amount(), 5.05)
Test.assert_equals(shopy.cheapest_item(), "espresso")
Test.assert_equals(shopy.drinks_only(), [
                   "espresso", "iced caramel macchiato", "cortado", "nitro cold brew tester"])
Test.assert_equals(shopy.food_only(), [
                   "turkey english muffin", "avocado toast", "chocolate croissant"])

shopz = CoffeeShop("Tesha's", menu3, list())
Test.assert_equals(shopz.add_order("hot cocoa"),
                   "This item is currently unavailable!")
Test.assert_equals(shopz.due_amount(), 0)
Test.assert_equals(shopz.add_order("cheeseburger with fries"), "Order added!")
Test.assert_equals(shopz.add_order("lemon tea"), "Order added!")
Test.assert_equals(shopz.add_order("iced coffee"), "Order added!")
Test.assert_equals(shopz.list_orders(), [
                   "cheeseburger with fries", "lemon tea", "iced coffee"])
Test.assert_equals(shopz.due_amount(), 10.94)
Test.assert_equals(shopz.fulfill_order(),
                   "The cheeseburger with fries is ready!")
Test.assert_equals(shopz.fulfill_order(), "The lemon tea is ready!")
Test.assert_equals(shopz.fulfill_order(), "The iced coffee is ready!")
Test.assert_equals(shopz.list_orders(), [])
Test.assert_equals(shopz.cheapest_item(), "lemon tea")
Test.assert_equals(shopz.drinks_only(), [
                   "hot chocolate", "lemon tea", "iced coffee", "vanilla chai latte"])
Test.assert_equals(shopz.food_only(), [
                   "cheeseburger with fries", "cinnamon roll"])
