import sqlite3
import matplotlib.pyplot as plt

DB_PATH = "C:/Users/MAHMUD/Desktop/Finance_Data/company_crm.db"
IMAGE_PATH = "C:/Users/MAHMUD/Desktop/Finance_Data/crm_revenue_chart.png"

def generate_pipeline_chart():
    print("🎨 Querying database for visualization data...")
    
    # Extract raw financial targets
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT company_name, deal_value FROM crm_leads ORDER BY deal_value DESC LIMIT 10")
    rows = cursor.fetchall()
    connection.close()
    
    if not rows:
        print("⚠️ No data found to map out.")
        return
        
    # Unpack company names and deal sizes for the top 10 leads
    companies = [row[0] for row in rows]
    values = [row[1] for row in rows]
    
    print("📈 Rendering financial bar graph asset...")
    
    # Initialize the plot layout dimensions
    plt.figure(figsize=(10, 6))
    
    # Create horizontal bars for long company names
    bars = plt.barh(companies, values, color='#3498db', edgecolor='#2980b9')
    
    # Style formatting rules
    plt.title('Top 10 High-Value Enterprise Accounts in Pipeline', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Deal Value ($ USD)', fontsize=12, fontweight='bold', labelpad=10)
    plt.gca().invert_yaxis()  # Put the highest value deal at the top
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    
    # Add data value numbers cleanly to the end of each bar
    for bar in bars:
        width = bar.get_width()
        plt.text(width + (width * 0.01), bar.get_y() + bar.get_height()/2, 
                 f"${width:,}", 
                 va='center', ha='left', fontsize=10, fontweight='bold', color='#2c3e50')

    plt.tight_layout()
    
    # Save chart asset directly to disk
    plt.savefig(IMAGE_PATH, dpi=300)
    plt.close()
    
    print(f"✅ Success! Live pipeline visual asset saved to:\n   {IMAGE_PATH}")

if __name__ == "__main__":
    generate_pipeline_chart()