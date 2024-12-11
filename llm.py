from transformers import pipeline

model = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
prompt = "Analyze this stock trend and recommend an action: ..."
decision = model(prompt)
print(decision)
