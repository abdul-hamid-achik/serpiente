from gimpfu import *
import os
import datetime
import sys
import time


def graphic_replace(template_path, graphic_path, result_path):
	print "Load Document"
	start = time.time()
	image = pdb.gimp_file_load(template_path, template_path, run_mode=RUN_NONINTERACTIVE)
	end = time.time()
	print "Loaded Document: ", end - start
	print "Load Graphic"
	start = time.time()
	graphic = pdb.gimp_file_load_layer(image, graphic_path)
	end = time.time()
	print "Loaded Graphic: ", end - start

	replace = image.layers[3].layers[3].layers[9].layers[0]

	print "Replace Graphic"
	start = time.time()
	pdb.gimp_image_insert_layer(image, graphic, replace.parent, 0)
	end = time.time()
	print "Replaced Graphic: ", end - start

	factor = min(
		replace.width / float(graphic.width), 
		replace.height / float(graphic.height)
	)

	new_width = int(graphic.width * factor)

	new_height = int(graphic.height * factor)

	print "Scale graphic"
	start = time.time()
	graphic.scale(new_width, new_height)
	end = time.time()
	print "Scaled Graphic: ", end - start


	print "Set offests for graphic"
	start = time.time()
	graphic.set_offsets(replace.offsets[1], replace.offsets[0])
	end = time.time()
	print "setted offsets for Graphic: ", end - start

	graphic.visible = True


	print "Save Document"
	start = time.time()
	image.remove_layer(replace)

	new_image = pdb.gimp_image_duplicate(image)

	layer = pdb.gimp_image_merge_visible_layers(new_image, 1)

	# pdb.gimp_file_save(new_image, layer, result_path, '?')
	pdb.file_png_save(new_image, layer, result_path, result_path, 0, 0, 0, 0, 0, 0, 0)
	pdb.gimp_image_delete(new_image)
	end = time.time()
	print "Saved Document: ", end - start

