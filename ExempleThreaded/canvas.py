import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.rcParams.update({'font.size': 8})

class Canvas(FigureCanvas):
  def __init__(self,parent,dpi=100.0):
    size = parent.size()
    self.dpi = dpi
    self.width = size.width() / dpi
    self.height = size.height() / dpi
    self.figure = Figure(figsize=(self.width, self.height), dpi=self.dpi, facecolor='w', edgecolor='k', frameon=False)
    self.figure.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=None, hspace=None)
    self.axes = self.figure.add_subplot(111)
    self.axes.axis((-1,1,-1,1))
    FigureCanvas.__init__(self, self.figure)
    self.updateGeometry()
    self.draw()
    self.cc = self.copy_from_bbox(self.axes.bbox)
    self.particle_plot = None
    self.setParent(parent)
    self.blit(self.axes.bbox)

  def on_pre_draw(self):
    self.restore_region(self.cc)

  def on_draw(self):
    raise NotImplementedError

  def on_post_draw(self):
    self.blit(self.axes.bbox)

  def redraw(self):
    self.on_pre_draw()
    self.on_draw()
    self.on_post_draw()