#!/usr/bin/env python
"""
Script to add new columns to an existing fits file.
http://docs.astropy.org/en/stable/io/fits/usage/table.html
"""

import os 
import sys 
import numpy as np
import astropy.io.fits as fits 

if not os.path.exists('output_table.fits'):
	sys.stderr.write('This code should be run after making output_table.fits via example_create_fitsfile.py.\n')
	quit()

try:
	with fits.open('output_table.fits')	as hdu_original:
		original_table = hdu_original[1].data
		original_columns = hdu_original[1].columns
except OSError as e:
	raise 

new_column_bool = np.array([True,False,False,True,True,False],dtype='bool')		
new_column_int = np.array([3,1,4,5,2,3],dtype='int')
new_columns = fits.ColDefs([
	fits.Column(name='NEW_FLAG',format='L',array=new_column_bool),
	fits.Column(name='NEW_INT',format='I',array=new_column_int)
	])
	
outfitsfile = 'output_table_append.fits'	
hdu_primary = fits.PrimaryHDU()
hdu_newtable = fits.BinTableHDU.from_columns(original_columns+new_columns,name='TRBLIST')	
hdulist = fits.HDUList([hdu_primary,hdu_newtable])
hdulist.writeto(outfitsfile,overwrite=True)	