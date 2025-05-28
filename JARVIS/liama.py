from llama_cpp import Llama

#llm = Llama(model_path="path/to/your/model.gguf")  # Download a model first
#response = llm("Write two lines about .")
response = Llama("Write two lines about .")
print(response)
