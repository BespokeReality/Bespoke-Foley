from flask import Flask, render_template
import pygame
import gpiozero as gpio
from .audio_init import audio_init
from .sound_manager import SoundManager

app = Flask(__name__)
audio_init()
soundManager = SoundManager()


# Initialize GPIO components.
# Default is pin 17, change and add as needed.
button = gpio.Button(17, pull_up=False)


# THIS FUNCTION NEEDS TO BE CHANGED BASED ON THE USE CASE
def on_release():
    """
    Play sound when sensor is released
    """
    soundManager.play_random_sound()
    return


button.when_released = on_release


@app.route("/")
def index():
    """
    Return index.html template.
    """
    return render_template("index.html")


@app.route("/play")
def play_default_sound():
    """
    Play the default sound (index 0).
    """
    soundManager.play_sound(0)
    return "Playing default sound"


@app.route("/play/<int:index>")
def play_sound(index: int):
    """
    Play sound by index.
    :param index: Index of the sound to play.
    """
    soundManager.play_sound(index)
    return f"Playing sound {index}"


@app.route("/play/random")
def play_random_sound():
    """
    Play a random sound.
    """
    soundManager.play_random_sound()
    return "Playing random sound"


@app.route("/stop")
def stop_sound():
    """
    Stop any currently playing sound.
    """
    pygame.mixer.music.stop()
    return "Stopped sound"


if __name__ == "__main__":
    app.run()
