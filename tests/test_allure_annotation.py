import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Search')
@allure.link('https://github.com', name='Testing')
@allure.story('User can find issue')
@allure.label('owner', 'ailichev')
@allure.description('Test-case to check allure annotations')


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.label('owner', 'ailichev')
    allure.dynamic.story('User can find issue')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature('Search')
    allure.dynamic.link('https://github.com', name='Testing')
    allure.dynamic.description('Test-case to check allure annotations')
    pass
