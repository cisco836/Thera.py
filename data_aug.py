import random
import googletrans
from googletrans import Translator
import pandas as pd
from csv import writer
#data augmentation
translator = Translator()

def back_translate(sentence):
  # get a list of available languages  
  available_langs = list(googletrans.LANGUAGES.keys())
  
  # randomly pick a language
  trans_lang = random.choice(available_langs) 
  
  # print the selected language
  print(f"Translating to {googletrans.LANGUAGES[trans_lang]}")

  # translate the english sentence to selected language
  translated_sentence = translator.translate(sentence, 
                                             dest = trans_lang,
                                             src = 'en'
                                            ) 

  # back translate to english
  back_translated_sentence = translator.translate(translated_sentence.text,  
                                                  dest = 'en',src = trans_lang) 
  
  return back_translated_sentence.text


df = pd.read_csv("./20200325_counsel_chat.csv", encoding='utf-8')
temp_df = df


for i in range(len(temp_df)):
    if(i<=200):
        text=back_translate(temp_df['questionText'][i])
        text = pd.Series(text)
        label = temp_df['topic'][i]
        label = pd.Series(label)
        u_votes = temp_df['upvotes'][i]
        u_votes = pd.Series(u_votes)
        q_link = temp_df['questionLink'][i]
        q_link = pd.Series(q_link)
        sp = temp_df['split'][i]
        sp = pd.Series(sp)
        t_url = temp_df['therapistURL'][i]
        t_url = pd.Series(t_url)
        temp_df['questionText'].append(text)
        temp_df['topic'].append(label)
        temp_df['upvotes'].append(u_votes)
        temp_df['split'].append(sp)
        temp_df['questionLink'].append(q_link)
        temp_df['therapistURL'].append(t_url)
        temp_df.to_csv('20200325_counsel_chat.csv', mode='a', index=False, header=False)
        

print("Data aaugmented Successfully")

