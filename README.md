# 🚆 AI Railway Assistant & Smart Travel Advisor

An AI-powered IRCTC-like assistant that helps users plan their railway journey end-to-end — from PNR analysis to smart alerts, transport suggestions, maps, food, and hotel recommendations.

This project demonstrates agentic AI thinking, real-world system design, and user-centric decision automation inspired by IRCTC, ixigo, and MakeMyTrip.

---

## 🔥 Key Features

### 📄 PNR Intelligence
- Enter a PNR number
- Fetch:
  - Train number & name
  - Source, boarding station, and destination
  - Station-wise schedule
  - Booking status

### 🚦 Live Train Awareness (Mocked)
- Simulated real-time:
  - Current station
  - Delay status
- Easily replaceable with real APIs

### 🚕 Smart Transport Advisor
- Compares multiple travel modes:
  - Uber
  - Rapido
  - Private Vehicle
- Calculates:
  - ETA
  - Estimated fare
- Automatically highlights:
  - Cheapest option
  - Fastest option

### ⏰ Intelligent Alert System
- Calculates exact leave-from-home time
- Sends alerts like:
  - “Time to leave NOW. Book Rapido immediately!”
  - “You are safe. Leave by 18:55”

### 🗺 Journey Map (No API Key Required)
- Visualizes:
  - Home → Boarding Station → Destination
- Uses Google Maps embed
- No API key needed

### 🍽 Destination Recommendations
- Best food places near destination
- Hotel recommendations:
  - Budget
  - Mid-range
  - Luxury

### 📊 Visual Analytics
- ETA comparison chart
- Journey timeline visualization

---

## 🧠 Agentic AI Design

The system is built using multiple decision-making agents:

| Agent | Responsibility |
|------|---------------|
| PNR Agent | Ticket & journey details |
| Train Status Agent | Train delay & status |
| Transport Agent | Travel mode comparison |
| Alert Agent | Leave-time decision |
| Destination Agent | Food & hotel suggestions |

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Datetime
- Google Maps Embed
- Agent-based architecture (LLM-ready)

No OpenAI or paid API keys required.

---

## 🚀 How to Run Locally

```bash
pip install streamlit pandas
streamlit run IRCTC_AGENT5.py
