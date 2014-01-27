import sys, os
import Image

def show(pic_filename):
	os.system(pic_filename)

def process(image):
	return image.resize((400, 400))


# for infile in sys.argv[1:]:
for infile in ["test.jpg"]:
    f, e = os.path.splitext(infile)
    outfile = f + "400x400.jpg"
    if infile != outfile:
        try:
            im = process(Image.open(infile))
            im.save(outfile)
            show(outfile)
        except IOError:
            print "cannot convert", infile

	
	