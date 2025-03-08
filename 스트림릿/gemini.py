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

class Main:
  def __init__(self):
      os.environ["GOOGLE_API_KEY"] = API
      genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
      self.model = genai.GenerativeModel(
         'gemini-1.5-flash',
         generation_config={
            "max_output_tokens": 200, # 최대 출력 토큰 수
            "temperature" : 0.4 # 창의력 지수 0~1
         }
         )
      self.chat_history = []  # 대화 기록 저장용 리스트, 맥락파악용
      self.max_history = 5  # 최대 5개까지만 저장

  def run(self, input):
      # 사용자 입력 저장
        self.chat_history.append(f"사용자: {input}")

        # 대화 기록이 너무 많으면 최근 5개만 유지
        if len(self.chat_history) > self.max_history * 2:
            self.chat_history = self.chat_history[-(self.max_history * 2):]

        # 전체 대화 내용을 하나의 프롬프트로 전달
        full_prompt = "\n".join(self.chat_history)

        # 모델 응답 생성
        response = self.model.generate_content(full_prompt)
        bot_response = response.text

        # 챗봇 응답 저장
        self.chat_history.append(f"챗봇: {bot_response}")

        return bot_response