import json
import os
from unittest.mock import patch, MagicMock
from ln_church_agent.cli import inspect_url

# This script safely validates the public classification boundaries using local mock data.
# It actively loads and parses the schema files from docs/review/sample-payloads/.
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

    # Test 1: Standard L402 (Valid) - Dynamically loading external-observe.valid.json
    valid_data = load_mock_payload("external-observe.valid.json")
    rail = valid_data["protocol"]["rail"]
    run_mock_inspection(
        target_url=valid_data["targetUrl"],
        simulate_headers={"WWW-Authenticate": f'{rail} macaroon="mock_mac", invoice="mock_inv"'},
        simulate_body={}
    )

    # Test 2: Unmapped / Invalid Shape - Dynamically loading external-observe.unmapped.json
    unmapped_data = load_mock_payload("external-observe.unmapped.json")
    run_mock_inspection(
        target_url=unmapped_data["targetUrl"],
        simulate_headers={"WWW-Authenticate": 'UnknownScheme param="123"'},
        simulate_body={}
    )

    # Test 3: Agent Commerce Surface (AP2) - Dynamically loading external-observe.observe-only.json
    observe_data = load_mock_payload("external-observe.observe-only.json")
    run_mock_inspection(
        target_url=observe_data["targetUrl"],
        simulate_headers={"Content-Type": "application/json"},
        # Passing the protocol and intent from the contract payload to simulate the server response
        simulate_body={
            "protocol": observe_data["protocol"]["payment_intent"], 
            "intent": observe_data["protocol"]["payment_intent"]
        }
    )

if __name__ == "__main__":
    main()