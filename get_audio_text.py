import requests
import json
import time

#Get api key from https://console.cloud.google.com/apis/credentials?project=adx-service
YOURAPIKEYHERE = "GET_API_KEY_FROM_YOUR_APIS_LINK"

url = "https://speech.googleapis.com/v1/speech:longrunningrecognize?key={}".format(YOURAPIKEYHERE)

print url

# Change uri of the file location
payload = {
    "config": {
      "encoding": "FLAC",
      "language_code": "en-US"
    },
    "audio": {
        "uri": "gs://xera/tensorflow_siraj.flac"
    }
}

filename = payload['audio']['uri'].split('/')[-1].split('.')[0]

r = requests.post(url, data=json.dumps(payload))
json_resp = r.json()
print json_resp

token_resp = json_resp['name']
print token_resp

url = "https://speech.googleapis.com/v1/operations/" + str(token_resp) + "?key=" + YOURAPIKEYHERE

output=''

while True:
    try:
        content_response = requests.get(url)
        content_json = content_response.json()

        for line in content_json['response']['results']:
          for t in line['alternatives']:
            output = output +  t['transcript'] + '\n'
    except:
        print 'Wait for 10 seconds for audio detection...'
        time.sleep(10)
        continue
    break

with open('audio_detection_output_{0}.txt'.format(filename), 'w') as f:
    f.write(output)

print 'Finished writing audio detection ouput to file audio_detection_output_{0}.txt'.format(filename)
