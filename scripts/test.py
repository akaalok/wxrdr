import wx_radar as wx_radar

file1 = "../test_files/netcdf3/single_sweep/JPR240302001242-IMD-B.nc"

jpr = wx_radar.WxRadar(file1)
print(jpr.get_fields())