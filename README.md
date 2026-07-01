# AI-Powered CRM Lead Ingestion & Scoring Pipeline

An asynchronous B2B financial lead generation infrastructure. This system automates the process of discovering corporate entities, running data-driven financial predictions, and routing high-priority client acquisitions directly to internal CRM systems and communication channels.

## ⚙️ Core Architecture & System Flow

* **Automated Data Scraper (`live_scraper.py`):** Extracts real-time organization metrics, deal values, and corporate contact structures.
* **REST API Gateway (`lead_API.py`):** An asynchronous FastAPI backend handling high-throughput lead payloads and background task execution loops.
* **Neural Scoring Engine:** Uses a localized machine learning schema to analyze balance sheet profiles and output a precise `closing_probability` score.
* **Data Log Registry (`check_database.py`):** Automatically structures, maps, and logs active pipelines into an integrated SQLite database matrix.
* **Broadcast Module:** Fires webhooks to push instant notifications for high-priority targets directly to business channels.

## 📊 Sample Pipeline Output

```text
ID   | Timestamp           | Company Name              | Value      | AI Score | Status
-----------------------------------------------------------------------------------------------
1    | 2026-06-29 12:25:23 | Apex Global Logistics     | $12,500    | 85.00%   | 🔥 HIGH PRIORITY
2    | 2026-06-29 12:25:25 | Quantum Tech Labs         | $4,200     | 0.01%    | ⏳ STANDARD PIPELINE
3    | 2026-06-29 12:25:28 | Vanguard Real Estate      | $19,000    | 85.00%   | 🔥 HIGH PRIORITY