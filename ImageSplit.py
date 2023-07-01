import argparse
import os

from PIL import Image
from itertools import product

''' Defaults '''
sheet_w  = 1328
sheet_h  = 800
base_col = 5
base_row = 3 
base_wh  = 256 
base_gap = 8 

def tile(filename, dir_out):
    name, ext = os.path.splitext(filename)
    img = Image.open(filename) 
    w, h = img.size
   
    scale = float(w) / sheet_w
    img_size = int(scale * base_wh)
    gap_size = int(scale * base_gap)

    grid = product(range(0, h - (h % img_size), img_size), range(0, w - (w % img_size), img_size))

    for r in range(base_row):
        start_y = (r * img_size) + (gap_size * (r + 1))
        for c in range(base_col):
            start_x = (c * img_size) + (gap_size * (c + 1))
            box = (start_x, start_y, start_x + img_size, start_y + img_size)
            out = os.path.join(dir_out, f'{name}_{r}_{c}{ext}')
            img.crop(box).save(out)

if __name__ == "__main__":

    ''' Command line args '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="filename", help="Input image file directory/name", metavar="FILE")
    parser.add_argument("-d", dest="directory", help="Output directory [defaults to local]", metavar="DEST")
    args = parser.parse_args()

    outdir = "./"
    if args.directory and os.path.exists(args.directory):
        outdir = args.directory

    tile(args.filename, outdir)
