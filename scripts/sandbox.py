#Features from other repos that I liked and should do changes to make it work.

#Convert video to audio
    if link[0] == "convert":
        try:
            username = os.getlogin()
            os.chdir(r'''C:\Users\{}\Desktop'''.format(username))
            if link[1] == "na":
                form_in = link[2]
                video1 = link[3]
                form_out = link[4]
                video2 = link[5]
                if (form_in == "avi" or form_in == "webm" or form_out == "mp4" or form_out == "mkv") and (form_out == "mp4" or form_out == "mkv"):
                    subprocess.call(r'''ffmpeg -i {} -c:v libx264 -an {}'''.format(video1,video2), shell = True)
                elif (form_in == "avi" or form_out == "mp4" or form_out == "mkv") and form_out == "webm":
                    subprocess.call(r'''ffmpeg -i {} -c:v libvpx-vp9 -b:v 2M -an {}'''.format(video1,video2),shell=True)
            else:
                form_in = link[1]
                video1 = link[2]
                form_out = link[3]
                video2 = link[4]
                if (form_in == "avi" or form_in == "webm" or form_out == "mp4" or form_out == "mkv") and (form_out == "mp4" or form_out == "mkv"):
                    subprocess.call(r'''ffmpeg -i {} -c:v libx264 -acodec aac {}'''.format(video1,video2), shell = True)
                elif (form_in == "avi" or form_in == "mp4" or form_in == "mkv") and form_out == "webm":
                    subprocess.call(r'''ffmpeg -i {} -c:v libvpx-vp9 -b:v 2M -cpu-used -5 -deadline realtime -c:a libvorbis {}'''.format(video1,video2), shell = True)
                elif (form_in == "mp4" or form_in == "mkv" or form_in == "webm") and form_out == "avi":
                    subprocess.call(r'''ffmpeg -i {} -c:v mpeg4 -vtag xvid -qscale:v 0 -acodec libmp3lame {}'''.format(video1,video2), shell = True)
                elif (form_in == "avi" or form_in == "webm" or form_in == "mp4" or form_in == "mkv" or form_in == "mp3" or form_in == "m4a") and (form_out == "m4a" or form_out == "mp3"):
                    subprocess.call(r'''ffmpeg -i {} {}'''.format(video1,video2), shell = True)
        except:
            print("Unable to process requested service!")
    #Images to video
    elif put.startswith("images to video "):
        try:
            framerate = link[3]
            username = os.getlogin()
            os.chdir(r'''C:\Users\{}\Desktop\Images'''.format(username))
            subprocess.call(r'''ffmpeg -framerate 1/{} -i img%03d.jpg -vcodec mpeg4 -vtag xvid -qscale:v 0 -crf 0 output.avi'''.format(framerate),shell=True)
            speak.say("Video created!")
            speak.runAndWait()
        except:
            print("Unable to create video file!")

    elif put.startswith("images to video "):
         try:
             framerate = link[3]
             home_dir = os.environ['HOME']
#             os.chdir(r'''C:\Users\{}\Desktop\Images'''.format(username))
             subprocess.call(r'''ffmpeg -framerate 1/{} -i '''+home_dir+'''Pictures/img%03d.jpg -vcodec mpeg4 -vtag xvid -qscale:v 0 -crf 0 output.avi'''.format(framerate),shell=True)
             speak.say("Video created!")
             speak.runAndWait()
         except:
             print("Unable to create video file!")

    elif put.startswith('news'):
        url = ('https://newsapi.org/v1/articles?source=cric-info&sortBy=latest&apiKey=e4fb8075753141e2af2b0cc5d0fbc9b2')
        try:
            newsresponse = requests.get(url)
            newsjson = newsresponse.json()
            speak.say('Our agents from report this')
            speak.runAndWait()
            print('  ====='+ say.upper() +'===== \n')
            i = 1
            for item in newsjson['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                i += 1
        except:
            print('Unable to retrieve data!')
