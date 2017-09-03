# Implementation of the org.freedesktop.Secret.Prompt interface
# TODO unregister when client disconnects from dbus

import pydbus
from pydbus.generic import signal
import uuid
from gi.repository import GLib

from common.debug import debug_me
from common.names import base_path

class Prompt(object):
    """
      <node>
        <interface name='org.freedesktop.Secret.Prompt'>
          <method name='Prompt'>
            <arg type='s' name='window-id' direction='in'/>
          </method>
          <method name='Dismiss'/>
          <signal name='Completed'>
            <arg type='b' name='dismissed' direction='in'/>
            <arg type='v' name='result' direction='in'/>
          </signal>
        </interface>
      </node>
    """
    
    @debug_me
    def __init__(self, bus):
        self.bus = bus
        self.path = base_path + '/prompt/' + str(uuid.uuid4()).replace('-', '_')
        self.pub_ref = bus.register_object(self.path, self, None)

    @debug_me
    def Prompt(self, window_id):
        pass

    @debug_me
    def Dismiss(self):
        self.pub_ref.unregister()
        return None

    Completed = signal()
