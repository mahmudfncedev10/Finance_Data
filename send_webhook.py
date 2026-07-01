import requests

TARGET_URL = "http://127.0.0.1:8000/webhook/lead"

# 🟢 VALID HIGH-VALUE LEAD TEMPLATE
payload = {
    "company_name": "Hyperion Logistics",
    "contact_email": "deals@hyperion.io",  # Switch 'operations' to 'deals' or a corporate domain string
    "deal_value": 14200
}

print("🚀 Launching data packet across local network...")
try:
    response = requests.post(TARGET_URL, json=payload)
    print(f"📡 SERVER RESPONSE CODE: {response.status_code}")
    print(f"📩 SERVER MESSAGE      : {response.json()}")
except requests.exceptions.ConnectionError as e:
    print(f"❌ Connection Refused! Is lead_API.py running in the other terminal?\nDetails: {e}")