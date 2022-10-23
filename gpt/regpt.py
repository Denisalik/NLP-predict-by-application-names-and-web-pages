import pandas as pd
import openai
import time

api_key = ''

openai.api_key = api_key
model = 'gpt-3.5-turbo'
categories = ['Utilities', 'Entertainment', 'Development', 'Communication', 'Management', 'Education', 'Design/Creativity']
categories_str = ', '.join(categories)
pattern = f"Categorize the text by following 7 categories: {categories_str}. Text is: "

df = pd.read_csv('../data/tagged.csv', sep='\t', index_col='id')

def categorize(text: pd.Series) -> str:
    if isinstance(text['Category'], str):
        for category in categories:
            if category in text['Category']:
                return category
    messages = [
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": pattern + text['browser_title']}
    ]
    try:
        time.sleep(3)
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        answer = '|'.join([choice.message.content for choice in response.choices])
        return apply(answer)
    except:
        return ''

def apply(x: any):
    if not isinstance(x, str):
        return ''
    for category in categories:
        if category in x:
            return category
    return ''
df['Category'] = df[['browser_title', 'Category']].apply(lambda x: categorize(x), axis=1)
df.to_csv('../data/tagged.csv', sep='\t')