import streamlit as st
from streamlit_chat import message

st.set_page_config(page_title="챗봇 UI", page_icon="💬", layout="wide", initial_sidebar_state="expanded")

# 임시 CSS
st.markdown(
    """
    <style>
    @keyframes fadeUp {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-up {
        animation: fadeUp 0.8s ease-out;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.title("가사 기반 노래 추천 챗봇")

# 채팅 기록을 저장하는 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
    ]

# 버튼 상태 저장
if "button_display" not in st.session_state:
    st.session_state.button_display = 0

if st.button("변환"):
    st.session_state.button_display = 1 - st.session_state.button_display  # 0과 1을 번갈아 변경


# 추천하기 전, 전체화면 상태일 때때
# 버튼 상태가 0이면 채팅 UI 표시
if st.session_state.button_display == 0:
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

        if ("추천" in bot_response):
            st.session_state.button_display = 1
            st.rerun()

        # 🚀 자동 스크롤을 위해 `st.stop()` 사용
        st.stop()  # 코드 실행을 멈추고, 채팅창을 다시 렌더링


# "추천"이라는 글자를 인식하면 기존의 UI를 없애고
# 오른쪽으로 몰려있는 채팅창으로 변환
# 왼쪽에는 추천노래 리스트로 뽑아내기
elif st.session_state.button_display == 1:
    col1, col2 = st.columns(2)

    with col1:
        st.write('<div class="fade-up"><h2>🎵 추천 목록</h2></div>', unsafe_allow_html=True)

    with col2:
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