import asyncio
import signal
from asyncio.subprocess import PIPE

@asyncio.coroutine
def cat(loop):
	proc = yield from asyncio.create_subprocess_shell(
		"cat", stdin=PIPE, stdout=PIPE)
	print('pid %s' % proc.pid)

	message = "Hello World!"
	print('message %r' % message)

	stdout, _ = yield from proc.communicate(message.encode('ascii'))
	print('cat read: %r' % stdout.decode('ascii'))

	exitcode = yield from proc.wait()
	print('exit code: %s' % exitcode)

loop = asyncio.get_event_loop()
loop.run_until_complete(cat(loop))
loop.close()

