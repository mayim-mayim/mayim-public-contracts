import json
import os
from unittest.mock import patch, MagicMock
from ln_church_agent.cli import inspect_url

# This script safely validates the public classification boundaries using local mock data.
# It does NOT execute payments and does NOT connect to private Hondō infrastructure.

def load_mock_payload(filename: str) -> dict:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, '..', 'docs', 'review', 'sample-payloads', filename)
    with open(path, 'r') as f:
        return json.load(f)

@patch("ln_church_agent.cli.requests.request")
def run_mock_inspection(mock_req, target_url: str, simulate_headers: dict, simulate_body: dict):
    # Setup safe mock response
    mock_res = MagicMock()
    mock_res.status_code = 402
    mock_res.headers = simulate_headers
    mock_res.content = json.dumps(simulate_body).encode() if simulate_body else b""
    if simulate_body:
        mock_res.json.return_value = simulate_body
    else:
        mock_res.json.side_effect = ValueError()
    mock_res.url = target_url
    mock_req.return_value = mock_res

    # Run inspection
    print(f"\n🔍 Inspecting Mock Target: {target_url}")
    result = inspect_url(target_url)
    
    print(f"  Recommended Action : {result.recommended_action}")
    print(f"  Rails Detected     : {result.rails_detected}")
    print(f"  Surfaces Detected  : {result.surfaces_detected}")
    print(f"  Handoff Mode       : {getattr(result, 'handoff_mode', 'None')}")

def main():
    print("==================================================")
    print(" 🧪 Public Contract Classification Mock Harness")
    print("==================================================")

    # Test 1: Standard L402 (Valid)
    run_mock_inspection(
        target_url="https://api.example.test/valid-l402",
        simulate_headers={"WWW-Authenticate": 'L402 macaroon="mock_mac", invoice="mock_inv"'},
        simulate_body={}
    )

    # Test 2: Unmapped / Invalid Shape
    run_mock_inspection(
        target_url="https://api.example.test/unmapped",
        simulate_headers={"WWW-Authenticate": 'UnknownScheme param="123"'},
        simulate_body={}
    )

    # Test 3: Agent Commerce Surface (AP2) -> Expected: observe_only
    run_mock_inspection(
        target_url="https://api.example.test/ap2-commerce",
        simulate_headers={"Content-Type": "application/json"},
        simulate_body={"protocol": "ap2", "intent": "payment_mandate"}
    )

if __name__ == "__main__":
    main()