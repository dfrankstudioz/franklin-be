import requests
from bs4 import BeautifulSoup

def test_ui_serves_html_title():
    res = requests.get("http://localhost:9006/ui/")
    assert res.status_code == 200, "/ui/ route did not return HTTP 200"

    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.find("title")
    assert title is not None, "No <title> tag found in /ui/ response"
    assert "Franklin" in title.text, "Expected 'Franklin' in <title>"
