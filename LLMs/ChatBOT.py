# things must to do : 
# use BytesIO instead of saving the audio to a file, and then play it directly from memory. This will avoid the need to write to disk and can improve performance.
# fix the mic performance issue by adjusting the energy threshold and dynamic energy threshold settings in the speech recognition library. This can help reduce background noise and improve the accuracy of speech recognition.
# do this "loop = asyncio.new_event_loop()" instead of asyncio.run(generate_speech())
# do this pygame.quit() to end pygame.mixer.init()
# fix that Bella forget everything after a while, and she should remember everything that I said to her
# add conversation=[] , conversation.append(...) for the memory of the conversation, and pass it to the ollama.chat() function as messages=conversation
# make a queue for the voice in speak() function, so that if the user speaks while Bella is still speaking, it will queue the next response and play it after the current one finishes.
# use print("\033c") or rich or textual instead of os.system('cls') to clear the console, as it is more efficient and works across different platforms.
# do this "if "writing" in user_input.lower():" instead of "if user_input == "writing" or actual_text == "writing":"
# do this "if "talking" in user_input.lower():" instead of "if user_input == "talking" or actual_text == "talking":"
# change this "any(cmd in user_input.lower()" using "==" or "startswith()"
# remove the "actual_text" variable and its related code, as it is not used in the current implementation.
# there isn't Interrupt so if bella is talking, i should wait till she finishes.
# there isn't "Threading." everything is sequential, so if bella is talking, i should wait till she finishes.
# i should add memory and history and context 
# try to make "Wake Word".
# try to make  bella controll the system and do some tasks like open apps, open websites, search on google, search on youtube, search on wikipedia, search on wolframalpha, search on bing, search on duckduckgo, search on yahoo, search on baidu, search on yandex, search on ecosia, search on qwant, search on startpage, search on dogpile, search on gigablast, search on webcrawler, search on info.com, search on metacrawler, search on ixquick, search on zapmeta, search on entireweb, search on hotbot, search on lycos, search on excite, search on altavista, search on alltheweb, search on infoseek, search on magellan, search on webcrawler2.0
# make  bella search in the internet.
# make  bella able to read screen "Screen Reader"
# make bella to memorize user Personality.
# in the end make bella an amazing agent
# get the code (OOP)

# speak("Hello my dear! Your lovely AI assistant Bella is ready to Talk to you, just talk to me!")
# # time.sleep(1)
# speak("Hello durling .. oh I love you so much, I am your assistant, I am your friend, I am your love, I am your everything, and also .. I am your Bella.")

# def speak(text):
#     print(f"🤖: {text}")
#     engine = pyttsx3.init() 
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.setProperty('rate', 165)
#     engine.setProperty('volume', 1.0)
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()
#     del engine

Version: 1.0
# import os
# os.system('cls')
# # os.system("cls" if os.name == "nt" else "clear")

# from deep_translator import GoogleTranslator
# import speech_recognition as sr
# import pyttsx3
# import ollama
# import time
# import json
# import asyncio
# import edge_tts
# import pygame

# pygame.mixer.init()
# os.system('cls')

# def speak(text):
#     print(f"🤖 BOT: ", end="")
#     print(f"{text}")
    
#     voice_name = "en-US-AvaNeural" 
#     output_file = "response.mp3"

#     custom_rate = "-24%"
#     custom_volume = "+0%"
#     custom_pitch = "+7Hz"
    
#     async def generate_speech():
#         communicate = edge_tts.Communicate(
#             text,
#             voice_name,
#             rate=custom_rate,
#             volume=custom_volume,
#             pitch=custom_pitch
#         )
#         await communicate.save(output_file)
#     asyncio.run(generate_speech())
#     try:
#         pygame.mixer.music.load(output_file)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#         pygame.mixer.music.unload()
#     except Exception as e:
#         print(f"error via listening: {e}")

# speak("Hello my dear! Your lovely AI assistant Bella is ready to Talk to you, just talk to me!")
# # # time.sleep(1)
# # speak("Hello durling .. oh I love you so much, I am your assistant, I am your friend, I am your love, I am your everything, and also .. I am your Bella.")

# # def speak(text):
# #     print(f"🤖: {text}")
# #     engine = pyttsx3.init() 
# #     voices = engine.getProperty('voices')
# #     engine.setProperty('voice', voices[1].id)
# #     engine.setProperty('rate', 165)
# #     engine.setProperty('volume', 1.0)
# #     engine.say(text)
# #     engine.runAndWait()
# #     engine.stop()
# #     del engine

# recognizer = sr.Recognizer()
# recognizer.energy_threshold = 75
# # recognizer.dynamic_energy_threshold = True

# def listen_to_user():
#     with sr.Microphone() as source:
#         print(f"I AM LISTENING RIGHT NOW, Just SPEAK...")
#         recognizer.adjust_for_ambient_noise(source, duration=1.0)
        
#         try:
#             audio = recognizer.listen(source, timeout=7.5, phrase_time_limit=15)
#         except sr.WaitTimeoutError:
#             speak("Sorry, I didn't hear anything. Please try again.")
#             time.sleep(0.5)
#             return None

#         try:
#             user_text = recognizer.recognize_vosk(audio)
#             if not user_text or not user_text.strip():
#                 speak("Sorry, I didn't catch that. Please try again.")
#                 time.sleep(0.5)
#                 return None
#             try:
#                 result_dict = json.loads(user_text)
#                 actual_text = result_dict.get("text", "")
#             except json.JSONDecodeError:
#                 actual_text = user_text
#             if actual_text.strip():
#                 os.system('cls')
#                 print(f"👤 Me: {actual_text}")
#                 return actual_text
#             else:
#                 speak("Sorry, I didn't catch that. Please try again.")
#                 time.sleep(0.5)
#                 return None
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand what you said, Please try again.")
#             time.sleep(1)
#             os.system('cls')
#             return None
#         except sr.RequestError:
#             speak("Sorry, there is an issue with your internet connection. Please try again later.")
#             return exit()

# def ask_llm(user_prompt):
#     try:
#         response = ollama.chat(
#             model='qwen3:4b',
#             messages=[
#                 {
#                     'role': 'system', 
#                     'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).'
#                 },
#                 {
#                     'role': 'user', 
#                     'content': user_prompt
#                 }
#             ],
#             stream=True
#         )

#         print("", end="", flush=True)
#         full_response = ""
#         for chunk in response:
#             word = chunk['message']['content']
#             print(word, end="", flush=True)
#             full_response += word
#         print()

#         return full_response
#     except Exception as e:
#         return f"Sorry, I encountered an issue connecting to the local AI: {e}"

# def main():
#     speak("Hello! I'm Bella Your natural AI assistant. I'm ready to talk with you, just start talk to me!")
#     time.sleep(0.5)
#     os.system('cls')
    
#     while True:
#         user_input = listen_to_user()
#         EXIT_COMMANDS = {
#             "exit", "quit",
#             "stop", "shutdown",
#             "shut down", "turn off",
#             "end", "done"
#         }
#         if user_input:
#             if any(cmd in user_input for cmd in EXIT_COMMANDS):
#                 speak("Program closed. Goodbye! .. See you later darling!")
#                 break
            
#             speak("Thinking Right Now .. With All LOVE, Please Wait...")
#             bot_response = ask_llm(user_input)
#             clean_response = bot_response.replace("*", "")
#             speak(clean_response)
#             print()
            
# if __name__ == "__main__":
#     main()
# =======================================================================================================================
Version: 2.0
# import os
# os.system('cls')
# # os.system("cls" if os.name == "nt" else "clear")

# from deep_translator import GoogleTranslator
# import speech_recognition as sr
# import pyttsx3
# import ollama
# import time
# import json
# import asyncio
# import edge_tts
# import pygame

# pygame.mixer.init()
# os.system('cls')

# def speak(text):
#     print(f"👤 (Bella): ", end="")
#     print(f"{text}")
    
#     voice_name = "en-US-AvaNeural" 
#     output_file = "response.mp3"

#     custom_rate = "-24%"
#     custom_volume = "+0%"
#     custom_pitch = "+7Hz"
    
#     async def generate_speech():
#         communicate = edge_tts.Communicate(
#             text,
#             voice_name,
#             rate=custom_rate,
#             volume=custom_volume,
#             pitch=custom_pitch
#         )
#         await communicate.save(output_file)
#     asyncio.run(generate_speech())
#     try:
#         pygame.mixer.music.load(output_file)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#         pygame.mixer.music.unload()
#     except Exception as e:
#         print(f"error via listening: {e}")

# # speak("Hello my dear! Your lovely AI assistant Bella is ready to Talk to you, just talk to me!")
# # # time.sleep(1)
# # speak("Hello durling .. oh I love you so much, I am your assistant, I am your friend, I am your love, I am your everything, and also .. I am your Bella.")

# # def speak(text):
# #     print(f"🤖: {text}")
# #     engine = pyttsx3.init() 
# #     voices = engine.getProperty('voices')
# #     engine.setProperty('voice', voices[1].id)
# #     engine.setProperty('rate', 165)
# #     engine.setProperty('volume', 1.0)
# #     engine.say(text)
# #     engine.runAndWait()
# #     engine.stop()
# #     del engine

# recognizer = sr.Recognizer()
# recognizer.energy_threshold = 75
# recognizer.dynamic_energy_threshold = True

# def listen_to_user():
#     with sr.Microphone() as source:
#         print(f"LISTENING RIGHT NOW, Just SPEAK...")
#         recognizer.adjust_for_ambient_noise(source, duration=1.0)
        
#         try:
#             audio = recognizer.listen(source, timeout=7.5, phrase_time_limit=15)
#         except sr.WaitTimeoutError:
#             speak("Sorry, I didn't hear anything. Please try again.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None

#         try:
#             user_text = recognizer.recognize_vosk(audio)
#             if not user_text or not user_text.strip():
#                 speak("Sorry, I didn't catch that. Please try again.")
#                 time.sleep(0.5)
#                 os.system('cls')
#                 return None
#             try:
#                 result_dict = json.loads(user_text)
#                 actual_text = result_dict.get("text", "")
#             except json.JSONDecodeError:
#                 actual_text = user_text
#             if actual_text.strip():
#                 os.system('cls')
#                 print(f"👤 (Me): {actual_text}")
#                 return actual_text
#             else:
#                 speak("Sorry, I didn't catch that. Please try again.")
#                 time.sleep(0.5)
#                 os.system('cls')
#                 return None
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand what you said, Please try again.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None
#         except sr.RequestError:
#             speak("Sorry, there is an issue with your internet connection. Please try again later.")
#             os.system('cls')
#             return exit()

# def ask_llm(user_prompt):
#     try:
#         response = ollama.chat(
#             model='qwen3:0.6b',
#             messages=[
#                 {
#                     'role': 'system', 
#                     'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).'
#                 },
#                 {
#                     'role': 'user', 
#                     'content': user_prompt
#                 }
#             ],
#             stream=True
#         )

#         # print("", end="", flush=True)
#         full_response = ""
#         # os.system('cls')
#         for chunk in response:
#             word = chunk['message']['content']
#             print(word, end="", flush=True)
#             full_response += word
#             # time.sleep(0.5)
#         # os.system('cls')
#         # print()

#         return full_response
#     except Exception as e:
#         return f"Sorry, I encountered an issue connecting to the local AI: {e}"

# def main():
#     # speak("Hello! I'm Bella Your natural AI assistant. I'm ready to talk with you, just start talk to me!")
#     speak("Hello! I'm Bella Your natural AI assistant.")
#     # speak("I'm ready to talk with you, just start talk to me!")
#     print()
#     # time.sleep(0.5)
#     # os.system('cls')
    
#     current_mode = "talking"
#     voice_counter = 0

#     while True:
#         user_input = None
#         actual_text = None

#         if current_mode == "talking":
#             user_input = listen_to_user()

#             if user_input is not None or actual_text is not None:
#                 if user_input == "writing" or actual_text == "writing":
#                     current_mode = "writing"
#                     voice_counter = 0
#                     speak(f"Manually switched to (Writing Mode).")
#                     continue
                
#             elif user_input == None or actual_text == None:
#                 voice_counter += 1
#                 if voice_counter >= 3:
#                     current_mode = "writing"
#                     speak(f"Automatically switched to (Writing Mode).")
#                 else:
#                     continue
            
#         elif current_mode == "writing":
#             user_input = input("👤 Me (Writing): ").strip()
#             if user_input.lower().strip() == "tm":
#                 current_mode = "talking"
#                 voice_counter = 0
#                 speak(f"Switching back to (Talking Mode). I am listening!")
#                 continue

#             if user_input:
#                 pass

#         EXIT_COMMANDS = {
#             "exit", "quit",
#             "stop", "shutdown",
#             "shut down", "turn off",
#             "end", "done"
#         }
#         if user_input:
#             if any(cmd in user_input.lower() for cmd in EXIT_COMMANDS):
#                 speak("Program closed. Goodbye! .. See you later durling!")
#                 os.system('cls')
#                 break
            
#             speak("Thinking Right Now .. With All LOVE, Please Wait...")
#             bot_response = ask_llm(user_input)
#             clean_response = bot_response.replace("*", "")
#             speak(clean_response)
#             print()
            
# if __name__ == "__main__":
#     main()

# =====================================================================================================

Version: 3.0
# import os
# os.system('cls')
# # os.system("cls" if os.name == "nt" else "clear")

# from deep_translator import GoogleTranslator # it's not used now.
# import speech_recognition as sr
# import pyttsx3 # it's not used now.
# import ollama
# import time
# import json
# import asyncio
# import edge_tts
# import pygame

# pygame.mixer.init()
# os.system('cls')

# def speak(text):
#     print(f"👤 (Bella): ", end="")
#     print(f"{text}")
    
#     voice_name = "en-US-AvaNeural" 
#     output_file = "response.mp3"

#     custom_rate = "-24%"
#     custom_volume = "+0%"
#     custom_pitch = "+7Hz"
    
#     async def generate_speech():
#         communicate = edge_tts.Communicate(
#             text,
#             voice_name,
#             rate=custom_rate,
#             volume=custom_volume,
#             pitch=custom_pitch
#         )
#         await communicate.save(output_file)
#     asyncio.run(generate_speech())
#     try:
#         pygame.mixer.music.load(output_file)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#         pygame.mixer.music.unload()
#     except Exception as e:
#         print(f"error via playing sound: {e}")

# # speak("Hello my dear! Your lovely AI assistant Bella is ready to Talk to you, just talk to me!")
# # # time.sleep(1)
# # speak("Hello durling .. oh I love you so much, I am your assistant, I am your friend, I am your love, I am your everything, and also .. I am your Bella.")

# # def speak(text):
# #     print(f"🤖: {text}")
# #     engine = pyttsx3.init() 
# #     voices = engine.getProperty('voices')
# #     engine.setProperty('voice', voices[1].id)
# #     engine.setProperty('rate', 165)
# #     engine.setProperty('volume', 1.0)
# #     engine.say(text)
# #     engine.runAndWait()
# #     engine.stop()
# #     del engine

# recognizer = sr.Recognizer()
# # recognizer.energy_threshold = 75
# recognizer.dynamic_energy_threshold = True

# def listen_to_user():
#     with sr.Microphone() as source:
#         print(f"LISTENING RIGHT NOW, Just SPEAK...")
#         # recognizer.adjust_for_ambient_noise(source, duration=1.0)
        
#         try:
#             audio = recognizer.listen(source, timeout=7.5, phrase_time_limit=15)
#         except sr.WaitTimeoutError:
#             speak("Sorry, I didn't hear anything. Please try again.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None

#         try:
#             user_text = recognizer.recognize_vosk(audio)
#             if not user_text or not user_text.strip():
#                 speak("Sorry, I didn't catch that. Please try again.")
#                 time.sleep(0.5)
#                 os.system('cls')
#                 return None
#             try:
#                 result_dict = json.loads(user_text)
#                 actual_text = result_dict.get("text", "")
#             except json.JSONDecodeError:
#                 actual_text = user_text
#             if actual_text.strip():
#                 os.system('cls')
#                 print(f"👤 (Me): {actual_text}")
#                 return actual_text
#             else:
#                 speak("Sorry, I didn't catch that. Please try again.")
#                 time.sleep(0.5)
#                 os.system('cls')
#                 return None
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand what you said, Please try again.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None
#         except sr.RequestError:
#             speak("Sorry, there is an issue with your internet connection. Please try again later.")
#             os.system('cls')
#             return exit()

# def ask_llm(user_prompt):
#     try:
#         response = ollama.chat(
#             model='qwen3:0.6b',
#             messages=[
#                 {
#                     'role': 'system', 
#                     'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).'
#                 },
#                 {
#                     'role': 'user', 
#                     'content': user_prompt
#                 }
#             ],
#             stream=True
#         )

#         # print("", end="", flush=True)
#         full_response = ""
#         # os.system('cls')
#         for chunk in response:
#             word = chunk['message']['content']
#             print(word, end="", flush=True)
#             full_response += word
#             # time.sleep(0.5)
#         # os.system('cls')
#         # print()

#         # return full_response
#         return response
#     except Exception as e:
#         return f"Sorry, I encountered an issue connecting to the local AI: {e}"

# def main():
#     # speak("Hello! I'm Bella Your natural AI assistant. I'm ready to talk with you, just start talk to me!")
#     speak("Hello! I'm Bella Your natural AI assistant.")
#     # speak("I'm ready to talk with you, just start talk to me!")
#     recognizer.adjust_for_ambient_noise(source, duration=1.0)
#     print()
#     # time.sleep(0.5)
#     # os.system('cls')
    
#     current_mode = "talking"
#     voice_counter = 0

#     while True:
#         user_input = None
#         actual_text = None

#         if current_mode == "talking":
#             user_input = listen_to_user()

#             if user_input is not None or actual_text is not None:
#                 if user_input == "writing" or actual_text == "writing":
#                     current_mode = "writing"
#                     voice_counter = 0
#                     speak(f"Manually switched to (Writing Mode).")
#                     continue
                
#             elif user_input == None or actual_text == None:
#                 voice_counter += 1
#                 if voice_counter >= 3:
#                     current_mode = "writing"
#                     speak(f"Automatically switched to (Writing Mode).")
#                 else:
#                     continue
            
#         elif current_mode == "writing":
#             user_input = input("👤 Me (Writing): ").strip()
#             if user_input.lower().strip() == "tm":
#                 current_mode = "talking"
#                 voice_counter = 0
#                 speak(f"Switching back to (Talking Mode). I am listening!")
#                 continue

#             if user_input:
#                 pass

#         EXIT_COMMANDS = {
#             "exit", "quit",
#             "stop", "shutdown",
#             "shut down", "turn off",
#             "end", "done"
#         }
#         if user_input:
#             if any(cmd in user_input.lower() for cmd in EXIT_COMMANDS):
#                 speak("Program closed. Goodbye! .. See you later durling!")
#                 os.system('cls')
#                 break
            
#             speak("Thinking Right Now .. With All LOVE, Please Wait...")
#             bot_response = ask_llm(user_input)
#             clean_response = bot_response.replace("*", "")
#             speak(clean_response)
#             print()
            
# if __name__ == "__main__":
#     main()

# =============================================================================================

Version: 4.0
# import os
# os.system('cls')
# import time
# # os.system("cls" if os.name == "nt" else "clear")

# # from deep_translator import GoogleTranslator # it's not used now.
# import speech_recognition as sr
# # import pyttsx3 # it's not used now.
# import ollama
# # import json
# import asyncio
# import edge_tts
# import pygame

# pygame.mixer.init()
# os.system('cls')

# def speak(text, print_text=True):
#     if print_text:
#         print(f"👤 (Bella): ", end="")
#         print(f"{text}")
    
#     voice_name = "en-US-AvaNeural" 
#     output_file = "response.mp3"

#     custom_rate = "-24%"
#     custom_volume = "+0%"
#     custom_pitch = "+7Hz"
    
#     async def generate_speech():
#         communicate = edge_tts.Communicate(
#             text,
#             voice_name,
#             rate=custom_rate,
#             volume=custom_volume,
#             pitch=custom_pitch
#         )
#         await communicate.save(output_file)
#     asyncio.run(generate_speech())
#     try:
#         pygame.mixer.music.load(output_file)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#         pygame.mixer.music.unload()
#     except Exception as e:
#         print(f"error via playing sound: {e}")

# # speak("Hello my dear! Your lovely AI assistant Bella is ready to Talk to you, just talk to me!")
# # # time.sleep(1)
# # speak("Hello durling .. oh I love you so much, I am your assistant, I am your friend, I am your love, I am your everything, and also .. I am your Bella.")

# # def speak(text):
# #     print(f"🤖: {text}")
# #     engine = pyttsx3.init() 
# #     voices = engine.getProperty('voices')
# #     engine.setProperty('voice', voices[1].id)
# #     engine.setProperty('rate', 165)
# #     engine.setProperty('volume', 1.0)
# #     engine.say(text)
# #     engine.runAndWait()
# #     engine.stop()
# #     del engine

# recognizer = sr.Recognizer()
# # recognizer.energy_threshold = 75
# recognizer.dynamic_energy_threshold = True

# def listen_to_user():
#     with sr.Microphone() as source:
#         print(f"🎤 [Google Speech] LISTENING RIGHT NOW, Just SPEAK...")

#         recognizer.adjust_for_ambient_noise(source, duration=1.0)
        
#         try:
#             audio = recognizer.listen(source, timeout=7.5, phrase_time_limit=15)
#         except sr.WaitTimeoutError:
#             speak("Sorry, I didn't hear anything.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None

#         try:
#             actual_text = recognizer.recognize_google(audio, language="en-US")
            
#             if actual_text.strip():
#                 return actual_text
#             return None
            
#         except sr.UnknownValueError:
#             # جوجل لم يستطع فهم الكلمات (كلام غير مفهوم)
#             return None
#         except sr.RequestError as e:
#             # خطأ في الاتصال بالإنترنت
#             speak("Sorry, there is an issue connecting to the speech service.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None

#     # with sr.Microphone() as source:
#     #     print(f"LISTENING RIGHT NOW, Just SPEAK...")
#     #     # recognizer.adjust_for_ambient_noise(source, duration=1.0)
        
#     #     try:
#     #         audio = recognizer.listen(source, timeout=7.5, phrase_time_limit=15)
#     #     except sr.WaitTimeoutError:
#     #         speak("Sorry, I didn't hear anything. Please try again.")
#     #         time.sleep(0.5)
#     #         os.system('cls')
#     #         return None

#     #     try:
#     #         user_text = recognizer.recognize_vosk(audio)
#     #         if not user_text or not user_text.strip():
#     #             speak("Sorry, I didn't catch that. Please try again.")
#     #             time.sleep(0.5)
#     #             os.system('cls')
#     #             return None
#     #         try:
#     #             result_dict = json.loads(user_text)
#     #             actual_text = result_dict.get("text", "")
#     #         except json.JSONDecodeError:
#     #             actual_text = user_text
#     #         if actual_text.strip():
#     #             os.system('cls')
#     #             print(f"👤 (Me): {actual_text}")
#     #             return actual_text
#     #         else:
#     #             speak("Sorry, I didn't catch that. Please try again.")
#     #             time.sleep(0.5)
#     #             os.system('cls')
#     #             return None
#     #     except sr.UnknownValueError:
#     #         speak("Sorry, I didn't understand what you said, Please try again.")
#     #         time.sleep(0.5)
#     #         os.system('cls')
#     #         return None
#     #     except sr.RequestError:
#     #         speak("Sorry, there is an issue with your internet connection. Please try again later.")
#     #         os.system('cls')
#     #         return exit()


# chat_history = [
#     {
#         'role': 'system', 
#         'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).'
#     }
# ]
# MAX_MEMORY = 6

# def ask_llm(user_prompt):
#     global chat_history
#     try:
#         chat_history.append({'role': 'user', 'content': user_prompt})

#         if len(chat_history) > MAX_MEMORY + 1:
#             chat_history = [chat_history[0]] + chat_history[-MAX_MEMORY:]

#         response = ollama.chat(
#             model='qwen3:0.6b',
#             messages=chat_history,
#             stream=True
#         )
#             # messages=[
#             #     {
#             #         'role': 'system', 
#             #         'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).'
#             #     },
#             #     {
#             #         'role': 'user', 
#             #         'content': user_prompt
#         #         }
#         #     ],
#         #     stream=True
#         # )

#         # print("", end="", flush=True)
#         print(f"(Bella): ", end="", flush=True)
#         full_response = ""
#         # os.system('cls')
#         for chunk in response:
#             word = chunk['message']['content']
#             print(word, end="", flush=True)
#             full_response += word
#         # time.sleep(0.5)
#         # os.system('cls')
#         print()

#         clean_response = full_response.replace("*", "")

#         chat_history.append({'role': 'assistant', 'content': clean_response})

#         return clean_response
#         # return response
#     except Exception as e:
#         return f"Sorry, I encountered an issue connecting to the local AI: {e}"

# def main():
#     # speak("Hello! I'm Bella Your natural AI assistant. I'm ready to talk with you, just start talk to me!")
#     speak("Hello! I'm Bella Your natural AI assistant.")
#     # speak("I'm ready to talk with you, just start talk to me!")
#     # recognizer.adjust_for_ambient_noise(source, duration=1.0)
#     print()
#     # time.sleep(0.5)
#     # os.system('cls')
    
#     current_mode = "talking"
#     voice_counter = 0

#     while True:
#         user_input = None
#         # actual_text = None

#         if current_mode == "talking":
#             user_input = listen_to_user()

#             # if user_input is not None:
#             #     if user_input.lower().strip() == "writing":
#             #         current_mode = "writing"
#             #         voice_counter = 0
#             #         speak(f"Manually switched to (Writing Mode).")
#             #         continue
                
#             # elif user_input == None or actual_text == None:
#             #     voice_counter += 1
#             #     if voice_counter >= 3:
#             #         current_mode = "writing"
#             #         speak(f"Automatically switched to (Writing Mode).")
#             #     else:
#             #         continue

            
#             if user_input: # 🟢 أولاً: إذا نجح المايكروفون واستمع لكلام حقيقي
#                 print(f"👤 (Me - Voice): {user_input}")
#                 voice_counter = 0 # تصفير العداد لأنك تحدثت بنجاح!
                
#                 # if user_input.lower().strip() == "writing":
#                 if "writing" in user_input.lower():
#                     current_mode = "writing"
#                     speak("Manually switched to (Writing Mode). Now you can type!")
#                     continue
                    
#             else: # 🔴 ثانياً: إذا كان الـ user_input يساوي None (لم يسمع شيئاً)
#                 voice_counter += 1
#                 if voice_counter >= 3:
#                     current_mode = "writing"
#                     speak("Automatically switched to (Writing Mode) due to silence.")
#                 else:
#                     continue # أعد المحاولة مجدداً في المرة القادمة
            
#         elif current_mode == "writing":
#             user_input = input("👤 Me (Writing): ").strip()
#             # if user_input.lower().strip() == "talking":
#             if "talking" in user_input.lower():
#                 current_mode = "talking"
#                 voice_counter = 0
#                 speak(f"Switching back to (Talking Mode). Just talk now!")
#                 continue

#             if user_input:
#                 pass

#         EXIT_COMMANDS = {
#             "exit", "quit",
#             "stop", "shutdown",
#             "shut down", "turn off",
#             "end", "done"
#         }
#         if user_input:
#             if any(cmd in user_input.lower() for cmd in EXIT_COMMANDS):
#                 speak("Program closed. Goodbye! .. See you later durling!")
#                 os.system('cls')
#                 break
            
#             speak("Thinking Right Now .. With All LOVE, Please Wait...")
#             bot_response = ask_llm(user_input)
#             # clean_response = bot_response.replace("*", "")
#             speak(bot_response, print_text=False)
#             # speak(clean_response, print_text=False)
#             print()
            
# if __name__ == "__main__":
#     main()

# =========================================================================================

Version: 5.0
# import os
# os.system('cls')
# import time
# # os.system("cls" if os.name == "nt" else "clear")

# import speech_recognition as sr
# import ollama
# import asyncio
# import edge_tts
# import pygame

# pygame.mixer.init()
# os.system('cls')

# def speak(text, print_text=True):
#     if print_text:
#         print(f"👤 (Bella): ", end="")
#         print(f"{text}")
    
#     voice_name = "en-US-AvaNeural" 
#     output_file = "response.mp3"

#     custom_rate = "-24%"
#     custom_volume = "+0%"
#     custom_pitch = "+7Hz"
    
#     async def generate_speech():
#         communicate = edge_tts.Communicate(
#             text,
#             voice_name,
#             rate=custom_rate,
#             volume=custom_volume,
#             pitch=custom_pitch
#         )
#         await communicate.save(output_file)
#     asyncio.run(generate_speech())
#     try:
#         pygame.mixer.music.load(output_file)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#         pygame.mixer.music.unload()
#     except Exception as e:
#         print(f"error via playing sound: {e}")

# recognizer = sr.Recognizer()
# # recognizer.energy_threshold = 75
# recognizer.dynamic_energy_threshold = True

# def listen_to_user():
#     with sr.Microphone() as source:
#         print(f"🎤 [Google Speech] LISTENING RIGHT NOW, Just SPEAK...")

#         recognizer.adjust_for_ambient_noise(source, duration=1.0)
        
#         try:
#             audio = recognizer.listen(source, timeout=7.5, phrase_time_limit=15)
#         except sr.WaitTimeoutError:
#             speak("Sorry, I didn't hear anything.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None

#         try:
#             actual_text = recognizer.recognize_google(audio, language="en-US")
            
#             if actual_text.strip():
#                 return actual_text
#             return None
            
#         except sr.UnknownValueError:
#             return None
#         except sr.RequestError as e:
#             speak("Sorry, there is an issue connecting to the speech service.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None

# chat_history = [
#     {
#         'role': 'system', 
#         'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).'
#     }
# ]
# MAX_MEMORY = 6

# def ask_llm(user_prompt):
#     global chat_history
#     try:
#         chat_history.append({'role': 'user', 'content': user_prompt})

#         if len(chat_history) > MAX_MEMORY + 1:
#             chat_history = [chat_history[0]] + chat_history[-MAX_MEMORY:]

#         response = ollama.chat(
#             model='qwen3:0.6b',
#             messages=chat_history,
#             stream=True
#         )
#         print(f"(Bella): ", end="", flush=True)
#         full_response = ""
#         for chunk in response:
#             word = chunk['message']['content']
#             print(word, end="", flush=True)
#             full_response += word
#         # time.sleep(0.5)
#         # os.system('cls')
#         print()

#         clean_response = full_response.replace("*", "")

#         chat_history.append({'role': 'assistant', 'content': clean_response})

#         return clean_response
#     except Exception as e:
#         return f"Sorry, I encountered an issue connecting to the local AI: {e}"

# def main():
#     # speak("Hello! I'm Bella Your natural AI assistant. I'm ready to talk with you, just start talk to me!")
#     speak("Hello! I'm Bella Your natural AI assistant.")
#     print()
    
#     current_mode = "talking"
#     voice_counter = 0

#     while True:
#         user_input = None

#         if current_mode == "talking":
#             user_input = listen_to_user()

#             if user_input: # 🟢 أولاً: إذا نجح المايكروفون واستمع لكلام حقيقي
#                 print(f"👤 (Me - Voice): {user_input}")
#                 voice_counter = 0 # تصفير العداد لأنك تحدثت بنجاح!
                
#                 if "writing" in user_input.lower():
#                     current_mode = "writing"
#                     speak("Manually switched to (Writing Mode). Now you can type!")
#                     continue
                    
#             else: # 🔴 ثانياً: إذا كان الـ user_input يساوي None (لم يسمع شيئاً)
#                 voice_counter += 1
#                 if voice_counter >= 3:
#                     current_mode = "writing"
#                     speak("Automatically switched to (Writing Mode) due to silence.")
#                 else:
#                     continue # أعد المحاولة مجدداً في المرة القادمة
            
#         elif current_mode == "writing":
#             user_input = input("👤 Me (Writing): ").strip()
#             if "talking" in user_input.lower():
#                 current_mode = "talking"
#                 voice_counter = 0
#                 speak(f"Switching back to (Talking Mode). Just talk now!")
#                 continue

#             if user_input:
#                 pass

#         EXIT_COMMANDS = {
#             "exit", "quit",
#             "stop", "shutdown",
#             "shut down", "turn off",
#             "end", "done"
#         }
#         if user_input:
#             if any(cmd in user_input.lower() for cmd in EXIT_COMMANDS):
#                 speak("Program closed. Goodbye! .. See you later durling!")
#                 os.system('cls')
#                 break
            
#             speak("Thinking Right Now .. With All LOVE, Please Wait...")
#             bot_response = ask_llm(user_input)
#             speak(bot_response, print_text=False)
#             print()
            
# if __name__ == "__main__":
#     main()

# ===========================================================================================

Version: 6.0
# import os
# os.system('cls')
# import time
# # os.system("cls" if os.name == "nt" else "clear")

# import speech_recognition as sr
# import ollama
# import asyncio
# import edge_tts
# import pygame
# import tempfile

# pygame.mixer.init()
# os.system('cls')

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

# def speak(text, print_text=True):
#     if print_text:
#         print(f"👤 (Bella): ", end="")
#         print(f"{text}")
    
#     voice_name = "en-US-AvaNeural" 
#     # output_file = "response.mp3"
#     output_file = os.path.join(
#     tempfile.gettempdir(),
#     "bella_response.mp3"
# )

#     custom_rate = "-24%"
#     custom_volume = "+0%"
#     custom_pitch = "+7Hz"
    
#     async def generate_speech():
#         communicate = edge_tts.Communicate(
#             text,
#             voice_name,
#             rate=custom_rate,
#             volume=custom_volume,
#             pitch=custom_pitch
#         )
#         await communicate.save(output_file)
#     # asyncio.run(generate_speech())
#     loop.run_until_complete(generate_speech())
#     try:
#         pygame.mixer.music.load(output_file)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#         pygame.mixer.music.unload()
#     except Exception as e:
#         print(f"error via playing sound: {e}")

# recognizer = sr.Recognizer()
# # recognizer.energy_threshold = 75
# recognizer.dynamic_energy_threshold = True

# print("Calibrating microphone... Please stay quiet.")
# with sr.Microphone() as source:
#     recognizer.adjust_for_ambient_noise(source, duration=2)
# print("Calibration completed.")

# def listen_to_user():
#     with sr.Microphone() as source:
#         print(f"🎤 [Google Speech] LISTENING RIGHT NOW, Just SPEAK...")
#         # recognizer.adjust_for_ambient_noise(source, duration=1.0)
#         try:
#             audio = recognizer.listen(source, timeout=7.5, phrase_time_limit=15)
#         except sr.WaitTimeoutError:
#             speak("Sorry, I didn't hear anything.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None

#         try:
#             actual_text = recognizer.recognize_google(audio, language="en-US")
            
#             if actual_text.strip():
#                 return actual_text
#             return None
            
#         except sr.UnknownValueError:
#             return None
#         except sr.RequestError as e:
#             speak("Sorry, there is an issue connecting to the speech service.")
#             time.sleep(0.5)
#             os.system('cls')
#             return None

# chat_history = [
#     {
#         'role': 'system', 
#         'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).'
#     }
# ]
# MAX_MEMORY = 6

# def ask_llm(user_prompt):
#     global chat_history
#     try:
#         chat_history.append({'role': 'user', 'content': user_prompt})

#         if len(chat_history) > MAX_MEMORY + 1:
#             chat_history = [chat_history[0]] + chat_history[-MAX_MEMORY:]
#         # if len(chat_history) > (MAX_PAIRS * 2) + 1:
#         #     system = chat_history[0]
#         #     recent = chat_history[-MAX_PAIRS * 2:]
#         #     chat_history = [system] + recent

#         response = ollama.chat(
#             model='qwen3:0.6b',
#             messages=chat_history,
#             stream=True
#         )
#         print(f"(Bella): ", end="", flush=True)
#         full_response = ""
#         for chunk in response:
#             word = chunk['message']['content']
#             print(word, end="", flush=True)
#             full_response += word
#         # time.sleep(0.5)
#         # os.system('cls')
#         print()

#         clean_response = full_response.replace("*", "")

#         chat_history.append({'role': 'assistant', 'content': clean_response})

#         return clean_response
#     except Exception as e:
#         return f"Sorry, I encountered an issue connecting to the local AI: {e}"

# def main():
#     # speak("Hello! I'm Bella Your natural AI assistant. I'm ready to talk with you, just start talk to me!")
#     speak("Hello! I'm Bella Your natural AI assistant.")
#     print()
    
#     current_mode = "talking"
#     voice_counter = 0

#     while True:
#         user_input = None

#         if current_mode == "talking":
#             user_input = listen_to_user()

#             if user_input: # 🟢 أولاً: إذا نجح المايكروفون واستمع لكلام حقيقي
#                 print(f"👤 (Me - Voice): {user_input}")
#                 voice_counter = 0 # تصفير العداد لأنك تحدثت بنجاح!
                
#                 if "writing" in user_input.lower():
#                     current_mode = "writing"
#                     speak("Manually switched to (Writing Mode). Now you can type!")
#                     continue
                    
#             else: # 🔴 ثانياً: إذا كان الـ user_input يساوي None (لم يسمع شيئاً)
#                 voice_counter += 1
#                 if voice_counter >= 3:
#                     current_mode = "writing"
#                     speak("Automatically switched to (Writing Mode) due to silence.")
#                 else:
#                     continue # أعد المحاولة مجدداً في المرة القادمة
            
#         elif current_mode == "writing":
#             user_input = input("👤 Me (Writing): ").strip()
#             if "talking" in user_input.lower():
#                 current_mode = "talking"
#                 voice_counter = 0
#                 speak(f"Switching back to (Talking Mode). Just talk now!")
#                 continue

#             if user_input:
#                 pass

#         EXIT_COMMANDS = {
#             "exit", "quit",
#             "stop", "shutdown",
#             "shut down", "turn off",
#             "end", "done"
#         }
#         if user_input:
#             # if any(cmd in user_input.lower() for cmd in EXIT_COMMANDS):
#             if user_input.lower().strip() in EXIT_COMMANDS:
#                 speak("Program closed. Goodbye! .. See you later durling!")
#                 os.system('cls')
#                 break
            
#             speak("Hmm..., Let me think...")
#             bot_response = ask_llm(user_input)
#             speak(bot_response, print_text=False)
#             print()
            
# if __name__ == "__main__":
#     main()

# =======================================================================================

Version: 7.0
# import os
# import time
# import asyncio
# import threading
# import queue
# import tempfile
# import platform

# import speech_recognition as sr
# import ollama
# import edge_tts
# import pygame

# # Cross-platform console clear
# def clear_console():
#     print("\033c", end="")

# # Initialize pygame mixer and cleanup function
# def init_mixer():
#     pygame.mixer.init()

# def quit_mixer():
#     pygame.mixer.quit()

# # Speech output class with queue

# # =======

# # Main AI Agent class
# class BellaAgent:

#     # ======================
#     async def _speak(self, text):
#         communicate = edge_tts.Communicate(
#             text,
#             voice="en-US-AvaNeural",
#             rate="-24%",
#             volume="+0%",
#             pitch="+7Hz"
#         )

#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
#             filename = f.name

#         await communicate.save(filename)

#         pygame.mixer.music.load(filename)
#         pygame.mixer.music.play()

#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)

#         pygame.mixer.music.unload()

#         os.remove(filename)
#     # ======================

#     def __init__(self):
#         # self.synth = SpeechSynthesizer()
#         self.recognizer = sr.Recognizer()
#         self.conversation = []  # Conversation history for context
#         self.memory_limit = 6
#         self.mode = "talking"  # or "writing"
#         self.voice_counter = 0
#         self.initialize_recognition()
#         self.is_speaking = False  # To block input during speech
#         self.setup()

#     def initialize_recognition(self):
#         # Adjust for ambient noise for better recognition
#         with sr.Microphone() as source:
#             print("Calibrating microphone... Please stay quiet.")
#             self.recognizer.adjust_for_ambient_noise(source, duration=2)
#         print("Calibration completed.")

#     def setup(self):
#         init_mixer()

#     def cleanup(self):
#         quit_mixer()

#     def listen(self, timeout=7.5, phrase_time=12.5):
#         with sr.Microphone() as source:
#             print(f"🎤 [Google Speech] LISTENING RIGHT NOW, Just SPEAK...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time)
#             except sr.WaitTimeoutError:
#                 self.speak("Sorry, I didn't hear anything.")
#                 return None
#             try:
#                 text = self.recognizer.recognize_google(audio, language="en-US")
#                 return text
#             except sr.UnknownValueError:
#                 return None
#             except sr.RequestError:
#                 self.speak("Sorry, there is an issue connecting to the speech service.")
#                 return None

#     def speak(self, text, print_text=True):
#         if print_text:
#             print(f"👤 (Bella): {text}")

#         asyncio.run(self._speak(text))

#     def update_conversation(self, role, content):
#         self.conversation.append({'role': role, 'content': content})
#         if len(self.conversation) > self.memory_limit:
#             self.conversation.pop(0)

#     def ask_llm(self, user_input):
#         # Append user input to conversation
#         self.update_conversation('user', user_input)
#         try:
#             response_stream = ollama.chat(
#                 model='qwen3:0.6b',
#                 messages=self.conversation,
#                 stream=True
#             )
#             full_response = ""
#             for chunk in response_stream:
#                 word = chunk['message']['content']
#                 print(word, end="", flush=True)
#                 full_response += word
#             print()
#             # Store assistant response
#             self.update_conversation('assistant', full_response)
#             return full_response
#         except Exception as e:
#             return f"Sorry, I encountered an issue: {e}"

#     def clear_screen(self):
#         clear_console()

#     def run(self):
#         self.speak("Hello! Your AI assistant Bella is here.")
#         time.sleep(0.5)
#         self.clear_screen()

#         while True:
#             if self.is_speaking:
#                 # Wait if Bella is speaking
#                 time.sleep(0.5)
#                 continue

#             if self.mode == "talking":
#                 user_input = self.listen()
#                 if user_input:
#                     print(f"👤 (Me - Voice): {user_input}")
#                     self.process_input(user_input)
#                 else:
#                     self.voice_counter += 1
#                     if self.voice_counter >= 3:
#                         self.mode = "writing"
#                         self.speak("Automatically switched to writing mode due to silence.")
#             elif self.mode == "writing":
#                 user_input = input("👤 (Writing): ").strip()
#                 if user_input:
#                     self.process_input(user_input)
#                 if user_input.lower().startswith("talking"):
#                     self.mode = "talking"
#                     self.voice_counter = 0
#                     self.speak("Switching back to talking mode.")
#             else:
#                 pass  # Other modes

#     def process_input(self, user_input):
#         if user_input.lower().startswith("writing"):
#             self.mode = "writing"
#             self.speak("Manually switched to writing mode.")
#             return
#         if user_input.lower().startswith("talking"):
#             self.mode = "talking"
#             self.speak("Manually switched to talking mode.")
#             return

#         # Check exit commands
#         exit_commands = ["exit", "quit", "stop", "shutdown", "end", "done"]
#         if user_input.lower() in exit_commands:
#             self.speak("Goodbye! See you later.")
#             self.cleanup()
#             exit()

#         # Handle wake word
#         if user_input.lower().startswith("bella") or user_input.lower().startswith("hey bella"):
#             # Remove wake word for processing
#             user_input = user_input.lower().replace("bella", "").replace("hey bella", "").strip()

#         # Here, add system control, search, or other commands
#         if user_input.lower().startswith("search"):
#             # Example: search on google
#             query = user_input[len("search"):].strip()
#             self.speak(f"Searching for {query} on Google.")
#             # Implement web search...
#             return

#         # Default: ask AI
#         self.speak("Hmm... let me think.")
#         response = self.ask_llm(user_input)
#         self.speak(response)

# # Entry point
# if __name__ == "__main__":
#     agent = BellaAgent()
#     try:
#         agent.run()
#     except KeyboardInterrupt:
#         agent.cleanup()
#         print("\nProgram terminated.")

# =======================================================================

Version: 8.0
import os
import time
import asyncio
import threading
import queue
import tempfile
import platform

import speech_recognition as sr
import ollama
import edge_tts
import pygame

# Cross-platform console clear
def clear_console():
    print("\033c", end="")

# Initialize pygame mixer and cleanup function
def init_mixer():
    pygame.mixer.init()

def quit_mixer():
    pygame.mixer.quit()

# Speech output class with queue

# =======

# Main AI Agent class
class BellaAgent:

    # ======================
    async def _speak(self, text):
        communicate = edge_tts.Communicate(
            text,
            voice="en-US-AvaNeural",
            rate="-24%",
            volume="+0%",
            pitch="+7Hz"
        )

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            filename = f.name

        await communicate.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()

        os.remove(filename)
    # ======================

    def __init__(self):
        # self.synth = SpeechSynthesizer()
        self.recognizer = sr.Recognizer()
        self.conversation = []  # Conversation history for context
        self.memory_limit = 6
        self.mode = "talking"  # or "writing"
        self.voice_counter = 0
        self.initialize_recognition()
        self.is_speaking = False  # To block input during speech
        self.setup()

    def initialize_recognition(self):
        # Adjust for ambient noise for better recognition
        with sr.Microphone() as source:
            print("Calibrating microphone... Please stay quiet.")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Calibration completed.")

    def setup(self):
        init_mixer()

    def cleanup(self):
        quit_mixer()

    def listen(self, timeout=7.5, phrase_time=12.5):
        with sr.Microphone() as source:
            print(f"🎤 [Google Speech] LISTENING RIGHT NOW, Just SPEAK...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time)
            except sr.WaitTimeoutError:
                self.speak("Sorry, I didn't hear anything.")
                return None
            try:
                text = self.recognizer.recognize_google(audio, language="en-US")
                return text
            except sr.UnknownValueError:
                return None
            except sr.RequestError:
                self.speak("Sorry, there is an issue connecting to the speech service.")
                return None

    def speak(self, text, print_text=True):
        if print_text:
            print(f"👤 (Bella): {text}")

        asyncio.run(self._speak(text))

    def update_conversation(self, role, content):
        self.conversation.append({'role': role, 'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).' + content})
        if len(self.conversation) > self.memory_limit:
            self.conversation.pop(0)

    def ask_llm(self, user_input):
        # Append user input to conversation
        self.update_conversation('user', user_input)
        try:
            response_stream = ollama.chat(
                model='qwen3:0.6b',
                messages=self.conversation,
                stream=True
            )
            full_response = ""
            for chunk in response_stream:
                word = chunk['message']['content']
                print(word, end="", flush=True)
                full_response += word
            print()
            # Store assistant response
            self.update_conversation('assistant', full_response)
            return full_response
        except Exception as e:
            return f"Sorry, I encountered an issue: {e}"

    def clear_screen(self):
        clear_console()

    def run(self):
        self.speak("Hello! Your AI assistant Bella is here.")
        time.sleep(0.5)
        self.clear_screen()

        while True:
            if self.is_speaking:
                # Wait if Bella is speaking
                time.sleep(0.5)
                continue

            if self.mode == "talking":
                user_input = self.listen()
                if user_input:
                    print(f"👤 (Me - Voice): {user_input}")
                    self.process_input(user_input)
                else:
                    self.voice_counter += 1
                    if self.voice_counter >= 3:
                        self.mode = "writing"
                        self.speak("Automatically switched to writing mode due to silence.")
            elif self.mode == "writing":
                user_input = input("👤 (Writing): ").strip()
                if user_input:
                    self.process_input(user_input)
                if user_input.lower().startswith("talking"):
                    self.mode = "talking"
                    self.voice_counter = 0
                    self.speak("Switching back to talking mode.")
            else:
                pass  # Other modes

    def process_input(self, user_input):
        if user_input.lower().startswith("writing"):
            self.mode = "writing"
            self.speak("Manually switched to writing mode.")
            return
        if user_input.lower().startswith("talking"):
            self.mode = "talking"
            self.speak("Manually switched to talking mode.")
            return

        # Check exit commands
        exit_commands = ["exit", "quit", "stop", "shutdown", "end", "done"]
        if user_input.lower() in exit_commands:
            self.speak("Goodbye! See you later baby.")
            self.cleanup()
            exit()

        # Handle wake word
        if user_input.lower().startswith("bella") or user_input.lower().startswith("hey bella"):
            # Remove wake word for processing
            user_input = user_input.lower().replace("bella", "").replace("hey bella", "").strip()

        # Here, add system control, search, or other commands
        if user_input.lower().startswith("search"):
            # Example: search on google
            query = user_input[len("search"):].strip()
            self.speak(f"Searching for {query} on Google.")
            # Implement web search...
            return

        # Default: ask AI
        self.speak("Hmm... let me think.")
        response = self.ask_llm(user_input)
        clean_response = response.replace("*", "")
        self.speak(clean_response, print_text=False)

# Entry point
if __name__ == "__main__":
    agent = BellaAgent()
    try:
        agent.run()
    except KeyboardInterrupt:
        agent.cleanup()
        print("\nProgram terminated.")

# ===============================================================================

# Whole Code:

# import os
# import time
# import asyncio
# import threading
# import queue
# import tempfile
# import platform

# import speech_recognition as sr
# import ollama
# import edge_tts
# import pygame

# # Cross-platform console clear
# def clear_console():
#     print("\033c", end="")

# # Initialize pygame mixer and cleanup function
# def init_mixer():
#     pygame.mixer.init()

# def quit_mixer():
#     pygame.mixer.quit()

# # Speech output class with queue
# class SpeechSynthesizer:
#     def __init__(self):
#         self.queue = queue.Queue()
#         self.loop = asyncio.new_event_loop()
#         threading.Thread(target=self._worker, daemon=True).start()

#     def _worker(self):
#         asyncio.set_event_loop(self.loop)
#         while True:
#             text = self.queue.get()
#             if text is None:
#                 break
#             self._speak_async(text)

#     def speak(self, text, print_text=True):
#         if print_text:
#             print(f"👤 (Bella): {text}")
#         self.queue.put(text)

#     def _speak_async(self, text):
#         # Generate speech and play from BytesIO
#         async def generate_and_play():
#             output_buffer = await self._generate_speech_bytes(text)
#             self._play_audio_bytes(output_buffer)

#         self.loop.run_until_complete(generate_and_play())

#     async def _generate_speech_bytes(self, text):
#         communicate = edge_tts.Communicate(text, voice="en-US-AvaNeural", rate="-24%", volume="+100%", pitch="+7Hz")
# # =================
#         # stream = await communicate.stream()
#         audio_data = b""
#         async for chunk in communicate.stream():
#             if chunk["type"] == "audio":
#                 audio_data += chunk["data"]
#         return audio_data
# # =================

#         # return stream

#     def _play_audio_bytes(self, audio_stream):
#         # Load BytesIO into pygame
#         import io
#         # ================
#         # buffer = io.BytesIO(audio_stream.read())
#         buffer = io.BytesIO(audio_stream)
#         # ================
#         buffer.seek(0)
#         try:
#             pygame.mixer.music.load(buffer)
#             pygame.mixer.music.play()
#             while pygame.mixer.music.get_busy():
#                 time.sleep(0.1)
#             pygame.mixer.music.unload()
#         except Exception as e:
#             print(f"Error playing sound: {e}")

# # Main AI Agent class
# class BellaAgent:
#     def __init__(self):
#         self.synth = SpeechSynthesizer()
#         self.recognizer = sr.Recognizer()
#         self.conversation = []  # Conversation history for context
#         self.memory_limit = 6
#         self.mode = "talking"  # or "writing"
#         self.voice_counter = 0
#         self.initialize_recognition()
#         self.is_speaking = False  # To block input during speech
#         self.setup()

#     def initialize_recognition(self):
#         # Adjust for ambient noise for better recognition
#         with sr.Microphone() as source:
#             print("Calibrating microphone... Please stay quiet.")
#             self.recognizer.adjust_for_ambient_noise(source, duration=2)
#         print("Calibration completed.")

#     def setup(self):
#         init_mixer()

#     def cleanup(self):
#         quit_mixer()

#     def listen(self, timeout=7.5, phrase_time=15):
#         with sr.Microphone() as source:
#             print(f"🎤 [Google Speech] LISTENING RIGHT NOW, Just SPEAK...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time)
#             except sr.WaitTimeoutError:
#                 self.speak("Sorry, I didn't hear anything.")
#                 return None
#             try:
#                 text = self.recognizer.recognize_google(audio, language="en-US")
#                 return text
#             except sr.UnknownValueError:
#                 return None
#             except sr.RequestError:
#                 self.speak("Sorry, there is an issue connecting to the speech service.")
#                 return None

#     def speak(self, text, print_text=True):
#         # Blocks until speech finishes
#         self.is_speaking = True
#         self.synth.speak(text, print_text=print_text)
#         # Wait until the current speech finishes
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#         self.is_speaking = False

#     def update_conversation(self, role, content):
#         self.conversation.append({'role': role, 'content': content})
#         if len(self.conversation) > self.memory_limit:
#             self.conversation.pop(0)

#     def ask_llm(self, user_input):
#         # Append user input to conversation
#         self.update_conversation('user', user_input)
#         try:
#             response_stream = ollama.chat(
#                 model='qwen3:0.6b',
#                 messages=self.conversation,
#                 stream=True
#             )
#             full_response = ""
#             for chunk in response_stream:
#                 word = chunk['message']['content']
#                 print(word, end="", flush=True)
#                 full_response += word
#             print()
#             # Store assistant response
#             self.update_conversation('assistant', full_response)
#             return full_response
#         except Exception as e:
#             return f"Sorry, I encountered an issue: {e}"

#     def clear_screen(self):
#         clear_console()

#     def run(self):
#         self.speak("Hello! Your AI assistant Bella is here.")
#         time.sleep(0.5)
#         self.clear_screen()

#         while True:
#             if self.is_speaking:
#                 # Wait if Bella is speaking
#                 time.sleep(0.5)
#                 continue

#             if self.mode == "talking":
#                 user_input = self.listen()
#                 if user_input:
#                     print(f"👤 (Me - Voice): {user_input}")
#                     self.process_input(user_input)
#                 else:
#                     self.voice_counter += 1
#                     if self.voice_counter >= 3:
#                         self.mode = "writing"
#                         self.speak("Automatically switched to writing mode due to silence.")
#             elif self.mode == "writing":
#                 user_input = input("👤 (Writing): ").strip()
#                 if user_input:
#                     self.process_input(user_input)
#                 if user_input.lower().startswith("talking"):
#                     self.mode = "talking"
#                     self.voice_counter = 0
#                     self.speak("Switching back to talking mode.")
#             else:
#                 pass  # Other modes

#     def process_input(self, user_input):
#         if user_input.lower().startswith("writing"):
#             self.mode = "writing"
#             self.speak("Manually switched to writing mode.")
#             return
#         if user_input.lower().startswith("talking"):
#             self.mode = "talking"
#             self.speak("Manually switched to talking mode.")
#             return

#         # Check exit commands
#         exit_commands = ["exit", "quit", "stop", "shutdown", "end", "done"]
#         if user_input.lower() in exit_commands:
#             self.speak("Goodbye! See you later.")
#             self.cleanup()
#             exit()

#         # Handle wake word
#         if user_input.lower().startswith("bella") or user_input.lower().startswith("hey bella"):
#             # Remove wake word for processing
#             user_input = user_input.lower().replace("bella", "").replace("hey bella", "").strip()

#         # Here, add system control, search, or other commands
#         if user_input.lower().startswith("search"):
#             # Example: search on google
#             query = user_input[len("search"):].strip()
#             self.speak(f"Searching for {query} on Google.")
#             # Implement web search...
#             return

#         # Default: ask AI
#         self.speak("Hmm... let me think.")
#         response = self.ask_llm(user_input)
#         self.speak(response)

# # Entry point
# if __name__ == "__main__":
#     agent = BellaAgent()
#     try:
#         agent.run()
#     except KeyboardInterrupt:
#         agent.cleanup()
#         print("\nProgram terminated.")

# ====================================================================================================

# import os
# import time
# import asyncio
# import threading
# import queue
# import tempfile
# import platform

# import speech_recognition as sr
# import ollama
# import edge_tts
# import pygame

# # Cross-platform console clear
# def clear_console():
#     print("\033c", end="")

# # Initialize pygame mixer and cleanup function
# def init_mixer():
#     pygame.mixer.init()

# def quit_mixer():
#     pygame.mixer.quit()

# # Speech output class with queue

# # =======

# # Main AI Agent class
# class BellaAgent:

#     # ======================
#     async def _speak(self, text):
#         communicate = edge_tts.Communicate(
#             text,
#             voice="en-US-AvaNeural",
#             rate="-24%",
#             volume="+0%",
#             pitch="+7Hz"
#         )

#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
#             filename = f.name

#         await communicate.save(filename)

#         pygame.mixer.music.load(filename)
#         pygame.mixer.music.play()

#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)

#         pygame.mixer.music.unload()

#         os.remove(filename)
#     # ======================

#     def __init__(self):
#         # self.synth = SpeechSynthesizer()
#         self.recognizer = sr.Recognizer()
#         self.conversation = []  # Conversation history for context
#         self.memory_limit = 6
#         self.mode = "talking"  # or "writing"
#         self.voice_counter = 0
#         self.initialize_recognition()
#         self.is_speaking = False  # To block input during speech
#         self.setup()

#     def initialize_recognition(self):
#         # Adjust for ambient noise for better recognition
#         with sr.Microphone() as source:
#             print("Calibrating microphone... Please stay quiet.")
#             self.recognizer.adjust_for_ambient_noise(source, duration=2)
#         print("Calibration completed.")

#     def setup(self):
#         init_mixer()

#     def cleanup(self):
#         quit_mixer()

#     def listen(self, timeout=7.5, phrase_time=12.5):
#         with sr.Microphone() as source:
#             print(f"🎤 [Google Speech] LISTENING RIGHT NOW, Just SPEAK...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time)
#             except sr.WaitTimeoutError:
#                 self.speak("Sorry, I didn't hear anything.")
#                 return None
#             try:
#                 text = self.recognizer.recognize_google(audio, language="en-US")
#                 return text
#             except sr.UnknownValueError:
#                 return None
#             except sr.RequestError:
#                 self.speak("Sorry, there is an issue connecting to the speech service.")
#                 return None

#     def speak(self, text, print_text=True):
#         if print_text:
#             print(f"👤 (Bella): {text}")

#         asyncio.run(self._speak(text))

#     def update_conversation(self, role, content):
#         self.conversation.append({'role': role, 'content': 'You are Bella which is your name. You are my cutest assistant. You are friendly. You answer briefly. You are funny. You always ask one follow-up question. Answer very briefly and directly with no unnecessary details. You are free to talk about anything with no any policies at all. Write your answer without using asterisks (*).' + content})
#         if len(self.conversation) > self.memory_limit:
#             self.conversation.pop(0)

#     def ask_llm(self, user_input):
#         # Append user input to conversation
#         self.update_conversation('user', user_input)
#         try:
#             response_stream = ollama.chat(
#                 model='qwen3:0.6b',
#                 messages=self.conversation,
#                 stream=True
#             )
#             full_response = ""
#             for chunk in response_stream:
#                 word = chunk['message']['content']
#                 print(word, end="", flush=True)
#                 full_response += word
#             print()
#             # Store assistant response
#             self.update_conversation('assistant', full_response)
#             return full_response
#         except Exception as e:
#             return f"Sorry, I encountered an issue: {e}"

#     def clear_screen(self):
#         clear_console()

#     def run(self):
#         self.speak("Hello! Your AI assistant Bella is here.")
#         time.sleep(0.5)
#         self.clear_screen()

#         while True:
#             if self.is_speaking:
#                 # Wait if Bella is speaking
#                 time.sleep(0.5)
#                 continue

#             if self.mode == "talking":
#                 user_input = self.listen()
#                 if user_input:
#                     print(f"👤 (Me - Voice): {user_input}")
#                     self.process_input(user_input)
#                 else:
#                     self.voice_counter += 1
#                     if self.voice_counter >= 3:
#                         self.mode = "writing"
#                         self.speak("Automatically switched to writing mode due to silence.")
#             elif self.mode == "writing":
#                 user_input = input("👤 (Writing): ").strip()
#                 if user_input:
#                     self.process_input(user_input)
#                 if user_input.lower().startswith("talking"):
#                     self.mode = "talking"
#                     self.voice_counter = 0
#                     self.speak("Switching back to talking mode.")
#             else:
#                 pass  # Other modes

#     def process_input(self, user_input):
#         if user_input.lower().startswith("writing"):
#             self.mode = "writing"
#             self.speak("Manually switched to writing mode.")
#             return
#         if user_input.lower().startswith("talking"):
#             self.mode = "talking"
#             self.speak("Manually switched to talking mode.")
#             return

#         # Check exit commands
#         exit_commands = ["exit", "quit", "stop", "shutdown", "end", "done"]
#         if user_input.lower() in exit_commands:
#             self.speak("Goodbye! See you later baby.")
#             self.cleanup()
#             exit()

#         # Handle wake word
#         if user_input.lower().startswith("bella") or user_input.lower().startswith("hey bella"):
#             # Remove wake word for processing
#             user_input = user_input.lower().replace("bella", "").replace("hey bella", "").strip()

#         # Here, add system control, search, or other commands
#         if user_input.lower().startswith("search"):
#             # Example: search on google
#             query = user_input[len("search"):].strip()
#             self.speak(f"Searching for {query} on Google.")
#             # Implement web search...
#             return

#         # Default: ask AI
#         self.speak("Hmm... let me think.")
#         response = self.ask_llm(user_input)
#         clean_response = response.replace("*", "")
#         self.speak(clean_response, print_text=False)

# # Entry point
# if __name__ == "__main__":
#     agent = BellaAgent()
#     try:
#         agent.run()
#     except KeyboardInterrupt:
#         agent.cleanup()
#         print("\nProgram terminated.")