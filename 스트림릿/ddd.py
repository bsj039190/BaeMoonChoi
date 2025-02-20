import streamlit as st
from streamlit_chat import message
from datetime import datetime

st.set_page_config(page_title="챗봇 UI", page_icon="💬", layout="wide")

st.title("가사 기반 노래 추천 챗봇")

# CSS 애니메이션 스타일 정의
st.markdown(
    """
    <style>
        .animated-element {
            animation: fadeInUp 0.5s ease-in-out; /* 0.5초로 변경 */
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if "button_display" not in st.session_state:
    st.session_state.button_display = 0

if st.button("왼쪽"):
    st.session_state.button_display = 1 - st.session_state.button_display

with st.container():
    if st.session_state.button_display == 1:
        # 애니메이션 적용된 텍스트
        st.markdown("<div class='animated-element'>엄엄엄</div>", unsafe_allow_html=True)

with st.container():
    # 애니메이션 적용된 텍스트 영역
    st.text("몰라레후")
    st.text_area("엄준식")

col1, col2, col3 = st.columns(3)

with col1, col2:
    st.header("첫 번째 열")
    st.write("첫 번째 열의 내용입니다.")
    st.image("https://via.placeholder.com/150") # 예시 이미지

# with col2:
#     st.header("두 번째 열")
#     st.write("두 번째 열의 내용입니다.")
#     st.slider("선택하세요", 0, 100) # 예시 슬라이더

with col3:
    st.header("세 번째 열")
    st.write("세 번째 열의 내용입니다.")
    st.line_chart({"data": [1, 2, 3]}) # 예시 차트


# 사이드바는 직접적으로 코드로 컨트롤이 불가능함
# 가운데에 있다가 추천이 되면 왼쪽으로 이동하고 오른쪽에 리스트를 주루루룩 하고싶었으나
# 왼쪽으로 이동하는게 좀 어려움
# 일단 양옆으로 정렬하는건 알아냈음 이거를 기반으로
# col1, col2로 나눠서 하면 좋을 것 같음
# 추천해주기 전에는 가운데 정렬이다가
# 추천해줄때는 col1, 2로 나눠서 나뉘는걸로 하면 좋을 것같음
# 근데 애니메이션까지 넣어서 나누는게 가능할지 모르겠음