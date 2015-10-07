#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MplayerCtrl as mpc
import wx

class Frame(wx.Frame):
    def __init__(self, parent, id, files):
        wx.Frame.__init__(self, parent, id, size=(-1, -1))
        
        self.files = iter(files)
        self.mpc = mpc.MplayerCtrl(self, -1, 'C:/Program Files (x86)/MPlayer for Windows/mplayer.exe') # my path to the mplayer

        self.Bind(mpc.EVT_MEDIA_STARTED, self.media_started)
        self.Bind(mpc.EVT_MEDIA_FINISHED, self.media_finished)
        self.Bind(mpc.EVT_PROCESS_STARTED, self.process_started)
        self.Bind(mpc.EVT_PROCESS_STOPPED, self.process_stopped)
        self.Bind(mpc.EVT_STDERR, self.stderr)
        
        self.mpc.Loadfile(self.files.next())

        self.Center()
        self.Show()
        
    def media_started(self, evt):
        print '----------> Media started'
    def media_finished(self, evt):
        print '----------> Media finished'
        try:
            self.mpc.Loadfile(self.files.next()) # begin with the playback of the next file (self.files)
        except StopIteration:
            print 'no more files in the playlist!'
            print 'Quitting the mplayer '
            self.mpc.Destroy() # Destroy() quits/kills the mplayerprocess *and* destroys the widget
        # more information to iter() and .next() => http://docs.python.org/library/functions.html#iter
    def process_started(self, evt):
        print '----------> Process started'
    def process_stopped(self, evt):
        print '----------> Process stopped'
    def stderr(self, evt):
        print 'Stderr >>>', evt.data
            
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    f = Frame(None, -1, ['VID_20140210_131605.3gp'])#, '"The  unforgiven 2.flv"', '"Until It Sleeps.mp3"'])
    app.MainLoop()