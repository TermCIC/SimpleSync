from tkinter import *
from tkinter.filedialog import askdirectory
import time
import os
from colorama import Fore
from colorama import init
from dirsync import sync
init()

print(Fore.LIGHTGREEN_EX + '簡單資料備份 by TermiteChiu')

sourcePath = '備份資料夾路徑.....'
mirrorPath = '同步資料夾路徑.....'


def defSourcePath():
    global sourcePath
    sourcePath = askdirectory()
    label1['text'] = '備份資料夾路徑為 ' + sourcePath
    pass


def defMirrorPath():
    global mirrorPath
    mirrorPath = askdirectory()
    label2['text'] = '同步資料夾路徑為 ' + mirrorPath
    pass


def runSyncTwoway():
    sync(sourcePath, mirrorPath, 'sync', verbose=True, create=True)
    sync(sourcePath, mirrorPath, 'update', twoway=True)
    for dirname, dirnames, filenames in os.walk(sourcePath):
        for subdirname in dirnames:
            newSourcePath = os.path.join(dirname, subdirname)
            newMirrorPath = newSourcePath.replace(sourcePath, mirrorPath)
            print('正在同步資料夾 {} 與 {} .....'.format(newSourcePath, newMirrorPath))
            sync(newSourcePath, newMirrorPath, 'sync', verbose=True, create=True)
            sync(newSourcePath, newMirrorPath, 'update', twoway=True)
            print('資料夾 {} 與 {} 同步完成。'.format(newSourcePath, newMirrorPath))

    sync(mirrorPath, sourcePath, 'sync', verbose=True, create=True)
    sync(mirrorPath, sourcePath, 'update', twoway=True)
    for dirname, dirnames, filenames in os.walk(sourcePath):
        for subdirname in dirnames:
            newSourcePath = os.path.join(dirname, subdirname)
            newMirrorPath = newSourcePath.replace(sourcePath, mirrorPath)
            print('正在同步資料夾 {} 與 {} .....'.format(newMirrorPath, newSourcePath))
            sync(newSourcePath, newMirrorPath, 'sync', verbose=True, create=True)
            sync(newSourcePath, newMirrorPath, 'update', twoway=True)
            print('資料夾 {} 與 {} 同步完成。'.format(newMirrorPath, newSourcePath))


def runSyncOneway():
    sync(sourcePath, mirrorPath, 'sync', verbose=True, create=True)
    sync(sourcePath, mirrorPath, 'update', twoway=True)
    for dirname, dirnames, filenames in os.walk(sourcePath):
        for subdirname in dirnames:
            newSourcePath = os.path.join(dirname, subdirname)
            newMirrorPath = newSourcePath.replace(sourcePath, mirrorPath)
            print('正在同步資料夾 {} 與 {} .....'.format(newSourcePath, newMirrorPath))
            sync(newSourcePath, newMirrorPath, 'sync', verbose=True, create=True)
            sync(newSourcePath, newMirrorPath, 'update', twoway=True)
            print('資料夾 {} 與 {} 同步完成。'.format(newSourcePath, newMirrorPath))


def runUpdate():
    sync(sourcePath, mirrorPath, 'update', twoway=True)
    for dirname, dirnames, filenames in os.walk(sourcePath):
        for subdirname in dirnames:
            newSourcePath = os.path.join(dirname, subdirname)
            newMirrorPath = newSourcePath.replace(sourcePath, mirrorPath)
            print('正在同步資料夾 {} 與 {} .....'.format(newSourcePath, newMirrorPath))
            sync(newSourcePath, newMirrorPath, 'update', twoway=True)
            print('資料夾 {} 與 {} 同步完成。'.format(newSourcePath, newMirrorPath))

    sync(mirrorPath, sourcePath, 'update', twoway=True)
    for dirname, dirnames, filenames in os.walk(sourcePath):
        for subdirname in dirnames:
            newSourcePath = os.path.join(dirname, subdirname)
            newMirrorPath = newSourcePath.replace(sourcePath, mirrorPath)
            print('正在同步資料夾 {} 與 {} .....'.format(newMirrorPath, newSourcePath))
            sync(newSourcePath, newMirrorPath, 'update', twoway=True)
            print('資料夾 {} 與 {} 同步完成。'.format(newMirrorPath, newSourcePath))


root = Tk()
root.title("簡單資料備份 by TermiteChiu")
root.geometry('450x130')

label1 = Label(root, text=sourcePath)
label1.grid(column=2, row=1)
label2 = Label(root, text=mirrorPath)
label2.grid(column=2, row=2)
button1 = Button(root, text="選擇備份資料夾", command=defSourcePath)
button1.grid(column=1, row=1)
button2 = Button(root, text="選擇同步資料夾", command=defMirrorPath)
button2.grid(column=1, row=2)
button3 = Button(root, text="......單向同步......", command=runSyncOneway)
button3.grid(column=1, row=3)
label3 = Label(root, text='檔案複製: 備份資料夾--->同步資料夾')
label3.grid(column=2, row=3)
button4 = Button(root, text="......雙向同步......", command=runSyncTwoway)
button4.grid(column=1, row=4)
label4 = Label(root, text='檔案複製: 備份資料夾<-->同步資料夾')
label4.grid(column=2, row=4)
button5 = Button(root, text="..僅更新舊檔案..", command=runUpdate)
button5.grid(column=1, row=5)
label4 = Label(root, text='不複製、僅更新現存檔案版本: 備份資料夾<-->同步資料夾')
label4.grid(column=2, row=5)
root.resizable(0, 0)
root.mainloop()
