import random
# from utils.videoCreate import createVideo
from moviepy.editor import (
    CompositeVideoClip, CompositeAudioClip,
    VideoFileClip, AudioFileClip, ImageClip, TextClip,
    concatenate_videoclips, concatenate_audioclips
)
from moviepy.video.tools.cuts import find_video_period

video_file = 'video.mp4'
audio_file = 'audio.mp3'
image_file = 'image.png'
output = 'output.mp4'
screensize = (1980, 1280)
texts = "PEGOU FOGO! ESPERA AÍ! MERMÃO, o técnico da Seleção NÃO PODE... DEBATE FERVE sobre Diniz!"

# txt_clip = TextClip(texts, 
#                     fontsize=32,
#                     color="white",
#                     align='center',
#                     method='caption',
#                     size=(660, None))
# txt_clip = CompositeVideoClip( [txt_clip.set_pos('center')],
#                     size=screensize2)
# video = video.resize(screensize1)
    # video = video.rotate(180)
# video = video.crop(x_center=1920 / 2, y_center=1080 / 4, width=1920, height=1080)

# def createVideo(video, image, output):
#     print('CREATE VIDEO')
#     txt_clip = TextClip(texts, fontsize=70)
#     txt_clip = txt_clip.set_pos('center').set_duration(5)
    
#     video = (VideoFileClip(video, audio=False).subclip(0))
    
#     image = ImageClip(image, duration=5)
    
#     print(str(video.duration))  
    
#     # clip = CompositeVideoClip([image, video, txt_clip])
#     clip = CompositeVideoClip([image, video, txt_clip], size = screensize)
#     clip.write_videofile('output.mp4')

def createVideo(video_file, audio_file, image_file, output):
    
    video = VideoFileClip(video_file).subclip(0, 15).resize(2)
    texto = TextClip(texts, fontsize=70).set_duration(10)
    audio = AudioFileClip(audio_file).subclip(15, 30)
    image = ImageClip(image_file, duration=1)
    
    print(str(video.duration), str(video.size), str(video.fps)) 
     
    compose = CompositeVideoClip([video, image, texto], size = screensize)
    compose.audio = audio

    compose.write_videofile(output)


createVideo(
    video_file,
    audio_file,
    image_file,
    output
)
