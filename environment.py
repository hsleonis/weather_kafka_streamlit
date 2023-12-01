from dotenv import load_dotenv
import os

# take environment variables from .env
load_dotenv()

# AccuWeather API key
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Kafka broker address
KAFKA_BROKER = os.getenv("KAFKA_BROKER")

# Kafka topic
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# Kafka Group Id
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")
