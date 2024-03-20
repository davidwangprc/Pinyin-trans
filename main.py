

import sys
import json
import pypinyin
from pypinyin import pinyin
from pypinyin import lazy_pinyin
import streamlit as st

st.title('Convert Chinese to other languages')

# 加载转换表
with open('./data/language.json', encoding='utf_8') as json_file:
    language = json.load(json_file)

def translate(text, language_id):
    sentence = pypinyin.pinyin(text, style=pypinyin.NORMAL)
    result = ''
    language_dic = {'-jp': 'Japanese', '-uk': 'English', '-gm': 'German', '-fr': 'French', '-ru': 'Russian', '-kr': 'Korean', '-th': 'Thai'}
    if language_id in language_dic:
        for word in sentence:
            result += language[language_dic[language_id]].get(word[0], '') + ' '
        result = result.rstrip()  # Remove trailing spaces
    else:
        result = 'Error: Unspecified language'
    return result

# 获取用户输入的文本和语种
text = st.text_input('请输入文本:')
language_id = st.selectbox(
    '请选择语种:',
    ('-jp', '-uk', '-gm', '-fr', '-ru', '-kr', '-th')
)

# 若用户输入了文本，调用翻译函数进行处理，否则不进行处理
if text:
    result_text = translate(text, language_id)
    # st.success('翻译结果:{}'.format(result_text))
    if result_text:
        st.success(f'翻译结果: {result_text}')
    else:
        st.success('翻译结果: 没有结果')


    # 取拼音
    pinyin_list = lazy_pinyin(text)
    # 拼接拼音
    pinyin_text = ' '.join(pinyin_list)
    st.text('拼音:{}'.format(pinyin_text))
    print(translate(text, language_id))