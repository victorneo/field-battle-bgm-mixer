## Field & Battle music generator

Most action RPGs, such as Kingdom Hearts, interleave field and battle music
when you are out exploring the world while soundtracks for these games have
both field and battle music as different tracks. This simple script will
generate a MP3 file interleaving the field and battle track to recreate the
in-game music experience.

This is a simple script and all it does is interleave battle music at fixed
intervals for now.

### Installation

[pydub](https://github.com/jiaaro/pydub/) is used to generate music. Please
install either libav or ffmpeg before proceeding:

```
# libav
brew install libav --with-libvorbis --with-sdl --with-theora

# ffmpeg
brew install ffmpeg --with-libvorbis --with-ffplay --with-theora
```

Then, install pydub and other required dependencies:

```
pip install -r requirements.txt
```

### Usage

Copy and rename your field music as `field.mp3` and battle music as
`battle.mp3` into the same directory as the script.

```
python gen.py
```

Play the resulting `output.mp3` in your favourite music player and enjoy the
in-game music experience!


### Configuration

None at the moment, but you can open `gen.py` in your text editor
to change the number of battles interleaved.

Commandline options may be in future.


## License

Copyright 2015 Victor Neo

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
