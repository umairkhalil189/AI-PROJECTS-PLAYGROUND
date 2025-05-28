from openai import OpenAI
import user_config

client = OpenAI(api_key = user_config.openai_key)

completion = client.chat.completions.create(
    model = "gpt-4ALL",
    messages =[
        { "role" : "system", "content": "You are a helpful assistant." },
        { 
            "role" : "user" ,
            "content" : "Write me two lines about ...."
        }


    ]

)

print(completion.choices[0].message)