import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_search_issue():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_number('#76')




@allure.step('Open main page')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Find Allure repository {repo}')
def search_for_repository(repo):
    s('.search-input').click()
    s('#query-builder-test').type(repo)
    s('#query-builder-test').submit()

@allure.step('Follow the link {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Open Issues')
def open_issue_tab():
    s('#issues-tab').click()

@allure.step('Check issue {number} availability')
def should_see_number(number):
    s(by.partial_text(number)).should(be.visible)