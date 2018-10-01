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

dump  = 'Ion Symbol &   Lya2   &   Lya1   &    Lyb2   &   Lyb1   & Reference       \\\\ \n'
dump += '           &   (eV)   &   (eV)   &    (eV)   &   (eV)   &                 \\\\ \n'
dump += '\\hline \\hline\n'
for ion in OrderedDict(sorted(ions.items(),key=lambda x:x[1])):
	ion_n = '%s_%d' % (ion.lower(),ions[ion])
	lvfits_candidate = glob.glob(
		'%s/%s/%s/%s_LV_v*_a.fits' % (
			APEDDIR,ion.lower(),ion_n,ion_n))
	if len(lvfits_candidate) == 0:
		print('corresponding file does not exit for %s' % ion)
		quit()
	lvfits = lvfits_candidate[0]
	hdu = fits.open(lvfits)
	ion_state = hdu[1].name
	Lya_list = [];
	Lyb_list = [];
	for elv in hdu[1].data:
		if elv['ELEC_CONFIG'] == '2p1':
			Lya_list.append(elv['ENERGY'])
		if elv['ELEC_CONFIG'] == '3p1':
			Lyb_list.append(elv['ENERGY'])			
		ref = elv['ENERGY_REF']
	Lya2 = min(Lya_list)
	Lya1 = max(Lya_list)	
	Lyb2 = min(Lyb_list)
	Lyb1 = max(Lyb_list)		
	dump += '{:<11}& {:7,.2f} & {:7,.2f} & {:7,.2f} & {:7,.2f} & {:15} \\\\ \n'.format(ion_state,Lya2,Lya1,Lyb2,Lyb1,ref)
dump += '\\hline'	
print(dump)

