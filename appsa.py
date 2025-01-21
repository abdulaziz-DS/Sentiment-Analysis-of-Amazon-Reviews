import streamlit as st
import pandas as pd
import random

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Title with animation-like style
st.markdown("""
<style>
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.title {
    background: linear-gradient(90deg, #42a5f5, #64b5f6);
    background-size: 200% 200%;
    animation: gradient 3s ease infinite;
    font-size: 2.5rem;
    font-weight: bold;
    color: white;
    text-align: center;
    padding: 10px;
    border-radius: 10px;
}
</style>
<div class="title">Sentiment Analysis</div>
""", unsafe_allow_html=True)

# Sidebar for file upload
uploaded_file = st.sidebar.file_uploader("Upload a TSV file", type=["tsv"])

if uploaded_file:
    # Load the dataset
    corpus = pd.read_csv(uploaded_file, sep='\t')
    colored_header("Dataset Preview", color_name="blue-70")
    st.dataframe(corpus.head())

    # Perform sentiment analysis on the dataset
    if st.sidebar.button("Analyze Sentiments in Dataset"):
        corpus['Sentiment'] = corpus['review'].apply(
            lambda x: 'Positive' if analyzer.polarity_scores(x)['compound'] >= 0 else 'Negative'
        )

        # Cool visual layout for results
        st.write("### Sentiment Analysis Results")
        for index, row in corpus[['review', 'Sentiment']].iterrows():
            sentiment = row['Sentiment']
            if sentiment == 'Positive':
                icon = ":smiley:"
                color = "#4caf50"  # Lush green
            else:
                icon = ":disappointed:"
                color = "#e57373"  # Soft red

            st.markdown(f"<div style='padding:10px; background-color:{color}; border-radius:5px;'>"
                        f"<strong>{icon} Sentiment:</strong> {sentiment}<br>"
                        f"<strong>Review:</strong> {row['review']}"
                        f"</div>", unsafe_allow_html=True)

# Manual text input for sentiment analysis
st.write("### Analyze Sentiment for Custom Text")
input_text = st.text_area("Enter text to analyze sentiment:", "")
if st.button("Analyze Sentiment"):
    if input_text.strip():
        sentiment_score = analyzer.polarity_scores(input_text)
        sentiment = 'Positive' if sentiment_score['compound'] >= 0 else 'Negative'

        # Display result with animation-like icons
        if sentiment == 'Positive':
            icon = random.choice(['🎉', '😊', '🌟', '👍'])
            color = "#4caf50"  # Lush green
        else:
            icon = random.choice(['😔', '☹️', '👎', '💔'])
            color = "#e57373"  # Soft red

        st.markdown(f"<div style='text-align:center; padding:20px; background-color:{color}; border-radius:10px;'>"
                    f"<span style='font-size:2rem;'>{icon}</span><br>"
                    f"<strong style='font-size:1.5rem;'>Sentiment: {sentiment}</strong><br>"
                    f"<em style='color: #ffffff;'>{input_text}</em>"
                    f"</div>", unsafe_allow_html=True)
        st.write(f"### Details")
        st.json(sentiment_score)
    else:
        st.warning("Please enter valid text to analyze.")
