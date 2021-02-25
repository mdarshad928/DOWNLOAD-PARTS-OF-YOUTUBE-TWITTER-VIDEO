#(Usage: StartTime partLength OutputFileName.extension) i.e. 01:01 00:40 Output.mkv)
import os, subprocess
#Taking Url input
t=('"' + input('Enter Video Url:  ') + '"')
while (True):
 try:
    strt, end, outfn= input("Enter StartTime partLength OutputFileName: ").split()
    break
 except:
    print("Enter Correctly")
y = "youtube-dl -g " + t          
output = subprocess.getoutput(y)
find=output.find('\n',50)        #To find the position of the string and to split it from their
urlvid='"' + output[0:find] + '"'
urlaudio='"' + output[find+1: ] + '"'
#function to run the ffmpeg command
def runcommand(commandarray):
	os.system(commandarray)
#final run
runcommand("ffmpeg" + " -ss " + str(strt) + " -i " + str(urlvid) + " -ss " + str(strt) + " -i " + str(urlaudio) + " -to " + str(end) + " -map 0:v -map 1:a -c:v libx264 -c:a aac "+ str(outfn))
