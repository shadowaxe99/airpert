```python
from transformers import pipeline

class Summarizer:
    def __init__(self):
        self.summarizer_model = pipeline('summarization')

    def generate_summary(self, text):
        summary = self.summarizer_model(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']

def main():
    summarizer = Summarizer()
    text = "Your text here"
    summary = summarizer.generate_summary(text)
    print(summary)

if __name__ == "__main__":
    main()
```