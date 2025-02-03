import requests
API_KEY git commit = "your_huggingface_api_key"
url = "https://api-inference.huggingface.co/models/facebook/musicgen"
def generate_music(prompt):
headers = {"Authorization": f"Bearer {API_KEY}"}
payload = {"inputs": prompt}
response = requests.post(url, headers=headers, json=payload)
audio_url = response.json().get("audio_url", "No URL")
print("Generated Music URL:", audio_url)
