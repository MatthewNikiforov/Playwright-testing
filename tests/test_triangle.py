import pytest
from pages.triangle_page import TrianglePage


@pytest.mark.parametrize('side1, side2, side3', [('1', '1', '1'), ('3', '3', '3')])
def test_tr_equilateral(page, side1, side2, side3):
    tr_page = TrianglePage(page)
    tr_page.open()
    tr_page.fill_triangle_sides(side1, side2, side3)
    assert tr_page.identify_triangle() == 'Equilateral'


@pytest.mark.parametrize('side1, side2, side3', [('3', '5', '3'), ('2', '2', '3')])
def test_tr_isosceles(page, side1, side2, side3):
    tr_page = TrianglePage(page)
    tr_page.open()
    tr_page.fill_triangle_sides(side1, side2, side3)
    assert tr_page.identify_triangle() == 'Isosceles'


@pytest.mark.parametrize('side1, side2, side3', [('3', '5', '4'), ('6', '4', '9')])
def test_tr_scalene(page, side1, side2, side3):
    tr_page = TrianglePage(page)
    tr_page.open()
    tr_page.fill_triangle_sides(side1, side2, side3)
    assert tr_page.identify_triangle() == 'Scalene'


@pytest.mark.parametrize('side1, side2, side3, missing_side', [('', '5', '4', '1'), ('6', '', '9', '2'),
                                                               ('6', '4', '', '3')])
def test_tr_missing_side(page, side1, side2, side3, missing_side):
    tr_page = TrianglePage(page)
    tr_page.open()
    tr_page.fill_triangle_sides(side1, side2, side3)
    assert tr_page.identify_triangle() == f'Error: Side {missing_side} is missing'


@pytest.mark.parametrize('side1, side2, side3', [('0', '0', '0'), ('6', '3', '9'), ('3', '-4', '5')])
def test_tr_not_triangle(page, side1, side2, side3):
    tr_page = TrianglePage(page)
    tr_page.open()
    tr_page.fill_triangle_sides(side1, side2, side3)
    assert tr_page.identify_triangle() == 'Error: Not a Triangle'
