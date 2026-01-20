
# import streamlit as st
# from datetime import datetime, timedelta
# import random
# import pandas as pd
# import requests
# import polyline
# import streamlit.components.v1 as components

# # -------------------------
# # MOCK DATABASE
# # -------------------------
# PNR_DB = {
#     "1234567890": {
#         "train_number": "12951",
#         "train_name": "Rajdhani Express",
#         "source": "Ahmedabad",
#         "boarding_station": "Surat",
#         "destination": "Delhi",
#         "schedule": {
#             "Ahmedabad": "17:40",
#             "Vadodara": "18:45",
#             "Surat": "20:10",
#             "Delhi": "08:30"
#         },
#         "booking_status": "Confirmed",
#         # Mock station addresses
#         "stations_address": {
#             "Ahmedabad": "Ahmedabad, India",
#             "Vadodara": "Vadodara, India",
#             "Surat": "Surat, India",
#             "Delhi": "New Delhi, India"
#         }
#     }
# }

# FOOD_PLACES = {
#     "Delhi": ["Karim’s", "Bukhara", "Saravana Bhavan"]
# }

# HOTELS = {
#     "Delhi": {
#         "Budget": ["Budget Inn", "Hotel City View"],
#         "Mid": ["Radisson Blu", "Lemon Tree"],
#         "Luxury": ["Taj Palace", "ITC Maurya"]
#     }
# }

# # -------------------------
# # FUNCTIONS
# # -------------------------
# def pnr_agent(pnr):
#     return PNR_DB.get(pnr)

# def train_status_agent(boarding_station):
#     return {
#         "delay": random.choice([0, 10, 15]),
#         "current_station": boarding_station
#     }

# def transport_comparison_agent(home, boarding_station):
#     base_eta = random.randint(20, 40)  # Mock ETA in minutes
#     options = {
#         "Uber": {"eta": base_eta + 5, "fare": 280},
#         "Rapido": {"eta": base_eta, "fare": 140},
#         "Private Vehicle": {"eta": base_eta - 5, "fare": 90}
#     }
#     cheapest = min(options, key=lambda x: options[x]["fare"])
#     fastest = min(options, key=lambda x: options[x]["eta"])
#     return options, cheapest, fastest

# def alert_agent(leave_time, mode):
#     now = datetime.now()
#     if now >= leave_time:
#         return f"⚠️ Time to leave NOW. Book {mode} immediately!"
#     return f"✅ You are safe. Leave by {leave_time.strftime('%H:%M')}"

# def destination_agent(destination):
#     return {
#         "food": FOOD_PLACES.get(destination, ["Local Popular Restaurant"]),
#         "hotels": HOTELS.get(destination, {})
#     }

# def get_google_maps_route(origin, destination):
#     """
#     Uses free Google Maps Directions API demo key to fetch route polyline and distance.
#     Replace `API_KEY` with your own key for full usage.
#     """
#     API_KEY = "YOUR_FREE_DEMO_KEY"  # Can use a free/test key
#     url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}"
#     response = requests.get(url)
#     if response.status_code != 200:
#         return None
#     data = response.json()
#     if len(data['routes']) == 0:
#         return None
#     route = data['routes'][0]
#     overview_polyline = route['overview_polyline']['points']
#     distance = route['legs'][0]['distance']['text']
#     duration = route['legs'][0]['duration']['text']
#     return overview_polyline, distance, duration

# def display_route_map(origin, destination):
#     route_info = get_google_maps_route(origin, destination)
#     if not route_info:
#         st.warning("Map route unavailable (API limit or error).")
#         return
#     overview_polyline, distance, duration = route_info
#     coords = polyline.decode(overview_polyline)
#     # Display simple HTML map
#     html_map = f"""
#     <iframe
#       width="100%"
#       height="400"
#       frameborder="0" style="border:0"
#       src="https://www.google.com/maps/embed/v1/directions?key=YOUR_FREE_DEMO_KEY
#       &origin={origin.replace(' ', '+')}
#       &destination={destination.replace(' ', '+')}"
#       allowfullscreen>
#     </iframe>
#     """
#     st.components.v1.html(html_map, height=450)

# # -------------------------
# # STREAMLIT UI
# # -------------------------
# st.set_page_config(page_title="AI Railway Assistant", layout="wide")
# st.title("🚆 AI Railway Assistant + Smart Travel Advisor")

# with st.sidebar:
#     st.header("Journey Input")
#     pnr = st.text_input("PNR Number", placeholder="1234567890")
#     home = st.text_input("Home Location", placeholder="Your Home Address")
#     preferred_mode = st.selectbox("Preferred Mode", ["Uber", "Rapido", "Private Vehicle"])
#     check_btn = st.button("Check Journey Status")

# if check_btn:
#     data = pnr_agent(pnr)
#     if not data:
#         st.error("❌ Invalid PNR")
#     else:
#         boarding_station = data["boarding_station"]
#         boarding_time_str = data["schedule"][boarding_station]
#         boarding_time = datetime.strptime(boarding_time_str, "%H:%M")
        
#         train_status = train_status_agent(boarding_station)
#         transport_options, cheapest, fastest = transport_comparison_agent(home, boarding_station)
#         eta = transport_options[preferred_mode]["eta"]
#         leave_time = boarding_time - timedelta(minutes=eta + 15)
#         alert = alert_agent(leave_time, preferred_mode)
#         destination_info = destination_agent(data["destination"])

#         # -------------------------
#         # PNR & Train Info
#         # -------------------------
#         st.subheader("📄 PNR Details")
#         st.json(data)

#         st.subheader("🚉 Boarding Info")
#         st.markdown(f"**Station:** {boarding_station}  \n**Departure:** {boarding_time_str}")

#         st.subheader("🚦 Train Status")
#         st.markdown(f"**Current Station:** {train_status['current_station']}  \n**Delay:** {train_status['delay']} min")

#         # -------------------------
#         # Transport Options
#         # -------------------------
#         st.subheader("🚕 Transport Options")
#         cols = st.columns(3)
#         for i, (mode, info) in enumerate(transport_options.items()):
#             with cols[i]:
#                 st.markdown(f"### {mode}")
#                 st.markdown(f"**ETA:** {info['eta']} min")
#                 st.markdown(f"**Fare:** ₹{info['fare']}")
#                 if mode == cheapest:
#                     st.success("Cheapest")
#                 if mode == fastest:
#                     st.info("Fastest")

#         # -------------------------
#         # Timeline
#         # -------------------------
#         st.subheader("🕒 Timeline")
#         st.markdown(f"🏠 Leave Home: **{leave_time.strftime('%H:%M')}**")
#         st.markdown(f"🚉 Reach Station: **{(leave_time + timedelta(minutes=eta)).strftime('%H:%M')}**")
#         st.markdown(f"🚆 Train Departs (Boarding): **{boarding_time_str}**")

#         # -------------------------
#         # Alerts
#         # -------------------------
#         st.subheader("⏰ Alert")
#         if "⚠️" in alert:
#             st.warning(alert)
#         else:
#             st.success(alert)

#         # -------------------------
#         # Map Visualization (dynamic with Google Maps)
#         # -------------------------
#         st.subheader("🗺 Journey Map")
#         display_route_map(home, data["stations_address"][boarding_station])

#         # -------------------------
#         # Destination Info
#         # -------------------------
#         with st.expander("🍽 Best Food Near Destination"):
#             for food in destination_info["food"]:
#                 st.markdown(f"• {food}")

#         with st.expander("🏨 Hotels Near Destination"):
#             for category, hotels in destination_info["hotels"].items():
#                 st.markdown(f"**{category} Hotels:**")
#                 for h in hotels:
#                     st.markdown(f"• {h}")

#         # -------------------------
#         # ETA Comparison Chart
#         # -------------------------
#         st.subheader("📊 ETA Comparison")
#         eta_df = pd.DataFrame([
#             {"Mode": mode, "ETA (min)": info["eta"], "Fare (₹)": info["fare"]}
#             for mode, info in transport_options.items()
#         ])
#         st.bar_chart(eta_df.set_index("Mode")["ETA (min)"])

#         st.success("🎉 Smart journey planning completed!")
import streamlit as st
from datetime import datetime, timedelta
import random
import pandas as pd
import streamlit.components.v1 as components

# -------------------------
# MOCK DATABASE
# -------------------------
PNR_DB = {
    "1234567890": {
        "train_number": "12951",
        "train_name": "Rajdhani Express",
        "source": "Ahmedabad",
        "boarding_station": "Surat",
        "destination": "Delhi",
        "schedule": {
            "Ahmedabad": "17:40",
            "Vadodara": "18:45",
            "Surat": "20:10",
            "Delhi": "08:30"
        },
        "booking_status": "Confirmed"
    }
}

FOOD_PLACES = {
    "Delhi": ["Karim’s", "Bukhara", "Saravana Bhavan"]
}

HOTELS = {
    "Delhi": {
        "Budget": ["Budget Inn", "Hotel City View"],
        "Mid": ["Radisson Blu", "Lemon Tree"],
        "Luxury": ["Taj Palace", "ITC Maurya"]
    }
}

# -------------------------
# AGENT FUNCTIONS
# -------------------------
def pnr_agent(pnr):
    return PNR_DB.get(pnr)

def train_status_agent(boarding_station):
    return {
        "delay": random.choice([0, 10, 15]),
        "current_station": boarding_station
    }

def transport_comparison_agent(home, boarding_station):
    # Simple dynamic ETA logic based on fake distance
    base_eta = random.randint(20, 40)  # minutes
    options = {
        "Uber": {"eta": base_eta + 5, "fare": 280},
        "Rapido": {"eta": base_eta, "fare": 140},
        "Private Vehicle": {"eta": base_eta - 5, "fare": 90}
    }
    cheapest = min(options, key=lambda x: options[x]["fare"])
    fastest = min(options, key=lambda x: options[x]["eta"])
    return options, cheapest, fastest

def alert_agent(leave_time, mode):
    now = datetime.now()
    if now >= leave_time:
        return f"⚠️ Time to leave NOW. Book {mode} immediately!"
    return f"✅ You are safe. Leave by {leave_time.strftime('%H:%M')}"

def destination_agent(destination):
    return {
        "food": FOOD_PLACES.get(destination, ["Local Popular Restaurant"]),
        "hotels": HOTELS.get(destination, {})
    }

def display_route_map(home, boarding_station, destination):
    """
    Display map using Google Maps iframe.
    Shows route: Home → Boarding Station → Destination
    No API key needed for demo.
    """
    origin = home.replace(" ", "+")
    via = boarding_station.replace(" ", "+")
    dest = destination.replace(" ", "+")
    html_map = f"""
    <iframe
        width="100%"
        height="450"
        style="border:0"
        loading="lazy"
        allowfullscreen
        src="https://www.google.com/maps/dir/?api=1&origin={origin}&destination={dest}&waypoints={via}">
    </iframe>
    """
    st.components.v1.html(html_map, height=450)

# -------------------------
# STREAMLIT UI
# -------------------------
st.set_page_config(page_title="AI Railway Assistant", layout="wide")
st.title("🚆 AI Railway Assistant + Smart Travel Advisor")

with st.sidebar:
    st.header("Journey Input")
    pnr = st.text_input("PNR Number", placeholder="1234567890")
    home = st.text_input("Home Location", placeholder="Your Home Address")
    preferred_mode = st.selectbox("Preferred Mode", ["Uber", "Rapido", "Private Vehicle"])
    check_btn = st.button("Check Journey Status")

if check_btn:
    data = pnr_agent(pnr)
    if not data:
        st.error("❌ Invalid PNR")
    else:
        boarding_station = data["boarding_station"]
        boarding_time_str = data["schedule"][boarding_station]
        boarding_time = datetime.strptime(boarding_time_str, "%H:%M")
        
        train_status = train_status_agent(boarding_station)
        transport_options, cheapest, fastest = transport_comparison_agent(home, boarding_station)
        eta = transport_options[preferred_mode]["eta"]
        leave_time = boarding_time - timedelta(minutes=eta + 15)
        alert = alert_agent(leave_time, preferred_mode)
        destination_info = destination_agent(data["destination"])

        # -------------------------
        # PNR & Train Info
        # -------------------------
        st.subheader("📄 PNR Details")
        st.json(data)

        st.subheader("🚉 Boarding Info")
        st.markdown(f"**Station:** {boarding_station}  \n**Departure:** {boarding_time_str}")

        st.subheader("🚦 Train Status")
        st.markdown(f"**Current Station:** {train_status['current_station']}  \n**Delay:** {train_status['delay']} min")

        # -------------------------
        # Transport Options
        # -------------------------
        st.subheader("🚕 Transport Options")
        cols = st.columns(3)
        for i, (mode, info) in enumerate(transport_options.items()):
            with cols[i]:
                st.markdown(f"### {mode}")
                st.markdown(f"**ETA:** {info['eta']} min")
                st.markdown(f"**Fare:** ₹{info['fare']}")
                if mode == cheapest:
                    st.success("Cheapest")
                if mode == fastest:
                    st.info("Fastest")

        # -------------------------
        # Timeline
        # -------------------------
        st.subheader("🕒 Timeline")
        st.markdown(f"🏠 Leave Home: **{leave_time.strftime('%H:%M')}**")
        st.markdown(f"🚉 Reach Station: **{(leave_time + timedelta(minutes=eta)).strftime('%H:%M')}**")
        st.markdown(f"🚆 Train Departs (Boarding): **{boarding_time_str}**")

        # -------------------------
        # Alerts
        # -------------------------
        st.subheader("⏰ Alert")
        if "⚠️" in alert:
            st.warning(alert)
        else:
            st.success(alert)

        # -------------------------
        # Map Visualization
        # -------------------------
        st.subheader("🗺 Journey Map")
        display_route_map(home, boarding_station, data["destination"])

        # -------------------------
        # Destination Info
        # -------------------------
        with st.expander("🍽 Best Food Near Destination"):
            for food in destination_info["food"]:
                st.markdown(f"• {food}")

        with st.expander("🏨 Hotels Near Destination"):
            for category, hotels in destination_info["hotels"].items():
                st.markdown(f"**{category} Hotels:**")
                for h in hotels:
                    st.markdown(f"• {h}")

        # -------------------------
        # ETA Comparison Chart
        # -------------------------
        st.subheader("📊 ETA Comparison")
        eta_df = pd.DataFrame([
            {"Mode": mode, "ETA (min)": info["eta"], "Fare (₹)": info["fare"]}
            for mode, info in transport_options.items()
        ])
        st.bar_chart(eta_df.set_index("Mode")["ETA (min)"])

        st.success("🎉 Smart journey planning completed!")

