from transformers import pipeline

# Load a pre-trained model and tokenizer
text_gen_pipeline = pipeline("text-generation", model="gpt-2")

# Generate a response
response = text_gen_pipeline("Hello, how are you?", max_length=50)
print(response)
