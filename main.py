from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

import time

SCROLL_NUMBER = 10
SIMILAR_ACC = "positivo_buenasvibras"
USERNAME = "frasesdevibraspositivas"
PASSWORD = "XX"

CHROME_PATH = r"C:\Users\pc\PycharmProjects\Web Development_DONE/chromedriver.exe"


class InstaFollower:
    def __init__(self, path):
        service = Service(path)
        self.driver = webdriver.Chrome(service=service)

    def login(self, username, pw):
        d = self.driver
        d.maximize_window()
        d.get("http://instagram.com")

        time.sleep(1)
        cookies = d.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        cookies.click()

        time.sleep(2)
        login = d.find_element(By.XPATH,
                               "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        login.send_keys(username)

        password = d.find_element(By.XPATH,
                                  "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password.send_keys(pw)
        time.sleep(1)
        password.send_keys(Keys.ENTER)

    def find_followers(self, sim_acc):
        d = self.driver
        time.sleep(5)
        notifications = d.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
        notifications.click()
        time.sleep(2)

        search = d.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys(sim_acc)
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)

        time.sleep(2)
        followers = d.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()

        time.sleep(3)
        scroll_button = d.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]")
        for _ in range(100):
            d.execute_script("arguments[0].scrollTop=arguments[0].scrollHeight", scroll_button)
            print(_)

    def follow(self):
        d = self.driver
        time.sleep(1)
        followers = d.find_elements(By.CLASS_NAME, "PZuss li button")
        for element in followers:
            time.sleep(1)
            try:
                element.click()
            except ElementClickInterceptedException:
                try:
                    cancel = d.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                    cancel.click()
                except NoSuchElementException:
                    ok = d.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[2]/button[2]")
                    ok.click()


insta_follower = InstaFollower(CHROME_PATH)
insta_follower.login(USERNAME, PASSWORD)
insta_follower.find_followers(SIMILAR_ACC)
insta_follower.follow()
