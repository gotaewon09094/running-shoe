import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(
    page_title="조선시대 전생 테스트",
    page_icon="👑",
    layout="centered"
)

# 2. 스타일 꾸미기
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        margin-top: 20px;
        background-color: #FFD700;
        color: black;
        font-weight: bold;
        height: 50px;
        border-radius: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FFA500;
        color: white;
    }
    div[data-testid="stSliderTickBarMin"] {
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# 3. 질문 리스트
questions = [
    # E vs I
    {"q": "왁자지껄한 5일장이 열렸다! 나는...", "type": "EI", "A": "사람 구경 너무 재밌다! 장터 한복판으로 간다.", "B": "기가 빨린다... 필요한 것만 사고 조용히 빠진다."},
    {"q": "주막에서 모르는 사람이 합석을 제안한다면?", "type": "EI", "A": "오 좋소! 술잔을 기울이며 형님 동생 한다.", "B": "어색하다... 핑계를 대고 자리를 피한다."},
    {"q": "쉬는 날, 내가 선호하는 시간은?", "type": "EI", "A": "친구들을 불러 모아 술판을 벌인다.", "B": "방에서 조용히 책을 읽거나 낮잠을 잔다."},
    {"q": "마을 잔치에서 춤판이 벌어졌을 때 나는?", "type": "EI", "A": "내가 빠질 수 없지! 센터로 나가 춤을 춘다.", "B": "구석에서 박수만 치며 구경한다."},
    {"q": "억울한 일을 당했을 때 나는?", "type": "EI", "A": "동네방네 소리치며 내 억울함을 알린다.", "B": "속으로 삭히거나 친한 사람에게만 털어놓는다."},

    # S vs N
    {"q": "멍하니 하늘을 바라볼 때 드는 생각은?", "type": "SN", "A": "구름이 많네. 내일 비가 오려나?", "B": "저 구름 타고 신선들이 노닐고 있을까?"},
    {"q": "길을 가다 처음 보는 신기한 꽃을 발견했다.", "type": "SN", "A": "색깔이 예쁘네. 무슨 꽃이지?", "B": "이 꽃에는 슬픈 전설이 있을 것 같아."},
    {"q": "서양에서 온 새로운 물건(안경)을 보았다.", "type": "SN", "A": "이건 어떻게 만드는 거지? 재질이 뭐지?", "B": "이걸 쓰면 세상이 다르게 보일까?"},
    {"q": "요리(수라상)를 할 때 나는?", "type": "SN", "A": "내려오는 조리법을 정확히 지킨다.", "B": "감으로 간을 맞추고 새로운 재료도 넣어본다."},
    {"q": "과거 시험 공부를 할 때 나는?", "type": "SN", "A": "족집게 기출문제 위주로 외운다.", "B": "이 학문의 근본적인 원리와 철학을 탐구한다."},

    # T vs F
    {"q": "친구가 상사병에 걸려 밥도 안 먹는다.", "type": "TF", "A": "그 사람은 너한테 관심 없어. 정신 차리고 밥 먹어.", "B": "얼마나 마음이 아프면... (죽이라도 쑤어준다)"},
    {"q": "동료가 실수를 해서 곤장을 맞게 생겼다.", "type": "TF", "A": "안타깝지만 규율은 규율이다. 어쩔 수 없다.", "B": "어떻게든 용서받을 수 있게 같이 빌어준다."},
    {"q": "누군가 내 그림을 비판했다.", "type": "TF", "A": "어디가 부족한지 논리적으로 묻는다.", "B": "기분이 나빠서 며칠 동안 붓을 잡지 않는다."},
    {"q": "고을 사또가 판결을 내릴 때 더 중요한 것은?", "type": "TF", "A": "국법과 증거에 따른 공정한 판결.", "B": "피고인의 딱한 사정과 정상참작."},
    {"q": "고민 상담을 해줄 때 나는?", "type": "TF", "A": "해결책을 제시해 주는 게 진정한 도움이다.", "B": "일단 공감해 주고 위로해 주는 게 먼저다."},

    # J vs P
    {"q": "한양으로 긴 여행을 떠난다. 나의 준비 스타일은?", "type": "JP", "A": "숙소, 경로, 맛집까지 꼼꼼하게 계획한다.", "B": "발길 닿는 대로 간다. 그게 낭만이지!"},
    # 👇👇👇 (수정됨) 사랑방(내 방)으로 변경했습니다! 👇👇👇
    {"q": "사랑방(내 방)의 상태는?", "type": "JP", "A": "책과 붓이 항상 제자리에 정리되어 있다.", "B": "어디에 뭐가 있는지만 알면 된다. 좀 어지럽다."},
    {"q": "오늘 할 일을 마감 기한보다 일찍 끝냈다.", "type": "JP", "A": "미리 끝내서 속이 시원하다. 다음 계획을 짠다.", "B": "오! 남은 시간 동안 뭐 하고 놀지 생각한다."},
    {"q": "친구가 갑자기 '지금 나와!'라고 한다면?", "type": "JP", "A": "갑자기? 나 오늘 계획 있는데... (스트레스)", "B": "오 재밌겠다! 당장 나간다."},
    {"q": "새로운 기술을 배울 때 나는?", "type": "JP", "A": "기초부터 단계별로 차근차근 익힌다.", "B": "일단 이것저것 만져보면서 몸으로 익힌다."}
]

# 4. 결과 데이터
results = {
    "ISTJ": {"name": "대쪽 같은 사헌부 관리", "desc": "원칙주의자! 깐깐하지만 일처리는 확실하군요.", "good": "ESFP", "bad": "ENFP"},
    "ISFJ": {"name": "충직한 내관/상궁", "desc": "섬세한 살림꾼! 뒤에서 묵묵히 챙겨주는 천사표.", "good": "ESTP", "bad": "ENTP"},
    "INFJ": {"name": "미래를 보는 관상가", "desc": "통찰력 갑! 조용하지만 사람의 속을 꿰뚫어 봅니다.", "good": "ENTP", "bad": "ESTP"},
    "INTJ": {"name": "왕의 비밀 책사", "desc": "전략가! 차가워 보이지만 머릿속엔 큰 그림이 있습니다.", "good": "ENFP", "bad": "ESFP"},
    "ISTP": {"name": "전설의 호위무사", "desc": "만능 재주꾼! 말보다 행동으로 보여주는 해결사.", "good": "ESFJ", "bad": "ENFJ"},
    "ISFP": {"name": "도화서 화원", "desc": "예술가! 감수성이 풍부하고 평화로운 영혼의 소유자.", "good": "ESTJ", "bad": "ENTJ"},
    "INFP": {"name": "방랑 시인 김삿갓", "desc": "낭만파! 현실보다는 이상을 꿈꾸는 감성적인 시인.", "good": "ENFJ", "bad": "ESTJ"},
    "INTP": {"name": "방구석 괴짜 발명가", "desc": "아이디어 뱅크! 남들은 이해 못 할 천재성을 가졌군요.", "good": "ENTJ", "bad": "ESFJ"},
    "ESTP": {"name": "마포나루 거상", "desc": "수완가! 돈 냄새를 기가 막히게 맡는 타고난 사업가.", "good": "ISFJ", "bad": "INFJ"},
    "ESFP": {"name": "저잣거리 광대", "desc": "슈퍼스타! 내가 가는 곳이 곧 무대인 분위기 메이커.", "good": "ISTJ", "bad": "INTJ"},
    "ENFP": {"name": "팔도 유람객", "desc": "자유로운 영혼! 새로운 사람과 모험을 찾아 떠납니다.", "good": "INTJ", "bad": "ISTJ"},
    "ENTP": {"name": "상소문 폭격기 유생", "desc": "논리왕! 말발로 조정 대신들을 다 이겨먹는 토론가.", "good": "INFJ", "bad": "ISFJ"},
    "ESTJ": {"name": "호랑이 훈장님", "desc": "지도자! 규칙과 예절을 중시하는 카리스마 리더.", "good": "ISFP", "bad": "INFP"},
    "ESFJ": {"name": "인심 좋은 주막 주모", "desc": "마당발! 정이 많아 주변 사람들을 알뜰살뜰 챙깁니다.", "good": "ISTP", "bad": "INTP"},
    "ENFJ": {"name": "백성을 이끄는 의병장", "desc": "언변가! 사람의 마음을 움직여 세상을 바꿉니다.", "good": "INFP", "bad": "ISTP"},
    "ENTJ": {"name": "야망 넘치는 왕(군주)", "desc": "지배자! 타고난 리더십으로 나라를 이끄는 야망가.", "good": "INTP", "bad": "ISFP"}
}

# 5. 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'score' not in st.session_state:
    st.session_state.score = {"EI": 0, "SN": 0, "TF": 0, "JP": 0}

# 6. 메인 로직

# [시작 화면]
if st.session_state.step == 0:
    st.title("👑 조선시대 내 전생 찾기")
    st.subheader("나는 한양 핵인싸였을까, 방구석 선비였을까?")
    
    st.image("main.png", use_container_width=True)
    
    st.write("---")
    st.write("⏳ **소요시간: 약 3분**")
    st.write("총 20문항 / 솔직하게 답변해주세요!")
    
    if st.button("테스트 시작하기 👉"):
        st.session_state.step = 1
        st.rerun()

# [질문 화면]
elif 1 <= st.session_state.step <= 20:
    q_index = st.session_state.step - 1
    q_data = questions[q_index]
    
    st.progress(st.session_state.step / 20)
    
    st.write(f"### Q{st.session_state.step}. {q_data['q']}")
    
    options = ["👈 왼쪽이 확실함", "👈 왼쪽인 편", "😐 잘 모르겠음", "👉 오른쪽인 편", "👉 오른쪽이 확실함"]
    choice = st.select_slider("어느 쪽이 더 내 모습에 가깝나요?", options=options, value="😐 잘 모르겠음")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Left**\n\n{q_data['B']}")
    with col2:
        st.success(f"**Right**\n\n{q_data['A']}")

    if st.button("다음으로 넘어감"):
        score_map = {
            "👈 왼쪽이 확실함": -2, 
            "👈 왼쪽인 편": -1, 
            "😐 잘 모르겠음": 0, 
            "👉 오른쪽인 편": 1, 
            "👉 오른쪽이 확실함": 2
        }
        st.session_state.score[q_data['type']] += score_map[choice]
        st.session_state.step += 1
        st.rerun()

# [결과 화면]
elif st.session_state.step > 20:
    mbti = ""
    mbti += "E" if st.session_state.score["EI"] > 0 else "I"
    mbti += "S" if st.session_state.score["SN"] > 0 else "N"
    mbti += "T" if st.session_state.score["TF"] > 0 else "F"
    mbti += "J" if st.session_state.score["JP"] > 0 else "P"
    
    result = results[mbti]
    
    st.balloons()
    
    st.title("당신의 조선시대 전생 직업은?")
    st.header(f"✨ {result['name']} ✨")
    
    st.write(f"### {result['desc']}")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error(f"💖 환상의 짝꿍: \n\n**{results[result['good']]['name']}**")
    with col2:
        st.warning(f"💔 최악의 짝꿍: \n\n**{results[result['bad']]['name']}**")
        
    st.write("---")
    if st.button("다시 테스트하기"):
        st.session_state.step = 0
        st.session_state.score = {"EI": 0, "SN": 0, "TF": 0, "JP": 0}
        st.rerun()
        