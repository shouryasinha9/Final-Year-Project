#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import cv2
import numpy as np
from PIL import Image

IMAGE_SIZE = 1800
BINARY_THREHOLD = 180

size = None


def get_size_of_scaled_image(im):
    global size
    if size is None:
        length_x, width_y = im.size
        factor = max(1, int(IMAGE_SIZE / length_x))
        size = factor * length_x, factor * width_y
    return size


def process_image_for_ocr(image):
    logging.info('Processing image for text Extraction')
    temp_im = set_image_dpi(image)
    im_new = remove_noise_and_smooth(temp_im)
    return im_new


def set_image_dpi(im):
    # size = (1800, 1800)
    color_coverted = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(color_coverted)
    size_im = get_size_of_scaled_image(pil_image)
    im_resized = pil_image.resize(size_im, Image.ANTIALIAS)
    return im_resized


def image_smoothening(img):
    ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th2, (1, 1), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th3


def remove_noise_and_smooth(img):
    logging.info('Removing noise and smoothening image')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    img = image_smoothening(img)
    or_image = cv2.bitwise_or(img, closing)
    return or_image
