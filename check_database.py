import sqlite3
import os

# Absolute exact path to ensure no cross-directory confusion
DB_PATH = "C:/Users/MAHMUD/Desktop/Finance_Data/company_crm.db"

def inspect_database():
    print("💾 Querying records from company_crm.db...\n")
    
    if not os.path.exists(DB_PATH):
        print(f"❌ ERROR: The database file does not exist at: {DB_PATH}")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Pull data fields explicitly
        cursor.execute("SELECT id, timestamp, company_name, deal_value, closing_probability, status_label FROM crm_leads")
        rows = cursor.fetchall()
        
        if not rows:
            print("⚠️ The database file exists, but the 'crm_leads' table is currently empty.")
            conn.close()
            return
            
        print(f"{'ID':<4} | {'Timestamp':<19} | {'Company Name':<25} | {'Value':<10} | {'AI Score':<8} | {'Status'}")
        print("-" * 95)
        
        for row in rows:
            print(f"{row[0]:<4} | {row[1]:<19} | {row[2]:<25} | ${row[3]:<9,} | {row[4]:.2f}% | {row[5]}")
            
        conn.close()
        print(f"\n📊 Total records tracked: {len(rows)}")
        
    except sqlite3.OperationalError as e:
        print(f"❌ SQLite Error: {e} (The table might not be generated yet)")
    except Exception as e:
        print(f"❌ Unknown Error reading database: {e}")

if __name__ == "__main__":
    inspect_database()