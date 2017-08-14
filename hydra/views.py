from django.http import Http404
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from hydra.lib.image_processing import ImageProcessing
import subprocess
import pdb
import datetime
import os

def index(request):
	return render(request, 'index.html', {})


def jobs(request):
	if (request.method == "POST" and request.FILES):
		graphic = request.FILES['graphic']
		fs = FileSystemStorage()
		graphic.name = "graphic_" + datetime.datetime.now().isoformat() + ".png"
		filename = fs.save(graphic.name, graphic)
		uploaded_file_url = fs.url(filename)
		template_path = os.getcwd() + "/hydra/assets/preview.xcf"
		static_path = "/static/output/preview_" + datetime.datetime.now().isoformat() +'.png'
		result_path = os.getcwd() + static_path
		graphic_url = "/Users/sicksid/projects/hydra-project/media/" + graphic.name
		ImageProcessing(template_path, graphic_url, result_path).run()
		return render(request, 'preview.html', {
				"image": static_path
			}
		)
	else:
		return redirect(index)
