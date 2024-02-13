import speech_recognition as sr

def audio_to_text(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        # Use recognizer to convert audio to text
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Error: {0}".format(e)

if __name__ == "__main__":
    # Example usage
    audio_file = "C:\\Users\\.wav"  # Replace with your audio file path
    result = audio_to_text(audio_file)
    print("Text from audio:", result)
