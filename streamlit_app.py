import streamlit as st
from openai import OpenAI
from utils import get_embedding, compute_mu, compute_token_entropy, compute_variance, generate_field

st.set_page_config(page_title="LLM Checksum", layout="wide")

# Load OpenAI key from Streamlit Cloud secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)

# Sidebar setup
st.sidebar.header("Settings")
model_choice = st.sidebar.selectbox("Select LLM model", ["gpt-4o", "gpt-3.5-turbo"])
k_v = st.sidebar.slider("Variance weight (k_v)", 1.0, 100.0, 50.0)
k_e = st.sidebar.slider("Entropy weight (k_e)", 0.1, 10.0, 1.0)

# App title
st.title("LLM Checksum")
st.markdown("Semantic checksum analysis using DGFT-inspired metrics")

# Input
prompt = st.text_area("Enter your prompt here:")

if st.button("Analyze") and prompt:
    # Compute metrics
    embedding = get_embedding(prompt)
    var = compute_variance(embedding)
    ent = compute_token_entropy(prompt)
    mu = compute_mu(var, ent, kv=k_v, ke=k_e)

    # Generate response
    resp = client.chat.completions.create(
        model=model_choice,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    response_text = resp.choices[0].message.content

    # Display metrics and response
    st.subheader("Metrics")
    st.write(f"**Variance:** {var:.6f}")
    st.write(f"**Entropy:** {ent:.6f}")
    st.write(f"**μ (checksum):** {mu:.6f}")

    st.subheader("Response")
    st.write(response_text)

    # 3D field visualization
    X, Y, Z = generate_field(mu, ent, var)
    import plotly.graph_objects as go
    fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
    fig.update_layout(title="Response Opportunity Landscape", autosize=True)
    st.plotly_chart(fig, use_container_width=True)
