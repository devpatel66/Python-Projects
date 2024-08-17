from PIL import Image,ImageFilter
IMG_URL = 'deadpool.jpg'
# im = Image.open('deadpool.jpg')

# print(im.format, im.size, im.mode)

# im.show()

def ImgFilter(filter):
    print("\n Image is beign processed...")
    filter = filter.upper()
    im = Image.open(IMG_URL)
    match filter:
        case 'BLUR':
            blur_image = im.filter(ImageFilter.BLUR)
            blur_image.show()
            # return "Images has been blurred"
        case 'DETAIL':
            detail_image = im.filter(ImageFilter.DETAIL)
            detail_image.show()
            print("hghg",detail_image.url)
            # return "Images has been detailed"
        case 'EDGE_ENHANCE':
            edgeEnchane = im.filter(ImageFilter.EDGE_ENHANCE)
            edgeEnchane.show()
            # return "Images has been edge enhanced"
        case 'SMOOTH':
            smooth = im.filter(ImageFilter.SMOOTH)
            smooth.show()
            # return "Images has been SMOOTH"
        
    print("Image has been processed")

def displayOptions():
    print("\nChoose Image Filter Options: ") 
    print("\n1. Blur \n2. Detail\n3. Edge Enhance\n4. Smooth \n\n0. EXIT \n")
    options ={
        0: 0,
        1: 'BLUR',
        2: 'DETAIL',
        3: 'EDGE_ENHANCE',
        4: 'SMOOTH'
    }
    
    opt = int(input("Enter your choice: "))
    
    try:
        return options[opt]
    except Exception:
        print("Invalid choice || Choose Between Above Options and Try Again") 

while True:
    res = displayOptions()
    if(res == 0):
        break
    print(f'{res} is selected')
    ImgFilter('EDGE_ENHANCE')