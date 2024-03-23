from openai import OpenAI
import sys

def analyze_text(text):
    try:
        client = OpenAI()

        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": f"Analyze the underlying sentiments or psychological dynamics reflected in this conversation. I'm interested in understanding the emotional tone, any implicit attitudes, and the possible psychological states of the speakers involved. Please focus on the deeper insights and refrain from summarizing the conversation or listing keywords. Here's the conversation.\n\n\'\'\'{text}\'\'\'"
            }
        ],
        temperature=0,
        top_p=1,
        
        )
        return response.choices[0].message.content
    
    except Exception as e:
        raise CustomException(e,sys)