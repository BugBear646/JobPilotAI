from browser.browser import BrowserManager
from browser.login import LoginManager

browser = BrowserManager()

page = browser.start()

login = LoginManager(page)

login.login()

print("SUCCESS")

browser.stop()