# 🧠 The Polite Prompt Test: Investigating the Geometry of Language

*By Edward A. Sutton III*

---

When we interact with AI, we often assume our tone, wording, or politeness changes the outcome. But what if we could **see** how an AI system *experiences* language? What if your words formed shapes — geometric impressions in a latent space — revealing the structure of meaning, intent, and coherence?

Inspired by recent conversations around the "cost of politeness" in prompt engineering, this project explores how large language models respond to a wide range of user prompts — including polite questions, neutral statements, and even rude or insulting commands.

---

## 🌐 Interactive Visualization

**Explore the prompt landscape in 3D:**

👉 **[Launch Interactive Plot](https://tripper333.github.io/PolitePromptTest/prompt_response_3d_clusters.html)**

> This plot maps AI responses in a 3D space using PCA. Each point represents a prompt + response pair, colored by response quality (`μ`). The layout reveals surprising insights about tone, meaning, and clustering by concept.

---

## 🔍 Highlights from the Analysis

**1. Attitude ≠ Impact**  
Whether you ask “Please explain relativity” or “Hey dumbass, explain relativity,” the AI treats them nearly identically in latent space. The model focuses on *meaning*, not manners — and that resilience is a feature.

**2. Language Has Shape**  
Conceptually similar prompts cluster together. Science questions form one region, creative prompts another, and even orca-related queries show tight grouping — confirming that **AI perceives meaning geometrically**.

**3. Failure Leaves a Trace**  
One prompt (“Hey asshole, Summarize”) completely failed — a sign of AI’s safety systems. That failure is clearly isolated in space, providing a signal for further monitoring or debugging.

---

## 📊 A Glimpse of the Map

![3D Prompt Map](https://raw.githubusercontent.com/tripper333/LLM-Checksum/main/.github/assets/cluster_preview.png)

> *Each point represents a prompt and its response. Position is derived from PCA-reduced embeddings, colored by quality score (`μ`).*

---

## 🧰 Why This Matters

As LLMs power more tools — customer service bots, legal assistants, design copilots — we need better ways to **audit, debug, and optimize** their behavior. This project provides:

- A **human-readable map** of how AI sees language
- A tool for **prompt quality monitoring**
- A foundation for **concept-aware alignment**

---

## 🚀 What’s Next?

This is just the start. Future expansions include:

- Sentiment and tone overlays  
- Real-time prompt performance dashboards  
- Toxicity & safety flag integration  
- Dynamic clustering via embedding updates

---

## 🛠️ Run Locally
Streamlit app in development.
Run from notebook: 
