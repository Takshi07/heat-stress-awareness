📌 Project Overview

The AI-Based Heat Stress Awareness Assistant is an interactive Streamlit web dashboard designed to help users understand, assess, and visualize heat stress risks caused by rising temperatures and extreme working conditions.

This project focuses on awareness and prevention, not medical diagnosis. Using transparent rule-based logic combined with an AI-style explanation layer, the tool helps workers, planners, and organizations make informed decisions about heat exposure, hydration, and rest strategies.

The dashboard is suitable for:
	•	Outdoor workers
	•	Construction and industrial safety teams
	•	Urban planners
	•	Climate resilience researchers
	•	Educational and policy-awareness use cases

⸻

🌍 Sustainability & SDG Impact
	•	SDG 3 (Good Health & Well-being): Reduces heat-related health risks through awareness and early warnings
	•	SDG 13 (Climate Action): Addresses climate-driven heat stress impacts in real-world environments

By promoting safer work practices under extreme heat, the project contributes to climate adaptation and worker well-being.

⸻

🚀 Key Features

🌡️ Heat Stress Risk Assessment
	•	Temperature input (°C)
	•	Humidity percentage
	•	Work duration (hours)
	•	Activity intensity (Light / Moderate / Heavy)

🧠 AI-Guided Awareness Layer
	•	Natural-language explanations of risk levels
	•	Actionable, non-medical safety guidance
	•	Transparent and explainable logic

📊 Interactive Visualizations (Matplotlib + Seaborn)
	•	Risk score gauge
	•	Radar chart of contributing factors
	•	Temperature–Humidity heatmap
	•	Scenario comparison bar charts
	•	Historical trend and distribution analysis

📂 Multiple Analysis Modes
	•	Single Assessment – Evaluate one scenario
	•	Comparison Mode – Compare multiple scenarios side-by-side
	•	Historical Tracking – Track assessments over time
	•	Batch Analysis – Upload CSV files for bulk risk evaluation

📥 Export & Reporting
	•	Download assessment results as CSV
	•	Export comparison and batch analysis data

⸻

🧮 Risk Modeling Logic

The project uses a rule-based heat stress scoring system to ensure transparency and fairness:

Factor	Condition	Score
Temperature	≥ 40°C	+3
Temperature	35–39°C	+2
Humidity	≥ 70%	+2
Work Duration	≥ 6 hrs	+2
Activity	Light / Moderate / Heavy	+1 / +2 / +3

Risk Levels:
	•	High: Score ≥ 8
	•	Moderate: Score 5–7
	•	Low: Score ≤ 4

⸻

⚖️ Responsible AI Principles

This project strictly follows Responsible AI guidelines:
	•	Transparency: All risk calculations are rule-based and explainable
	•	Fairness: No personal or demographic data is collected
	•	Ethics: The system provides awareness only, not diagnosis
	•	Privacy: No user data is stored externally
	•	Safety: Clear disclaimers and non-alarmist guidance

⸻

🛠️ Technology Stack
	•	Python 3.9+
	•	Streamlit – Web application framework
	•	Matplotlib & Seaborn – Data visualization
	•	Pandas & NumPy – Data handling and analysis

⸻

📁 Project Structure

heat_stress_app/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file


⸻

🔧 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/Heat-Stress-Awareness-Assistant.git
cd Heat-Stress-Awareness-Assistant

2️⃣ (Optional) Create Virtual Environment

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt


⸻

▶️ Running the Application

streamlit run app.py

The app will launch in your browser at:

http://localhost:8501


⸻

📊 Usage Instructions
	1.	Select a dashboard mode from the sidebar
	2.	Enter environmental and work-related inputs
	3.	View risk level, AI guidance, and visual insights
	4.	Compare scenarios or upload CSV data
	5.	Download results for reporting or analysis

⸻

📈 Expected Impact
	•	Increased awareness of heat stress risks
	•	Safer work practices during extreme heat
	•	Support for climate adaptation planning
	•	Educational tool for sustainability and public health

⸻

🤝 Contributing

Contributions are welcome:
	1.	Fork the repository
	2.	Create a feature branch (git checkout -b feature/YourFeature)
	3.	Commit your changes
	4.	Push to the branch
	5.	Open a Pull Request

⸻

📜 License

This project is licensed under the MIT License.

⸻

📬 Contact

Takshitha A
GitHub: @Takshi07

⸻

⭐ If you find this project useful, consider giving it a star!