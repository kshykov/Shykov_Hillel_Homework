import pytest
from Shykov_Homework.hw_lesson_17 import ArtPrint, CanvasPrint, PrintedProduct


@pytest.mark.art_prints_tests
def test_art_print():
    title_test = "Print to test"
    author_test = "Generated author"
    price_test = 99.99

    test_art_print_1 = ArtPrint(title_test, author_test, price_test, "paper")

    assert title_test == test_art_print_1.title
    assert author_test == test_art_print_1.author
    assert price_test == test_art_print_1.price


@pytest.mark.canvas_prints_tests
def test_canvas_print():
    title_test = "Canvas to test"
    author_test = "Generated author# 2"
    price_test = 123.44
    frame_test = "metal"

    test_canvas_print_1 = CanvasPrint(title_test, author_test, price_test, frame_test)

    assert title_test == test_canvas_print_1.title
    assert author_test == test_canvas_print_1.author
    assert price_test == test_canvas_print_1.price