
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Hugging Face Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Zunoo Text Summarization")
st.write("Summarize articles using Hugging Face Pipelines.")

# Load and cache the model
@st.cache_resource
def load_summarizer():
    return pipeline(
        "text-generation",
        model="HuggingFaceTB/SmolLM2-360M-Instruct"
    )

text = st.text_area(
    "Enter your article or paragraph:",
    height=250,
    placeholder="Paste your text here..."
)

length = st.select_slider(
    "Summary length",
    options=["Short", "Medium", "Long"],
    value="Medium"
)

token_limits = {
    "Short": 60,
    "Medium": 100,
    "Long": 150
}

if st.button("✨ Generate Summary", type="primary"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            with st.spinner("Generating summary..."):
                summarizer = load_summarizer()

                messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are a text summarization assistant. "
                            "Summarize the user's text accurately. "
                            "Keep the important facts and main ideas. "
                            "Do not add information that is not in the text. "
                            "Return only the summary."
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            "Summarize the following text:\n\n" + text
                        )
                    }
                ]

                result = summarizer(
                    messages,
                    max_new_tokens=token_limits[length],
                    do_sample=False,
                    return_full_text=False
                )

                generated = result[0]["generated_text"]

                if isinstance(generated, list):
                    summary = generated[-1]["content"].strip()
                else:
                    summary = generated.strip()

            st.subheader("📌 Generated Summary")
            st.write(summary)

            st.download_button(
                "⬇️ Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {e}")
            st.info(
                "Check your internet connection, available memory, "
                "and model download status."
            )
