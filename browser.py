import webbrowser
from urllib.parse import quote

def browser():
    search_query = input('openbrowser > Enter text for search >> ')
    encoded_query = quote(search_query)  # кодируем кириллицу в URL
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)
