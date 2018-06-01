import requests
import json
import time

#Get api key from https://console.cloud.google.com/apis/credentials?project=adx-service
YOURAPIKEYHERE = ""

url = "https://vision.googleapis.com/v1/images:annotate?key={}".format(YOURAPIKEYHERE)

print url

# Change uri of the file location
payload = {
  "requests": [
  {
    "image": {
      "source": {
        "imageUri": "gs://xera/test4.jpeg"
      }
    },
    "features": {
        "type": "TEXT_DETECTION"
    }
  }
  ]
}


r = requests.post(url, data=json.dumps(payload))
json_resp = r.json()
print json_resp['responses'][0]['textAnnotations'][0]['description']

#for text in json_resp['responses'][0]['textAnnotations']:
#  print text['description']


