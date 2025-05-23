from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key is set
if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in .env file.")
    exit()

# Configure the generative AI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Run chatbot loop
print("🤖 Gemini Chatbot (type 'exit' to quit)\n")
while True:
    que = input("You: ")
    if que.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    try:
        r = model.generate_content(que)
        print("Gemini:", r.text)
    except Exception as e:
        print("⚠️ Error:", e)
