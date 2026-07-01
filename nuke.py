import sqlite3
conn = sqlite3.connect("C:/Users/MAHMUD/Desktop/Finance_Data/company_crm.db")
conn.cursor().execute("DROP TABLE IF EXISTS crm_leads")
conn.commit()
conn.close()
print("💥 [SUCCESS] Old table wiped clean! Your pipeline is ready for a fresh start.")