#!/usr/bin/python

#-*- coding: utf-8 -*-

#center.py

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self.__init__(parent,title=title,size=(1024,768))

        #self.Centre()
        #self.Show()


if __name__ == '__main__':

         app = wx.App()
         Example(None, title='Center')
         app.MainLoop()
