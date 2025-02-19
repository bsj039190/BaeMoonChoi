import streamlit as st
from streamlit_chat import message  # streamlit-chat 라이브러리

# 페이지 설정
st.set_page_config(page_title="Chatbot", page_icon="💬")

st.title("💬 Streamlit-Chat 기반 챗봇")

# 채팅 기록을 저장하는 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
    ]

# 채팅 UI 출력
for i, msg in enumerate(st.session_state.messages):
    is_user = msg["role"] == "user"  # 사용자인지 여부
    message(msg["content"], is_user=is_user, key=str(i))

# 입력창을 하단에 고정
user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    message(user_input, is_user=True, key=str(len(st.session_state.messages)))

    # 챗봇 응답 추가 (단순 Echo 응답)
    bot_response = f"Echo: {user_input}"
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    message(bot_response, is_user=False, key=str(len(st.session_state.messages)))

    # 🚀 자동 스크롤을 위해 `st.stop()` 사용
    st.stop()  # 코드 실행을 멈추고, 채팅창을 다시 렌더링


# 설계
# 그냥 챗봇 형식으로 가다가 ~~ 추천해줘 해서 하면
# 전체적으로 왼쪽 or 오른쪽으로 옮기고 빈곳에다가 추천해줄 노래 정보 띄워놓기