#!/usr/bin/env python

import glob 
from collections import OrderedDict
import astropy.io.fits as fits 

APEDDIR = '/Users/enoto/Dropbox/enoto/library/atomdb/data/v3.0.9/atomdb_v3.0.9_lineid/APED'

# ion names and atomic number (number of electrons)
ions = {
"C":6,
"N":7,
"O":8,
"Ne":10,
"Na":11,
"Mg":12,
"Al":13,
"Si":14,
"S":16,
"Ar":18,
"Ca":20,
"Fe":26,
"Ni":28}

dump  = 'Ion state  & forbidden & Intercommbination & resonance & Reference       \\\\ \n'
dump += '           &  F or z & I1 or y   & I2 or x  & R or x    &  \\\\ \n'
dump += '           &   (eV)  &   (eV)    &   (eV)   &   (eV)    &  \\\\ \n'
dump += '\\hline \\hline\n'
for ion in OrderedDict(sorted(ions.items(),key=lambda x:x[1])):
	ion_n = '%s_%d' % (ion.lower(),ions[ion]-1)
	lvfits_candidate = glob.glob(
		'%s/%s/%s/%s_LV_v*_a.fits' % (
			APEDDIR,ion.lower(),ion_n,ion_n))
	if len(lvfits_candidate) == 0:
		print('corresponding file does not exit for %s' % ion)
		quit()
	lvfits = lvfits_candidate[0]
	print(lvfits)
	hdu = fits.open(lvfits)
	ion_state = hdu[1].name
	Lya_list = []
	for elv in hdu[1].data:
		if elv['ELEC_CONFIG'] == '1s1 2s1' and elv['S_QUAN'] == 1:
			forbidden = elv['ENERGY']
		if elv['ELEC_CONFIG'] == '1s1 2p1' and elv['S_QUAN'] == 0:
			resonance = elv['ENERGY']
		if elv['ELEC_CONFIG'] == '1s1 2p1' and elv['S_QUAN'] == 1 and elv['LEV_DEG'] == 5:
			intercombination1 = elv['ENERGY']	
		if elv['ELEC_CONFIG'] == '1s1 2p1' and elv['S_QUAN'] == 1 and elv['LEV_DEG'] == 3:
			intercombination2 = elv['ENERGY']						
		ref = elv['ENERGY_REF']
	dump += '{:<11}& {:8,.2f} &  {:8,.2f} &  {:8,.2f} & {:8,.2f} & {:15} \\\\ \n'.format(ion_state,forbidden,intercombination2,intercombination1,resonance,ref)
dump += '\\hline'	
print(dump)

