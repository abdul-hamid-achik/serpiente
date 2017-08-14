from gimpfu import *
import os
import datetime
import sys


def graphic_replace(template_path, graphic_path, result_path):
	image = pdb.gimp_file_load(template_path, template_path, run_mode=RUN_NONINTERACTIVE)

	graphic = pdb.gimp_file_load_layer(image, graphic_path)

	replace = image.layers[3].layers[3].layers[9].layers[0]

	pdb.gimp_image_insert_layer(image, graphic, replace.parent, 0)

	factor = min(
		replace.width / float(graphic.width), 
		replace.height / float(graphic.height)
	)

	new_width = int(graphic.width * factor)

	new_height = int(graphic.height * factor)

	graphic.scale(new_width, new_height)

	graphic.set_offsets(replace.offsets[1], replace.offsets[0])

	graphic.visible = True

	image.remove_layer(replace)

	new_image = pdb.gimp_image_duplicate(image)

	layer = pdb.gimp_image_merge_visible_layers(new_image, 1)

	pdb.gimp_file_save(new_image, layer, result_path, '?')

	pdb.gimp_image_delete(new_image)


