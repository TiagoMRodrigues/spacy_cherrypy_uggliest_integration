import os
import sys
import subprocess
import threading

def stdin(p):
	while True:
		x = input()
		#p.communicate(input=bytes(x, 'utf-8'))
		p.stdin.write(bytes("%s\n"%x, 'utf-8'))
		p.stdin.flush()

def stdout(p):
	while True:
		print(p.stdout.readline().decode("utf-8"), end="",flush=True)

def stderr(p):
	while True:
		print(p.stderr.readline().decode("utf-8"), end="",flush=True, file=sys.stderr)

if __name__ == '__main__':
	print("removing lock")
	if(os.path.isfile("/tmp/run_this.lock")):
		os.remove("/tmp/run_this.lock")
	#os.popen("python preload.py")

	p = subprocess.Popen([sys.executable, "preload.py"], bufsize=0, stdout=subprocess.PIPE,  stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	a = threading.Thread(target=stdin, args=[p])
	b = threading.Thread(target=stdout, args=[p])
	c = threading.Thread(target=stderr, args=[p])
	a.start()
	b.start()
	c.start()
	a.join()
	b.join()
	c.join()