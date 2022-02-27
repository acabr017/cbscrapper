import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


def cb_cvs_writer(driver):
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    assignment_name = driver.find_element(By.CSS_SELECTOR, 'h1.text-center').text
    assessment_csv = str(assignment_name) + '.csv'
    header = 'Question Number, Topic, Skill, Correct, Incorrect, Blank, Total \n'
    file = open(assessment_csv, 'w')
    file.write(header)
    for row in rows[1:22]:
        question_number = str(row.find_element(By.CLASS_NAME, 'font-bold').text)
        topic = str(row.find_element(By.TAG_NAME, 'button ').text)
        skill = str(row.find_element(By.CLASS_NAME, 'PracticeSkillsContainer').text)
        try:
            blank = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--default').text
        except NoSuchElementException:
            blank = '0'

        try:
            incorrect = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--incorrect').text
        except NoSuchElementException:
            incorrect = '0'

        try:
            correct = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--correct').text
        except NoSuchElementException:
            correct = '0'

        file.write(
            question_number + ',' + topic + ',' + skill + ',' + correct + ',' + incorrect + ',' + blank + ',' + str(
                int(correct) + int(incorrect) + int(blank)) + '\n')
    file.close()
