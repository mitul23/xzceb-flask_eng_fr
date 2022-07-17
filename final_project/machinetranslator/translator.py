"""translator"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(entext):
    """
    This function translate english to french
    """
    if entext=='':
        return 'Empty'

    entext = language_translator.translate(entext, 
model_id='en-fr').get_result()
    return entext.get('translations')[0].get('translation')

def frenchToEnglish(frtext):
    """
    This function translate french to english
    """
    if frtext=='':
        return 'Empty'
    frtext = language_translator.translate(frtext, 
model_id='fr-en').get_result()
    return frtext.get('translations')[0].get('translation')


#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))
#print(englishToFrench("Hello"))
#print(frenchToEnglish("Bonjour"))

