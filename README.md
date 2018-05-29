# audio-detection-translation

$ virtualenv env
$ source env/bin/activate

1. Upload audio flac file to google storageo https://console.cloud.google.com/storage/browser/xera?project=adx-service
2. Change gs file link in get_audio_text.py
3. python get_audio_text.py 
4. Get the print filename and run 'python get_translation.py filename'  
5. The translation is stored in output file
