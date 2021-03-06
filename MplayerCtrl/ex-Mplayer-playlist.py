#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MplayerCtrl as mpc
import wx

class Frame(wx.Frame):
    def __init__(self, parent, id, files):
        wx.Frame.__init__(self, parent, id, size=(-1, -1))
        
        self.mpc = mpc.MplayerCtrl(self, -1, 'C:/Program Files (x86)/MPlayer for Windows/mplayer.exe') # my path to the mplayer

        self.Bind(mpc.EVT_MEDIA_STARTED, self.media_started)
        self.Bind(mpc.EVT_MEDIA_FINISHED, self.media_finished)
        self.Bind(mpc.EVT_PROCESS_STARTED, self.process_started)
        self.Bind(mpc.EVT_PROCESS_STOPPED, self.process_stopped)
        self.Bind(mpc.EVT_STDERR, self.stderr)
        
        for f in files:
            self.mpc.Loadfile(f, 1) # add to mplayers playlist

        self.Center()
        self.Show()
        

    def media_started(self, evt):
        print '----------> Media started'
        print 'Now playing:', self.mpc.GetMetaTitle()
        wx.FutureCall(3000, self.mpc.PtStep, '+') # after 3 seconds switch to the
                                                  # next file in the playlist
    def media_finished(self, evt):
        print '----------> Media finished'
    def process_started(self, evt):
        print '----------> Process started'
    def process_stopped(self, evt):
        print '----------> Process stopped'
    def stderr(self, evt):
        print 'Stderr >>>', evt.data
            
    
if __name__ == '__main__':
    start()
    app = wx.PySimpleApp()
    f = Frame(None, -1, ['testmovie.mpg', '"Until It Sleeps.mp3"', '"The  unforgiven 2.flv"'])
    app.MainLoop()