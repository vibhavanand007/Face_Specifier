from pygoogle_image import image as pi

keyword = input('keyword : ')
limit = int(input('limit : '))
pi.download(keywords=keyword, limit=limit)
