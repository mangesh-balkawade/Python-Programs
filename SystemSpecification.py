import multiprocessing
import os
import platform
import shutil

import psutil


def main():
    print("----Welcome To Mangesh Balkawade SystemSpecification Application-----")
    print("Operating System Name with version in your System is", platform.platform())
    print("Name Of MicroProcessor in your Sysetm ",platform.processor())
    print("No of cores present in your Processor of your System ",multiprocessing.cpu_count())
    print("Size of Ram in Your System in Bytes", psutil.virtual_memory())
    print("CLock Speed of Your System Processor is ",psutil.cpu_freq())
    print("Secondary Storage Present in your system in the C Drive is in bytes is ",shutil.disk_usage("C:/"))
    print("Secondary Storage Present in your system in the D Drive is in bytes is ", shutil.disk_usage("D:/"))
    print("_____________________________________________________________")

if __name__=="__main__":
    main()