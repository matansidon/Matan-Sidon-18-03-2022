import keyboard as keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbra:
    driver = ''

    def setup(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.get('https://automation.herolo.co.il/')
        self.driver.maximize_window()
        time.sleep(2)

    def test_want_to_hear_more(self):
        search=self.driver.find_element(By.XPATH,"//input[@id='name']")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        search.send_keys('check')
        search=self.driver.find_element(By.XPATH, "//input[@id='company']")
        search.send_keys('check')
        search=self.driver.find_element(By.XPATH, "//input[@id='email']")
        search.send_keys('check@g.com')
        search=self.driver.find_element(By.XPATH, "//input[@id='telephone']")
        search.send_keys('035555555')
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@class='commun__Button-zi6nvq-0 commun__ButtonContact-zi6nvq-1 form__ButtonContact-y0ft28-1 llCdxe']").click()
        time.sleep(3)
        expected_url='https://automation.herolo.co.il/thank-you/'
        assert self.driver.current_url == expected_url
        self.driver.find_element_by_xpath("//a[@class='thankYou__backLink-avz2fr-10 bBzcJF']").click()

    def test_how_can_i_help(self):
        search=self.driver.find_element_by_xpath("//input[@name='name']")
        search.send_keys('check')
        time.sleep(1)
        search=self.driver.find_element_by_xpath("//input[@name='email']")
        search.send_keys('check@g.com')
        time.sleep(1)
        search=self.driver.find_element_by_xpath("//input[@name='phone']")
        search.send_keys('035555555')
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='Footer__Button-sc-159s1ql-7 kOOAFW']").click()
        time.sleep(3)
        expected_url = 'https://automation.herolo.co.il/thank-you/'
        assert self.driver.current_url == expected_url
        self.driver.find_element_by_xpath("//a[@class='thankYou__backLink-avz2fr-10 bBzcJF']").click()

    def test_whatsapp_btn(self):
        self.driver.find_element_by_xpath("//a[@class='callUsWhatsapp__BtnWhatsapp-rkzbui-0 cjunrQ']").click()
        time.sleep(3)
        assert len(self.driver.window_handles) == 2

    def test_down_btns(self):
        self.driver.find_element_by_xpath("//a[@class='socialMediaBar__ImgSocial-sc-1ry1db0-2 gcUHBk']").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath("//a[@class='socialMediaBar__ImgSocial-sc-1ry1db0-2 jOgeKm']").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath("//a[@class='socialMediaBar__ImgSocial-sc-1ry1db0-2 eufMcD']").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath("//a[@class='socialMediaBar__ImgSocial-sc-1ry1db0-2 bXWGqN']").click()

        assert len(self.driver.window_handles) == 5

    def test_email(self):
        self.driver.find_element_by_xpath("//a[@class='commun__ContactText-zi6nvq-7 kTeJTM']").click()
        time.sleep(2)
        actual_mail_address=self.driver.find_element_by_xpath("//a[@class='commun__ContactText-zi6nvq-7 kTeJTM']").get_attribute('href')
        keyboard.press('alt')
        keyboard.press('f4')
        expected_mail_address='mailto:mati@herolo.co.il'
        assert actual_mail_address==expected_mail_address

    def test_to_top_btn(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@class='backToTop__BtnGoUp-z83xj1-0 huPgzm']").click()
        time.sleep(3)

    def test_scroll_btns_of_sample_jobs_and_clients(self):
        self.driver.execute_script("document.body.style.zoom='40%'")
        search = self.driver.find_element_by_xpath("//section[@class='portfolio__Portfolio-sc-80s039-0 bMmzri']")
        search.location_once_scrolled_into_view
        btns=self.driver.find_elements(By.XPATH,"//div[@class='commun__Paging-zi6nvq-3 jZSvee']")
        time.sleep(2)
        for btn in btns:
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)

    def teardown(self):
        self.driver.quit()
