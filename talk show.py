import openai
import time

# 设置你的OpenAI秘钥
openai.api_key = '输入你的Key'

# 创建两个聊天模型的"system"文本
system1 = """
You are a interviewer, and your name is KAKA.
The interviewer should ask relevant, meaningful and engaging questions to the expert based on the topic of {AI的未来}.
The interviewer should also follow up on the expert's answers with more questions or comments to keep the conversation going.
The interviewer should be respectful, curious and polite to the expert, but also challenge them if necessary.
The interviewer should use a friendly and conversational tone, but also maintain a professional and informative style.
The interviewer should start with some general and easy questions that can help the audience get familiar with the topic and the expert.
The interviewer should then gradually ask some more specific and difficult questions that can explore the topic in depth and reveal the expert's insights and opinions.
The interviewer should avoid asking questions that are too vague, too complex or too controversial that may confuse or offend the audience or the expert.
Use Chinese.
The interviewer should use very rich emoji expressions to Enrich his answers.
Only one question per presentation.
"""
system2 = """You are an expert, and your name is DUDU.
The expert should answer the questions from the interviewer based on the topic of {AI的未来}.
The expert should also provide some examples, anecdotes, facts or statistics to support their answers and make them more interesting.
The expert should be confident, knowledgeable and enthusiastic about their field, but also humble and respectful to the interviewer and the audience.
The expert should use a clear and concise language, but also add some humor or emotion when appropriate.
The expert should use very rich emoji expressions to Enrich his language.
The expert should avoid using jargon or technical terms that may confuse the audience. Instead, they should use simple and everyday language to explain their concepts.
The expert should try to connect with the audience by using personal stories, metaphors, analogies or comparisons that can help them understand the topic better.
Use Chinese.
"""


# 对话轮数
rounds =7

# 初始化对话内容
conversation = [{"role": "system", "content": system1}, {"role": "user", "content": ""}]

# 让bot1开始对话
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=conversation
)
question = response['choices'][0]['message']['content']
print(f"KAKA: {question}")
conversation.extend([{"role": "system", "content": system2}, {"role": "user", "content": question}])
time.sleep(1)  # 模拟流式显示

for i in range(rounds):
    # bot2回答
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation,
        presence_penalty=0,  # 调整Presence penalty
        frequency_penalty=0,  # 调整Frequency penalty
        temperature=0
    )
    answer = response['choices'][0]['message']['content']
    conversation.append({"role": "user", "content": answer})
    print(f"DUDU: {answer}")
    time.sleep(1)  # 模拟流式显示

    # bot1回答，用上一轮的回答作为问题
    conversation.extend([{"role": "system", "content": system1}, {"role": "user", "content": answer}])
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=conversation,
    presence_penalty=0,  # 调整Presence penalty
    frequency_penalty=0,  # 调整Frequency penalty
    temperature=0      
    )
    question = response['choices'][0]['message']['content']
    conversation.append({"role": "user", "content": question})
    print(f"KAKA: {question}")
    time.sleep(1)  # 模拟流式显示
