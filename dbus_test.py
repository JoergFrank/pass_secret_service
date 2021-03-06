#!/usr/bin/env python3

import pydbus
from gi.repository import GLib

from common.names import bus_name, base_path

if __name__ == '__main__':
    bus = pydbus.SessionBus()
    service = bus.get(bus_name)
    print(service)
    output, session_path = service.OpenSession('plain', GLib.Variant('i', 0))
    session = bus.get(bus_name, session_path)
    print(session)
    session.Close()
    collection_path, promt_path = service.CreateCollection({}, '')
    collection = bus.get(bus_name, collection_path)
    print(collection)
    print(collection.Locked)
    print(collection.Label)
    collection.Delete()

#    loop = GLib.MainLoop()
#    loop.run()
