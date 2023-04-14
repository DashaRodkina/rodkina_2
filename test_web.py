import pytest


@pytest.mark.usefixtures("setup")
class Tests:
    def test_title(self):
        self.driver.get('https://dodopizza.ru/saransk')
        assert self.driver.title == "Пицца Саранск — заказать с доставкой на дом бесплатно, доставка еды из пиццерии Додо"
