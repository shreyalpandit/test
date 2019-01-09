from __future__ import print_function
import time
import deepaffects
from deepaffects.rest import ApiException
from pprint import pprint
# import pydub
# from pydub import AudioSegment


# Configure API key authorization: UserSecurity
deepaffects.configuration.api_key['apikey'] = '3RVW9BCSGBdZxhGZSdwlGe8F9qcLnGtA'

# sound = pydub.AudioSegment.from_mp3("/Users/shreyalpandit/Desktop/sample.mp3")
# sound.export("/Users/shreyalpandit/Desktop/sample.wav", format="wav")

file = "/Users/shreyalpandit/Desktop/sample.wav"
# create an instance of the API class
api_instance = deepaffects.DiarizeApiV2()
body = deepaffects.DiarizeAudio.from_file("/Users/shreyalpandit/Desktop/sample.wav") # DiarizeAudio | Audio object that needs to be diarized.
webhook = 'https://webhook.site/224858ac-865c-4fcc-9684-3bcd1922ec6d' # str | The webhook url where result from async resource is posted
# request_id =

try:
    api_response = api_instance.async_diarize_audio(body, webhook) # , request_id=request_id
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiarizeApiV2->async_diarize_audio: %s\n" % e)