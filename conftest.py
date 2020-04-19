import pytest
from pytest import fixture
from selenium import webdriver


@fixture(scope='module')
def test_link():
    case_link = 'https://three.jcdev.ru/cases/open/falchion'
    return case_link


@fixture(scope='module')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser


@fixture(scope='module')
def login():
    acc_name = 'levian5'
    return acc_name


@fixture(scope='module')
def password():
    valid_password = 'Nokiabesthpkkbest1'
    return valid_password

