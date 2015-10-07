import os
import wx
import MplayerCtrl as mpc
import wx.lib.buttons as buttons

dirName = os.path.dirname(os.path.abspath(__file__))
bitmapDir = os.path.join(dirName, 'bitmaps')

class Frame(wx.Frame):
    
    #----------------------------------------------------------------------
    def __init__(self, parent, id, title, mplayer):
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self)
        
        sp = wx.StandardPaths.Get()
        self.currentFolder = sp.GetDocumentsDir()

        self.create_menu()
        self.mpc = mpc.MplayerCtrl(self.panel, -1, mplayer)
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        controlSizer = self.build_controls()
        mainSizer.Add(self.mpc, 1, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(controlSizer, 0, wx.ALL|wx.CENTER, 5)
        self.panel.SetSizer(mainSizer)
        
        self.Bind(mpc.EVT_MEDIA_STARTED, self.on_media_started)
        self.Bind(mpc.EVT_MEDIA_FINISHED, self.on_media_finished)
        self.Bind(mpc.EVT_PROCESS_STARTED, self.on_process_started)
        self.Bind(mpc.EVT_PROCESS_STOPPED, self.on_process_stopped)
        
        self.Show()
        self.panel.Layout()
        
    #----------------------------------------------------------------------
    def build_btn(self, btnDict, sizer):
        """"""
        bmp = btnDict['bitmap']
        handler = btnDict['handler']
                
        img = wx.Bitmap(os.path.join(bitmapDir, bmp))
        btn = buttons.GenBitmapButton(self.panel, bitmap=img,
                                      name=btnDict['name'])
        btn.SetInitialSize()
        btn.Bind(wx.EVT_BUTTON, handler)
        sizer.Add(btn, 0, wx.LEFT, 3)
        
    #----------------------------------------------------------------------
    def build_controls(self):
        """
        Builds the audio bar controls
        """
        controlSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        btnData = [{'bitmap':'player_pause.png', 
                    'handler':self.on_pause, 'name':'pause'},
                   {'bitmap':'player_stop.png',
                    'handler':self.on_stop, 'name':'stop'}]
        for btn in btnData:
            self.build_btn(btn, controlSizer)
            
        return controlSizer
    
    #----------------------------------------------------------------------
    def create_menu(self):
        """
        Creates a menu
        """
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        add_file_menu_item = fileMenu.Append(wx.NewId(), "&Add File", "Add Media File")
        menubar.Append(fileMenu, '&File')
        
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_add_file, add_file_menu_item)
        
    #----------------------------------------------------------------------
    def on_add_file(self, event):
        """
        """
        wildcard = "Media Files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentFolder, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.currentFolder = os.path.dirname(path[0])
            trackPath = '"%s"' % path.replace("\\", "/")
            self.mpc.Loadfile(trackPath)
        
        
    #----------------------------------------------------------------------
    def on_media_started(self, event):
        print 'Media started!'
        
    #----------------------------------------------------------------------
    def on_media_finished(self, event):
        print 'Media finished!'
        self.mpc.Quit() # quits the Mplayer-process
        
    #----------------------------------------------------------------------
    def on_pause(self, event):
        """"""
        self.mpc.Pause()
        
    #----------------------------------------------------------------------
    def on_process_started(self, event):
        print 'Process started!'
        
    #----------------------------------------------------------------------
    def on_process_stopped(self, event):
        print 'Process stopped!'
        
    #----------------------------------------------------------------------
    def on_stop(self, event):
        """"""
        print "stopping..."
        self.mpc.Stop()

#----------------------------------------------------------------------
if __name__ == "__main__":
    import os, sys
    
    paths = [r'C:/Program Files (x86)/MPlayer for Windows/mplayer.exe',
             r'E:\MPlayer-rtm-svn-31170\mplayer.exe']
    mplayerPath = None
    for path in paths:
        if os.path.exists(path):
            mplayerPath = path
        
    if not mplayerPath:
        print "mplayer not found!"
        sys.exit()
            
    app = wx.App(redirect=False)
    frame = Frame(None, -1, 'Hello MplayerCtrl', mplayerPath)
    app.MainLoop()
