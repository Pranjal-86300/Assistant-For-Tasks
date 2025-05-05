import re
from transformers import pipeline

# Initialize the Hugging Face pipeline for token classification (tokenizer)
nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_keywords(text: str):
    """
    Extract important keywords from user query using Hugging Face transformers.
    Returns a set of lowercase keywords.
    """
    # Simple extraction using named entity recognition
    entities = nlp(text)
    keywords = set()

    for entity in entities:
        keywords.add(entity['word'].lower())  # Add recognized entities as keywords
    
    return keywords

def extract_dates(text: str):
    """
    Extract any explicit dates (e.g., 'May 1', 'last week', etc.)
    This version uses regex for simple date phrases.
    """
    date_keywords = []
    if "today" in text.lower():
        date_keywords.append("today")
    if "yesterday" in text.lower():
        date_keywords.append("yesterday")
    if "last week" in text.lower():
        date_keywords.append("last week")
    if "this week" in text.lower():
        date_keywords.append("this week")
    # Extend as needed for more patterns
    return date_keywords
