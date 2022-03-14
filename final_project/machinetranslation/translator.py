"""This program implements IBM's Language translator to translate
    a user input from eng to french or vice versa"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey_lt = os.environ['apikey']
url_lt = os.environ['url']

VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url_lt)

def main():
    """main function"""

    english_to_french(input)
    french_to_english(input)

def english_to_french(english_text):    
    """This function translates english to french."""
    
    translation = language_translator.translate(
    text= english_text,
    model_id='en-fr').get_result()
    french_text = json.dumps(translation)
    split_json_file = french_text.split(',')
    split_json_file_1 = split_json_file[0]
    split_json_file_2 = split_json_file_1.split(':')
    split_json_file_3 = split_json_file_2[2]
    split_json_file_4 = split_json_file_3.split('"')
    final_output = split_json_file_4[1]
    print(final_output)
    return final_output
def french_to_english(french_text):   
    """This function translates french to english."""
    
    translation = language_translator.translate(
    text= french_text,
    model_id='fr-en').get_result()
    english_text = json.dumps(translation)
    split_json_file = english_text.split(',')
    split_json_file_1 = split_json_file[0]
    split_json_file_2 = split_json_file_1.split(':')
    split_json_file_3 = split_json_file_2[2]
    split_json_file_4 = split_json_file_3.split('"')
    final_output = split_json_file_4[1]
    print(final_output)
    return final_output

main()