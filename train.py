# load the default config file and update with the local paths and settings.
import json
from TTS.utils.io import load_config
from TTS.bin.train_tacotron import train

if __name__ == '__main__':

    CONFIG = load_config('/content/TTS/TTS/tts/configs/config_manos.json')
    CONFIG['audio']['stats_path'] = None  # do not use mean and variance stats to normalizat spectrograms. Mean and variance stats need to be computed separately.
    CONFIG['output_path'] = '../'
    with open('config.json', 'w') as fp:
        json.dump(CONFIG, fp)

    #  python TTS/bin/train_tacotron.py --config_path config.json | tee training.log