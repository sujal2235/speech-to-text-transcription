import speech_recognition as sr

def transcribe_from_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("✅ Ready! Speak something...")
        audio = recognizer.listen(source)

    try:
        print("📝 Transcribing...")
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)

        # Save to a file
        with open("transcription.txt", "w") as f:
            f.write(text)

        print("📂 Transcription saved to 'transcription.txt'")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")


def transcribe_from_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("🎶 Reading audio file...")
        audio = recognizer.record(source)

    try:
        print("📝 Transcribing...")
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)

        # Save to file
        with open("transcription.txt", "w") as f:
            f.write(text)

        print("📂 Transcription saved to 'transcription.txt'")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")


if __name__ == "__main__":
    print("Choose an option:")
    print("1. 🎤 Record from Microphone")
    print("2. 🎶 Transcribe from Audio File")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        transcribe_from_microphone()
    elif choice == "2":
        file_path = input("Enter audio file path (wav/mp3): ")
        transcribe_from_audio(file_path)
    else:
        print("❌ Invalid choice")
