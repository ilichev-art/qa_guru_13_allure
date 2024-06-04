from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_search_issue():
    browser.open('https://github.com')

    s('.search-input').click()
    s('#query-builder-test').type('eroshenkoam/Allure-example')
    s('#query-builder-test').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)


