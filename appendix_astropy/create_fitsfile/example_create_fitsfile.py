#!/usr/bin/env python

import pandas as pd
import astropy.io.fits as fits 

input_table = 'input_table.txt'
outfitsfile = 'output_table.fits'

try:
	df = pd.read_csv(input_table,header=0,delim_whitespace=True)
except OSError as e:
	raise 
print("{} is successfully loaded.".format(input_table))

cols = []
cols.append(fits.Column(name='Event',format='10A',array=df['Event']))		
cols.append(fits.Column(name='Date',format='10A',array=df['Date'],unit='yyyy-mm-dd'))
cols.append(fits.Column(name='Time',format='10A',array=df['Time'],unit='hh:mm:ss'))
cols.append(fits.Column(name='Type',format='5A',array=df['Type']))		
cols.append(fits.Column(name='Detector',format='12A',array=df['Detector']))		
cols.append(fits.Column(name='Photons',format='K',array=df['Photons'],unit='count'))		
cols.append(fits.Column(name='Significance',format='D',array=df['Significance']))		

# http://docs.astropy.org/en/stable/io/fits/
# http://docs.astropy.org/en/stable/io/fits/usage/table.html
hdu_primary = fits.PrimaryHDU()
hdu_table = fits.BinTableHDU.from_columns(cols,name='TRBLIST')
hdulist = fits.HDUList([hdu_primary,hdu_table])
hdulist.writeto(outfitsfile,overwrite=True)	
