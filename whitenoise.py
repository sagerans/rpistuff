'''
This is a white, brown, pink, and green noise generator.
It relies on the numpy and simpleaudio Python packages.

The user may input a run time in seconds and select the type of
noise they want.

'''
import numpy as np
import simpleaudio as sa

sample_rate = 192000
perturb_range = (0.9, 1.1)

def perturb(wave):
    '''
    The purpose of this function is to accept a frequency sample array
    and perturb it randomly to vary the output a bit and improve the 
    noisiness of the signal.
    '''
    wavetime = len(wave)
    pert_rate = 0.001
    rands = np.random.uniform(perturb_range[0], perturb_range[1], len(wave))
    for i in range(len(wave) // int(wavetime * pert_rate)):
        wave[int(wavetime * pert_rate * i)] *= rands[int(wavetime * pert_rate * i)]

    return wave

# full set of random frequencies
def white_noise(t):
    T = t 
    sample_rate = 192000
    white = np.random.random_sample(size = int(T * sample_rate))
    t = np.linspace(0, 1.0 * T, int(T * sample_rate), False)
    print(white)
    audio = white
    # audio = np.sin(white * t * 2 * np.pi)
    audio *= 32767 / np.max(np.abs(white))
    print(audio)
    audio = audio.astype(np.int16)

    play_ob = sa.play_buffer(audio,1,2,sample_rate)
    play_ob.wait_done()

def brown_noise(T):
    '''
    Brown noise is a random mix of frequencies from about 20Hz to 20kHz
    that heavily weights lower frequencies and essentially cuts out higher
    frequencies. This can be modeled with exponential decay.

    This function first creates an array of frequencies to sample, then
    weights those frequencies using a 2^(-x) curve.
    '''

    freqs = np.array([100*2**x for x in np.linspace(-2,8,120)]).astype(np.int16)
    print(freqs)
    t = np.linspace(0, 1.0 * T, int(T * sample_rate), False)
    dist_waves = []
    i = 1
    for freq in freqs:
        print('Perturbing Wave', i, '...')
        wave = np.sin(freq * t * 2 * np.pi)
        wave = perturb(wave)
        dist_waves.append(wave)
        i += 1

    print(dist_waves)



def pink_noise(t):
    pass

def green_noise(t):
    pass

def blue_noise(t):
    pass


if __name__ == "__main__":
    time = int(input('For how long would you like to hear noise? '))
    print('Please select a type of noise:')
    choices = '\t[1] White\n\t[2] Brown\n\t[3] Pink\n\t[4] Green\n\t[5] Blue'
    print(choices)
    choice = input()

    match choice:
        case '1':
            white_noise(time)
        case '2':
            brown_noise(time)
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case _:
            print('You didn\'t pick a valid number. Bye!')


