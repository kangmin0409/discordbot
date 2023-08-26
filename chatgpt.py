import openai

# API 키 설정
openai.api_key = '<youtapikey>' #chatgpt 웹에서 발급 가능

# ChatGPT에 요청 보내기
response = openai.Completion.create(
  engine='text-davinci-003',  # ChatGPT 모델 선택
  prompt='What is the meaning of life?',  # 대화 시작 문장
  max_tokens=50  # 생성할 최대 토큰 수
)

# 응답 출력
print(response.choices[0].text.strip())
