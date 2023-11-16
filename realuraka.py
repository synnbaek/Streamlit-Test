import streamlit as st

def main():
    # 웹사이트 아이콘과 배경 이미지 설정
    st.set_page_config(
        page_title="EPL 승부 예측기",
        page_icon="⚽",  # 웹사이트 아이콘 설정
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title('EPL 승부 예측기')

    # CSS를 사용하여 배경 색상 설정
    st.markdown(
        """
        <style>
            body {
                background-color: red;  /* 배경 색상을 원하는 색상으로 지정하세요 */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 유저한테 입력을 받는 방법
    # 1. 이름 입력 받기
    t1 = st.text_input('팀1을 입력하세요')
    t2 = st.text_input('팀2을 입력하세요')

    team = {'맨시티':57,'아스널':48,'맨유':39,'뉴캐슬':32,'리버풀':47,'브라이튼':30,'에스턴빌라':31,'토트넘':40,'브렌트포드':28,'풀럼':15,'크리스탈 팰리스':22,'첼시':32,'울버햄튼':26,'웨스트햄':27,'본머스':11,'노팅엄 포레스트':9,'에버턴':19,'레스터':23,'리즈':16,'사우샘프턴':6}

    if t1 in team and t2 in team: 
        if team[t1]  > team[t2] :
            st.success(t1)
        elif team[t1]  < team[t2] :
            st.success(t2)
        elif team[t1]  ==  team[t2]:
            st.success('무승부')
    else:
        st.error('정보를 입력하세요')

if __name__ == "__main__":
    main()
