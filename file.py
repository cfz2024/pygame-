
"""
import re

# 打开文件并读取内容
with open('D:\\py环境\\eyu\\english2\\record.txt', 'r') as file:
    content = file.read()

# 定义要查找的正则表达式模式
pattern = re.compile(r'123')  # 这里是一个简单的例子，您可以根据需要调整模式
matches = [m.start() for m in pattern.finditer(content)]
# 查找第一个匹配项并替换它


print(matches)
print(len(matches))
if len(matches) >= 2:
    # 替换第二个匹配项
    replacement = 'new_text'
    index = matches[1]
    new_content = content[:index] + replacement + content[index + len('123'):]
else:
    # 如果没有足够的匹配项，则内容保持不变
    new_content = content



#只替换一个
match = pattern.search(content)
# 注意：re.sub 默认替换所有匹配项，但我们可以使用 re.search 配合字符串操作来只替换第一个
if match:
    # 替换第一个匹配项
    replacement = 'new_text'
    new_content = content[:match.start()] + replacement + content[match.end():]

else:
    # 如果没有找到匹配项，则内容保持不变
    new_content = content


# 将修改后的内容写回文件
#with open('D:\\py环境\\eyu\\english2\\record.txt', 'w') as file:
 #   file.write(new_content)
"""

import re

# 正则表达式模式
# 匹配英语部分（一个或多个单词，由空格分隔，但不含逗号）
english_pattern = r'([a-zA-Z]+(?:\s[a-zA-Z]+)*)'
# 匹配汉语部分（一个或多个汉字，包括逗号分隔的）
chinese_pattern = r'([\u4e00-\u9fa5，]+)'
# 匹配数字部分（一个或多个数字）
number_pattern = r'(\d+)'

# 合并成一个正则表达式，用管道符 | 分隔，并允许任意字符（除了换行符）作为分隔符
combined_pattern = re.compile(rf'({english_pattern})\s+({chinese_pattern})\s+({number_pattern})', re.MULTILINE)


# 打开文件并读取内容
with open('record.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 查找所有匹配项
matches = combined_pattern.findall(content)

class words():
    def __init__(self):
        self.english=''
        self.chinese=''
        self.grade=''
# 处理找到的匹配项
words_list=[]

for match in matches:
    english_word = match[0]
    chinese_translation = match[2]
    grade=match[4]

    #new_txt=english_word+" "+chinese_translation+grade+"\n"
    new_word = words()
    new_word.english=english_word
    new_word.chinese=chinese_translation
    new_word.grade=grade
    #print(new_word.english,new_word.chinese,new_word.grade)

    words_list.append(new_word)

def refreash_word_list():
    words_list.clear()
    # 打开文件并读取内容
    with open('record.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    # 查找所有匹配项
    matches = combined_pattern.findall(content)
    for match in matches:
        english_word = match[0]
        chinese_translation = match[2]
        grade = match[4]

        # new_txt=english_word+" "+chinese_translation+grade+"\n"
        new_word = words()
        new_word.english = english_word
        new_word.chinese = chinese_translation
        new_word.grade = grade
        # print(new_word.english,new_word.chinese,new_word.grade)

        words_list.append(new_word)
    #with open('vocabulary.txt','w',encoding='utf-8') as file:
        #file.write(new_txt)
#for member in words_list:
   # print(member.english,member.chinese,member.grade)
    '''
    # 假设 match 是从 re.findall() 得到的匹配项
    split_result = match.split(maxsplit=1)
    print(match)
    # 检查 split_result 是否包含两个元素
    if len(split_result) == 2:
        english_word, chinese_translation = match.split(maxsplit=1)
        print(f"英语单词: {english_word}, 汉译: {chinese_translation}")
    else:
        print('error')'''