import streamlit as st
from datetime import datetime, timedelta

# Initialize session state to track multiple start and end times and total weekly records
if 'study_records' not in st.session_state:
    st.session_state['study_records'] = []  # Stores daily records (start, end, minutes)
if 'current_start_time' not in st.session_state:
    st.session_state['current_start_time'] = None
if 'weekly_records' not in st.session_state:
    st.session_state['weekly_records'] = []  # Stores weekly total time in minutes

# Function to calculate time difference in minutes
def calculate_time_spent(start, end):
    time_spent = end - start
    return time_spent.total_seconds() / 60  # Convert seconds to minutes

# Function to calculate total study hours for the week
def calculate_weekly_study_hours():
    total_minutes = sum(st.session_state['weekly_records'])
    total_hours = total_minutes / 60  # Convert minutes to hours
    return total_hours

# Display the current session study records
st.header("⏳Study Time Tracker")

# Show all study records for the day (start time, end time, minutes spent)
if st.session_state['study_records']:
    st.subheader("Today's Study Sessions:")
    total_minutes_today = 0
    for record in st.session_state['study_records']:
        start_time, end_time, minutes_spent = record
        st.write(f"Start: {start_time}, End: {end_time}, Time Spent: {minutes_spent:.2f} minutes")
        total_minutes_today += minutes_spent
    st.success(f"Total Study Time Today: {total_minutes_today:.2f} minutes")
else:
    st.write("No study sessions recorded yet.")

# Start Button
if st.button("Start Study Session"):
    if st.session_state['current_start_time'] is None:
        st.session_state['current_start_time'] = datetime.now()
        st.info(f"Study session started at {st.session_state['current_start_time']}")
    else:
        st.warning("A study session is already running. Please stop it first before starting a new one.")

# Stop Button
if st.button("Stop Study Session"):
    if st.session_state['current_start_time'] is not None:
        end_time = datetime.now()
        start_time = st.session_state['current_start_time']
        minutes_spent = calculate_time_spent(start_time, end_time)
        
        # Store the session record (start time, end time, minutes spent)
        st.session_state['study_records'].append((start_time, end_time, minutes_spent))
        
        # Add today's minutes to the weekly records
        st.session_state['weekly_records'].append(minutes_spent)
        
        # Clear current start time after stopping
        st.session_state['current_start_time'] = None
        
        st.success(f"Study session ended at {end_time}. You studied for {minutes_spent:.2f} minutes.")
    else:
        st.warning("No study session is currently running.")

# Calculate total study hours for the week


# Initialize the session state for password validation
if 'password_validated' not in st.session_state:
    st.session_state['password_validated'] = False

if 'weekly_hours_calculated' not in st.session_state:
    st.session_state['weekly_hours_calculated'] = None

if 'calculate_button_clicked' not in st.session_state:
    st.session_state['calculate_button_clicked'] = False

# Button to calculate weekly study hours
if st.button("Calculate Weekly Study Hours"):
    st.session_state['calculate_button_clicked'] = True  # Mark the button as clicked

# Prompt for password only if the button was clicked
if st.session_state['calculate_button_clicked']:
    pw = st.text_input("Password", key='pw', type='password')
    correct_password = 'Badboys'

    if pw:  # Ensure user has entered a password
        if pw == correct_password:
            st.success("Supervisor validation confirmed")
            st.session_state['password_validated'] = True  # Mark validation as successful

            # Calculate the total weekly hours once validation is successful
            total_weekly_hours = calculate_weekly_study_hours()
            st.session_state['weekly_hours_calculated'] = total_weekly_hours
        else:
            st.error("Incorrect password. Please try again.")

# Display the calculated study hours if they are available in session state
if st.session_state['weekly_hours_calculated'] is not None:
    st.success(f"Total Study Hours for the Week: {st.session_state['weekly_hours_calculated']:.2f} hours")



