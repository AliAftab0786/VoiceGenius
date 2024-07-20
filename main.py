from utills import *
def recognize_speech_from_mic():
    # Initialize the recognizer
    r = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise. Please wait...")
        r.adjust_for_ambient_noise(source, duration=2)  # Longer duration for noise adjustment

        print("Listening...")
        try:
            # Adjust timeout and phrase limit based on your testing
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return
        
    # Recognize speech using Google's free web API
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def speak(text , voice='Samantha'):
    try:
        # Using subprocess.run to avoid shell-related issues
        subprocess.run(['say', '-v', voice, text])
        print("Command executed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

inputtext=recognize_speech_from_mic()

API_KEY = 'Use-your-gemini-API-key'
URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}'

# Data to be sent to the API
data = {
    "contents": [
        {
            "parts": [
                {"text": f"{inputtext}"}
            ]
        }
    ]
}

# Set the headers
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(URL, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()
    print("Response from API:")
    print(response_data)
    
    # Extracting the text value
    if 'candidates' in response_data and len(response_data['candidates']) > 0:
        text_value = response_data['candidates'][0]['content']['parts'][0]['text']
        print("\nExtracted text value:")
        print(text_value)
        speak(text_value)
    else:
        print("No candidates found in the response.")
else:
    print(f"Failed to get response. Status code: {response.status_code}")
    print("Response text:")
    print(response.text)