import time

def test_mobile(andr):
    list=[]
    andr.driver.get("https://pfm.team/")
    time.sleep(5)
    andr.driver.swipe(470, 1400, 470, 1000, 400)
    my_elems = andr.driver.find_elements_by_xpath(".//*")
    for elem in my_elems:
        list.append(elem.text)
    assert "Recommendation-based social network." in list