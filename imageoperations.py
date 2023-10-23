from PIL import Image

def main():
    imageName = 'usfca_logo.png'
    imageSecret = 'red-image.png'
    inputImage = Image.open('/Users/notion/Desktop/CS110/project2/'+imageName)
    inputSecret = Image.open('/Users/notion/Desktop/CS110/project2/'+imageSecret)
    while True:
        try:
            userAction = int(input('\nWelcome to image Operation program!\n\nWhat action would you like to take?\n(0)copy image (1)flip image (2)find pattern (3)make grey scale: '))
            if not (0 <= userAction <= 3):
                raise ValueError('Invalid number selection. Please enter number 0-3')
            break
        except ValueError:
            print('\n\n### Please enter a valid integer from the selection (0-3). TRY AGAIN... ##\n\n')

    imageWidth, imageHeight = inputImage.size

    if(userAction == 0):
        copyImage(inputImage, imageWidth, imageHeight)

    if(userAction == 1):
        flipVertical(inputImage, imageWidth, imageHeight)

    if(userAction == 2):
        findPattern(inputSecret, imageWidth, imageHeight)
    
    if(userAction == 3):
        makeGrayscale(inputImage)

# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save("/Users/notion/Desktop/CS110/project2/copy.png")

def flipVertical(inputImage, imageWidth, imageHeight):

    imageWidth, imageHeight = inputImage.size
    imageFlipped = Image.new(inputImage.mode, (imageWidth, imageHeight))

    for x in range(imageWidth):
        for y in range(imageHeight):
            imageFlipped.putpixel((x, imageHeight - y - 1), inputImage.getpixel((x, y)))

    imageFlipped.save("/Users/notion/Desktop/CS110/project2/flipped_image.png")


def findPattern(inputSecret, imageWidth, imageHeight):
    patternImage = Image.new("RGB", (imageWidth, imageHeight))
    
    for x in range(imageWidth):
        for y in range(imageHeight):
            imageSecret = inputSecret.getpixel((x,y))
            if imageSecret == (255, 0, 0):
                imageSecret = (255, 255, 255)
            patternImage.putpixel((x,y), imageSecret)
    
    patternImage.save("/Users/notion/Desktop/CS110/project2/secret_image.png")

def makeGrayscale(inputImage):

    imagePixel = inputImage.getdata()

    grayscalePixelData = []
    for pixel in imagePixel:
        grayscalePixel = (pixel[0] + pixel[1] + pixel[2]) // 3
        grayscalePixelData.append((grayscalePixel,grayscalePixel,grayscalePixel))
    
    inputImage.putdata(grayscalePixelData)
    inputImage.save("/Users/notion/Desktop/CS110/project2/grayscale_image.png")


main()