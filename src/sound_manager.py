import random
import pygame
import os


class SoundManager:
    def __init__(self, sounds_directory: str = "sounds"):
        self.sounds_directory = sounds_directory
        self.sounds = self.load_sounds()
        self.current_index = 0

    def load_sounds(self, initial_load: bool = False) -> list:
        """
        Load all sound files from the specified directory.
        :return: List of sound file paths.
        """
        if not os.path.exists(self.sounds_directory):
            print(f"Sounds directory '{self.sounds_directory}' does not exist.")
            raise FileNotFoundError(f"Sounds directory '{self.sounds_directory}' not found.")
            return []

        sounds = os.listdir(self.sounds_directory)
        sound_files = [os.path.join(self.sounds_directory, sound) for sound in sounds]

        if sound_files:
            if initial_load:
                print(f"Loaded sound files: {sound_files}")
        else:
            print("No sound files found in the sounds directory.")
            raise FileNotFoundError("No sound files found in the sounds directory.")

        return sound_files

    def detect_new_sounds(self):
        """
        Detect and load any new sound files added to the sounds directory.
        """
        current_sounds = set(self.sounds)
        all_sounds = set(self.load_sounds())
        new_sounds = all_sounds - current_sounds

        if new_sounds:
            self.sounds.extend(new_sounds)
            print(f"New sounds detected and loaded: {new_sounds}")
        else:
            print("No new sounds detected.")

    def play_sound(self, index: int = 0):
        """
        Play a sound by index from the loaded sounds.
        :param index: Index of the sound to play.
        """
        if index < 0 or index >= len(self.sounds):
            print("Invalid sound index.")
            return

        sound_file = self.sounds[index]

        if pygame.mixer.music.get_busy():
            return  # Don't play if already playing

        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        print(f"Playing sound: {sound_file}")
        self.detect_new_sounds()

    def play_random_sound(self):
        """
        Play a random sound from the loaded sounds.
        """
        if not self.sounds:
            print("No sounds to play.")
            return

        random_index = random.randint(0, len(self.sounds) - 1)
        self.play_sound(random_index)
        self.detect_new_sounds()

    def play_next_sound(self):
        """
        Play the next sound in the list, cycling back to the start if at the end.
        """
        if not self.sounds:
            print("No sounds to play.")
            return

        self.play_sound(self.current_index)
        self.current_index = (self.current_index + 1) % len(self.sounds)
        self.detect_new_sounds()

    def stop_sound(self):
        """
        Stop any currently playing sound.
        """
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            print("Sound stopped.")
        else:
            print("No sound is currently playing.")
