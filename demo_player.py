import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
def play_music(folder, songname):
    file_path = os.path.join(folder, songname)
    
    if not os.path.exists(file_path):
        print(f"The file '{songname}' does not exist in the folder '{folder}'.")
        return
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print(f"Now playing: {songname}")
    print("command: [p] to pause, [r] to resume, [s] to stop")
    
    while True:
        
        commannd = input(">").lower()
        if commannd == 'p':
            pygame.mixer.music.pause()
            print("Music paused.")
        elif commannd == 'r':
            pygame.mixer.music.unpause()
            print("Music resumed.")
        elif commannd == 's':
            pygame.mixer.music.stop()
            print("Music stopped.")
            break
        else:
            print("Invalid command. Please enter 'p', 'r', or 's'.")    
    
def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Failed to initialize the mixer: {e}")
        return
    folder ="audio"
    
    if not os.path.exists(folder):
        print(f"The Folder '{folder}' does not exist.")
        return 
    
    mp3_files = [file for file in os.listdir(folder) if file.endswith('.mp3')]
    
    if not mp3_files:
        print(f"No MP3 files found in the folder '{folder}'.")
        return
    while True:
        print("****** MP3 Player ******")
        print("Available MP3 files:")
        
        for index,song in enumerate(mp3_files,start=1):
            print(f"{index}. {song}")
        
        choice_input = input("\nEnter the number of the song you want to play (or 'q' to quit): ")
        
        if choice_input.lower() == 'q':
            print("Exiting the MP3 player.")
            break
        
        if not choice_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        
        choice = int(choice_input) -1 
        if choice < 0 or choice >= len(mp3_files):
            print("Invalid choice. Please select a valid song number.")
            continue
        else:
            play_music(folder,mp3_files[choice])
        
    
if __name__ == "__main__":
    main()