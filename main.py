import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# 모델 및 프롬프트 템플릿 설정
template = """
아래 질문에 답변하세요.

대화 기록:{context}

질문:{question}

답변:
"""

model = OllamaLLM(model="bnksys/yanolja-eeve-korean-instruct-10.8b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit 애플리케이션
def main():
    # 페이지 제목 및 사이드바 설정
    st.set_page_config(page_title="학습 보조 AI", layout="wide")
    
    st.sidebar.header("학습 보조 AI")
    st.sidebar.write("궁금한 교과 내용을 질문해 보세요.")

    # 사이드바에 추가 기능
    st.sidebar.subheader("도움말")
    st.sidebar.write("이 앱은 교과 내용에 대해 질문하고 답변을 받는 데 도움을 줍니다.")
    st.sidebar.write("사용 방법: 질문을 입력하고 '전송' 버튼을 클릭하여 답변을 받으세요.")
    
    st.sidebar.subheader("참고사항")
   
    st.sidebar.write("- 대화 기록은 현재 세션에서만 유지됩니다.")
    st.sidebar.write("- 교과 내용 외의 질문에는 원하는 답을 얻기 힘들 수 있습니다.")
   

    st.title("학습 보조 AI")
    st.markdown("<h2 style='text-align: center;'>교과 내용 질문&응답</h2>", unsafe_allow_html=True)
    
    if 'context' not in st.session_state:
        st.session_state.context = ""

    # 입력 폼 및 버튼 배치
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input("질문을 입력하세요:", placeholder="입력란")

    with col2:
        if st.button("전송"):
            if user_input:
                result = chain.invoke({"context": st.session_state.context, "question": user_input})
                st.session_state.context += f"\n나: {user_input}\n학습 도우미: {result}"
                st.write("AI 답변:", result)
            else:
                st.write("질문을 입력해 주세요.")

if __name__ == "__main__":
    main()
