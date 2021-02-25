import os, subprocess
#y=input("youtube dl command:  ")
t=('"' + input('Video Url:  ') + '"')
while (True):
 try:
    strt, end, outfn= input("Enter StartTime VideoLength OutputFileName: ").split()
    break
 except:
    print("Enter Correctly")
y = "youtube-dl -g " + t
#os.system(ffmpeg -ss 12:15 -i "1st-URL" -ss 12:15 -i "2nd-URL" -t 5:15 -map 0:v -map 1:a -c:v libx264 -c:a aac output.mkv)
output = subprocess.getoutput(y)
#print(output)
find=output.find('\n',50)        #To find the position of the string and to split it from their
urlvid='"' + output[0:find] + '"'
urlaudio='"' + output[find+1: ] + '"'
#print(urlvid)
#def extract(video,audio):
#command = "ffmpeg -ss 00:00:15.00 -i "str(urlvid)" -t 00:00:10.00 -c copy out.mp4"#.format(video=video, audio=audio)
#subprocess.call(command,shell=True)
#extract(urlvid,urlaudio)
#os.system(ffmpeg -ss 1:01 -i '{urlvid}' -ss 01:01 -i '{urlaudio}' -t 1:00 -map 0:v -map 1:a -c:v libx264 -c:a aac output.mkv)
def runcommand(commandarray):
	os.system(commandarray)
#print("ffmpeg" + " -ss " + str(strt) + " -i " + str(urlvid) + " -ss " + str(strt) + " -i " + str(urlaudio) + " -to " + str(end) + " -map 0:v -map 1:a -c:v libx264 -c:a aac "+ "video_file.mp4")
#runcommand("ffmpeg" + " -ss " + str(01.01) + " -i " + str(urlvid) + " -t " + str(3.20) + " -c "+ "copy video_file.mp4")
runcommand("ffmpeg" + " -ss " + str(strt) + " -i " + str(urlvid) + " -ss " + str(strt) + " -i " + str(urlaudio) + " -to " + str(end) + " -map 0:v -map 1:a -c:v libx264 -c:a aac "+ str(outfn))
