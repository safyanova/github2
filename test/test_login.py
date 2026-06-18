import pytest
import allure

@allure.epic("User")
@allure.feature("login")
@allure.story("Test")
class TestPages:

    @allure.title("Login")
    @allure.link(url="fffhhg", name="Documention")
    @pytest.mark.smoke
    def test_open_login_page(self):
        with allure.step("Step1"):
            self.driver.get("https://demoqa.com/login")
            assert self.driver.current_url == "https://demoqa.com/login", "Ошибка ULR страницы входа"

    @pytest.mark.regression
    def test_open_books_page(self):
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка ULR страницы с книгами"

    @pytest.mark.profile    def test_open_profile_page(self):
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка ULR страницы профиля"