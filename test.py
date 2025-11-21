
import os 
import random

def play_music():
    music_dir = "D:\\Bappy\\Live Sessions\\Inception\\FSDS-with-GenAI-1.0\\Python-Programming\\JARVIS-Voice-Assistant-System\\music"
    try:
        songs = os.listdir(music_dir)
        if songs:
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))
    except Exception as e:
        print(e)
     

    
play_music()