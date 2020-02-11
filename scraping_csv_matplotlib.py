from pprint import pprint
from requests_html import HTMLSession


session = HTMLSession()
r = session.get('https://python.org/')

data = r.html.find('#touchnav-wrapper > header > div', first=True)
print(data.text)
# print(data.attrs)
