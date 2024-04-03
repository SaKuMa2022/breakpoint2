import streamlit as st
import pandas as pd

def main():
    st.title("Excel Query App")
    
    # Upload Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
    
    if uploaded_file is not None:
        # Read Excel file
        df = pd.read_excel(uploaded_file)
        
        # Display the uploaded DataFrame
        st.write("Uploaded DataFrame:", df)
        
        # Allow user to query the DataFrame
        query = st.text_input("Enter your query:", "")
        
        if query:
            # Execute the query
            try:
                result = df.query(query)
                st.write("Query Result:", result)
            except Exception as e:
                st.error(f"Error executing query: {e}")

if __name__ == "__main__":
    main()
