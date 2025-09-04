from fastapi.testclient import TestClient
from app import app  # Assuming your FastAPI app is in main.py

# Create a TestClient instance for your FastAPI application
client = TestClient(app)

# Create a TestClient instance for your FastAPI application
client = TestClient(app)

def test_create_valid_item():
    """
    Tests the POST /items/ endpoint with a valid JSON payload.
    This test should pass.
    """
    # Define a valid request body based on your Features class
    valid_data = {
        "clump_thickness": 5.0,
        "uniformity_of_cell_size": 10.0,
        "uniformity_of_cell_shape": 8.5,
        "marginal_adhesion": 7.0,
        "single_epithelial_cell_size": 4.0,
        "bare_nuclei": 9.5,
        "bland_chromatin": 3.0,
        "normal_nucleoli": 6.0,
        "mitoses": 1.0
    }
    
    # Send a POST request to the endpoint
    response = client.post("/items/", json=valid_data)
    
    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201
    
    # Assert that the response body contains the expected message
    response_json = response.json()
    assert response_json["message"] == "Item created successfully"
    assert "item_id" in response_json
    assert response_json["features"]["clump_thickness"] == 5.0

def test_create_item_with_invalid_data():
    """
    Tests the POST /items/ endpoint with an invalid value for clump_thickness.
    This test should now pass, as it correctly asserts the failure.
    """
    # Define an invalid request body (value outside the 1-10 range)
    invalid_data = {
        "clump_thickness": 11.0,  # This value is outside the valid range
        "uniformity_of_cell_size": 10.0,
        "uniformity_of_cell_shape": 8.5,
        "marginal_adhesion": 7.0,
        "single_epithelial_cell_size": 4.0,
        "bare_nuclei": 9.5,
        "bland_chromatin": 3.0,
        "normal_nucleoli": 6.0,
        "mitoses": 1.0
    }

    # Send a POST request with the invalid data
    response = client.post("/items/", json=invalid_data)
    
    # Assert that the response status code is 422 (Unprocessable Entity)
    # The app correctly detected the invalid data, so this test should pass.
    assert response.status_code == 422
    
    # Assert that the error message is present and correct
    response_json = response.json()
    assert "detail" in response_json
    assert response_json["detail"][0]["msg"] == "Input should be less than or equal to 10"

def test_create_item_with_missing_data():
    """
    Tests the POST /items/ endpoint with a missing required field.
    This test should pass.
    """
    # Define a request body with a missing required field
    missing_data = {
        "uniformity_of_cell_size": 10.0,
        "uniformity_of_cell_shape": 8.5,
        "marginal_adhesion": 7.0,
        "single_epithelial_cell_size": 4.0,
        "bare_nuclei": 9.5,
        "bland_chromatin": 3.0,
        "normal_nucleoli": 6.0,
        "mitoses": 1.0
    }

    # Send a POST request with the missing data
    response = client.post("/items/", json=missing_data)
    
    # Assert that the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422
    
    # Assert that the error message indicates a missing field
    response_json = response.json()
    assert response_json["detail"][0]["msg"] == "Field required"
