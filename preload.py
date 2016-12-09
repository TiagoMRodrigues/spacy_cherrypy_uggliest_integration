from importlib import __import__
import os
import traceback
import time
import sys
from multiprocessing import Process
from spacy.en import English
import os.path
#import signal

def func():
	try:
		x = eval(" __import__(\"Frontend\")")
		eval("x.setup(nlp)")

	except Exception as e:
		print("Unexpected error: " + str(e))
		traceback.print_exc()
		sys.stderr.flush()
		time.sleep(0.5)
		return "error"

	return "noerror"


if __name__ == '__main__':

	if(not os.path.isfile("/tmp/run_this.lock")):
		f=open("/tmp/run_this.lock","w")
		f.write("this is only a file")
		f.close()
		#catchable_sigs = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}
		#for sig in catchable_sigs:
		#	signal.signal(sig, print)

		#  Set the NLP object here for the parameters you want to see,
		#  or just leave it blank and get all the opts
		print("(run_this)Loading Spacy: waiting",end="",flush=True)
		

		#this is the line that takes to long  and originate all this
		nlp = English()      
		

		print("\r(run_this)Loading Spacy: done")
		first = False

		while True:
			try:
				if not first:
					print('================ To reload main module, press Enter ================')
					z = input()
				first = False
				th =Process(target=func)
				th.start()
				th.join()

			except Exception as e:
				print("Unexpected error: " + str(e))
				traceback.print_exc()
				sys.stderr.flush()
				time.sleep(0.5)

