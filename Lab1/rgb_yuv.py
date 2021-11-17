# Credit: https://newbedev.com/how-to-convert-rgb-yuv-rgb-both-ways

def rgb_to_yuv(r, g, b):

    #Defined operations to convert from rgb to yuv
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = -0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g - 0.071 * b + 128

    return y, u, v


def yuv_to_rgb(y, u, v):

    # Defined operations to convert from yuv to rgb
    y -= 16
    u -= 128
    v -= 128

    r = 1.164 * y + 1.596 * v
    g = 1.164 * y - 0.392 * u - 0.813 * v
    b = 1.164 * y + 2.017 * u

    return r, g, b
