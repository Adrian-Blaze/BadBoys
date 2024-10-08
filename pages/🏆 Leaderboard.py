import pandas as pd
import streamlit as st


# Sample DataFrame with dummy data
data = {
    'Student': ['Antonia', 'Blaze', 'Kachi', 'Adrian', 'Kintolo'],
    'Study_Hours': [15, 20, 10, 30, 11],  # Dummy study hours
    'Mock_Exam_Score': [80, 90, 70, 85, 75]  # Dummy exam scores
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate Weighted Score
weight_study_hours = 0.7
weight_mock_exam = 0.3

# Add a column for Weighted Score
df['Weighted_Score'] = (weight_study_hours * df['Study_Hours']) + (weight_mock_exam * df['Mock_Exam_Score'])

# Sort by Weighted Score
leaderboard = df.sort_values(by='Weighted_Score', ascending=False).reset_index(drop=True)

# Add Position Column
leaderboard['Position'] = leaderboard.index + 1

# Streamlit app layout
st.title("🌟 BBHS Monthly Study Hours Leaderboard 🌟")
st.write("Here are the top students based on their study hours and mock exam scores.")

# Customizing the DataFrame for visual appeal
def color_positions(val):
    """Colors the positions based on their rank (green to red)"""
    if val == 1:
        return 'background-color: lightgreen'
    elif val == 2:
        return 'background-color: lightyellow'
    elif val == 3:
        return 'background-color: lightcoral'
    else:
        return 'background-color: tomato'

# Prepare the leaderboard without the index column
styled_leaderboard = leaderboard[['Position', 'Student', 'Study_Hours', 'Mock_Exam_Score', 'Weighted_Score']].style.applymap(color_positions, subset=['Position'])

# Display the leaderboard
st.dataframe(styled_leaderboard)

# Additional decorative elements
st.markdown("""
<style>
    .streamlit-table {
        border-collapse: collapse;
        width: 100%;
    }
    .streamlit-table th, .streamlit-table td {
        border: 1px solid #ddd;
        padding: 10px;
        text-align: center;
    }
    .streamlit-table th {
        background-color: #4CAF50;
        color: white;
    }
    .streamlit-table td {
        background-color: #f9f9f9;
    }
</style>
""", unsafe_allow_html=True)

# Add an image or icon for visual appeal (Optional)
st.image("https://ds-images.bolavip.com/news/image?src=https%3A%2F%2Fimages.worldsoccertalk.com%2Fwebp%2FWST_20080328_WST_1706_Champions-League-trophy.webp&width=740&height=416", caption="Keep Studying!", use_column_width=True)

# Add a motivational quote
st.markdown("<h5 style='text-align: center;'>“The future belongs to those who READ.” - Adrian Blaze</h5>", unsafe_allow_html=True)


