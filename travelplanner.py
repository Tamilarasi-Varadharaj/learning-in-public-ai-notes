import warnings
warnings.filterwarnings("ignore")

import streamlit as st
from llmproviders import run_llm

st.set_page_config(page_title="Travel Planner AI", page_icon="🌍")
st.title("🌍 AI Travel Planner")

# ---------------- SIDEBAR ----------------
st.sidebar.header("✈️ Plan Your Trip")

destination = st.sidebar.text_input("📍 Destination", "Paris")
days = st.sidebar.slider("📅 Number of Days", 1, 10, 3)
budget = st.sidebar.selectbox("💰 Budget", ["Low", "Medium", "Luxury"])
travel_style = st.sidebar.selectbox("🎒 Travel Style", ["Relaxed", "Adventure", "Cultural", "Foodie"])

generate_plan = st.sidebar.button("🚀 Generate Plan")

# ---------------- CHAT HISTORY ----------------
if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "Hi! I can plan your perfect trip 🌍. Fill details on the left and click 'Generate Plan'!"}
    ]

for msg in st.session_state["history"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# ---------------- GENERATE PLAN ----------------
if generate_plan:
    prompt = f"""
    Create a COMPLETE {days}-day travel itinerary for {destination}.

    STRICT INSTRUCTIONS:
    - You MUST include ALL {days} days
    - Clearly label each day as: Day 1, Day 2, ..., Day {days}
    - Do NOT stop early
    - Do NOT summarize
    - Each day should include:

    Format EXACTLY like this:

    Day 1:
    🏛️ Places:
    🍜 Food:
    💡 Tips:

    Day 2:
    🏛️ Places:
    🍜 Food:
    💡 Tips:

    ...continue until Day {days}

    Details:
    Budget: {budget}
    Travel Style: {travel_style}
    """
    
    st.session_state["history"].append({"role": "user", "content": f"Plan my trip to {destination}"})
    st.chat_message("user").markdown(f"Plan my trip to {destination}")
    st.session_state["history"].append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Planning your trip... ✈️")

        response = run_llm(st.session_state["history"])

        message_placeholder.markdown(response)

        st.session_state["history"].append({"role": "assistant", "content": response})

# ---------------- FOLLOW-UP CHAT ----------------
if prompt := st.chat_input("Ask follow-up (e.g., best cafes, budget tips...)"):
    st.session_state["history"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")


        response = run_llm(st.session_state["history"])

        message_placeholder.markdown(response)

        st.session_state["history"].append({"role": "assistant", "content": response})

# ---------------- RESET ----------------
if st.button("♻️ Reset Chat"):
    st.session_state["history"] = [
        {"role": "assistant", "content": "Chat reset! Plan a new trip 🌍"}
    ]
    st.rerun()