import sqlite3
import time
import os

DB_PATH = "C:/Users/MAHMUD/Desktop/Finance_Data/company_crm.db"

while True:
    try:
        # 1. CLEAR THE TERMINAL SCREEN
        # This clears out old text so the new data prints cleanly in the exact same spot!
        # 'nt' means Windows. It runs the standard 'cls' terminal command automatically.
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=" * 60)
        print("🔴 LIVE AUTOMATED ENTERPRISE MANAGEMENT CONTROLLER")
        print("=" * 60)

        # 2. Extract live counts from our SQL file
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM crm_leads")
        total_leads = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(deal_value) FROM crm_leads")
        total_revenue = cursor.fetchone()[0]
        if total_revenue is None: total_revenue = 0

        cursor.execute("SELECT company_name, contact_email, deal_value FROM crm_leads WHERE deal_value >= 8000 ORDER BY deal_value DESC LIMIT 5")
        top_leads = cursor.fetchall()

        connection.close()

        # 3. Print the fresh UI Metrics Matrix
        print(f"📊 PIPELINE NETWORK ENGINE : RUNNING (Surveillance Active)")
        print(f"👥 ACTIVE LEAD MATRIX     : {total_leads} accounts logged")
        print(f"💰 FORECASTED REVENUE TRK  : ${total_revenue:,} USD")
        print("-" * 60)
        print("🔥 TOP 5 HIGH-VALUE CONTRACT TARGETS:")
        print("-" * 60)

        for lead in top_leads:
            company, email, value = lead
            print(f"   ► {company:<22} | {email:<25} | ${value:,}")

        print("=" * 60)
        print("🔄 Screen auto-refreshing in 3 seconds... Press Ctrl+C to halt.")

    except Exception as error:
        print(f"DASHBOARD RUNTIME ERROR: {error}")
        if 'connection' in locals(): connection.close()

    # Pause execution before wiping the screen and querying again
    time.sleep(3)