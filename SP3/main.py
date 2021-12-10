import subprocess
import os

if __name__ == '__main__':
    option = input("Choose exercise: ")
    if option == 1:
    #EXERCISE 1
    # Credit https://opensource.com/article/17/6/
    # ffmpeg-convert-media-file-formats
    #https://stackoverflow.com/questions/58742765/
    # convert-videos-from-264-to-265-hevc-with-ffmpeg
        print("Exercise 1")
        video_name = str(input("Write video's name and format in quotes "
                           "(Ex: 'bbb_cut.mp4'): "))

        # line commands on terminal
        # ffmpeg -i input.mp4 -c:v libaom-av1 -crf 30 -b:v 0 av1_test.mkv
        # ffmpeg -i input.mp4 -c:v vp9 -c:a libvorbis output.mkv

        #VP9
        os.system("ffmpeg -i "+video_name+" -c:v vp9 -c:a libvorbis outVP9.mkv")
        #VP8
        os.system("ffmpeg -i "+video_name+" -c:v vp8 -c:a libvorbis outVP8.mkv")
        #h265
        os.system("ffmpeg -i "+video_name+" -c:v libx265 -c:a "
                                          "libvorbis -vtag hvc1 outh265.mp4")
        #AV1 VERY slow (left commented)
        #os.system("ffmpeg -i "+video_name+" -c:v libaom-av1 "
        #                                 "-crf 63 -b:v 0 outav1.mkv")





    if option == 2:
    #EXERCISE 2
    # Credit https://unix.stackexchange.com/questions/
    # 233832/merge-two-video-clips-into-one-placing-them-next-to-each-other
        print("Exercise 2")
        video1_name = str(input("Write first video's name and format in quotes "
                           "(Ex: 'outVP9.mkv'): "))
        video2_name = str(input("Write second video's name and format "
                                "in quotes (Ex: 'outVP8.mkv'): "))

        # line command on terminal
        # ffmpeg -i left.mp4 -i right.mp4 -filter_complex hstack output.mp4
        os.system("ffmpeg -i "+video1_name+" -i "
                  +video1_name+" -filter_complex hstack merge.mp4")






    if option == 3:
    #EXERCISE 3
    # Credit: https://stackoverflow.com/questions/
    # 43826675/how-to-live-stream-a-local-video-using-ffmpeg/43830096
        print("Exercise 3")
        ip = str(input("Write, in quotes,  the IP and port to "
                       "stream bbb.mp4 on: (Ex: '127.0.0.1:23000'): "))

        # line command on terminal to start streaming
        # ffmpeg -i bbb.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000
        os.system("ffmpeg -i bbb.mp4 -v 0 -vcodec "
                  "mpeg4 -f mpegts udp://" + ip)

        # Command to write in VLC to watch the streaming:
        # udp://@127.0.0.1:23000

        # Command to watch the stream on ffmpeg by calling the terminal
        # ffplay udp://127.0.0.1:23000











