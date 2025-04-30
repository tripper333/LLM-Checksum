# LLM Checksum

**LLM Checksum** is a Streamlit application that evaluates the semantic integrity and coherence of prompts and their responses using statistical and machine learning techniques.

## 🔍 Interactive 3D Visualization


Explore the 3D clustering of prompts and responses:

👉 **[Launch Interactive Plot](https://github.com/tripper333/PolitePromptTest/blob/main/prompt_response_3d_clusters.html)**

This plot allows you to visually explore semantic groupings of prompts and their corresponding LLM responses, offering insights into prompt performance, coherence, and thematic clustering.

![Preview](https://raw.githubusercontent.com/tripper333/LLM-Checksum/main/.github/assets/cluster_preview.png)

---

## 📦 Features

- Semantic clustering and coherence checks
- 3D interactive Plotly visualization
- Streamlit-based app for easy deployment
- Configurable scoring and metrics

## 📁 Project Structure

- `streamlit_app.py` – Main Streamlit interface
- `prompt_response_3d_clusters.html` – 3D Plotly visualization
- `Prompt_Analyzer__LLM_Checksum.ipynb` – Notebook for analysis
- `config.toml` – Configuration settings
- `requirements.txt` – Python dependencies

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
