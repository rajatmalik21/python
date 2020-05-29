from selenium import webdriver

from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path="C:/Users/Rajat/Downloads/chromedriver_win32/chromedriver.exe")

chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote)
