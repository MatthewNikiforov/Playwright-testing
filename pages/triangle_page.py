class TrianglePage:

    def __init__(self, page):
        self.url = 'https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html'
        self.page = page

    def open(self):
        self.page.goto(self.url)

    def fill_triangle_sides(self, first_side, second_side, third_side):
        self.page.fill('id=side1', first_side)
        self.page.fill('id=side2', second_side)
        self.page.fill('id=side3', third_side)
        self.page.click('id=identify-triangle-action')

    def identify_triangle(self):
        return self.page.text_content('id=triangle-type')

