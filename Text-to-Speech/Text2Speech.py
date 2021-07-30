from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



apikey = 'RqPKu4qmYCObGYOxUXeEcZrK8xLaAx_Vv4eGAyXgarRJ'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/6230d00c-ed46-4e7c-b78b-3a1693a427cf'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


def readText(filename):
    with open(filename+'.txt', 'r') as f:
        text = f.readlines()
    text = [line.replace('\n','') for line in text]
    text = ''.join(str(line) for line in text)
    return text

text=readText("text")

with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_LisaV3Voice').get_result()
    audio_file.write(res.content)