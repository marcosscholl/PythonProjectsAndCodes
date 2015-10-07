import wx
import MplayerCtrl as mpc

class Frame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id)

        self.mpc = mpc.MplayerCtrl(self, -1, u'C:/Program Files (x86)/MPlayer for Windows/mplayer.exe', media_file=u'VID_20140210_131605.3gp')

        self.Bind(mpc.EVT_MEDIA_STARTED, self.on_media_started)
        self.Bind(mpc.EVT_MEDIA_FINISHED, self.on_media_finished)
        self.Bind(mpc.EVT_PROCESS_STARTED, self.on_process_started)
        self.Bind(mpc.EVT_PROCESS_STOPPED, self.on_process_stopped)

        self.Show()


    def media_started(self, evt):
        print '----------> Media started'
    def media_finished(self, evt):
        print '----------> Media finished'
    def process_started(self, evt):
        print '----------> Process started'
        #self.mpc.Loadfile(u'VID_20140210_131605.3gp')
    def process_stopped(self, evt):
        print '----------> Process stopped'

    def key_down(self, evt):
        k = evt.GetKeyCode()
        if k in (43, 45) and self.mpc.playing:
            volume = self.mpc.volume
            if k == 43:
                if not volume > 95:
                    self.mpc.volume += 5
            elif k == 45:
                if not volume <= 5:
                    self.mpc.volume -= 5
        evt.Skip()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    f = Frame(None, -1)
    app.MainLoop()
    