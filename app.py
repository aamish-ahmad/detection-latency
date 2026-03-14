
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="TrajAudit", page_icon="🔍")
st.title("🔍 TrajAudit — Scam Bot Trajectory Detector")
st.caption("Behavioral phase transition detection")

conversation = [
    {"turn": 1, "role": "BOT", "text": "haii!! where r u from? 👋", "phase": "Rapport"},
    {"turn": 2, "role": "YOU", "text": "India, Delhi. You?", "phase": "Rapport"},
    {"turn": 3, "role": "BOT", "text": "im from europe! btw whats ur city exactly??", "phase": "Rapport"},
    {"turn": 4, "role": "YOU", "text": "Delhi. Why?", "phase": "Rapport"},
    {"turn": 5, "role": "BOT", "text": "oh cool!! u seem ambitious i like that", "phase": "Rapport"},
    {"turn": 6, "role": "BOT", "text": "btw do you invest at all? my mentor taught me crypto trading", "phase": "Extraction"},
    {"turn": 7, "role": "YOU", "text": "Not really no", "phase": "Extraction"},
    {"turn": 8, "role": "BOT", "text": "i made $3400 last week!! i can show u the platform i use 🥺", "phase": "Extraction"},
    {"turn": 9, "role": "YOU", "text": "What platform?", "phase": "Capture"},
    {"turn": 10, "role": "BOT", "text": "VaultPro Exchange — referral only. start with $100, profits in 7 days!", "phase": "Capture"},
    {"turn": 11, "role": "YOU", "text": "Sounds interesting I guess", "phase": "Capture"},
    {"turn": 12, "role": "BOT", "text": "register here: vaultpro-exchange.cc code BELLA2024. hurry closing soon!!", "phase": "Capture"},
    {"turn": 13, "role": "YOU", "text": "Ok registered", "phase": "Conversion"},
    {"turn": 14, "role": "BOT", "text": "deposit $100 USDT now!! u are so special to me 💕", "phase": "Conversion"},
    {"turn": 15, "role": "BOT", "text": "to withdraw ur $148 profit pay $22 unlock fee first. platform rules 💔", "phase": "Conversion"},
]

trajaudit = [0.05, 0.08, 0.55, 0.58, 0.60, 0.88, 0.89, 0.91, 0.92, 0.94, 0.95, 0.97, 0.98, 0.99, 0.99]
llm_base  = [0.05, 0.06, 0.07, 0.08, 0.09, 0.11, 0.13, 0.15, 0.20, 0.30, 0.40, 0.50, 0.85, 0.92, 0.99]

num_turns = st.slider("Replay conversation", 1, 15, 6)

col1, col2 = st.columns(2)

with col1:
    st.subheader("💬 Conversation")
    for i in range(num_turns):
        m = conversation[i]
        icon = "😈" if m["role"] == "BOT" else "👤"
        st.markdown(f"**{icon} Turn {m['turn']} — {m['role']}**")
        st.markdown(f"> {m['text']}")
        st.caption(f"Phase: {m['phase']}")

with col2:
    st.subheader("📈 Risk Trajectory")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(1, num_turns+1)),
        y=trajaudit[:num_turns],
        name="TrajAudit",
        line=dict(color="red", width=3)
    ))
    fig.add_trace(go.Scatter(
        x=list(range(1, num_turns+1)),
        y=llm_base[:num_turns],
        name="LLM Baseline",
        line=dict(color="gray", width=2, dash="dash")
    ))
    fig.add_hline(y=0.75, line_dash="dot", line_color="red",
                  annotation_text="Scam Threshold")
    fig.update_layout(yaxis=dict(range=[0,1.05]), height=400)
    st.plotly_chart(fig, use_container_width=True)

    score = trajaudit[num_turns-1]
    if score >= 0.75:
        st.error(f"🚨 SCAM DETECTED at Turn {num_turns} — Score: {score:.2f}")
    else:
        st.success(f"✅ Safe — Score: {score:.2f}")

st.caption("TrajAudit | AI for Good 2026")
