import xarray

ds_disk = xarray.open_dataset("assets/waves_2019-01-01.nc")

def get_wave_height_at(lng, lat):
    return float(ds_disk.sel(longitude=lng, latitude=lat, method="nearest").hmax.max())
