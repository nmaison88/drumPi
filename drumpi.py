"""
Receive messages from the input port and print them out.
"""
import sys
import pygame
import os
import mido
# startup/initialization goes here
pygame.mixer.init(44000, -16, 1, 1024)
dirname = os.path.dirname(os.path.abspath(__file__))
sound_player = pygame.mixer.Channel(2)
kick = pygame.mixer.Sound(dirname + '/kick.wav')
snare = pygame.mixer.Sound(dirname + '/snare.wav')

if len(sys.argv) > 1:
    portname = sys.argv[1]
else:
    portname = None  # Use default port

try:
    with mido.open_input(portname) as port:
        print(f'Using {port}')
        print('Waiting for messages...')
        for message in port:
            print(f'Received {message}')

            # play kick on c1
            if message.type == 'note_on' and message.note == 36:
                sound_player.play(kick)
            # play snare sound on d1
            if message.type == 'note_on' and message.note == 38:
                sound_player.play(snare)
            sys.stdout.flush()
except KeyboardInterrupt:
    pass
