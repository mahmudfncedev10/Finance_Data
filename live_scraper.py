import requests
from bs4 import BeautifulSoup
import time
import random

# Point this directly to your live FastAPI Webhook Gateway
API_URL = "http://127.0.0.1:8000/webhook/lead"

def scrape_and_forward_leads():
    print("🕸️ [SCRAPER START] Activating live data extraction engine...")
    
    # Simulating targeting a business directory or marketplace
    # In production, you would use requests.get("TARGET_URL") here
    mock_web_source = """
    <div class="business-card">
        <h3 class="company-name">Apex Global Logistics</h3>
        <p class="email">contact@apexlogistics.com</p>
        <span class="deal-size">$12,500</span>
    </div>
    <div class="business-card">
        <h3 class="company-name">Quantum Tech Labs</h3>
        <p class="email">info@quantumtech.io</p>
        <span class="deal-size">$4,200</span>
    </div>
    <div class="business-card">
        <h3 class="company-name">Vanguard Real Estate</h3>
        <p class="email">deals@vanguardre.com</p>
        <span class="deal-size">$19,000</span>
    </div>
    """
    
    # Initialize BeautifulSoup to parse the HTML structure
    soup = BeautifulSoup(mock_web_source, 'html.parser')
    cards = soup.find_all('div', class_='business-card')
    
    for card in cards:
        try:
            # Extract raw text nodes from the HTML elements
            name = card.find('h3', class_='company-name').text.strip()
            email = card.find('p', class_='email').text.strip()
            
            # Clean up the financial string into a strict integer for your Pydantic Schema
            raw_val = card.find('span', class_='deal-size').text
            clean_value = int(raw_val.replace('$', '').replace(',', '').strip())
            
            # Package the scraped web elements into your strict Pydantic JSON payload structure
            payload = {
                "company_name": name,
                "contact_email": email,
                "deal_value": clean_value
            }
            
            print(f"\n🎯 [FOUND] Extracted live lead: {name} | Value: ${clean_value:,}")
            print(f"🚀 Forwarding to AI Gateway API...")
            
            # Fire the HTTP POST request straight across your local network to your FastAPI server
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                print(f"✅ [SUCCESS] Gateway processed lead. AI Reply: {response.json()}")
            else:
                print(f"❌ [API ERROR] Gateway rejected payload with code: {response.status_code}")
                
            # Anti-bot human simulation delay: sleep randomly between 2 to 4 seconds
            time.sleep(random.uniform(2.0, 4.0))
            
        except Exception as e:
            print(f"⚠️ [PARSING ERROR] Failed to extract card data: {e}")

if __name__ == "__main__":
    scrape_and_forward_leads()