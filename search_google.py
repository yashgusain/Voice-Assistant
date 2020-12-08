import webbrowser as wb
def google_search(query):
  search=query
  search.replace(" ","+")
  return wb.open("https://www.google.com/search?sxsrf=ALeKk01BD6AglxCcg54Xt0IE5sKU1pTDkw%3A1607436721145&ei=sYnPX_6tCMz39QOW74iIBA&q="+search+"&oq="+search+"&gs_lcp=CgZwc3ktYWIQAxgAUABYAGAkaABwAHgAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpeg&sclient=psy-ab")
