from moviepy.editor import (
    CompositeVideoClip, CompositeAudioClip,
    VideoFileClip, AudioFileClip, ImageClip, TextClip,
    concatenate_videoclips, concatenate_audioclips
)

def createVideo(video, image, output):
    print('CREATE VIDEO')
    clip = VideoFileClip(video).subclip(50,60)
    video = CompositeVideoClip([clip])
    video.write_videofile("my_concatenation.mp4")