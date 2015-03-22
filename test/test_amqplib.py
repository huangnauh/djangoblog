#!/usr/bin/env python
# coding: utf-8

from amqblib import client_0_8 as amqp
conn = amqp.Connection(host="localhost:5672",userid="guest",password="guest",virtual_host="/",insist=False)
chan = conn.channel()

chan.queue_declare(queue="po_box",durable=True,
        exclusive=False,auto_delete=False)

chan.exchange_declare(exchange="sorting_room",
        type="direct",durable=True,auto_delete=False)

chan.queue_bind(queue="po_box",exchange="sorting_room",routing_key="huang")

msg = chan.basic_get("po_box")
print msg.body
chan.basic_ack(msg.delivery_tag)
chan.close()
conn.close()
