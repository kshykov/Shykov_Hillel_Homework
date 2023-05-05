import pytest
from Shykov_Homework.hw_lesson_17 import ArtPrint, CanvasPrint

@pytest.fixture
def art_print():
    test_art_print = ArtPrint("Clouds at the night", "Cho Lee", 99.99, "paper")


@pytest.fixture
def canvas():
    test_canvas = CanvasPrint("Burger menu", "David-D", 9999, "metal")



