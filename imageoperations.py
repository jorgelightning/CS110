from PIL import Image

def main():
 #   imageName = input('What image should you like to take action on (enter image name and exention): ')
    imageName = 'usfca_logo.png'
    inputImage = Image.open('/Users/notion/Desktop/CS110/project2/'+imageName)
    userAction = int(input('\nWelcome to image Operation program!\n\nWhat action would you like to take?\n(0)copy image (1)flip image (2)find pattern (3)make grey scale\n'))
    imageWidth, imageHeight = inputImage.size

    if(userAction == 0):
        copyImage(inputImage, imageWidth, imageHeight)

    if(userAction == 1):
        imageFlipper(inputImage, imageWidth, imageHeight)

    if(userAction == 2):
        imageGrayScale(inputImage)



# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save("/Users/notion/Desktop/CS110/project2/copy.png")

def imageFlipper(inputImage, imageWidth, imageHeight):

    imageWidth, imageHeight = inputImage.size
    imageFlipped = Image.new(inputImage.mode, (imageWidth, imageHeight))

    for x in range(imageWidth):
        for y in range(imageHeight):
            imageFlipped.putpixel((x, y), inputImage.getpixel((imageWidth - x - 1, y)))

    imageFlipped.save("/Users/notion/Desktop/CS110/project2/flipped_image.png")

def imageGrayScale(inputImage):

    imagePixel = inputImage.getdata()

    grayscalePixelData = []
    for pixel in imagePixel:
        grayscalePixel = (pixel[0] + pixel[1] + pixel[2]) // 3
        grayscalePixelData.append((grayscalePixel,grayscalePixel,grayscalePixel))
    
    inputImage.putdata(grayscalePixelData)
    inputImage.save("/Users/notion/Desktop/CS110/project2/grayscale_image.png")


main()