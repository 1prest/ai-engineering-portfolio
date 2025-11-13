# Product Review Sentiment Classifier

## Overview
This project predicts the sentiment (Positive, Neutral, Negative) of product reviews using a Naive Bayes classifier with TF-IDF vectorization.

## Dataset
- Amazon product reviews (English)
- Original file: `product_reviews.jsonl`
- Columns used: `review_body` (text), `label_text` (sentiment)
- Converted to CSV: `product_reviews.csv`

## Preprocessing
- Dropped missing values
- Cleaned text (lowercase, remove punctuation, remove URLs)
- Train-test split: 80% training, 20% testing

## Model
- TF-IDF vectorization (`max_features=7000`, unigrams + bigrams)
- Classifier: Multinomial Naive Bayes

## Performance
- Accuracy: 0.48285 (multi-class classification)
- Confusion matrix and classification report included

## Insights
1. Positive reviews often contain words like "great", "excellent", "love".
2. Negative reviews include words like "poor", "broke", "terrible".
3. Neutral reviews are short or ambiguous, making them hard to classify.

## Files
| File | Description |
|------|-------------|
| `review_sentiment.ipynb` | Notebook workflow |
| `sentiment_model.pkl` | Trained Naive Bayes model |
| `tfidf_vectorizer.pkl` | TF-IDF vectorizer |
| `data/product_reviews.csv` | Cleaned dataset |

## Next Steps (Optional Improvements)
- Use **advanced models** like Random Forest, XGBoost, or Transformers (BERT)  
- Hyperparameter tuning (TF-IDF n-grams, min_df, max_features)  
- Add **lemmatization or stopword customization** to improve accuracy  
