import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from io import BytesIO
from datetime import datetime, timedelta

# ============================================================================
# RESPONSIBLE AI NOTICE
# ============================================================================
# This application provides heat stress awareness and educational guidance only.
# - NO MEDICAL DIAGNOSIS is provided
# - Rule-based logic ensures transparency and explainability
# - AI layer improves accessibility and understanding of risk factors
# - Users should consult medical professionals for health concerns
# ============================================================================

st.set_page_config(page_title="Heat Stress Awareness Dashboard", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #FF6B6B, #FFA500, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# INITIALIZE SESSION STATE
# ============================================================================
if 'history' not in st.session_state:
    st.session_state.history = []
if 'comparison_mode' not in st.session_state:
    st.session_state.comparison_mode = False

# ============================================================================
# DYNAMIC TITLE BASED ON MODE
# ============================================================================
mode_titles = {
    "Single Assessment": "Single Risk Assessment",
    "Comparison Mode": "Scenario Comparison",
    "Historical Tracking": "Historical Data Analysis",
    "Batch Analysis": "Batch Processing"
}

# Placeholder for title (will be updated after mode selection)
title_placeholder = st.empty()

# ============================================================================
# SIDEBAR - MODE SELECTOR
# ============================================================================
st.sidebar.title("Dashboard Controls")
dashboard_mode = st.sidebar.radio(
    "Select Mode",
    ["Single Assessment", "Comparison Mode", "Historical Tracking", "Batch Analysis"],
    help="Choose how you want to analyze heat stress data"
)

# Update title based on selected mode
title_placeholder.markdown(f'<h1 class="main-header">{mode_titles[dashboard_mode]}</h1>', unsafe_allow_html=True)

st.sidebar.markdown("---")

# ============================================================================
# RULE-BASED HEAT STRESS RISK CALCULATOR
# ============================================================================
def calculate_risk(temp, humidity, hours, activity):
    risk_score = 0
    
    if temp >= 40:
        risk_score += 3
    elif temp >= 35:
        risk_score += 2
    
    if humidity >= 70:
        risk_score += 2
    
    if hours >= 6:
        risk_score += 2
    
    activity_scores = {"Light": 1, "Moderate": 2, "Heavy": 3}
    risk_score += activity_scores[activity]
    
    if risk_score >= 8:
        risk_level = "High"
    elif risk_score >= 5:
        risk_level = "Moderate"
    else:
        risk_level = "Low"
    
    return risk_level, risk_score

def get_risk_color(risk_level):
    colors = {"High": "#FF4444", "Moderate": "#FFA500", "Low": "#44FF44"}
    return colors.get(risk_level, "#888888")

# ============================================================================
# AI EXPLANATION
# ============================================================================
def ai_explain_risk(temp, humidity, hours, activity, risk):
    explanations = {
        "High": f"🚨 HIGH RISK DETECTED\n\nConditions: {temp}°C, {humidity}% humidity, {hours}h duration\n\nImmediate action required\nImplement all safety protocols\nIncrease hydration frequency\nMandatory rest breaks\nMonitor for heat stress symptoms",
        "Moderate": f"⚠️ MODERATE RISK\n\nConditions: {temp}°C, {humidity}% humidity, {hours}h duration\n\nCaution advised\nRegular hydration breaks\nMonitor comfort levels\nAdjust work pace as needed",
        "Low": f"✅ LOW RISK\n\nConditions: {temp}°C, {humidity}% humidity, {hours}h duration\n\nNormal safety protocols apply\nMaintain regular hydration\nStandard work practices acceptable"
    }
    return explanations.get(risk, "No assessment available")

# ============================================================================
# MODE 1: SINGLE ASSESSMENT
# ============================================================================
if dashboard_mode == "Single Assessment":
    st.sidebar.header("Environmental Inputs")
    
    col_input1, col_input2 = st.sidebar.columns(2)
    with col_input1:
        temperature = st.number_input("Temperature (°C)", min_value=25, max_value=50, value=35, step=1)
        work_duration = st.number_input("Duration (hrs)", min_value=1, max_value=10, value=4, step=1)
    
    with col_input2:
        humidity = st.number_input("Humidity (%)", min_value=30, max_value=90, value=60, step=5)
        activity_level = st.selectbox("Activity", ["Light", "Moderate", "Heavy"])
    
    if st.sidebar.button("Assess Risk", type="primary", use_container_width=True):
        risk_level, risk_score = calculate_risk(temperature, humidity, work_duration, activity_level)
        
        # Add to history
        st.session_state.history.append({
            'timestamp': datetime.now(),
            'temp': temperature,
            'humidity': humidity,
            'duration': work_duration,
            'activity': activity_level,
            'risk_level': risk_level,
            'risk_score': risk_score
        })
        
        # Display Results in Cards
        st.subheader("Assessment Results")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Temperature", f"{temperature}°C", delta=f"{temperature-35}°C from avg")
        with col2:
            st.metric("Humidity", f"{humidity}%", delta=f"{humidity-60}% from avg")
        with col3:
            st.metric("Risk Score", risk_score, delta=f"Level: {risk_level}")
        with col4:
            st.markdown(f"<div style='background-color: {get_risk_color(risk_level)}; padding: 20px; border-radius: 10px; text-align: center; color: white; font-size: 20px; font-weight: bold;'>{risk_level} RISK</div>", unsafe_allow_html=True)
        
        # Tabs for different views
        tab1, tab2, tab3, tab4 = st.tabs(["Visual Analysis", "AI Guidance", "Export Data", "Risk Breakdown"])
        
        with tab1:
            col_viz1, col_viz2 = st.columns(2)
            
            with col_viz1:
                # Gauge Chart
                fig_gauge, ax_gauge = plt.subplots(figsize=(6, 4), subplot_kw=dict(projection='polar'))
                theta = np.linspace(0, np.pi, 100)
                r = np.ones(100)
                
                colors_gradient = ['green']*33 + ['orange']*33 + ['red']*34
                for i, (t, color) in enumerate(zip(theta, colors_gradient)):
                    ax_gauge.plot([t, t], [0, 1], color=color, linewidth=8)
                
                score_angle = (risk_score / 12) * np.pi
                ax_gauge.arrow(score_angle, 0, 0, 0.8, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
                
                ax_gauge.set_ylim(0, 1)
                ax_gauge.set_theta_zero_location('W')
                ax_gauge.set_theta_direction(1)
                ax_gauge.set_xticks([])
                ax_gauge.set_yticks([])
                ax_gauge.set_title(f"Risk Gauge\nScore: {risk_score}/12", fontsize=14, fontweight='bold', pad=20)
                st.pyplot(fig_gauge)
            
            with col_viz2:
                # Radar Chart
                categories = ['Temperature\nImpact', 'Humidity\nImpact', 'Duration\nImpact', 'Activity\nImpact']
                temp_impact = 3 if temperature >= 40 else 2 if temperature >= 35 else 1
                humidity_impact = 2 if humidity >= 70 else 1
                duration_impact = 2 if work_duration >= 6 else 1
                activity_impact = {"Light": 1, "Moderate": 2, "Heavy": 3}[activity_level]
                
                values = [temp_impact, humidity_impact, duration_impact, activity_impact]
                values += values[:1]
                
                angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
                angles += angles[:1]
                
                fig_radar, ax_radar = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
                ax_radar.plot(angles, values, 'o-', linewidth=2, color='#FF6B6B')
                ax_radar.fill(angles, values, alpha=0.25, color='#FF6B6B')
                ax_radar.set_xticks(angles[:-1])
                ax_radar.set_xticklabels(categories, size=10)
                ax_radar.set_ylim(0, 3)
                ax_radar.set_title("Risk Factor Breakdown", fontsize=14, fontweight='bold', pad=20)
                ax_radar.grid(True)
                st.pyplot(fig_radar)
            
            # Heatmap
            st.subheader("Temperature-Humidity Risk Matrix")
            temp_range = np.arange(25, 51, 1)
            humidity_range = np.arange(30, 91, 1)
            heatmap_data = np.zeros((len(temp_range), len(humidity_range)))
            
            for i, t in enumerate(temp_range):
                for j, h in enumerate(humidity_range):
                    _, score = calculate_risk(t, h, work_duration, activity_level)
                    heatmap_data[i, j] = score
            
            fig_heat, ax_heat = plt.subplots(figsize=(12, 8))
            sns.heatmap(heatmap_data, cmap='RdYlGn_r', cbar_kws={'label': 'Risk Score'}, ax=ax_heat)
            ax_heat.set_xlabel("Humidity (%)", fontsize=12, fontweight='bold')
            ax_heat.set_ylabel("Temperature (°C)", fontsize=12, fontweight='bold')
            ax_heat.set_title("Comprehensive Risk Matrix", fontsize=14, fontweight='bold')
            
            current_temp_idx = temperature - 25
            current_humidity_idx = humidity - 30
            ax_heat.plot(current_humidity_idx, current_temp_idx, 'b*', markersize=20, markeredgewidth=2, markeredgecolor='blue')
            
            ax_heat.set_xticks(np.arange(0, 61, 10))
            ax_heat.set_xticklabels(np.arange(30, 91, 10))
            ax_heat.set_yticks(np.arange(0, 26, 5))
            ax_heat.set_yticklabels(np.arange(25, 51, 5))
            
            st.pyplot(fig_heat)
        
        with tab2:
            st.info(ai_explain_risk(temperature, humidity, work_duration, activity_level, risk_level))
            
            st.subheader("Recommended Actions")
            if risk_level == "High":
                st.error("Critical Actions Required")
                actions = [
                    "Stop work immediately if symptoms appear",
                    "Drink 200ml water every 15 minutes",
                    "Take 15-minute breaks in shade every hour",
                    "Implement buddy system for monitoring",
                    "Have emergency cooling measures ready"
                ]
            elif risk_level == "Moderate":
                st.warning("Precautionary Measures")
                actions = [
                    "Increase water intake frequency",
                    "Take breaks every 2 hours",
                    "Monitor for discomfort",
                    "Adjust work pace as needed",
                    "Wear appropriate clothing"
                ]
            else:
                st.success("Standard Protocols")
                actions = [
                    "Maintain regular hydration",
                    "Follow normal break schedule",
                    "Stay aware of conditions",
                    "Keep communication open"
                ]
            
            for action in actions:
                st.markdown(f"- {action}")
        
        with tab3:
            st.subheader("Export Assessment Data")
            
            export_data = pd.DataFrame([{
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'Temperature_C': temperature,
                'Humidity_Percent': humidity,
                'Duration_Hours': work_duration,
                'Activity_Level': activity_level,
                'Risk_Score': risk_score,
                'Risk_Level': risk_level
            }])
            
            csv = export_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"heat_stress_assessment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
            
            st.dataframe(export_data, use_container_width=True)
        
        with tab4:
            st.subheader("Detailed Risk Scoring Breakdown")
            
            breakdown_data = {
                'Factor': ['Temperature', 'Humidity', 'Work Duration', 'Activity Level', 'TOTAL'],
                'Contribution': [
                    3 if temperature >= 40 else 2 if temperature >= 35 else 0,
                    2 if humidity >= 70 else 0,
                    2 if work_duration >= 6 else 0,
                    {"Light": 1, "Moderate": 2, "Heavy": 3}[activity_level],
                    risk_score
                ],
                'Threshold': ['≥40°C (+3) or 35-39°C (+2)', '≥70% (+2)', '≥6 hrs (+2)', 'Light(+1), Mod(+2), Heavy(+3)', '≥8 High, 5-7 Mod, ≤4 Low']
            }
            
            st.dataframe(pd.DataFrame(breakdown_data), use_container_width=True)

# ============================================================================
# MODE 2: COMPARISON MODE
# ============================================================================
elif dashboard_mode == "Comparison Mode":
    st.subheader("Compare Multiple Scenarios")
    
    num_scenarios = st.sidebar.slider("Number of Scenarios", 2, 4, 2)
    
    scenarios = []
    cols = st.columns(num_scenarios)
    
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"### Scenario {i+1}")
            temp = st.slider(f"Temp {i+1} (°C)", 25, 50, 30+i*5, key=f"temp_{i}")
            humid = st.slider(f"Humidity {i+1} (%)", 30, 90, 50+i*10, key=f"humid_{i}")
            duration = st.slider(f"Duration {i+1} (hrs)", 1, 10, 4, key=f"dur_{i}")
            activity = st.selectbox(f"Activity {i+1}", ["Light", "Moderate", "Heavy"], key=f"act_{i}")
            
            risk_level, risk_score = calculate_risk(temp, humid, duration, activity)
            scenarios.append({
                'name': f"Scenario {i+1}",
                'temp': temp,
                'humidity': humid,
                'duration': duration,
                'activity': activity,
                'risk_level': risk_level,
                'risk_score': risk_score
            })
            
            st.markdown(f"<div style='background-color: {get_risk_color(risk_level)}; padding: 15px; border-radius: 8px; color: white; text-align: center; margin-top: 10px;'><strong>{risk_level}</strong><br>Score: {risk_score}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Comparison Analysis")
    
    tab1, tab2 = st.tabs(["Bar Comparison", "Detailed Table"])
    
    with tab1:
        fig_comp, ax_comp = plt.subplots(figsize=(12, 6))
        names = [s['name'] for s in scenarios]
        scores = [s['risk_score'] for s in scenarios]
        colors_bar = [get_risk_color(s['risk_level']) for s in scenarios]
        
        bars = ax_comp.bar(names, scores, color=colors_bar, edgecolor='black', linewidth=2)
        ax_comp.set_ylabel('Risk Score', fontsize=12, fontweight='bold')
        ax_comp.set_title('Scenario Risk Comparison', fontsize=14, fontweight='bold')
        ax_comp.set_ylim(0, 12)
        ax_comp.grid(axis='y', alpha=0.3)
        
        for bar, score in zip(bars, scores):
            height = bar.get_height()
            ax_comp.text(bar.get_x() + bar.get_width()/2., height,
                        f'{score}',
                        ha='center', va='bottom', fontweight='bold', fontsize=12)
        
        st.pyplot(fig_comp)
    
    with tab2:
        comparison_df = pd.DataFrame(scenarios)
        st.dataframe(comparison_df, use_container_width=True)
        
        csv_comp = comparison_df.to_csv(index=False)
        st.download_button(
            "Download Comparison",
            csv_comp,
            f"scenario_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            "text/csv",
            use_container_width=True
        )

# ============================================================================
# MODE 3: HISTORICAL TRACKING
# ============================================================================
elif dashboard_mode == "Historical Tracking":
    st.subheader("Historical Risk Tracking")
    
    if len(st.session_state.history) == 0:
        st.info("No historical data yet. Perform assessments in Single Assessment mode to build history.")
    else:
        history_df = pd.DataFrame(st.session_state.history)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Assessments", len(history_df))
        with col2:
            high_risk_count = len(history_df[history_df['risk_level'] == 'High'])
            st.metric("High Risk Events", high_risk_count)
        with col3:
            avg_score = history_df['risk_score'].mean()
            st.metric("Average Risk Score", f"{avg_score:.1f}")
        
        st.markdown("---")
        
        fig_trend, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # Trend line
        ax1.plot(range(len(history_df)), history_df['risk_score'], marker='o', linewidth=2, markersize=8)
        ax1.fill_between(range(len(history_df)), history_df['risk_score'], alpha=0.3)
        ax1.set_xlabel('Assessment Number', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Risk Score', fontsize=12, fontweight='bold')
        ax1.set_title('Risk Score Trend', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Distribution
        risk_counts = history_df['risk_level'].value_counts()
        colors_pie = [get_risk_color(level) for level in risk_counts.index]
        ax2.pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%',
                colors=colors_pie, startangle=90)
        ax2.set_title('Risk Level Distribution', fontsize=14, fontweight='bold')
        
        st.pyplot(fig_trend)
        
        st.subheader("Historical Data Table")
        display_df = history_df.copy()
        display_df['timestamp'] = display_df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
        st.dataframe(display_df, use_container_width=True)
        
        if st.button("Clear History", type="secondary"):
            st.session_state.history = []
            st.rerun()

# ============================================================================
# MODE 4: BATCH ANALYSIS
# ============================================================================
elif dashboard_mode == "Batch Analysis":
    st.subheader("Batch Risk Analysis")
    
    st.info("Upload a CSV file with columns: temperature, humidity, duration, activity")
    
    uploaded_file = st.file_uploader("Choose CSV file", type=['csv'])
    
    if uploaded_file is not None:
        batch_df = pd.read_csv(uploaded_file)
        
        if all(col in batch_df.columns for col in ['temperature', 'humidity', 'duration', 'activity']):
            results = []
            for _, row in batch_df.iterrows():
                risk_level, risk_score = calculate_risk(
                    row['temperature'],
                    row['humidity'],
                    row['duration'],
                    row['activity']
                )
                results.append({'risk_level': risk_level, 'risk_score': risk_score})
            
            results_df = pd.DataFrame(results)
            batch_df['risk_level'] = results_df['risk_level']
            batch_df['risk_score'] = results_df['risk_score']
            
            st.success(f"Processed {len(batch_df)} records")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("High Risk", len(batch_df[batch_df['risk_level'] == 'High']))
            with col2:
                st.metric("Moderate Risk", len(batch_df[batch_df['risk_level'] == 'Moderate']))
            with col3:
                st.metric("Low Risk", len(batch_df[batch_df['risk_level'] == 'Low']))
            
            st.dataframe(batch_df, use_container_width=True)
            
            csv_output = batch_df.to_csv(index=False)
            st.download_button(
                "Download Results",
                csv_output,
                f"batch_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                "text/csv",
                use_container_width=True
            )
        else:
            st.error("CSV must contain: temperature, humidity, duration, activity columns")
    else:
        st.markdown("### Sample CSV Format:")
        sample_df = pd.DataFrame({
            'temperature': [35, 40, 28],
            'humidity': [60, 75, 50],
            'duration': [4, 6, 3],
            'activity': ['Moderate', 'Heavy', 'Light']
        })
        st.dataframe(sample_df)