import os
import pygame


def audio_init(device_name: str = 'None') -> None:
    """
    Initialize the audio device for pygame mixer.
    This is especially important when running as a service on a pi.
    :param device_name: Name of the audio device to initialize.
    """
    # Force ALSA audio driver so that pygame works as a service.
    os.environ['SDL_AUDIODRIVER'] = 'alsa'

    # Common device mappings for raspberry pi
    devices = {
        'hdmi0': 'hw:0,0',
        'hdmi1': 'hw:1,0',
        'aux': 'hw:2,0',
        'usb': 'hw:3,0',
    }

    device = devices[device_name] if device_name in devices else None
    device_label = device or "default device"

    try:
        if device:
            os.environ['AUDIODEV'] = device

        pygame.mixer.init()
        print(f"Initialized audio on {device_label}.")
    except pygame.error as e:
        print(f"Failed to initialize audio on {device_label}: {e}")
        print(f"Did you remember to change the audio output in app.py, line 8, audio_init('{device_name}')?")
        raise RuntimeError("CRITICAL: Could not initialize chosen audio device. Service cannot start.")
