import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_search_issue():
    with allure.step('Open main page'):
        browser.open('https://github.com')

    with allure.step('Find Allure repository'):
        s('.search-input').click()
        s('#query-builder-test').type('eroshenkoam/Allure-example')
        s('#query-builder-test').submit()

    with allure.step('Follow the link'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open Issues'):
        s('#issues-tab').click()

    with allure.step('Check issue availability'):
        s(by.partial_text('#76')).should(be.visible)