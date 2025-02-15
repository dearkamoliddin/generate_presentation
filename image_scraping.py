import time

import requests
from selenium import webdriver
import os
from selenium.webdriver.common.by import By


def get_images(query):
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver'))
    wd = webdriver.Chrome(PATH)
    wd.get(f"https://www.google.com/search?q={query}&tbm=isch")

    image_set = set()
    while len(image_set) < 2:
        thumbnails = wd.find_elements(By.CLASS_NAME, "F0uyec")
        for thumbnail in thumbnails:
            thumbnail.click()
            time.sleep(4)
            images = wd.find_elements(By.CLASS_NAME, "sFlh5c")
            for image in images:
                image_set.add(image.get_attribute('src'))
                if len(image_set) >= 2:
                    return image_set


def download_images(image_set):
    for i, image in enumerate(image_set):
        with open(f"image{i}.jpg", "wb") as file:
            file.write(requests.get(image).content)


if __name__ == '__main__':
    print(get_images("polar bears"))




