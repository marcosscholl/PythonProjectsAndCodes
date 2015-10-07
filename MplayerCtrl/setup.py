#!/usr/bin/env python

from distutils.core import setup

long_description = '''
This is the documentation for the MplayerCtrl, a `wx.Panel
<http://docs.wxwidgets.org/stable/wx_wxpanel.html#wxpanel>`_ (wxPython,
wxWidgets), which wraps the well known `Mplayer <http://www.mplayerhq.hu/>`_
into wxPython. Through this panel you have access to each command of the
Mplayer's `-slave <http://www.mplayerhq.hu/DOCS/tech/slave.txt>`_ option.

Documentation: `<http://mplayerctrl.dav1d.de>`_


See the bitbucket `repository <http://bitbucket.org/dav1d/mplayerctrl/>`_ for
up to date files.'''

setup(name='MplayerCtrl',
      version='0.3.3',
      description='A wx.Panel, which wraps the Mplayer into wxPython',
      classifiers=[#'Development Status :: 4 - Beta',
                   'Development Status :: 5 - Production/Stable',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Multimedia',
                   'Topic :: Multimedia :: Sound/Audio :: Players',
                   'Topic :: Multimedia :: Video',
                   'Topic :: Multimedia :: Video :: Display'],
      keywords='mplayer wxpython video audio',
      author='David Herberth',
      author_email='admin@dav1d.de',
      url='http://mplayerctrl.dav1d.de',
      py_modules=['MplayerCtrl'],
      license='MIT',
      platforms='any'
     )
