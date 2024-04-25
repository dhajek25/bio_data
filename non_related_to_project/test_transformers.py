import torch
from transformers import pipeline

def sentiment_analysis(input_text):
    classifier = pipeline("sentiment-analysis")

    res = classifier(input_text)

    return print(res)

# sentiment_analysis("I have two cats and one super angry dog.")

def text_generator(input_text):
    generator = pipeline("text-generation", model="distilgpt2")

    res = generator(input_text, max_length=30, num_return_sequences=5)

    return print(res)

# text_generator("I wish I could")

def classification(input_text, candidate_labels):
    classifier = pipeline("zero-shot-classification")

    candidate_labels = candidate_labels

    res = classifier(input_text, candidate_labels)

    return print(res)

# classification("It is an animal which barks", ["dog", "cat", "fish", "bird", "human"])

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# model_name = "distilbert-base-uncased-finetuned-sst-2-english"
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# sequence = "I have two cats and one super angry dog."
# res = tokenizer(sequence)
# print(res)
#
# tokens = tokenizer.tokenize(sequence)
# print(tokens)
#
# ids = tokenizer.convert_tokens_to_ids(tokens)
# print(ids)
#
# decoded_string = tokenizer.decode(ids)
# print(decoded_string)

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

X_train = ["I have two cats and one super angry dog.",
           "Where is my banana?"]

res = classifier(X_train)
print("Classifer", res)

batch = tokenizer(X_train, padding=True, truncation=True, max_length=512, return_tensors="pt")
print("Batch", batch)

with torch.no_grad():
    outputs = model(**batch)
    print("Outputs", outputs)
    predictions = F.softmax(outputs.logits, dim=1)
    print("predictions", predictions)
    labels = torch.argmax(predictions, dim=1)
    print("labels", labels)