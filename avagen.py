import sys, os
import Image

def show(image):
	pass

def process(image):
	return image.resize((400, 400))


for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + "400x400.jpg"
    if infile != outfile:
        try:
            im = process(Image.open(infile))
        except IOError:
            print "cannot convert", infile

	
	