#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import Queue
import threading

import serial

class SerialMonitorThread(threading.Thread):
    """ A thread for monitoring a serial port. The serial port is
        opened when the thread is started.

        data_q:
            Queue for received data. Items in the queue are
            (data, timestamp) pairs, where data is a binary
            string representing the received data, and timestamp
            is the time elapsed from the thread's start (in
            seconds).

        error_q:
            Queue for error messages. In particular, if the
            serial port fails to open for some reason, an error
            is placed into this queue.
    """
    def __init__(self, data_q, error_q):
        threading.Thread.__init__(self)

        self.serial_port = None
        self.data_q = data_q
        self.error_q = error_q

        self.alive = threading.Event()
        self.alive.set()

    def run(self):
        try:
            if self.serial_port:
                self.serial_port.close()
            # Port hardcoded :)
            self.serial_port = serial.Serial("COM3")
        except serial.SerialException, e:
            self.error_q.put(e.message)
            return

        # Restart the clock
        time.clock()

        while self.alive.isSet():
            # Reading 1 byte, followed by whatever is left in the
            # read buffer, as suggested by the developer of
            # PySerial.
            # 
            data = self.serial_port.next()

            if len(data) > 0:
                timestamp = time.clock()
                self.data_q.put((data.strip(), timestamp))

        # clean up
        if self.serial_port:
            self.serial_port.close()

    def join(self, timeout=None):
        self.alive.clear()
        threading.Thread.join(self, timeout)

