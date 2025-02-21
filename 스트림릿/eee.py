import streamlit as st
from streamlit_chat import message
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="챗봇 UI", page_icon="", layout="wide", initial_sidebar_state="expanded")

st.title("가사 기반 노래 추천 챗봇")


if "button_display" not in st.session_state:
    st.session_state.button_display = 0

if st.button("변환"):
    st.session_state.button_display = 1 - st.session_state.button_display

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "안녕하세요! 가사 기반 노래 추천 챗봇입니다. 어떤 노래를 추천해 드릴까요?"}]


if st.session_state.button_display == 0:
    col1, col2, col3 = st.columns(3)

    with col2:
        # 채팅 메시지 표시 영역
        for i, msg in enumerate(st.session_state.messages):
            message(msg["content"], is_user=msg["role"] == "user", key=f"message_{i}")

        # 채팅 입력 영역
        user_input = st.text_input("당신의 메시지", key="user_input")


        components.html(
        """
        <script>
            const input = document.getElementById('user_input');  // 텍스트 입력 위젯 ID
            input.addEventListener('keydown', function(event) {
                if (event.key === 'Enter') {
                    const button = document.querySelector('button');  // "전송" 버튼 선택
                    button.click();  // "전송" 버튼 클릭
                }
            });
        </script>
        """,
        height=0,  # JavaScript 코드만 실행하고, HTML 요소는 표시하지 않음
    )

        if st.button("전송"):
            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                # 챗봇 응답 로직
                chatbot_response = f"당신의 메시지: {user_input}"
                st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
                st.rerun()

                # 입력창 초기화 (다음 실행 시 입력창이 비어 있도록 함)
                st.session_state.user_input = ""

if st.session_state.button_display == 1:

    col1, col2 = st.columns(2)

    with col1:
        # 채팅 메시지 표시 영역
        for i, msg in enumerate(st.session_state.messages):
            message(msg["content"], is_user=msg["role"] == "user", key=f"message_{i}")

        # 채팅 입력 영역
        user_input = st.text_input("당신의 메시지", key="user_input")

        if st.button("전송"):
            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                # 챗봇 응답 로직
                chatbot_response = f"당신의 메시지: {user_input}"
                st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
                st.rerun()

                # 입력창 초기화 (다음 실행 시 입력창이 비어 있도록 함)
                st.session_state.user_input = ""
    
    with col2:
        st.markdown("<div style='border: 1px solid black; padding: 10px;'>살아있다고? 그가?</div>", unsafe_allow_html=True)