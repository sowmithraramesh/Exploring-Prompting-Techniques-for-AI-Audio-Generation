import requests
API_KEY = "your_google_api_key"
url = "https://texttospeech.googleapis.com/v1/text:synthesize"
def generate_speech(prompt):
headers = {"Authorization": f"Bearer {API_KEY}"}
payload = {
"input": {"text": prompt},
"voice": {"languageCode": "en-US", "name": "en-US-Wavenet-D"},
"audioConfig": {"audioEncoding": "MP3"}
}
response = requests.post(url, headers=headers, json=payload)
if response.status_code == 200:
with open("speech.mp3", "wb") as file:
file.write(response.content)
print("Speech generated: speech.mp3")
else:
print("Error in generation:", response.json())
