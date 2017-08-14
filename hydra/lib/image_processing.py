import os
import subprocess
import sys

cwd = os.getcwd()

# file = "\"" + sys.argv[1] + "\""

# path = "/Applications/GIMP.app/Contents/MacOS/GIMP"

# script = "\"" + cwd + "/projects/hydra-project/hydra/lib/scripts/graphic-replace.py" + "\""

# result = ''
# command = path + " -n --no-interface --console-messages --batch-interpreter python-fu-eval --batch 'file = " + file + ";execfile(" + script + ")' --batch 'pdb.gimp_quit(1)'"

# process = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

# print result
# sys.stdout = result


class ImageProcessing:
	def __init__(self, template, graphic, result):
		self.template = "\"" + template + "\"" 
		self.graphic = "\"" + graphic + "\"" 
		self.result = "\"" + result + "\"" 
		self.run()

	def run(self):
		gimp_path = "/Applications/GIMP.app/Contents/MacOS/GIMP"
		command = gimp_path + " -n --no-interface --console-messages --batch-interpreter python-fu-eval --batch 'from hydra.lib.scripts.graphic_replace import graphic_replace;graphic_replace(" + self.template + "," + self.graphic + "," + self.result +")' --batch 'pdb.gimp_quit(1)'"
		print command
		process = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
		print process