import filetype as filetype
import xarray as xr

class WxRadar:
    """
    A class returing radar object for nc files with all metadata, able to handle single sweep files
    and plot ppi, maxz from cfradials, spectral width for single pole radar
    Can generate ppi plot with corresponding analysis of zdr, cc, etc for dual pol radars

    """

    def __init__(self, file):
        try:
            file_type = filetype.determine(file)
            if file_type == 'NETCDF3':
                self.radar = xr.open_dataset(file)
        except IOError as e:
            print(e)

    def get_fields(self):
        for r in self.radar:
            print(r, end="/")
        
    def get_metadata()



