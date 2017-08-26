from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
import os
from .utils import ImageSifter


def sift_images(url,
                  format_list=["jpg", "png", "gif", "svg", "jpeg", "JPEG", "JPG"],
                  download_path='images', size_limit=100000000, count_limit=None):
    """this function picks up and downloads originals of files (that formats in format_list) from html page"""
    sifter = ImageSifter()
    sifter.url = url
    sifter.size_limit = size_limit
    sifter.count_limit = count_limit
    sifter.format_list = format_list
    sifter.download_path = os.path.join(os.getcwd(), download_path)
    sifter.get_html()
    sifter.get_img_list()
    sifter.process_download_path()
    sifter.download_image()
