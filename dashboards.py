import streamlit as st


# Streamlit app
def dashboard(dashboard_type: str):
    # Default settings
    st.set_page_config(
        page_title="Real-time Weather Data App",
        page_icon="⛅",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Run the Streamlit app
    st.title(str.upper(dashboard_type) + " : Weather Data")

    # Add Logo
    st.sidebar.image("images/logo.png", width=250)

    # Sidebar with user instructions
    st.sidebar.markdown(
        """
        This app fetches real-time weather data from Accuweather APIs.
        This produce messages to the Kafka topic and consume messages from the Kafka topic, 
        then displays real-time weather data from Kafka messages.
        """
    )

    # Display weather data in the main section
    st.header("Real-Time Weather Data with Kafka + Streamlit")
