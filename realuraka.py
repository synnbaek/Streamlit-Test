import os
import streamlit as st
import openai

# OpenAI GPT-3 API 키 설정
api_key = os.environ.get("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")

def main():
    # CSS를 사용하여 배경 이미지 설정
    st.markdown(
        """
        <style>
            body {
                background-image: url('https://wallpapers.com/images/featured-full/premier-league-86d2ur0b5ryesbe7.jpg'); /* 배경 이미지 URL로 변경 */
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('EPL 승부 예측기')s

    # 팀 이름을 입력 받음
    t1 = st.text_input('팀1을 입력하세요')
    t2 = st.text_input('팀2을 입력하세요')

    team = {'맨시티': 57, '아스널': 48, '맨유': 39, '뉴캐슬': 32, '리버풀': 47, '브라이튼': 30, '에스턴빌라': 31, '토트넘': 40, '브렌트포드': 28, '풀럼': 15, '크리스탈 팰리스': 22, '첼시': 32, '울버햄튼': 26, '웨스트햄': 27, '본머스': 11, '노팅엄 포레스트': 9, '에버턴': 19, '레스터': 23, '리즈': 16, '사우샘프턴': 6}

    if t1 in team and t2 in team:
        team1_score = team[t1]
        team2_score = team[t2]

        # GPT-3를 사용하여 승자, 패자 또는 무승부를 예측
        prompt = f"{t1}과 {t2} 간의 EPL에서 승자를 예측합니다."
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1,
            n=1,
            stop=["\n"]
        )
        prediction = response.choices[0].text.strip()

        if prediction.lower() == "winner":
            if team1_score > team2_score:
                st.success(t1)
            elif team1_score < team2_score:
                st.success(t2)
            else:
                st.success('무승부')
        else:
            st.error('무승부')

    else:
        st.error('정보를 입력하세요')

if __name__ == "__main__":
    main()
