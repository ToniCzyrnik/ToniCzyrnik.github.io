# Repository for my personal Blog


The main blog directory needs to have the most files. Otherwise, the postings will not show.

## How to start hugo

### Install hugo
    $ brew install hugo

### Install submodules

	$ git submodule update --init --recursive
 

### Build locally
	$ hugo server

## Memes

- Font: Comic Sans
- Black Edge: 7 pt

## Images

Resize to 720 pixel width, 90 % quality strip all EXIF data:

	convert IMG_XXX.jpeg -resize x720 -quality 90 -strip img1.jpeg

To reduce the image to a target size:

	jpegoptim img1.jpeg --size=100k

## Gifs

	ffmpeg -ss 5 -t 7 -i IMG_xxx.mov -vf "fps=10, scale=320:-1:flags=lanczos" -loop 0  output.gif
	
- ss: Skip the first seconds
- t: length of the gif
- i: name of the input
- fps: frames per second
- scale: 320 pixels wide, aspect ration constant
- loop: 0 means infinite, - 1 means no looping, 1 means one loop (playing twice)

## Image Integration

	<figure>
    	<img src="./.jpg" alt="" height=auto width="400"/>
    	<figcaption></figcaption>
	</figure>



## Grammar Check

	https://www.reverso.net/spell-checker/english-spelling-grammar/
	
	https://www.deepl.com/write
	
## Colours

https://coolors.co/palette/e63946-f1faee-a8dadc-457b9d-1d3557

Red: #E63946
Dark Blue: #1D3557
Blue: #457B9D
Light Blue: #A8DADC
Light Green: #F1FAEE
