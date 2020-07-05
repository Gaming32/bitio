# What is BitIO?
A library that exports a BitIO class to read and write bits on streams.

``` python
>>> from io import BytesIO
from bitio import BitIO
>>> stream = BytesIO()
>>>
>>> wrapped = BitIO(stream)
>>> wrapped.write('00')
0
>>> wrapped.write('10000')
0
>>> wrapped.write([True] * 9)
2
>>> wrapped.close()
>>> stream.getvalue()
b'!\xff'
>>>
>>> stream.seek(0)
0
>>> wrapped = BitIO(stream)
>>> wrapped.read(4)
bitarray('0010')
>>> wrapped.read(6)
bitarray('000111')
>>> wrapped.read()
bitarray('111111')
```

# Installing BitIO
Either
``` shell
$ git clone https://github.com/gaming32/BitIO.git
$ cd BitIO
$ python setup.py install
```
or
``` shell
$ pip install BitIO2
```

# Documentation
## bitio.BitIO
`bitio.BitIO(stream:io.RawIOBase)`

Wraps an io stream and allows bitarray read and write to that stream.
However, it can only read or write. A new one must be created to do the
other function.

### bitio.BitIO.readable
`bitio.BitIO.readable() -> bool`

Returns `True` if this stream is readable (will always be `False` if a write has occured on it).

### bitio.BitIO.writable
`bitio.BitIO.writable() -> bool`

Returns `True` if this stream is writable (will always be `False` if a read has occured on it).

### bitio.BitIO.seekable
`bitio.BitIO.seekable() -> bool`

Returns `True` if this stream is seekable (will always be `False`).

### bitio.BitIO.seek
`bitio.BitIO.seek(where, whence=0) -> int`

Raises `io.UnsupportedOperation('seek')`.

### bitio.BitIO.tell
`bitio.BitIO.tell() -> int`

Raises `io.UnsupportedOperation('tell')`.

### bitio.BitIO.flush
`bitio.BitIO.flush(flush_wrapped_stream=True)`

Flushes the buffer to the wrapped stream (this should never have to happen).
If `flush_wrapped_stream` is `True`, this also calls `self._stream.flush()`.

### bitio.BitIO.write
`bitio.BitIO.write(bits:Sequence[bool]) -> int`

Returns the number of BYTES written.

### bitio.BitIO.read
`bitio.BitIO.read(c=-1) -> bitarray`

Reads `c` bits from the wrapped stream.
If `c` is ommitted or negative, reads all bits from the wrapped stream.

### bitio.BitIO.close
`bitio.BitIO.close()`

Calls `self.flush(flush_wrapped_stream=False)`.

### bitio.BitIO._stream
The wrapped stream.

### bitio.BitIO._buffer
The bits that are waiting to be flushed to the wrapped stream. The length of this object should always be less than eight. If it isn't, call `bitio.BitIO.flush(False)`.

### bitio.BitIO._readable
Used for the return value of `bitio.BitIO.readable`. If the value is `None`, `self._stream.readable()` is returned. Otherwise, `self._readable` is returned.

### bitio.BitIO._writable
Used for the return value of `bitio.BitIO.writable`. If the value is `None`, `self._stream.writable()` is returned. Otherwise, `self._writable` is returned.