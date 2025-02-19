import streamlit as st
from streamlit_chat import message
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="Chatbot", page_icon="💬")

st.title("💬 Streamlit-Chat 기반 챗봇")

# 버튼을 눌렀을 때 채팅 화면 중앙 -> 왼쪽 정렬
if "chat_on" not in st.session_state:
    st.session_state.chat_on = False

# 버튼 생성
button_clicked = st.button("On")

if button_clicked:
    st.session_state.chat_on = True

# CSS로 초기 중앙 정렬 및 상태에 따른 왼쪽 정렬 처리
chat_style = """
    <style>
        .chat-box {
            display: flex;
            flex-direction: column;
            align-items: center;  /* 기본 중앙 정렬 */
            width: 100%;
        }
        .left-align {
            align-items: flex-start;  /* 버튼 클릭 시 왼쪽 정렬 */
        }
    </style>
"""
st.markdown(chat_style, unsafe_allow_html=True)

# 채팅 기록을 저장하는 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
    ]

# 버튼 클릭 시 채팅 화면 왼쪽 정렬 및 현재 시간 표시
if st.session_state.chat_on:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.messages.append({"role": "assistant", "content": f"현재 시각: {current_time}"})
    message(f"현재 시각: {current_time}", is_user=False, key="time")

# 채팅 UI 출력 (채팅 박스를 감싸서 정렬을 제어)
with st.container():
    chat_class = "left-align" if st.session_state.chat_on else ""
    chat_box = st.empty()  # 동적으로 스타일을 적용할 공간 생성
    
    with chat_box:
        # 채팅 내용 표시
        st.markdown(f'<div class="chat-box {chat_class}">', unsafe_allow_html=True)
        for i, msg in enumerate(st.session_state.messages):
            is_user = msg["role"] == "user"  # 사용자인지 여부
            message(msg["content"], is_user=is_user, key=str(i))
        st.markdown('</div>', unsafe_allow_html=True)

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
