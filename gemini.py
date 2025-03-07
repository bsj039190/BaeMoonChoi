import pathlib
import textwrap
import os
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

API = "AIzaSyBeTlCYcneV_b73MHwtVKfLO7EgWhhixGw"

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


class Start:
    GOOGLE_API_KEY = os.getenv(API)

    os.environ["GOOGLE_API_KEY"] = API
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    model = genai.GenerativeModel('gemini-1.5-flash')
    
    def run(self, input):
       res = self.model.generate_content(f"{input}")
       return res.text