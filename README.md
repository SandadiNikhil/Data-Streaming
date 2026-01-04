# Real-Time Data Streaming Pipeline (Kafka + Flink + Postgres + Streamlit)

This project demonstrates a **real-time data streaming pipeline** built using modern backend and streaming technologies.  
It simulates continuous data ingestion, real-time processing, persistent storage, and live visualization.

---

## 🚀 Architecture Overview

Kafka Producer → Kafka → Flink → PostgreSQL → Streamlit UI


### Components
- **Kafka Producer**  
  Generates continuous weather data (city, temperature) and publishes events to Kafka.

- **Apache Kafka**  
  Acts as a durable, scalable event streaming platform that buffers incoming data.

- **Apache Flink**  
  Consumes Kafka events, performs real-time aggregations (average temperature per city), and outputs results.

- **PostgreSQL**  
  Stores the processed, aggregated results for querying and visualization.

- **Streamlit UI**  
  Displays live weather averages by querying PostgreSQL and auto-refreshing at a configurable interval.

---

## 🧠 What This Project Demonstrates

- Event-driven architecture
- Real-time stream processing
- Kafka producer/consumer pattern
- Flink windowed aggregations
- JDBC sink to PostgreSQL
- Docker-based local orchestration
- Live data visualization with Streamlit

---

## 🛠️ Tech Stack

- Apache Kafka
- Apache Flink
- PostgreSQL
- Python (Kafka Producer, Streamlit)
- Java (Flink job)
- Docker & Docker Compose

---

## ▶️ Running the Project

```bash
docker compose up -d --build

