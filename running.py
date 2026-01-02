import streamlit as st
import os

# 1. 경로 설정 (이미지 찾기용)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 페이지 설정
st.set_page_config(page_title="러닝화 소믈리에", page_icon="👟", layout="centered")

# 3. 스타일 (텍스트 디자인 강화)
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; height: 50px; background-color: #000000; color: white; }
    .stButton>button:hover { background-color: #333333; color: white; }
    .price-tag { font-size: 18px; font-weight: bold; color: #d32f2f; }
    .review-text { font-size: 14px; color: #333; margin-bottom: 2px; }
</style>
""", unsafe_allow_html=True)

# 4. 이미지 경로 함수
def get_image_path(filename):
    if not filename.endswith(".png") and not filename.endswith(".jpg"):
        filename += ".png"
    return os.path.join(current_dir, filename)

# 5. 신발 데이터 (3줄 요약 포함)
shoes_db = [
    # === [나이키] ===
    {
        "brand": "Nike", "name": "페가수스 40", "type": "입문/조깅용", "width": "보통", "price": 139000, 
        "img": "pegasus", "link": "https://link.coupang.com/a/dkp2d1",
        "detail": ["✅ 입문자부터 고수까지 전천후 사용", "☁️ 적당한 쿠션과 반발력의 조화", "💡 고민될 땐 그냥 이거 사면 됩니다"]
    },
    {
        "brand": "Nike", "name": "베이퍼플라이 3", "type": "대회용(레이싱)", "width": "보통", "price": 299000, 
        "img": "vaporfly", "link": "https://link.coupang.com/a/dkp3kj",
        "detail": ["✅ 마라톤 기록 단축을 노리는 러너", "🚀 신는 순간 앞으로 튕겨 나가는 느낌", "💡 세계 기록을 세운 바로 그 신발"]
    },
    {
        "brand": "Nike", "name": "인빈서블 3", "type": "입문/조깅용", "width": "보통", "price": 209000, 
        "img": "invincible", "link": "https://link.coupang.com/a/dkp3NT",
        "detail": ["✅ 무릎 보호가 최우선인 러너", "☁️ 마시멜로 같은 맥스 쿠션감", "💡 회복 러닝용으로 최고입니다"]
    },
    {
        "brand": "Nike", "name": "알파플라이 3", "type": "대회용(레이싱)", "width": "보통", "price": 329000, 
        "img": "alphafly", "link": "https://link.coupang.com/a/dkp4zK",
        "detail": ["✅ 풀코스 서브3 목표 주자", "🚀 에어팟의 미친 반발력", "💡 현존하는 러닝화 중 1티어 대장"]
    },

    # === [아식스] ===
    {
        "brand": "Asics", "name": "젤 카야노 30", "type": "안정화(평발)", "width": "넓음", "price": 189000, 
        "img": "kayano", "link": "https://link.coupang.com/a/dkp4XT",
        "detail": ["✅ 평발이거나 발목이 안쪽으로 꺾이는 분", "🛡️ 흔들림 없이 발을 꽉 잡아줌", "💡 부상 방지에는 이만한 게 없습니다"]
    },
    {
        "brand": "Asics", "name": "노바블라스트 4", "type": "훈련/대회겸용", "width": "보통", "price": 159000, 
        "img": "novablast", "link": "https://link.coupang.com/a/dkp5J2",
        "detail": ["✅ 조깅부터 스피드 훈련까지 하나로", "☁️ 쫀득쫀득한 트램폴린 같은 쿠션", "💡 디자인, 성능, 가격 3박자 완벽"]
    },
    {
        "brand": "Asics", "name": "슈퍼블라스트", "type": "훈련/대회겸용", "width": "보통", "price": 249000, 
        "img": "superblast", "link": "https://link.coupang.com/a/dkp6pr",
        "detail": ["✅ 카본화는 부담스럽지만 속도는 내고 싶을 때", "⚖️ 믿을 수 없을 만큼 가벼움", "💡 요즘 없어서 못 사는 품절 대란템"]
    },

    # === [뉴발란스] ===
    {
        "brand": "New Balance", "name": "프레쉬폼 1080 v13", "type": "입문/조깅용", "width": "넓음", "price": 179000, 
        "img": "nb1080", "link": "https://link.coupang.com/a/dkp7FO",
        "detail": ["✅ 발볼이 넓고 편한 신발 찾는 분", "☁️ 구름 위를 걷는 듯한 물렁한 쿠션", "💡 걷기용으로 신어도 너무 좋습니다"]
    },
    {
        "brand": "New Balance", "name": "SC 엘리트 v4", "type": "대회용(레이싱)", "width": "넓음", "price": 279000, 
        "img": "nb_elite", "link": "https://link.coupang.com/a/dkp8wh",
        "detail": ["✅ 발볼 넓은 러너를 위한 레이싱화", "🚀 각진 디자인으로 안정감 있는 반발력", "💡 디자인이 예뻐서 인기가 많아요"]
    },
    {
        "brand": "New Balance", "name": "SC 트레이너 v2", "type": "훈련/대회겸용", "width": "넓음", "price": 199000, 
        "img": "nb_trainer", "link": "https://link.coupang.com/a/dkp85M",
        "detail": ["✅ 장거리 훈련(LSD)을 즐기는 러너", "🛡️ 묵직하지만 밀어주는 힘이 좋음", "💡 카본 플레이트 입문용으로 추천"]
    },

    # === [호카] ===
    {
        "brand": "Hoka", "name": "클리프톤 9", "type": "입문/조깅용", "width": "보통", "price": 169000, 
        "img": "clifton", "link": "https://link.coupang.com/a/dkp9A1",
        "detail": ["✅ 가벼운 무게와 풍성한 쿠션을 원할 때", "☁️ 부드럽게 발을 감싸주는 느낌", "💡 호카의 가장 대표적인 모델"]
    },
    {
        "brand": "Hoka", "name": "마하 6", "type": "훈련/대회겸용", "width": "보통", "price": 179000, 
        "img": "mach", "link": "https://link.coupang.com/a/dkp9Rt",
        "detail": ["✅ 스피드를 즐기는 경량 러너", "⚡ 땅을 박차고 나가는 경쾌한 느낌", "💡 인터벌 훈련할 때 신으면 딱입니다"]
    },
    {
        "brand": "Hoka", "name": "본디 8", "type": "입문/조깅용", "width": "넓음", "price": 199000, 
        "img": "bondi", "link": "https://link.coupang.com/a/dkqahc",
        "detail": ["✅ 체중이 좀 나가거나 무릎이 아픈 분", "☁️ 호카 신발 중 가장 두꺼운 쿠션", "💡 키높이 효과는 덤입니다"]
    },

    # === [아디다스] ===
    {
        "brand": "Adidas", "name": "아디오스 프로 3", "type": "대회용(레이싱)", "width": "보통", "price": 279000, 
        "img": "adios_pro", "link": "https://link.coupang.com/a/dkqaCd",
        "detail": ["✅ 풀코스 완주가 목표인 중상급자", "🛡️ 탄탄한 쿠션과 훌륭한 내구성", "💡 악마의 뿌리(끈 구멍)만 조심하면 최고"]
    },
    {
        "brand": "Adidas", "name": "보스턴 12", "type": "훈련/대회겸용", "width": "보통", "price": 179000, 
        "img": "boston", "link": "https://link.coupang.com/a/dkqaY5",
        "detail": ["✅ 내구성 좋은 전천후 훈련화", "⚡ 유리섬유 뼈대가 들어간 탄력", "💡 가성비 최고의 슈퍼 트레이너"]
    },

    # === [써코니] ===
    {
        "brand": "Saucony", "name": "엔돌핀 스피드 4", "type": "훈련/대회겸용", "width": "보통", "price": 199000, 
        "img": "endorphin_speed", "link": "https://link.coupang.com/a/dkqbta",
        "detail": ["✅ 하나만 사야 한다면 무조건 이것", "🏆 러너들이 뽑는 '육각형' 올라운더", "💡 카본 대신 나일론판이라 발이 편해요"]
    },
    {
        "brand": "Saucony", "name": "트라이엄프 21", "type": "입문/조깅용", "width": "보통", "price": 189000, 
        "img": "triumph", "link": "https://link.coupang.com/a/dkqbPL",
        "detail": ["✅ 고급스러운 쿠션감을 원하는 분", "☁️ 푹신하면서도 쫀득한 프리미엄 폼", "💡 장거리 조깅에도 발바닥 불 안나요"]
    },

    # === [기타] ===
    {
        "brand": "Brooks", "name": "고스트 15", "type": "입문/조깅용", "width": "넓음", "price": 149000, 
        "img": "ghost", "link": "https://link.coupang.com/a/dkqb63",
        "detail": ["✅ 튀는 것보다 무난하고 튼튼한 게 좋을 때", "🛡️ 미국 시장 점유율 1위의 위엄", "💡 청바지에 신어도 어색하지 않아요"]
    },
    {
        "brand": "Puma", "name": "디비에이트 나이트로 3", "type": "훈련/대회겸용", "width": "보통", "price": 189000, 
        "img": "deviate", "link": "https://link.coupang.com/a/dkqcpW",
        "detail": ["✅ 비 오는 날에도 뛰는 열정 러너", "⚡ 푸마그립의 미친 접지력(안 미끄러짐)", "💡 카본 입문용으로 가성비 최고"]
    },
    {
        "brand": "On", "name": "클라우드몬스터", "type": "입문/조깅용", "width": "보통", "price": 199000, 
        "img": "cloudmonster", "link": "https://link.coupang.com/a/dkqddQ",
        "detail": ["✅ 남들과 다른 힙한 디자인을 원할 때", "☁️ 구멍 뚫린 중창이 통통 튀는 재미", "💡 요즘 러닝 크루에서 제일 핫해요"]
    }
]

# 6. 메인 화면
st.title("👟 나에게 맞는 러닝화 찾기")

# 사이드바
with st.sidebar:
    st.header("🔍 조건 선택")
    purpose = st.radio("용도", ["입문/조깅용", "훈련/대회겸용", "대회용(레이싱)", "안정화(평발)"])
    foot_width = st.radio("발볼", ["보통", "넓음 (발볼러)"])
    budget = st.slider("예산", 5, 40, 20) * 10000

# 필터링 로직
recommendations = []
for shoe in shoes_db:
    if shoe["price"] <= budget:
        if purpose == shoe["type"]:
            if foot_width == "넓음 (발볼러)":
                if shoe["width"] == "넓음": recommendations.append(shoe)
            else: recommendations.append(shoe)
        elif shoe["type"] == "훈련/대회겸용" and purpose == "입문/조깅용" and shoe["price"] <= budget:
             recommendations.append(shoe)

# 결과 출력
if len(recommendations) > 0:
    st.success(f"{len(recommendations)}개의 신발을 찾았습니다!")
    for shoe in recommendations:
        with st.container():
            c1, c2 = st.columns([1, 1.5])
            with c1:
                # 이미지 표시
                full_path = get_image_path(shoe["img"])
                if os.path.exists(full_path):
                    st.image(full_path, use_container_width=True)
                else:
                    st.error(f"❌ 사진 없음")
            
            with c2:
                st.subheader(shoe['name'])
                st.markdown(f"**{shoe['brand']}** | <span class='price-tag'>{shoe['price']:,}원</span>", unsafe_allow_html=True)
                st.write("") 
                
                # 3줄 요약 출력
                for point in shoe['detail']:
                    st.markdown(f"<div class='review-text'>{point}</div>", unsafe_allow_html=True)
                
                st.write("")
                st.link_button("🚀 최저가 확인하기", shoe['link'])
        st.divider()
else:
    # 👇👇👇 (여기가 수정되었습니다!) 👇👇👇
    st.warning("😭 조건에 딱 맞는 신발이 없네요. 예산을 조금만 더 올려보시겠어요?")

# ... (위에는 다른 코드들이 있겠죠?)

st.divider() # 구분선 한 번 그어주고
st.caption("이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.")