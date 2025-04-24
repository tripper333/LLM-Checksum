# DGFT Prompt-Response Landscape Analyzer

This Streamlit application analyzes prompts and their corresponding AI-generated responses using DGFT-inspired metrics (embedding variance, token entropy, combined 'μ'), allows for AI and user quality ratings, and provides an interactive visualization of the relationships.

## Features

* Calculates DGFT-inspired metrics (μ, Variance, Entropy) for both prompts and responses.
* Generates responses using configurable OpenAI models (e.g., GPT-4o, GPT-3.5-turbo).
* Gets AI-driven quality scores for responses using configurable OpenAI models.
* Allows users to interactively input their own quality scores (1-10).
* Visualizes the relationship between prompt metrics (μ, entropy, variance) and response quality (AI or user score) using an interactive Plotly scatter plot.
* Detailed tooltips show prompt/response text, metrics, and scores.
* Configurable models for generation, rating, and embeddings via the sidebar.
* Option to use a default list of prompts or enter custom prompts.

## Setup and Running Locally

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd your-repo-name
    ```

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

## Deployment to Streamlit Cloud

1.  **Push your code to a GitHub repository.** Ensure your `secrets.toml` file is included in your `.gitignore` file and is NOT pushed to GitHub.
2.  **Sign up or log in** to [Streamlit Community Cloud](https://streamlit.io/cloud).
3.  Click "**New app**" and connect your GitHub account.
4.  Select the repository and branch containing your `streamlit_app.py` and `requirements.txt` files.
5.  **Configure Secrets:** In the advanced settings during deployment (or later in the app settings), add your `OPENAI_API_KEY` as a secret. The key name must match what's used in the code (`OPENAI_API_KEY`).
6.  Click "**Deploy!**".

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
