import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

print("🎙️ Voice command mode started — say 'start' or 'stop' (Ctrl+C to exit)")

while True:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("\n🔄 Listening...")
        audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio).lower()
        print("✅ You said:", text)

        if "start" in text:
            print("🟢 ACTION: Start command detected")

        elif "stop" in text:
            print("🔴 ACTION: Stop command detected")

        else:
            print("ℹ️ Command not recognized. Say 'start' or 'stop'.")

    except sr.UnknownValueError:
        print("❌ Didn't catch that. Try again.")
    except sr.RequestError as e:
        print(f"⚠️ Google API error: {e}")
