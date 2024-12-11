import numpy as np
import simpleaudio as sa

def normalize_stereo(audio):
    maxamp = 0
    for bit in audio:
        maxbit = np.max(np.abs(bit))
        if maxbit > maxamp:
            maxamp = maxbit

    normalized = []
    for i in range(len(audio)):
        piece = np.array( [32767 / maxamp * audio[i][0], 32767 / maxamp * audio[i][1]] )
        normalized.append(piece.astype(np.int16))
    return np.array(normalized)

# calculate note frequencies
A_freq = 440
C_freq = A_freq * 2 ** (4 / 12)
Em_freq = A_freq * 2 ** (7 / 12)
G_freq = A_freq * 2 ** (11 / 12)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 192000
T = 0.5
t = np.linspace(0, 1.0 * T, int(T * sample_rate), False)

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
A_note_left = np.array(
        [ np.array([A_freq * t[i] * 2 * np.pi, 0]) for i in range(len(t))
            ]
        )
C_note = np.sin(C_freq * t * 2 * np.pi)
C_note_right = np.array(
        [ np.array([0, C_freq * t[i] * 2 * np.pi]) for i in range(len(t))
            ]
        )
Em_note = np.sin(Em_freq * t * 2 * np.pi)
G_note = np.sin(G_freq * t * 2 * np.pi)

A_note_left = normalize_stereo(A_note_left)
print(A_note_left)
print(C_note_right)
C_note_right = normalize_stereo(C_note_right)
audio = np.hstack((A_note_left, C_note_right))
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
play_obj.wait_done()

# concatenate notes
audio = np.hstack((A_note, C_note, Em_note, G_note))
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
print(audio)
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()

audio2 = np.add(A_note, C_note)
audio3 = np.add(Em_note, G_note)
audio4 = np.add(audio2, audio3)
audio4 *= 32767 / np.max(np.abs(audio4))
audio4 = audio4.astype(np.int16)
play_obj = sa.play_buffer(audio4, 1, 2, sample_rate)
play_obj.wait_done()

audio4 = []
maxamp = max( np.max(np.abs(audio2)), np.max(np.abs(audio3)) )
for i in range(len(audio3)):
    piece = np.array( [32767 / maxamp * audio2[i], 32767 / maxamp * audio3[i]] )
    audio4.append(piece.astype(np.int16))

audio4 = np.array(audio4)
play_obj = sa.play_buffer(audio4, 1, 2, sample_rate)
play_obj.wait_done()
