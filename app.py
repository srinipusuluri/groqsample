import streamlit as st
import ollama

st.title("Finance AI Advisor")
st.write("A Streamlit app using local Ollama models for financial queries. Works with free local models - no API keys required.")

st.write("### Available Modes")
st.write("- **General Mode (Grok-3)**: Designed for quick, concise responses to simple questions. Uses llama3.2:3b for faster responses.")
st.write("- **Reasoning Mode (Grok-4)**: Engineered for deep, analytical responses. Uses llama3:latest for complex queries with detailed analysis.")

mode = st.selectbox("Select mode:", ["General (Grok-3)", "Reasoning (Grok-4)"])
query = st.text_input("Enter your finance question:")

if st.button("Get Advice"):
    if not query.strip():
        st.error("Please enter a question.")
    else:
        if "General" in mode:
            model = "llama3.2:3b"  # Using as Grok-3 equivalent for general, faster responses
            prompt = f"Provide a concise, direct answer to this finance question: {query}"
        else:
            model = "llama3:latest"  # Using as Grok-4 equivalent for detailed reasoning
            prompt = f"Provide a detailed, reasoned step-by-step analysis for this complex finance question: {query}. Include financial concepts, calculations if applicable, and pros/cons."

        try:
            # Use the correct Ollama chat API
            response = ollama.chat(model=model, messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ])

            # Extract the response content safely
            response_text = response.get('message', {}).get('content', 'No response generated')

            st.subheader(f"Response ({mode}):")
            st.write(response_text)
            # Display behind the scenes info
            st.caption(f"*Behind the scenes: Generated using {model} via Ollama (prompt length: {len(prompt)} chars). No API keys - runs locally.*")
        except Exception as e:
            st.error(f"Error: {e}. Ensure Ollama is running locally with the required models.")

# Add quick topic examples
st.write("### Quick Topic Examples:")
st.write("- What is compound interest?")
st.write("- Pros and cons of investing in stocks vs bonds.")
st.write("- How to create a monthly budget?")
st.write("- What is diversification in portfolio?")
st.write("- Should I invest in ETFs?")
