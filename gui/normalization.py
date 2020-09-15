import wave
import numpy as np
import math
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as qtPlot
import wavio
qtPlot.setConfigOption('background', 'w')
qtPlot.setConfigOption('foreground', 'k')
class Normalization(object):
    def __init__(self,targetDb,filePath):
        self.targetDb = targetDb
        self.filePath = filePath
        print("file: {0} \nDB: {1}",self.filePath,self.targetDb)

    types = {
        1: np.int8,
        2: np.int16,
        4: np.int32
    }

    nchannels = 0  # кол-во каналов
    sampwidth = 0  # число бит на сэмпл
    framerate = 0  # числов фреймов в секунду
    nframes = 0  # общее число фреймов
    comptype = 0  # тип сжатия
    compname = 0  # имя типа сжатия


    def readWav(self,pathToFile):
        wav = wave.open(pathToFile, mode="r")
        global nchannels
        global sampwidth
        global framerate
        global nframes
        global comptype
        global compname
        (nchannels, sampwidth, framerate, nframes, comptype,
         compname) = wav.getparams()  # считываем все данные заголовка
        # считываем все фреймы и возвращаем
        print("byte {0}".format(sampwidth))
        return wav.readframes(nframes)


    def dbToAmplitude(self,targetDb):
        maxWavValue = 65535  # 2^16 == 16 bit wav audio
        return (math.pow(10, targetDb/20))*maxWavValue


    def amplitudeToDb(self,amplitudeValue):
        maxWavValue = 65535  # 2^16 == 16 bit wav audio
        return 20*math.log10(amplitudeValue/maxWavValue)


    def frameDataToSamples(self,data):
        return np.fromstring(data, dtype=self.types[sampwidth])


    def wavValueToDb(self,value):
        return 20 * math.log10(abs(value) / float(32))


    def format_time(self,xArray):
        yArray = []
        cutKoeff = 5
        global duration
        for pos in range(len(xArray)):
            progress = pos / framerate * cutKoeff
            mins, secs = divmod(progress, 60)
            hours, mins = divmod(mins, 60)
    #        out = "%d:%02d" % (mins, secs)
            if hours > 0:
                out = "%d:" % hours
            fout = '{:d}:{:.2f}'.format(int(mins), secs)
            yArray.append(fout)
        return yArray


    def printChar(self,xArray, yArray):
        win = qtPlot.GraphicsWindow()
        win.setWindowTitle('Audio plot')
        xdict = dict(enumerate(yArray))
        #bg1 = qtPlot.BarGraphItem(x=xArray,y1=300, width=0.5, brush='r')
        stringAxis = qtPlot.AxisItem(orientation='bottom')
        xtickts = [list(xdict.items())[::math.ceil(len(xArray)/10)]]
        stringAxis.setTicks(xtickts)
        plot = win.addPlot(axisItems={'bottom': stringAxis})
        plot.setXRange(0, len(xArray), padding=0)
        #plot.setYRange(min(xArray), max(xArray), padding=0)
        plot.setYRange(-32768, 32768, padding=0)
        curve = plot.plot(list(xdict.keys()),
                          xArray)
        curve.setPen(qtPlot.mkPen(width=1, color=(0, 0, 0)))
        # QtEventLoop
        if __name__ == '__main__':
            import sys
            if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                QtGui.QApplication.instance().exec_()
        
       # return curve


    def printBarChar(self,xDict):
        # barChart

        win = qtPlot.GraphicsWindow()
        win.setWindowTitle('Histogramm plot')
        x = list(xDict.keys())
        y1 = list(xDict.values())
        #
        stringAxis = qtPlot.AxisItem(orientation='bottom')

        plot = win.addPlot(axisItems={'bottom': stringAxis})
        
        curve = plot.plot(x,
                          y1)
        curve.setPen(qtPlot.mkPen(width=1, color=(0, 0, 0)))
        # QtEventLoop
        if __name__ == '__main__':
            import sys
            if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                QtGui.QApplication.instance().exec_()


    def normalize(self,audioFileName, targetDb):
        targetDb = targetDb - 1
        print('normalization file {0} with {1}'.format(audioFileName,targetDb))
        frameData = self.readWav(audioFileName)
        duration = nframes / framerate
        print('duration(sec) {0}'.format(duration))
        # только для одного канала!
        if (nchannels > 1):
            print("Error! Channel count > 1!")
            sys.exit()

        samplesArray = self.frameDataToSamples(frameData)

        #уменьшаем громкость участков выходящих за предел loundnessLimit
        startInterval = 0
        endInterval = 0
        intervalStarted = False
        intervalEnded = False

        # for i in range(0,len(samplesArray)):
        #     normalizedInterval = []
        #     if (samplesArray[i]>loundnessLimit and not intervalStarted):
        #         startInterval = i
        #         intervalStarted = True
        #     elif (samplesArray[i]<loundnessLimit and intervalStarted):
        #         endInterval = i
        #         intervalEnded = True
        #         intervalStarted = False
        #         normalizedInterval = normalizeInterval(samplesArray[startInterval:endInterval])
        #         print("start {0} end {1}".format(startInterval,endInterval))
        #         samplesArray[startInterval:endInterval] = normalizedInterval[:]

        # рисуем график

        cutKoeff = 5  # оставляем каждый 5-ый семпл, иначе долго рисуется
        self.plotSamplesArray1 = samplesArray[0::cutKoeff]
        self.yArray1 = self.format_time(self.plotSamplesArray1)
        self.printChar(self.plotSamplesArray1, self.yArray1)

        # проводим нормализацию
        maxDb = max(samplesArray)  # max level loundness

        minDb = min(samplesArray)
        print("max {0} min {1} ".format(maxDb, minDb))
        maxNormDb = self.dbToAmplitude(targetDb)
       # maxNormDb = 4134.915861316499 # max normalize loudness
        # 1 - считаем гистограмму
        self.histogramm = dict()
        for i in range(minDb, maxDb, 1):
            self.histogramm[i] = 0

        # rmsSum = 0
        # for i in samplesArray:
        #     rmsSum += i*i
        # print("RMS: {0}".format(rmsSum))
        # rmsSum = math.sqrt(rmsSum/len(samplesArray))
        # print("RMS: {0}".format(rmsSum))
        # print("RMS: {0}".format((58408.130230595016/56425.2255494178)))
        # for i in range(0,len(samplesArray)):
        #     samplesArray[i] = samplesArray[i]*(56425.2255494178/58408.130230595016)  #targetRMS/rmsSum

        for i in samplesArray:
            if (self.histogramm.get(i) != None):
                self.histogramm[i] += 1
            else:
                self.histogramm[i] = 1

        #self.printBarChar(self.histogramm)
        print("length {0}".format(len(samplesArray)))

        # 2 - вычисляем фактор нормализации
        alpha = maxNormDb / len(samplesArray)
        histAvg = np.mean(samplesArray)
        sigm = np.std(samplesArray)
        print("histAvg: {0}".format(histAvg))
        LUT = dict()

        LUT[minDb] = self.histogramm[minDb]
        lutMin = LUT[minDb]
        for i in range(minDb+1, maxDb, 1):
            #LUT[i] = LUT[i - 1] + histogramm[i]
            LUT[i] = LUT[i - 1] + self.histogramm[i]

        self.printBarChar(LUT)
        for i in range(minDb, maxDb, 1):
            #LUT[i] = LUT[i - 1] + histogramm[i]
            LUT[i] /= len(samplesArray)
            LUT[i] *= maxNormDb*2
            LUT[i] -= maxNormDb

        #

        #sk = dict()
        #for i in samplesArray:
        #    if (LUT[i] is not None):
        #        sk[i] = LUT[i]
        #*alpha

        #printBarChar(sk)

        newSamplesArray = []
        for i in list(range(0, len(samplesArray))):
            if (LUT.get(samplesArray[i]) != None):
                newSamplesArray.append(round(LUT.get(samplesArray[i])))
        #        print("{0} \n".format(round(LUT.get(samplesArray[i]))))

#графики
        cutKoeff = 5  # оставляем каждый 5-ый семпл, иначе долго рисуется
        self.plotSamplesArray2 = newSamplesArray[0::cutKoeff]
        self.yArray2 = self.format_time(self.plotSamplesArray2)

        self.histogramm2 = dict()
        for i in range(minDb, maxDb, 1):
           self.histogramm2[i] = 0
        for i in newSamplesArray:
           if (self.histogramm2.get(i) != None):
               self.histogramm2[i] += 1
           else:
               self.histogramm2[i] = 1
        #self.printBarChar(newHistogramm)

        npSmpArray = np.array(newSamplesArray)
        wavio.write("test.wav", npSmpArray, framerate, scale='none', sampwidth=2)
        print("All ok!")


    #main

    #filePath = "../audio/audio.wav"
    #targetDb = -24
    #normalize(filePath, targetDb)
if __name__ == "__main__":
    if (len(sys.argv) > 2):

        filePath = sys.argv[1]
        targetDb = float(sys.argv[2])  
        norm = Normalization(filePath, targetDb)    
        norm.normalize(filePath, targetDb)
    else:
        print("This application normalizes the sound.")
        print("Example of use: ")
        print("python3 wav.py /home/user/audio.wav -23.0 ")
        print("python3 wav.py /home/user/audio.wav --path to file")
        print("-23.0 --target LUFS\n")


