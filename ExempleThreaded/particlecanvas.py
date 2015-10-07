from numpy import array, where, abs
from numpy.random import random

from canvas import Canvas

class ParticleCanvas(Canvas):
  def __init__(self,parent,dpi=100.0):
    Canvas.__init__(self,parent,dpi)
    self.pos = None
    self.vel = None

  def reinitialize(self, npart):
    #self.pos = 2.0*(random((2,npart))-0.5)
    self.pos = (random((2,npart)))
    self.vel = 2.0*(random((2,npart))-0.5)
    self.particle_plot = None

  def move(self):
    if self.pos is None or self.vel is None: return
    dt = 0.01
    # change velocity if they go beyond box
    self.vel[where(abs(self.pos + dt*self.vel)>1.0)] *= -1.0
    self.pos += dt*self.vel

  def on_draw(self):
    if self.pos is None or self.vel is None: return
    if self.particle_plot is None:
      self.particle_plot, = self.axes.plot(self.pos[0],self.pos[1], 'ro', animated=True)
    self.particle_plot.set_xdata(self.pos[0])
    self.particle_plot.set_ydata(self.pos[1])
    self.axes.draw_artist(self.particle_plot)
