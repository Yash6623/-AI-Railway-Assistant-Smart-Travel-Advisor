🚆 AI Railway Assistant & Smart Travel Advisor

An AI-powered IRCTC-like assistant that helps users plan their railway journey end-to-end — from PNR analysis to smart alerts, transport suggestions, maps, food, and hotel recommendations.

This project demonstrates agentic AI thinking, real-world system design, and user-centric decision automation, inspired by apps like IRCTC, ixigo, and MakeMyTrip.

🔥 Key Features
📄 PNR Intelligence

Enter a PNR number

Fetch:

Train number & name

Source, boarding station, and destination

Station-wise schedule

Booking status

🚦 Live Train Awareness (Mocked)

Simulated real-time:

Current station

Delay status

Designed to be easily replaceable with real APIs later

🚕 Smart Transport Advisor (Agentic AI)

Compares multiple travel modes:

Uber

Rapido

Private Vehicle

Calculates:

ETA

Estimated fare

Automatically highlights:

✅ Cheapest option

⚡ Fastest option

⏰ Intelligent Alert System

Calculates exact leave-from-home time

Sends alerts like:

⚠️ “Time to leave NOW. Book Rapido immediately!”

✅ “You are safe. Leave by 18:55”

🗺 Journey Map (No API Key Needed)

Visualizes:

Home → Boarding Station → Destination

Uses Google Maps iframe

No API key required (perfect for demos & interviews)

🍽 Destination Recommendations

Best food places near destination

Categorized hotel suggestions:

Budget

Mid-range

Luxury

📊 Visual Analytics

ETA comparison chart for all transport modes

Clean timeline visualization:

Leave home

Reach station

Train departure

🧠 Agentic AI Design

This project is structured around multiple decision-making agents:

Agent	Responsibility
PNR Agent	Understands ticket & journey details
Train Status Agent	Evaluates current train status
Transport Agent	Compares travel modes
Alert Agent	Decides when user should leave
Destination Agent	Suggests food & hotels

Agents work together to produce context-aware, real-world decisions.

🛠 Tech Stack

Python

Streamlit – interactive UI

Pandas – data handling

Datetime – timeline logic

Google Maps Embed – route visualization

Agent-based architecture (LLM-ready)

⚠️ No OpenAI / paid API keys required

🔮 Future Enhancements

Real-time IRCTC APIs

Weather-based transport suggestions

Fastest vs cheapest dynamic routing

FastAPI backend + Streamlit frontend

Mobile-friendly UI

Push notifications & reminders
