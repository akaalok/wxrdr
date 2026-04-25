def determine(filename):
    """
    determining type of input file for proper handling
    """
    try:
        f = open(filename, "rb")
        begin = f.read(12)
        f.close()
    except TypeError:
        f = filename
        begin = f.read(12)
        f.seek(-12, 1)

    if begin[:3] == b"CDF":
        return "NETCDF3"
    
    # NetCDF4, read with read_cfradial, contained in a HDF5 container
    # HDF5 format signature from HDF5 specification documentation
    hdf5_signature = b"\x89\x48\x44\x46\x0d\x0a\x1a\x0a"
    if begin[:8] == hdf5_signature:
        return "NETCDF4"
    
    hdf4_signature = b"\x0e\x03\x13\x01"
    if begin[:4] == hdf4_signature:
        return "HDF4"
    
    gzip_signature = b"\x1f\x8b"
    if begin[:2] == gzip_signature:
        return "GZ"
    
    return "UNKNOWN"

    
