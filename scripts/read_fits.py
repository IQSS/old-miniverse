"""
Example using the astropy library: 
    http://www.astropy.org/
    http://docs.astropy.org/en/stable/io/fits/index.html
"""
from __future__ import print_function
from astropy.io import fits

def msg(m): print(m)
def msgt(m): msg('-'*60); msg(m); msg('-'*60)

def read_fits(fname):

    # Open the FITS file
    hdulist = fits.open(fname, memmap=True)

    # HDU summary
    msgt('HDU Summary')
    msg(hdulist.info())

    # Take the header from the primary HDU
    header = hdulist[0].header
    
    # Iterate through the header keys and values
    msgt('Iterate through header items (exclude "HISTORY")')
    for key, val in header.items(): 
        if not key == 'HISTORY':
            msg('key:[%s] val:[%s]' % (key, val))

    # Close the file
    hdulist.close()


if __name__=='__main__':
    fname = 'FITS_test/PerA_HI21cmGBT_F.fits'
    read_fits(fname)
