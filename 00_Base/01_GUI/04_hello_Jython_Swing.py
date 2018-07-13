# Jython(Python的Java实现)
# 唯一可用的GUI工具包是Java标准库包AWT和Swing

from javax.swing import *
import sys

def hello(event):
    print 'Hello,world'

btn = JButton('Hello')
btn.actionPerformed = hello

win = JFrame('Hello, Swing!')
win.contentPane.add(btn)

def closeHandler(event):
    sys.exit()

win.windowClosing = closeHandler

btn.size = win.size = 200,100
win.show()
