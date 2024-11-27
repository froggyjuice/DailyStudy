from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 1. 모델과 토크나이저 불러오기
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 2. 사용자 입력 받기
topic = input("주제를 입력하세요: ")
keywords = input("키워드를 입력하세요 (쉼표로 구분): ")

# 3. 프롬프트 생성
prompt = f"주제: {topic}\n키워드: {keywords}\n\n내용:\n"

# 4. 입력을 모델에 전달하기
inputs = tokenizer.encode(prompt, return_tensors="pt")
outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.95, temperature=0.7)

# 5. 결과 출력
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("\n생성된 텍스트:")
print(generated_text)