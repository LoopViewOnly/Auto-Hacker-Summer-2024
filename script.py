from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import random

def gen_rand_num(length):
    digs = ["0", "1", "2"]
    rand_num = ""
    for counter in range(length):
        rand_dig = random.choice(digs)
        rand_num += rand_dig

    return rand_num


browser = webdriver.Chrome()

browser.get("https://bruteforce-nu.vercel.app?animate=false")
number_input = browser.find_element(By.XPATH, '//*[@id="root"]/div/form/input[1]')

while True:
    if browser.title == 'Level 1':
        number_input.send_keys(gen_rand_num(2) + '\n')
    elif browser.title == 'Level 2':
        number_input.send_keys(gen_rand_num(3) + '\n')
    elif browser.title == 'Level 3':
        number_input.send_keys(gen_rand_num(4) + '\n')
    else:
        break
sleep(20)

