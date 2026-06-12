from browser.browser import BrowserManager
from browser.login import LoginManager
from browser.search import SearchManager

browser = BrowserManager()

page = browser.start()

login = LoginManager(page)

login.login()

search = SearchManager(page)

config = search.get_user_preferences()

print(config)

search.open_search(
    config["roles"],
    config["location"],
)

input("\nPress ENTER to exit...")

browser.stop()