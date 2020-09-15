import subprocess
import re
class Controller(object):
    def __init__(self, fileName):
        self._fileName = fileName

    def getAudioInfo(self):
        ffmpegCmd = ['/usr/bin/ffmpeg', '-nostats', '-i', self._fileName,
                     '-filter_complex', 'ebur128=peak=true', '-f', 'null', '-']
        p = subprocess.Popen(ffmpegCmd, stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, stdOutStr = p.communicate()
        # 300 последних символов выведено имперически, должно хватить с запасом
        stdOutStr = stdOutStr[len(stdOutStr) - 300:len(stdOutStr)].decode('utf-8')
        print(stdOutStr)
        integratedLoudness = re.search(r'I:\s+(-?\d+.\d+)\sLUFS',stdOutStr)
        luValue = re.search(r'LRA:\s+(-?\d+.\d+)\sLU',stdOutStr)
        rmsPeak = re.search(r'Peak:\s+(-?\d+.\d+)\sdBFS',stdOutStr)
        return integratedLoudness.group(1), luValue.group(1), rmsPeak.group(1)

if __name__ == "__main__":
    nameFile = sys.argv[1]
    contr = Controller(nameFile)
    contr.getAudioInfo()
