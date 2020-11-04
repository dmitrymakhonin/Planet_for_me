from selenium import webdriver
class Application:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(
            "user-data-dir=C:\\Users\\Dijta\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        # путь до профиля хрома для избежания прохождения капчи
        self.driver = webdriver.Chrome(chrome_options=options)

    def destroy(self):
        self.driver.quit()


