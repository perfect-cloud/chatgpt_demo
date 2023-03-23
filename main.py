# This is a sample Python script.
import os
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import json


def get_api_key():
    '''
    {"api": "你的 api keys"}
    '''
    openai_key_file = './apikey.json'
    with open(openai_key_file, 'r', encoding='utf-8') as f:
        openai_key = json.loads(f.read())
    return openai_key['api']


openai.api_key = get_api_key()
# print(openai.api_key)


# respeonse = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )


def test():
    q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
    respeonse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"},
            {"role": "user", "content": q}
        ]
    )
    print(respeonse.get("choices")[0]["message"]["content"])


class ChatGPT:
    def __init__(self, user):
        self.user = user
        self.messages = [{"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"}]
        self.filename = "./user_message.json"

    def ask_gpt(self):
        # q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
        rsp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        return rsp.get("choices")[0]["message"]["content"]

    def writeTojson(self):
        try:
            # 判断文件是否存在
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as f:
                    # 创建文件
                    pass
            # 读取
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                msgs = json.loads(content) if len(content) > 0 else {}
            # 追加
            msgs.update({self.user: self.messages})
            # 写入
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(msgs, f)
        except Exception as e:
            print(f"错误代码：{e}")


def main():
    user = input("请输入用户名称: ")
    chat = ChatGPT(user)
    # 循环
    while 1:
        # 限制对话次数
        if len(chat.messages) >= 11:
            print("************************************")
            print("******************强制重置对话******************")
            print("************************************")
            # 写入之前信息
            chat.writeTojson()
            user = input("请输入用户名称: ")
            chat = ChatGPT(user)
        # 提问
        q = input(f"【{chat.user}】")
        # 逻辑判断
        if q == "0":
            print("*********退出程序*********")
            # 写入之前信息
            chat.writeTojson()
            break
        elif q == "1":
            print("******************")
            print("*********重置对话*********")
            print("******************")
            # 写入之前信息
            chat.writeTojson()
            user = input("请输入用户名称: ")
            chat = ChatGPT(user)
            continue

        # 提问-回答-记录
        chat.messages.append({"role": "user", "content": q})
        answer = chat.ask_gpt()
        print(f"【ChatGPT】{answer}")
        chat.messages.append({"role": "assistant", "content": answer})


if __name__ == '__main__':
    main()
