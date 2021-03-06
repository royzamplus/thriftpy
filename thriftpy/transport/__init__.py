# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .socket import TSocketBase, TSocket, TServerSocket
from .transport import (
    TTransportBase,
    TTransportException,
    TMemoryBuffer,
    TBufferedTransport,
    TBufferedTransportFactory,
    TFramedTransport,
    TFramedTransportFactory,
)

from thriftpy._compat import PYPY
if not PYPY:
    from .cytransport import (
        TCyBufferedTransport,
        TCyBufferedTransportFactory,
        TCyFramedTransportFactory,
    )
else:
    TCyBufferedTransport = TBufferedTransport
    TCyBufferedTransportFactory = TBufferedTransportFactory
    TCyFramedTransportFactory = TFramedTransportFactory

__all__ = [
    'TSocketBase', 'TSocket', 'TServerSocket',
    'TTransportBase', 'TTransportException',
    'TMemoryBuffer',
    'TFramedTransport', 'TFramedTransportFactory',
    'TBufferedTransport', 'TBufferedTransportFactory',
    'TCyBufferedTransport', 'TCyBufferedTransportFactory',
    ]
