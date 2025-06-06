import os
from decouple import config
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
os.environ['X_API_KEY'] = config('X_API_KEY')

model = ChatGroq(model="llama-3.3-70b-versatile")
