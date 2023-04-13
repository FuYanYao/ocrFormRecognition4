import pytesseract
import cv2
from PIL import Image



def is_color_image(url):
  im = Image.open(url)
  pix = im.convert('RGB')
  width = im.size[0]
  height = im.size[1]
  oimage_color_type = False
  # is_color = []
  for x in range(width):
    for y in range(height):
      r, g, b = pix.getpixel((x, y))
      r = int(r)
      g = int(g)
      b = int(b)
      if (r == g) and (g == b):
        pass
      else:
        oimage_color_type = True
  return oimage_color_type


def continue_image(der):
    cv2.imshow('walao', der)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getTextFromImage(imPath):
    if is_color_image(imPath):
        text = getColorText(imPath)
        if text == "":
            text = getNoColorText(imPath)
    else:
        text = getNoColorText(imPath)
    return text


def getColorText(imPath):
    config = '-l chi_sim --oem 1 --psm 3'
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    thresh = 128
    img_binary = cv2.threshold(im, thresh, 255, cv2.THRESH_BINARY)[1]
    text = pytesseract.image_to_string(img_binary, config=config)
    # print(text)
    return text


def getNoColorText(imPath):
    tessdata_dir_config = '--tessdata-dir "./tesseract/tessdata"'
    lang = 'chi_sim'
    image = Image.open(imPath)
    code = pytesseract.image_to_string(image, config=tessdata_dir_config, lang=lang)
    # print(code)
    return code


if __name__ == '__main__':
    imPath = 'img.png'
    text = getTextFromImage(imPath)
    print(text)
    # print(is_color_image(imPath))
