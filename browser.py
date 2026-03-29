def browser():
  search_query = input(name + '@root > openbrowser > Enter text for search >>')
  url = f"https://www.google.com/search?q={search_query}"
  webbrowser.open(url)
