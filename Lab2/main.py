import subprocess
import os

if __name__ == '__main__':
    option = input("Choose exercise: ")
    if option == 1:
    #EXERCISE 1
    # Credit https://superuser.com/questions/138331/using-ffmpeg-to-cut-up-video
        print("Exercise 1")
        video_name = str(input("Write video's name and format in quotes "
                           "(Ex: 'bbb.mp4'): "))

        seconds = int(input("Cut N seconds of the video, choose N: "))
        minutes = 00

        # Check whether the time exceed 60 seconds to use the correct format
        if seconds > 59:
            minutes = seconds//60  # integer quotient
            seconds = seconds % 60  # remainder

        # line command on terminal
        # ffmpeg -ss 00:00:30.0 -i input.wmv -c copy -t 00:00:10.0 output.wmv
        os.system("ffmpeg -ss 00:00:00.0 -i " + video_name +
                  " -c copy -t 00:"+str(minutes)+
                  ":"+str(seconds)+" video_cut.mp4")

    if option == 2:
    #EXERCISE 2
    # Credit https://trac.ffmpeg.org/wiki/Histogram
        print("Exercise 2")
        video_name = str(input("Write video's name and format in quotes "
                           "(Ex: 'video_cut.mp4'): "))

    # To extract the YUV histogram
        # line command on terminal: ffplay video -vf histogram
        # subprocess.call(["ffplay", "bbb_cut.mp4", "-vf", "histogram"])

    # To extract YUV histogram and display it with the video
        # line command on terminal
        # ffmpeg -i video -vf "split=2[a][b],[b]histogram,
        # format=yuva444p[hh],[a][hh]overlay", output
        subprocess.call(["ffmpeg", "-i", video_name, "-vf",
                         "split=2[a][b],[b]histogram,"
                         "format=yuva444p[hh],[a][hh]overlay",
                         "overlay.mp4"])


    if option == 3:
    #EXERCISE 3
    # Credit: https://trac.ffmpeg.org/wiki/Scaling
        print("Exercise 3")
        video_name = str(input("Write video's name and format in quotes "
                       "(Ex: 'video_cut.mp4'): "))

        # line command on terminal
        # ffmpeg -i input -vf scale=360:240 output
        os.system("ffmpeg -i "+video_name+" -vf scale=360:240 video360x240.mp4")
        os.system("ffmpeg -i "+video_name+" -vf scale=160:120 video160x120.mp4")
        os.system("ffmpeg -i "+video_name+" -vf scale=1280:720 video720p.mp4")
        os.system("ffmpeg -i "+video_name+" -vf scale=720:480 video480p.mp4")

    if option == 4:
    #EXERCISE 4
    # Credit: https://trac.ffmpeg.org/wiki/AudioChannelManipulation
    #         https://stackoverflow.com/questions/9913032/how-can-i-
    #         extract-audio-from-video-with-ffmpeg
        print("Exercise 4")
        video_name = str(input("Write video's name and format in quotes "
                               "(Ex: 'video_cut.mp4'): "))

        # Extract audio from video
        # ffmpeg - i sample.mp4 -q:a 0 -map a sample.mp3
        os.system("ffmpeg -i " +video_name +" -q:a 0 -map a stereo.mp3")

        # Convert stereo to mono
        # line command on terminal: ffmpeg -i stereo.mp3 -ac 1 mono.mp3
        os.system("ffmpeg -i stereo.mp3 -ac 1 mono.mp3")

        # Change audio codec
        # ffmpeg -i input.mp3 -acodec flac -vcodec copy out.flac
        os.system("ffmpeg -i mono.mp3 -acodec flac -vcodec copy mono.flac")










