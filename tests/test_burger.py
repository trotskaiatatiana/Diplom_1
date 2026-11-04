import pytest
from unittest.mock import MagicMock

from praktikum.burger import Burger

class TestBurger:

    def test_init_bun_is_none(self):
        burger = Burger()
        assert burger.bun is None

    def test_init_ingredients_is_empty(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger):
        ingredients = [MagicMock(), MagicMock(), MagicMock()]
        burger.ingredients = ingredients.copy()

        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredients[0], ingredients[2]]

    @pytest.mark.parametrize(
        "index, new_index, expected_order",
        [
            (0, 2, [1, 2, 0]),
            (2, 0, [2, 0, 1]),
            (1, 1, [0, 1, 2]),
        ]
    )
    def test_move_ingredient(self, burger, index, new_index, expected_order):
        burger.ingredients = [0, 1, 2]

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == expected_order

    
    def test_get_price_without_ingredients_returns_double_bun_price(self, burger, bun):
        burger.set_buns(bun)

        assert burger.get_price() == 200

    def test_get_price_with_one_ingredient_adds_its_price(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 250

    def test_get_price_with_two_ingredients_returns_sum(self, burger, bun, ingredient, sauce):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(sauce)

        assert burger.get_price() == 280

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cheese =\n"
            "(==== black bun ====)\n\n"
            "Price: 250"
        )

        assert burger.get_receipt() == expected_receipt
