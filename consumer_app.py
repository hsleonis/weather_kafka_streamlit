import json
from kafka import KafkaConsumer
import streamlit as st
from environment import KAFKA_BROKER, KAFKA_TOPIC
from dashboards import dashboard


# Process weather data from kafka message
def process_weather_data(message):
    # Set the message value
    data = message.value

    # Update the Streamlit app with the weather data
    col1, col2, col3 = st.columns(3)
    col1.metric("Location", data['location'], data['country'])
    col2.metric("Weather", data['weather'])
    col3.metric("UVIndex", data['uvindex'])

    col1.metric(label="Temperature", value=f"{data['temperature']} °{data['temperature_unit']}")
    col2.metric(label="RealFeel", value=f"{data['realfeel']} °{data['realfeel_unit']}", delta=data['realfeel_status'])
    col3.metric("Wind", f"{data['wind']} {data['wind_unit']}", f"{data['wind_dir']} direction")

    col1.metric("Precipitation", f"{data['precipitation']}%")
    col2.metric("Humidity", f"{data['humidity']}%")
    col3.metric("Indoor Humidity", f"{data['indoor']}%")

    col1.metric("Rain", f"{data['rain']}%")
    col2.metric("Thunder", f"{data['thunder']}%")
    col3.metric("Snow", f"{data['snow']}%")

    st.success(f"Last updated: {data['datetime']}")


# Function to consume messages from Kafka topic
def consume_kafka_messages():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )

    for message in consumer:
        process_weather_data(message)


# Update the Streamlit app with data from the background thread
if __name__ == '__main__':
    # Streamlit dashboard
    dashboard("consumer")

    # Consume Kafka messages
    consume_kafka_messages()
