# LLM Checksum

**LLM Checksum** is a Streamlit application that evaluates the *semantic integrity* and *coherence* of prompts and their corresponding AI-generated responses using principles from **Dynamic Gradient Fields Theory (DGFT)**.

It introduces a novel scalar metric, **μ (mu)**—a *linguistic checksum*—which compactly summarizes a prompt's structure, embedding variance, and token entropy into a single, tunable signature. This checksum acts as a proxy for prompt quality, coherence, and semantic tension, enabling both monitoring and optimization of AI agent behavior.

---

## Features

- Calculates DGFT-inspired metrics (μ, Variance, Entropy) for both prompts and responses.
- Uses OpenAI's `text-embedding-ada-002` model for semantic vectorization.
- Generates responses using configurable OpenAI models (e.g., GPT-4o, GPT-3.5-turbo).
- AI-generated quality ratings using GPT-based evaluation prompts.
- Supports manual **user quality scoring** for human-in-the-loop calibration.
- Visualizes prompt and response relationships using interactive Plotly scatter plots.
- Tracks μ evolution across conversation turns to detect drift or degradation.
- Configurable models and inputs via the Streamlit sidebar.

---

## Setup and Running Locally

```bash
git clone <your-repo-url>
cd your-repo-name
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up OpenAI API Key:**
    * **Option A (Environment Variable - Recommended):** Set the `OPENAI_API_KEY` environment variable. The app will pick it up.
    * **Option B (Streamlit Secrets - Local):** Create a file `.streamlit/secrets.toml` (ensure this file is in your `.gitignore` and **never commit it!**) with the following content:
        ```toml
        OPENAI_API_KEY="your_openai_api_key_here"
        ```
    * **Option C (Direct Input):** Run the app and enter the key in the sidebar input field (less secure, not recommended for shared environments).

5.  **Run the Streamlit app:**
    ```bash
    streamlit run streamlit_app.py
    ```

## Usage

1.  Ensure your OpenAI API key is configured (via sidebar input or secrets).
2.  Select the desired OpenAI models for generation, rating, and embeddings in the sidebar.
3.  Choose whether to use the default prompt list or enter your own (one per line).
4.  Click the "**Analyze Prompts and Generate Responses**" button.
5.  Wait for the analysis to complete (progress will be shown).
6.  Review the results table.
7.  Optionally, provide your **User Quality Ratings** (1-10) in the interactive section. Use 0 or leave blank to skip rating a specific response. Click "**Apply User Ratings & Update Plot**".
8.  Explore the **Interactive Visualization**:
    * Select whether the Y-axis represents AI or User Quality Score.
    * Hover over points to see detailed information (prompt, response, metrics, scores).
    * Zoom, pan, and interact with the Plotly chart.

## DGFT-Inspired Metrics

* **Embedding Variance:** Measures the spread or diversity of the concepts within the text's embedding vector. Lower variance might suggest more focused content.
* **Token Entropy (Normalized):** Measures the predictability or repetitiveness of the token sequence based on Shannon entropy, normalized by the theoretical maximum for the sequence length. Lower entropy suggests more repetitive or predictable text.
* **Combined μ (Mu):** Calculated as `exp(-(kv * variance + ke * entropy))`. This metric combines variance and entropy, where lower variance and lower entropy result in a higher μ (closer to 1), potentially indicating lower "tension" or higher conceptual/lexical coherence/simplicity. The weights `kv` and `ke` are tunable parameters (currently set to 50 and 1).
