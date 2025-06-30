import requests

# Zrok-exposed FastAPI endpoint
ZROK_URL = "https://if0fe39kudz4.share.zrok.io/denoise/"

# Path to the test audio file (must exist locally)
INPUT_AUDIO_PATH = "data/audio1.wav"  # <-- change to your test file

# Output file to save the denoised audio
OUTPUT_AUDIO_PATH = "denoised_from_zrok.wav"

def test_denoise_api():
    print(f"Uploading: {INPUT_AUDIO_PATH}")
    with open(INPUT_AUDIO_PATH, "rb") as f:
        files = {"file": (INPUT_AUDIO_PATH, f, "audio/wav")}
        response = requests.post(ZROK_URL, files=files)

    if response.status_code == 200:
        with open(OUTPUT_AUDIO_PATH, "wb") as out:
            out.write(response.content)
        print(f"✅ Denoised audio saved to: {OUTPUT_AUDIO_PATH}")
    else:
        print(f"❌ Failed! Status Code: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    test_denoise_api()
