import google.generativeai as genai

genai.configure(api_key="*****************************")
model = genai.GenerativeModel("gemini-1.5-flash")
print("chatBot is initilized enter exit for stop chating")
while True:
    user_input=input("You:")
    if user_input=="exit":
        print("chatBot:bye")
        break
    else:
        response=model.generate_content(user_input)
        print(f"chatBot: {response.text}")
        
    
