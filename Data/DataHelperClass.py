# Imported libraries
import os
import netCDF4
import numpy
import cv2

# "Constants"
default_path: str = "Data/SPoc_Dataset/"

def LoadInDataset(path: str = default_path) -> tuple:
    datasets: list = []

    for file_name in os.listdir(path):
        full_file_path: str = "%s%s" % (path, file_name)        

        dataset = netCDF4.Dataset(full_file_path)
        datasets.append(dataset)

    return tuple(datasets)

def ExtractImageUint16(nc_data: netCDF4._netCDF4.Dataset):
    for value in nc_data.variables:
        image_index: int = len(nc_data[value])
        image_index_zero = nc_data[value][0][:][:]
        for i in range (image_index):
            current_img = nc_data[value][i][:][:]
            image_difference = image_index_zero - current_img

            image_scaled = cv2.normalize(image_difference, dst=None, alpha=-65535, beta=65535, norm_type=cv2.NORM_MINMAX)
            cv2.imshow("lol", image_scaled)
            cv2.waitKey(0)
        break

    return None

def GetChannels(nc_data: netCDF4._netCDF4.Dataset) -> tuple:
    values: list = []
    for value in nc_data.variables:
        values.append(value)
    return tuple(values)

def GetSentinelBandCombinations(channels: tuple) -> tuple:
    return (channels[3], channels[2], channels[1])

def ShowImage(nc_data: netCDF4._netCDF4.Dataset, channels: tuple):
    image_index: int = len(nc_data[channels[0]])
    print( channels)

    for i in range (image_index):
        image = nc_data[channels[0]][i][:][:]

        for channel in channels[1:]:
            current_channel = nc_data[channel][i][:][:]

            image = numpy.dstack((image, current_channel))

        image_scaled = cv2.normalize(image, dst=None, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX)
        cv2.imshow("lol", image_scaled)
        cv2.waitKey(0)

def ConvertTo():
    print("not yet implemented")

nc_dataset: tuple = LoadInDataset()
channels: tuple = GetChannels(nc_dataset[0])
natural_color_band: tuple = GetSentinelBandCombinations(channels)
ShowImage(nc_dataset[0], natural_color_band)