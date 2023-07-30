```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class TopicClassifier:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def classify_topic(self, text):
        inputs = self.tokenizer.encode(text, return_tensors='pt')
        outputs = self.model(inputs)[0]
        predicted_class_idx = torch.argmax(outputs).item()
        return predicted_class_idx

def load_topic_classifier(model_name):
    return TopicClassifier(model_name)

def classify_text(topic_classifier, text):
    return topic_classifier.classify_topic(text)
```
