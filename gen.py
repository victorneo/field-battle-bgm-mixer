from glob import glob
from pydub import AudioSegment


# Number of battles to include in the song
NUM_BATTLES = 3

field_song = AudioSegment.from_mp3('field.mp3')
battle_song = AudioSegment.from_mp3('battle.mp3')

field_duration = len(field_song)
battle_duration = len(battle_song)

# Trim fadeout from battle song in milliseconds, increase / decrease if necessary
battle_song = battle_song[:battle_duration-15000]

# Interval for battles to happen, for now it is not random, happens at fixed time
interval = field_duration / (NUM_BATTLES + 1)

output = field_song[:interval]

for i in xrange(1, NUM_BATTLES+1):
    battle_start = interval * i
    battle_end = battle_start + interval

    output = output.append(battle_song, crossfade=(1000))
    output = output.append(field_song[battle_start:battle_end], crossfade=(1000))

# Export music as output.mp3
out_f = open('output.mp3', 'wb')
output.export(out_f, format='mp3')
out_f.close()
