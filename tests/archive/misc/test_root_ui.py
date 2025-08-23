import requests

def test_root_serves_ui():
    url = "http://localhost:9006/"
    response = requests.get(url)

    print("Status code (should be 200):", response.status_code)
    print("Content-Type (should include text/html):", response.headers.get("Content-Type", ""))
    print("First 500 characters of the HTML page:")
    print(response.text[:500])

    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert "text/html" in response.headers.get("Content-Type", ""), "Expected HTML content type"
    assert "<html" in response.text.lower(), "Expected HTML content in response"

if __name__ == "__main__":
    test_root_serves_ui()
