#!/usr/bin/env python
# coding: utf-8

from tasks import add
import gevent
from gevent import monkey;monkey.patch_socket()

def foo(x,y):
    print "begin %s" % x
    r = add.delay(x,y)
    z = r.get()
    print "end %s" % x
    print "%s + %s = %s" % (x,y,z)

jobs = [gevent.spawn(foo,i,i) for i in range(10)]
gevent.joinall(jobs)

