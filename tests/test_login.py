import pytest
import allure

@allure.epic("User")
@allure.feature("login")
@allure.story("Test")
class TestPages:

    @allure.title("Login")
    @allure.link(url="fffhhg", name="Documention")
    @pytest.mark.smoke
    def test_open_login_page(self, driver):
        with allure.step("Step1"):
            self.driver.get("https://demoqa.com/login")
            assert self.driver.current_url == "https://demoqa.com/login", "Ошибка ULR страницы входа"

    @pytest.mark.regression
    def test_open_books_page(self, driver):
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка ULR страницы с книгами"
