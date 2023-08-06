import unittest
import surfshop


class SurfshopTest(unittest.TestCase):
    def setUp(self):
        self.card = surfshop.ShoppingCart()

    def test_add_1_surfboards(self):
        message = self.card.add_surfboards(1)
        self.assertEqual(message, "Successfully added 1 surfboard to cart!")

    def test_add_2_surfboads(self):
        message = self.card.add_surfboards(2)
        self.assertEqual(message, "Successfully added 2 surfboards to cart!")

    @unittest.skip
    def test_too_many(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    @unittest.expectedFailure
    def test_discount(self):
        self.assertTrue(surfshop.ShoppingCart.apply_locals_discount() is True)


unittest.main()
