#!/usr/bin/env python

import astropy.io.fits as fits

import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = '14'
mpl.rcParams['mathtext.default'] = 'regular'
mpl.rcParams['xtick.top'] = 'True'
mpl.rcParams['ytick.right'] = 'True'
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
#mpl.rcParams['axes.grid'] = 'True'
mpl.rcParams['axes.xmargin'] = '.05' #'.05'
mpl.rcParams['axes.ymargin'] = '.05'
mpl.rcParams['savefig.facecolor'] = 'None'
mpl.rcParams['savefig.edgecolor'] = 'None'
mpl.rcParams['savefig.bbox'] = 'tight'

# Swift 
# https://swift.gsfc.nasa.gov/proposals/swift_responses.html
hdu_xrt = fits.open('get_effective_area/swxs6_20010101v001.arf')

# NICEER
hdu_xti = fits.open('get_effective_area/ni_xrcall_onaxis_v1.01.arf')

# XMM
# ~/Dropbox/enoto/research/nicer/analysis/psrb0656p14/data/180621_kobayashi/phase_ana
hdu_pn = fits.open('get_effective_area/pn_sr.arf')

# Suzaku XIS 
# https://heasarc.nasa.gov/docs/suzaku/prop_tools/xis_mat.html
hdu_xisfi = fits.open('get_effective_area/XRT_FI_xisnom.arf')

hdu_xisbi = fits.open('get_effective_area/XRT_BI_xisnom.arf')


# XMM
# https://www.cosmos.esa.int/web/xmm-newton/calibration


plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))
plt.plot(
	0.5*(hdu_xti['SPECRESP'].data['ENERG_LO']+hdu_xti['SPECRESP'].data['ENERG_HI']),
	hdu_xti['SPECRESP'].data['SPECRESP'],
	label='NICER/XTI')
#plt.plot(
#	0.5*(hdu_xrt['SPECRESP'].data['ENERG_LO']+hdu_xrt['SPECRESP'].data['ENERG_HI']),
#	hdu_xrt['SPECRESP'].data['SPECRESP'],
#	label='Swift/XRT-PC')
#plt.plot(
#	0.5*(hdu_pn['SPECRESP'].data['ENERG_LO']+hdu_pn['SPECRESP'].data['ENERG_HI']),
#	hdu_pn['SPECRESP'].data['SPECRESP'],
#	label='XMM/PN')
#plt.plot(
#	0.5*(hdu_xisfi['SPECRESP'].data['ENERG_LO']+hdu_xisfi['SPECRESP'].data['ENERG_HI']),
#	hdu_xisfi['SPECRESP'].data['SPECRESP'],
#	label='Suzaku/XIS-FI')
#plt.plot(
#	0.5*(hdu_xisbi['SPECRESP'].data['ENERG_LO']+hdu_xisbi['SPECRESP'].data['ENERG_HI']),
#	hdu_xisbi['SPECRESP'].data['SPECRESP'],
#	label='Suzaku/XIS-BI')
#plt.plot(v104_hd['SPECRESP'].data['ENERGY'],v104_hd['SPECRESP'].data['SPECRESP'])
axes.set_xlim(0.12,12.0)
axes.set_ylim(0,2000)
axes.legend(loc='upper right')
axes.set_xlabel('Energy (keV)')
axes.set_ylabel('Effective area (cm$^{2}$)')
axes.set_xscale('log')
plt.savefig('effective_area_nicer.pdf')
