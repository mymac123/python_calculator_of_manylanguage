import json

# 加载语言文件
def load_languages():
with open('的语言s.json ', 'r', encoding='utf-8') as file:
        return json.load (file)

# 显示当前语言
def show当前语言(languages):
print(languages['当前语言'])

# 切换语言
def 切换语言(languages, current_language):
new_language = input("请输入新的语言代码（例如：zh, tw, en等）：")
if new_language in languages:
        current_language = new_language
        print(f"已切换到 {当前语言}")
else:
        print("无效的语言代码，请重新输入。")
return current_language

# 主函数
def 主():
languages = load_languages()
current_language = 'en'  # 默认使用英语

while True:
        user_input = input("输入计算表达式或命令（language, help, about）：")

        if user_input == 'language':
            current_language = 切换语言(languages, current_language)
        elif user_input == 'help':
            print(languages[current_language]['帮助'])
        elif user_input == 'about':
            print(languages[current_language]['关于'])
        else:
            try:
                result = 计算表达式(user_input)
                print(f"结果：{result}")
            except Exception as e:
                print(f"错误：{e}")

# 计算表达式函数
def 计算表达式表达式):
try:
        return str(eval(表达式))
except Exception as e:
        return str(e)

# 主运行
if __name__ == "__main__":
主()
