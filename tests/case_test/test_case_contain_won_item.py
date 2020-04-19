from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def case_page_loaded_successfully_test(chrome_browser, test_link):
    chrome_browser.maximize_window()
    chrome_browser.get(test_link)

    WebDriverWait(chrome_browser, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.user__logged-out .btn'))
    )
    login_button = len(chrome_browser.find_elements_by_css_selector('.user__logged-out .btn'))
    assert login_button == 1


def user_logged_in_successfully_test(chrome_browser, login, password):
    case_page = chrome_browser.current_window_handle

    login_button = chrome_browser.find_element_by_css_selector('.user__logged-out .btn')
    login_button.click()

    for handle in chrome_browser.window_handles:
        if handle != case_page:
            login_page = handle

    chrome_browser.switch_to.window(login_page)

    chrome_browser.find_element_by_id('steamAccountName').send_keys(login)
    chrome_browser.find_element_by_id('steamPassword').send_keys(password)
    chrome_browser.find_element_by_id('imageLogin').click()

    chrome_browser.switch_to.window(case_page)

    WebDriverWait(chrome_browser, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.user__logged-in'))
    )
    user_name = len(chrome_browser.find_elements_by_css_selector('.user__logged-in'))
    assert user_name == 1


def case_is_opened_successfully_test(chrome_browser):
    quick_open_button = chrome_browser.find_element_by_css_selector('.case-item__open-case-fast-btn')
    quick_open_button.click()
    WebDriverWait(chrome_browser, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.case-win-block__sell-item-btn'))
    )
    sell_item_box = len(chrome_browser.find_elements_by_css_selector('.case-win-block__sell-item-btn'))
    assert sell_item_box == 1


def won_item_contains_in_the_case_test(chrome_browser):

    actions = ActionChains(chrome_browser)
    won_item = chrome_browser.find_element_by_css_selector('.case-win-block__type')
    actions.move_to_element(won_item).perform()

    won_item_type = chrome_browser.find_element_by_css_selector('.case-win-block__type').get_attribute('innerText')
    won_item_name = chrome_browser.find_element_by_css_selector('.case-win-block__name').get_attribute('innerText')

    won_item = [won_item_type, won_item_name]
    separator = ' '
    won_item_full_name = (separator.join(won_item))

    social_line = chrome_browser.find_element_by_css_selector('.socials.socials_lines')
    actions.move_to_element(social_line).perform()

    items_names_in_case = []
    case_guns_names = chrome_browser.find_elements_by_css_selector('.case-items__item-name')
    for name in case_guns_names:
        items_names_in_case.append(name.get_attribute('innerText'))

    items_titles_in_case = []
    case_guns_titles = chrome_browser.find_elements_by_css_selector('.case-items__item-title')
    for title in case_guns_titles:
        items_titles_in_case.append(title.get_attribute('innerText'))

    case_guns_full_names = list(map(' '.join, zip(items_names_in_case, items_titles_in_case)))

    assert won_item_full_name in case_guns_full_names










