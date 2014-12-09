init python:
    renpy.music.register_channel('ambient',    mixer='sfx', loop=True, stop_on_mute=False, tight=True, file_prefix='snd/', file_suffix='.flac', buffer_queue=True)
    renpy.music.register_channel('ambientLow', mixer='sfx', loop=True, stop_on_mute=False, tight=True, file_prefix='snd/', file_suffix='.flac', buffer_queue=True)
    renpy.music.register_channel('angry', mixer='sfx', loop=True, stop_on_mute=False, tight=True, file_prefix='snd/', file_suffix='.flac', buffer_queue=True)
    renpy.music.register_channel('sound', mixer='sfx', loop=False, tight=False, file_prefix='snd/', file_suffix='.flac', buffer_queue=True)
    renpy.music.register_channel('music', mixer='music', loop=True, tight=True, file_prefix='ost/', file_suffix='.flac', buffer_queue=True)

label ambient_start:
    play ambient "ambient-crowd" fadeout 5.0 fadein 5.0
    play ambientLow "ambient-crowd-low" fadeout 5.0 fadein 5.0
    play angry "angry-crowd" fadeout 5.0 fadein 5.0
    
    call ambient_abrupt
    call angry_crowd(0, 0)
    return

label ambient_abrupt:
    $ renpy.music.set_volume(0, delay=0, channel='ambient')
    $ renpy.music.set_volume(0, delay=0, channel='ambientLow')
    return

label ambient_normal(v=1, d=5):
    $ renpy.music.set_volume(v, delay=d, channel='ambient')
    $ renpy.music.set_volume(0, delay=d, channel='ambientLow')
    return

label ambient_low(v=1, d=15):
    $ renpy.music.set_volume(1, delay=d, channel='ambientLow')
    $ renpy.music.set_volume(0, delay=d, channel='ambient')
    return

label angry_crowd(v=0.6, d=2):
    $ renpy.music.set_volume(v, delay=d, channel='angry')
    return

label music_fade(v=0.3, d=3):
    $ renpy.music.set_volume(v, delay=d, channel='music')
    return

label music_unfade(v=1, d=3):
    $ renpy.music.set_volume(v, delay=d, channel='music')
    return
