# Pinyin-trans

This project provides a simple yet powerful tool for translating the pinyin of input Chinese text into other languages.
Features
Uses the pypinyin library to obtain the pinyin of Chinese text
Directly translates the pinyin to a selected language through corresponding dictionaries
Supports translation into Japanese, English, German, French, Russian, Korean, and Thai
Usage
First, install the necessary dependencies:
```shell
pip install -r requirements.txt
```
Then, you can run the program and follow the prompts to enter your text and target language:
```shell
streamlit run translator.py
```
Data Source Acknowledgment
The data used in this project for language translations is derived from the [Fyzhq repository](https://github.com/Uahh/Fyzhq) on GitHub. We greatly appreciate the original contributor for creating and sharing such valuable language resources. This has facilitated us to leverage and build upon it for our pinyin to other languages translation tool.
