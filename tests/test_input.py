import pytest
from pages.input_page import InputPage


@pytest.mark.parametrize('name, surname, age, country, text', [('name0', 'surname0000', '22', 'Russia', 'text'),
                                                               ('name1', '', '42', 'Belgium', '')])
def test_valid_input(page, name, surname, age, country, text):
    input_page = InputPage(page)
    input_page.open()
    input_page.fill_inputs(name, surname, age, country, text)
    input_page.click_submit()
    assert input_page.input_validation() == 'Valid InputYour Input passed validation'


@pytest.mark.parametrize('name, surname, age, country, text', [('name', 'surname0000', '22', 'Russia', 'text'),
                                                               ('aaa', 'surname0000', '18', 'Afghanistan', 'text')])
def test_invalid_input(page, name, surname, age, country, text):
    input_page = InputPage(page)
    input_page.open()
    input_page.fill_inputs(name, surname, age, country, text)
    input_page.click_submit()
    assert input_page.input_validation() == 'Firstname ErrorFirstname too short'


@pytest.mark.parametrize('name, surname, age, country, text', [('', 'surname0000', '22', 'Russia', 'text'),
                                                               ('name1', 'surname0000', '12', 'Afghanistan', 'text'),
                                                               ('name1', 'surname', '25', 'Afghanistan', 'text')])
def test_wrong_input(page, name, surname, age, country, text):
    input_page = InputPage(page)
    input_page.open()
    input_page.fill_inputs(name, surname, age, country, text)
    input_page.click_submit()
    assert input_page.current_url() == input_page.url
