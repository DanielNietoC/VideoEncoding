#Credit:   https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.dct.html#scipy.fftpack.dct

from scipy.fftpack import dct, idct

def DCT(input):

    im_dct = dct(input, norm='ortho')

    return im_dct

def inverseDCT(input):

    inverse_dct = idct(input, norm='ortho')

    return inverse_dct

