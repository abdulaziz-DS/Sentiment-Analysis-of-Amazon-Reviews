# Sentiment Analysis of Amazon Reviews

This project focuses on analyzing customer sentiments from Amazon product reviews using natural language processing techniques. The primary goal is to classify reviews into positive or negative sentiments, leveraging the following tools and methodologies:

- **VADER (Valence Aware Dictionary and sEntiment Reasoner)**
- **Hugging Face Transformers**

## Features

1. **Dataset Analysis:**
   - Load and preview the dataset of Amazon reviews.
   - Perform exploratory data analysis (EDA) to understand the data distribution.

2. **Sentiment Analysis Methods:**
   - **VADER Sentiment Analysis:** A rule-based sentiment analysis tool.
   - **Hugging Face Sentiment Analysis:** Utilizes the `distilbert-base-uncased-finetuned-sst-2-english` model for more nuanced sentiment detection.

3. **Performance Comparison:**
   - Evaluate the performance of the two models using metrics like accuracy and classification reports.
   - Compare results and highlight key differences.

4. **Interactive Streamlit App:**
   - Upload review datasets and visualize sentiment predictions.
   - Input custom text for real-time sentiment analysis.
   - Enhanced user interface with animations and visually distinct indicators for sentiment classification.

## Dataset
The dataset used contains Amazon product reviews in tab-separated values (TSV) format. Each entry includes:
- **Review text:** The textual content of the review.
- **Label:** Ground truth sentiment (positive or negative).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the dataset in a `.tsv` format and place it in the appropriate directory.

## Usage

### Running the Jupyter Notebook
1. Open the `Sentiment Analysis of Amazon Reviews.ipynb` file in Jupyter Notebook.
2. Run all cells to:
   - Load and preprocess the dataset.
   - Perform sentiment analysis using both VADER and Hugging Face.
   - Compare performance metrics and accuracy.

### Running the Streamlit App
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Use the sidebar to upload a dataset or input custom text for analysis.
3. View sentiment predictions with detailed metrics and a user-friendly interface.

## Results

### VADER Sentiment Analysis
- Accuracy: ~71.29%
- Rule-based, fast, and efficient for straightforward tasks.

### Hugging Face Sentiment Analysis
- Accuracy: ~90.13%
- Leverages transformer-based models for superior performance.

### Key Insights
- Hugging Face outperforms VADER in capturing nuanced sentiments.
- VADER offers a lightweight alternative for basic sentiment analysis tasks.

## Conclusion
This project demonstrates the effectiveness of combining traditional and transformer-based sentiment analysis methods. While VADER is useful for quick analyses, Hugging Face provides a more robust solution for complex sentiment classification tasks.

## Future Work
- Extend the analysis to multi-class sentiment classification (e.g., neutral sentiment).
- Incorporate additional datasets to improve model robustness.
- Explore deployment options for a web-based sentiment analysis platform.

## Acknowledgments
- **VADER Sentiment Analysis** for its efficient and rule-based sentiment analysis.
- **Hugging Face** for providing state-of-the-art NLP models.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any queries or collaboration opportunities, please contact:
- **Name:** Abdul Aziz Shaikh
- **Email:** (mailto:shaikhaziz9920@gmail.com)
- **GitHub:** (https://github.com/abdulaziz-DS)

