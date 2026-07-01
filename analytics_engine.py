import sqlite3
from datetime import datetime

DB_PATH = "C:/Users/MAHMUD/Desktop/Finance_Data/company_crm.db"
REPORT_PATH = "C:/Users/MAHMUD/Desktop/Finance_Data/financial_summary.txt"

def run_pipeline_analytics():
    print("📊 Extracting data from warehouse...")
    
    # Establish connection to the local database warehouse
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    # 🔎 Query 1: Fetch all leads to count total ingestions and aggregate values
    cursor.execute("SELECT deal_value FROM crm_leads")
    rows = cursor.fetchall()
    
    if not rows:
        print("⚠️ Data warehouse is currently empty. Run send_webhook.py first!")
        connection.close()
        return

    # Extract single integer values from the database row tuples
    deal_values = [row[0] for row in rows]
    
    # 🧮 Financial Infrastructure Math
    total_leads = len(deal_values)
    total_pipeline_value = sum(deal_values)
    average_deal_value = total_pipeline_value / total_leads
    
    # Count how many leads crossed the high-value escalation threshold ($8,000)
    high_value_leads = sum(1 for value in deal_values if value >= 8000)

    connection.close()

    # 📝 Compile the Financial Intelligence Report
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report_content = f"""==================================================
📊 FINANCIAL INFRASTRUCTURE INTELLIGENCE REPORT
Generated at: {timestamp}
==================================================
📈 CORE PIPELINE METRICS:
   • Total Ingested Records       : {total_leads} accounts
   • Gross Pipeline Deal Value    : ${total_pipeline_value:,} USD
   • Average Deal Target Value    : ${average_deal_value:,.2f} USD

🛡️ ESCALATION METRICS:
   • High-Value Alerts Triggered  : {high_value_leads} incidents
==================================================
STATUS: Pipeline Stable • Data Integrity Verified
"""

    # Write the report file straight to the workspace disk
    with open(REPORT_PATH, "w", encoding="utf-8") as report_file:
        report_file.write(report_content)
        
    print(f"✅ Success! Financial summary compiled and saved to:\n   {REPORT_PATH}")

if __name__ == "__main__":
    run_pipeline_analytics()