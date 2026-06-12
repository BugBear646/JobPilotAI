from browser.browser import BrowserManager

browser = BrowserManager()

page = browser.start()

page.goto("https://example.com")

print(page.title())

browser.stop()