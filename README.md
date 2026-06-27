# Project Overview

The **AI-Based Heat Stress Awareness Assistant** is an interactive **Streamlit web dashboard** designed to help users understand, assess, and visualize heat stress risks caused by rising temperatures and extreme working conditions.

This project focuses on **awareness and prevention**, not medical diagnosis. Using **transparent rule-based logic** combined with an **AI-style explanation layer**, the tool helps workers, planners, and organizations make informed decisions about heat exposure, hydration, and rest strategies.

**The dashboard is suitable for:**
- Outdoor workers
- Construction and industrial safety teams
- Urban planners
- Climate resilience researchers
- Educational and policy-awareness use cases

---

# Sustainability & SDG Impact

- **SDG 3 (Good Health & Well-being):** Reduces heat-related health risks through awareness and early warnings
- **SDG 13 (Climate Action):** Addresses climate-driven heat stress impacts in real-world environments

---

# Key Features

## Heat Stress Risk Assessment
- Temperature input (°C)
- Humidity percentage
- Work duration (hours)
- Activity intensity (Light / Moderate / Heavy)

## AI-Guided Awareness Layer
- Natural-language explanations of risk levels
- Actionable, non-medical safety guidance
- Transparent and explainable logic

## Interactive Visualizations (Matplotlib + Seaborn)
- Risk score gauge
- Radar chart of contributing factors
- Temperature–Humidity heatmap
- Scenario comparison bar charts
- Historical trend and distribution analysis

## Multiple Analysis Modes
- Single Assessment – Evaluate one scenario
- Comparison Mode – Compare multiple scenarios side-by-side
- Historical Tracking – Track assessments over time
- Batch Analysis – Upload CSV files for bulk risk evaluation

## Export & Reporting
- Download assessment results as CSV
- Export comparison and batch analysis data

---

# Risk Modeling Logic

| Factor        | Condition       | Score                     |
|---------------|----------------|---------------------------|
| Temperature   | ≥ 40°C         | +3                        |
| Temperature   | 35–39°C        | +2                        |
| Humidity      | ≥ 70%          | +2                        |
| Work Duration | ≥ 6 hrs        | +2                        |
| Activity      | Light / Moderate / Heavy | +1 / +2 / +3 |

**Risk Levels:**
- High: Score ≥ 8
- Moderate: Score 5–7
- Low: Score ≤ 4

---

# Technology Stack

- Python 3.9+
- Streamlit – Web application framework
- Matplotlib & Seaborn – Data visualization
- Pandas & NumPy – Data handling and analysis

---

# 📁 Project Structure
```
heat_stress_app/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```
---

# 🔧 Installation & Setup

## Clone the Repository

```bash
git clone https://github.com/your-username/Heat-Stress-Awareness-Assistant.git
cd Heat-Stress-Awareness-Assistant
```
## (Optional) Create Virtual Environment
```
python -m venv venv
```
Activate it:

### Windows
```
venv\Scripts\activate
```
### macOS/Linux
```
source venv/bin/activate
```
## Install Dependencies
```
pip install -r requirements.txt
```

---

# Running the Application
```
streamlit run app.py
```
The app will launch in your browser at:
http://localhost:8501￼

---

#  Usage Instructions
-	1.	Select a dashboard mode from the sidebar
-	2.	Enter environmental and work-related inputs
-	3.	View risk level, AI guidance, and visual insights
-	4.	Compare scenarios or upload CSV data
-	5.	Download results for reporting or analysis


