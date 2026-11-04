
import pytest
from unittest.mock import MagicMock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    mock_bun = MagicMock()
    mock_bun.get_name.return_value = "black bun"
    mock_bun.get_price.return_value = 100
    return mock_bun


@pytest.fixture
def sauce():
    mock_sauce = MagicMock(spec=Ingredient)
    mock_sauce.get_name.return_value = "hot sauce"
    mock_sauce.get_price.return_value = 30
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_sauce


@pytest.fixture
def ingredient():
    mock_ingredient = MagicMock()
    mock_ingredient.get_name.return_value = "cheese"
    mock_ingredient.get_price.return_value = 50
    mock_ingredient.get_type.return_value = "FILLING"
    return mock_ingredient
