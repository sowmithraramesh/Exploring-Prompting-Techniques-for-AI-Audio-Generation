def generate_sound_effect(prompt):
url = "https://api-inference.huggingface.co/models/sound-effect-model"
headers = {"Authorization": f"Bearer your_huggingface_api_key"}
payload = {"inputs": prompt}
response = requests.post(url, headers=headers, json=payload)
print("Sound Effect URL:", response.json().get("audio_url", "No URL"))
