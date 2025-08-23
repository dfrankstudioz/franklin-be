import requests

def test_summarize_file():
    # Define the endpoint
    url = "http://localhost:9006/chat"
    
    # Prepare the payload for the API call to summarize the file
    payload = {"prompt": "Summarize file example.txt"}
    
    # Make the API request
    response = requests.post(url, json=payload)
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check if the response contains the expected summary of the file
    expected_summary = "Summary of example.txt (first 3 lines): Hello Franklin!"
    response_json = response.json()
    
    # Assert response contains the expected summary
    assert 'response' in response_json, "No 'response' field in the response"
    assert expected_summary in response_json['response'], f"Expected summary to contain '{expected_summary}', but got {response_json['response']}"

if __name__ == "__main__":
    test_summarize_file()

