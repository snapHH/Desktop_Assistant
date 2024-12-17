import webbrowser

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return {"status": "success", "message": f"Searching for {query}"}
