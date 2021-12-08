import subprocess
import os

def search(list, platform): #Function to search elements in a list
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False


if __name__ == '__main__':
    option = input("Choose exercise: ")
    if option == 1:
    #EXERCISE 1
    # Credit http://trac.ffmpeg.org/wiki/Debug/MacroblocksAndMotionVectors
        print("Exercise 1")
        video_name = str(input("Write video's name and format in quotes "
                           "(Ex: 'bbb_cut.mp4'): "))

        # line command on terminal
        # ffmpeg -flags2 +export_mvs -i input.mp4 -vf codecview=mv=pf+bf+bb output.mp4
        os.system("ffmpeg -flags2 +export_mvs -i "
                  +video_name+" -vf codecview=mv=pf+bf+bb motion_v.mp4")






    if option == 2:
    #EXERCISE 2
    # Credit    https://trac.ffmpeg.org/wiki/Encode/AAC
    #https://superuser.com/questions/370625/ffmpeg-command-to-convert-mp3-to-aac

        print("Exercise 2")
        video_name = str(input("Write video's name and format in quotes "
                           "(Ex: 'bbb.mp4'): "))

        # Cut into a 1 minute video
        os.system("ffmpeg -ss 00:00:00.0 -i " + video_name +
                " -c copy -t 00:01:00 1min_cut.mp4")

        # Export stereo mp3 track
        os.system("ffmpeg -i 1min_cut.mp4 -c:a mp3 stereo.mp3")
            # -q:a is quality (0 best, 9 worst)
            # -b:a is bitrate
            # -map is done to extract whichever stream (a: audio, v:video)

        # Export AAC with lower bitrate
        os.system("ffmpeg -i stereo.mp3 -c:a aac -b:a 64k output.m4a")

        # Package everything
        os.system("ffmpeg -i 1min_cut.mp4 -i stereo.mp3 -i output.m4a "
                  "-map 0:v -map 1:a -map 2:a -c copy container.mp4")








    if option == 3:
    #EXERCISE 3
    # Credit: https://pretagteam.com/question/how-to-get-
    # ffprobe-metadata-as-variable-to-parse-in-python
    # https://www.pythontutorial.net/python-basics/python-read-text-file/
        print("Exercise 3")
        container_name = str(input("Write container's name and format in quotes "
                       "(Ex: 'container.mp4'): "))
        os.system("ffprobe -v error -show_entries stream=index,codec_name "
                  + container_name + " >containerInfo.txt")
        file = open('containerInfo.txt', 'r')

        lines = list()
        lines = file.readlines()
        codec = [] #Array containing codecs
        for line in lines:
            if line[0:10]=="codec_name":
                codec.append(line[11:])

        print("Tracks detected: ")
        print(codec)
        print("\n")

        #Broadcast classification
        if search(codec, "avs\n") or search(codec, "dra\n") \
                or search(codec, "mp2\n"):
            print("Best Broadcast: DTMB")

        elif search(codec, "h264\n") or search(codec, "mpeg2video\n"):

            if search(codec, "aac:latm\n"):
                print("Best Broadcast: ISDB-T")
            elif search(codec, "aac\n") or search(codec, "mp3\n"):
                print("Best Broadcast: DVB-T")
            elif search(codec, "ac3\n"):
                print("Best Broadcast: ATSC")
            else:
                print("No audio detected. Best "
                      "broadcast: either DVB-T/ATSC/ISDB-T")
        else:
            print("Error: Does not fit in any broadcasting standard")
        print("\n")

        # DVB-T: mpeg2video, h264 / aac, ac3, mp3
        # ATSC: mpeg2video, h264 / ac3
        # ISDB-T: mpeg2video, h264 / aac:latm
        # DTMB: AVS, h264 / DRA, aac, ac3, mp2, mp3

        file.close()







    if option == 4:
    #EXERCISE 4
    # Credit: https://trac.ffmpeg.org/wiki/ExtractSubtitles
        print("Exercise 4")
        container_name = str(input("Write video's name and format in quotes "
                               "(Ex: 'video_cut.mp4'): "))

        os.system("ffprobe -v error -show_entries stream=index,codec_name "
                  + container_name + " >containerInfo.txt")
        file = open('containerInfo.txt', 'r')

        lines = list()
        lines = file.readlines()
        codec = []  # Array containing codecs
        for line in lines:
            if line[0:10] == "codec_name":
                codec.append(line[11:])

        print("Tracks detected: ")
        print(codec)
        print("\n")

        #Looks for subtitles in the container (in ssa and dvb_teletext formats)
        if search(codec, "ssa\n"):
            os.system("ffmpeg -ssa text -i "+container_name+" subtitles.srt")
            subtitle = str("subtitles.srt")
        elif search(codec, "dvb_teletext\n"):
            os.system("ffmpeg -dvb_teletext text -i "
                      + container_name + " subtitles.srt")
            subtitle = str("subtitles.srt")

        else:
            print("No subtitles found. Using default file")
            subtitle = str("default_subtitles.srt")
            print("\n")


        # Generate video with subtitles
        os.system("ffmpeg -i "+ container_name +" -vf subtitles="
                  +subtitle+" subtitled.mp4")

        file.close()











