class InputPage:

    def __init__(self, page):
        self.url = 'https://testpages.herokuapp.com/styled/validation/input-validation.html'
        self.page = page

    def open(self):
        self.page.goto(self.url)

    def fill_inputs(self, first_name, last_name, age, country, text=''):
        self.page.fill('id=firstname', first_name)
        self.page.fill('id=surname', last_name)
        self.page.fill('id=age', age)
        self.page.select_option('id=country', country)
        self.page.fill('id=notes', text)

    def click_submit(self):
        self.page.click('//input[@type="submit"]')

    def input_validation(self):
        return self.page.text_content('li')

    def current_url(self):
        return self.page.url







