import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose language: 'en' or 'es' or 'fr'")


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")

    if user_language == "en":
        print("\nstart chrome browser for test in en..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
        browser = webdriver.Chrome(options=options)
    elif user_language == "es":
        print("\nstart chrome browser for test in es..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        browser = webdriver.Chrome(options=options)
    elif user_language == "fr":
        print("\nstart chrome browser for test in fr..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nstart chrome browser for test in fr..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()