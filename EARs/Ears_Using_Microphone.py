print("\033c")
import speech_recognition as sr
import whisper
print('Whisper is working!')

def listen_to_user():
    languages = [
    "ar-SA",
    "en-US",
    "es-ES",
    ]
    recognizer = sr.Recognizer()
    # recognizer.energy_threshold = 250
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("\nCalibrating microphone for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(f"Calibration complete. Energy threshold set to {recognizer.energy_threshold}.")
        print("\nYou can speak now.")

        # recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            recognizer.pause_threshold = 2.5
            recognizer.phrase_threshold = 0.3
            recognizer.non_speaking_duration = 0.5
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=None)
            print("Processing Audio ...")

            # for language in languages:
            #     try:
            #         text = recognizer.recognize_google(
            #             audio_data,
            #             language = language
            #         )
            #         print(f"[{language}]: {text}")
            #     except sr.UnknownValueError:
            #         print(f"[Sorry, I could not understand the audio in {language}.]")

            text = recognizer.recognize_whisper(audio_data)

            # text = recognizer.recognize_google(audio_data)
            # print(f"You said {text}.")
            return text
        except sr.WaitTimeoutError:
            print("[No audio captured, did you speak?]")
            return None
        except sr.UnknownValueError:
            print("[Sorry, I could not understand the audio.]")
            return None
        except sr.RequestError as e:
            print(f"[Error connecting to speech recognition service: {e}]")
            return None

if __name__ == "__main__":

    for time in range(3):
        sentence = listen_to_user()
        print(f"Sentence {time + 1}: {sentence}")

# so now tell why and when should i create a repository and what is should be used for, and what if i have many projects i want to bublish them and tell me when i should create another repository and what it should includes??
