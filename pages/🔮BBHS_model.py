import pickle
import streamlit as st
import numpy as np
import  psycopg2

def initialize_DB_connection():
   # Connection string
  conn_str = 'postgresql://postgres:tFKz6F7xrxEjHCC9@fixedly-distinct-jackrabbit.data-1.use1.tembo.io:5432/postgres'

  try:
     global conn
      # Create a new database session
     conn = psycopg2.connect(conn_str)
  except Exception as e:
      print(f"Unable to connect to the database: {e}")
   

def get_mock_score():
   initialize_DB_connection()
   try:
        # Create a new cursor object.
        cur = conn.cursor()
        query = """
        Select performance 
        from performance
        where exam_type = 'mock'
        """

        # Test Query Select performance from performance  where exam_type = 'mock'
        cur.execute(query)
        global output

        # Fetch result
        output = cur.fetchall()
        # Extract values from the tuples
        values = [x[0] for x in output]

        # Calculate the average
        average = sum(values) / len(values)
        return(average)
   except Exception as e:
        print(f"An error occurred: {e}")


def get_term_score():
   initialize_DB_connection()
   try:
        # Create a new cursor object.
        cur = conn.cursor()
        query = """
        Select performance 
        from performance
        where exam_type = 'previous-term'
        """

        # Test Query Select performance from performance  where exam_type = 'mock'
        cur.execute(query)
        global output

        # Fetch result
        output = cur.fetchall()
        
        return(output[0][0])
   except Exception as e:
        print(f"An error occurred: {e}")


def get_study_hours():
    initialize_DB_connection()
    try:
        # Create a new cursor object.
        cur = conn.cursor()
        query = """
        SELECT study_hours 
        FROM students
        where username = 'BBHS-1002'
        """
        # Test Query Select performance from performance  where exam_type = 'mock'
        cur.execute(query)
        global output

        # Fetch result
        output = cur.fetchall()
        return(output[0][0])
    except Exception as e:
        print(f"An error occurred: {e}")


def predict_price():
    with open('model_pickle','rb') as file:
      pred_model = pickle.load(file)    

    x = np.zeros(3)
    x[0] = Study_hours
    x[1] = prev_grade
    x[2] = mock_grade
    prediction = pred_model.predict([x])[0]
    if prediction == 1:
        st.success('Likely to pass, Do not relent ')
    else:
      st.error('Likely to fail, Keep pushing harder') 



st.title('BBHS student prediction model for external exams 🔮')
st.write('Predict student likelihood of acing upcoming external exams from student data')
predict = st.button('Predict')
if predict:
    Study_hours = get_study_hours()
    st.write(f'Study hours as recorded in database is, {Study_hours} hours')
    mock_grade = get_mock_score()
    st.write(f'Mock Cummulative as recorded in database is, {mock_grade}%')
    prev_grade = get_term_score()
    st.write(f'Last Term Cummulative as recorded in database is, {prev_grade}%')
    predict_price()