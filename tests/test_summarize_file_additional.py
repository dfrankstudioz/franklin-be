
import requests

def test_summarize_file():
    # Define the endpoint
    url = "http://localhost:9006/chat"
    
    # Test 1: Valid file summarization
    payload = {"prompt": "Summarize file example.txt"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    expected_summary = "Summary of example.txt (first 3 lines): Hello Franklin!"
    response_json = response.json()
    assert 'response' in response_json, "No 'response' field in the response"
    assert expected_summary in response_json['response'], f"Expected summary to contain '{expected_summary}', but got {response_json['response']}"

    # Test 2: Nonexistent file - should return file not found error
    payload = {"prompt": "Summarize file non_existent_file.txt"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()
    assert 'response' in response_json, "No 'response' field in the response"
    assert "File not found" in response_json['response'], f"Expected 'File not found', but got {response_json['response']}"

    # Test 3: Raw text summarization
    payload = {"prompt": "Summarize: Hello Franklin!"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    expected_raw_text_summary = "Summary of provided text (first 3 lines): Hello Franklin!"
    response_json = response.json()
    assert 'response' in response_json, "No 'response' field in the response"
    assert expected_raw_text_summary in response_json['response'], f"Expected summary to contain '{expected_raw_text_summary}', but got {response_json['response']}"

    # Test 4: Empty file name should be treated as invalid input
    payload = {"prompt": "Summarize file "}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()
    assert 'response' in response_json, "No 'response' field in the response"
    assert "File not found" in response_json['response'], f"Expected 'File not found', but got {response_json['response']}"

    # Test 5: Empty prompt should return an error or warning
    payload = {"prompt": ""}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()
    assert 'response' in response_json, "No 'response' field in the response"
    assert "Error" in response_json['response'], f"Expected 'Error', but got {response_json['response']}"

if __name__ == "__main__":
    test_summarize_file()
