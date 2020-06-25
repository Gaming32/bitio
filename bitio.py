import io
from typing import Sequence

from bitarray import bitarray


class BitIO:
    __slots__ = ['_readable', '_writeable', '_stream', '_buffer']

    def __init__(self, stream:io.RawIOBase):
        self._stream = stream
        self._buffer = bitarray()
        self._readable = None
        self._writeable = None

    def readable(self):
        if self._readable is None:
            return self._stream.readable()
        return self._readable

    def writeable(self):
        if self._writeable is None:
            return self._stream.writeable()
        return self._writeable

    def seekable(self):
        return False

    def seek(self, where, whence=0):
        raise io.UnsupportedOperation('seek')

    def tell(self):
        raise io.UnsupportedOperation('tell')
        return max((self._stream.tell() - 1) * 8 + len(self._buffer), 0)

    def write(self, bits:Sequence[bool]) -> int:
        """Returns the number of BYTES written"""
        if not self.writeable():
            raise io.UnsupportedOperation('write')
        self._readable = False

        self._buffer.extend(bits)
        bytes_written = 0
        while len(self._buffer) >= 8:
            towrite, self._buffer = self._buffer[:8], self._buffer[8:]
            self._stream.write(towrite.tobytes())
            bytes_written += 1
        return bytes_written

    def read(self, c=-1) -> bitarray:
        if not self.readable():
            raise io.UnsupportedOperation('read')
        self._writeable = False

        if c < 0:
            return self._buffer + bitarray().frombytes(self._stream.read())
        result, self._buffer = self._buffer[:c], self._buffer[c:]
        c -= len(result)
        bytes_to_read, bits_to_read = divmod(c, 8)
        result.frombytes(self._stream.read(bytes_to_read))
        self._buffer.frombytes(self._stream.read(1))
        result, self._buffer = self._buffer[:bits_to_read], self._buffer[bits_to_read:]
        return result


del Sequence
