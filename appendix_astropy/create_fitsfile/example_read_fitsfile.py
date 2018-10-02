#!/usr/bin/env python

import os 
import astropy.io.fits as fits 

input_fitsfile = 'input_sample.evt' 

if not os.path.exists(input_fitsfile):
	raise FileNotFoundError("{} is not found.".format(input_fitsfile))
try:
	hdu = fits.open(input_fitsfile)
except OSError as e:
	raise 

print('EXTNAME : {}'.format(hdu['EVENTS'].name))
print('DATE-OBS: {}'.format(hdu['EVENTS'].header['DATE-OBS']))

num_of_display = 10; i = 0
print('TIME                 PI  PULSE_NUMBER PULSE_PHASE')
for event in hdu['EVENTS'].data:
	if i > num_of_display:
		break
	print('{:.8f} {:>4}  {:>}  {:.6f}'.format(
		event['TIME'],event['PI'],int(event['PULSE_NUMBER']),event['PULSE_PHASE']
		))
	i += 1