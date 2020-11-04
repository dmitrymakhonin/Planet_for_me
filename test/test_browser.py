import time

from selenium.webdriver.common.by import By
# не разделял тест на отдельные методы
def test_browser(app):
    links = []
    data = "https://pfm.team/"
    app.driver.get("https://www.google.com/")
    app.driver.find_element(By.NAME, "q").click()
    # Изменил текст вводимый в поисковик т.к на "Planet for me" мне не выдает указанный сайт
    # долистал до 5й страницы, дальше смотреть не стал
    app.driver.find_element(By.NAME, "q").send_keys("pfm.team")
    time.sleep(1)  # слип т.к кнопка поиска не успевает прогружаться
    app.driver.find_element(By.NAME, "btnK").click()
    l = list(app.driver.find_elements(By.XPATH, "//div[@class='rc']//div[@class='yuRUbf']//a"))
    # Создание списка со всеми ссылками со страницы
    for link in l:
        links.append(link.get_attribute("href"))
    assert data in links
    app.driver.find_element(By.XPATH, "//span[contains(.,\'Planet for me - personal recommendation service\')]").click()
    a = app.driver.find_element(By.CLASS_NAME, "main-heading").text
    assert a == "Recommendation-based social network."