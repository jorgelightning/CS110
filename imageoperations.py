from PIL import Image

def main():
    imageName = 'usfca_logo.png'
    imageSecret = 'red-image.png'
    inputImage = Image.open('/Users/notion/Desktop/CS110/project2/'+imageName)
    inputSecret = Image.open('/Users/notion/Desktop/CS110/project2/'+imageSecret)
    
    #Display menu and input validation, user will be repeated asked if input is incorrect 
    while True:
        try:
            userAction = int(input('\nWelcome to image Operation program!\n\nWhat action would you like to take?\n(0)copy image (1)flip image (2)find pattern (3)make grey scale: '))
            if not (0 <= userAction <= 3):
                raise ValueError('Invalid number selection. Please enter number 0-3')
            break
        except ValueError:
            print('\n\n### Please enter a valid integer from the selection (0-3). TRY AGAIN... ##\n\n')

    imageWidth, imageHeight = inputImage.size

    #integers action selection
    if(userAction == 0):
        copyImage(inputImage, imageWidth, imageHeight)

    if(userAction == 1):
        flipVertical(inputImage, imageWidth, imageHeight)

    if(userAction == 2):
        findPattern(inputSecret)
    
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


#Iterate through pixel (x,y) coordinates
#put pixels back in vertical order by reversing y axis
def flipVertical(inputImage, imageWidth, imageHeight):
    imageFlipped = Image.new('RGB', (imageWidth, imageHeight))

    for x in range(imageWidth):
        for y in range(imageHeight):
            imageFlipped.putpixel((x,-y), inputImage.getpixel((x, y)))

    imageFlipped.save("/Users/notion/Desktop/CS110/project2/flipped_image.png")

    #For findPattern I used .getdata to get all the pixel values 
    #then iterate through each pixel and when I found red (255,0,0) I would change it to (255,255,255)
    #add the new pixel value into my list (secretPixelData)
    #I would turn my new list into a new image using .putdata 
def findPattern(inputSecret):

    imagePixel = inputSecret.getdata()

    secretPixelData = []
    for pixel in imagePixel:
        if(pixel == (255,0,0)):
            secretPixel = (255,255,255)
            secretPixelData.append(secretPixel)

        else:
            secretPixelData.append(pixel)
    
    inputSecret.putdata(secretPixelData)
    inputSecret.save("/Users/notion/Desktop/CS110/project2/secret_image.png")
    

#For Greyscale I used .getdata to get all the pixel values 
#Then iterate through each pixel and did the math to turn it greyscale 
#I used two different math to turn it into grey scale, I prefer floor division by 3 
#Commented out the other math for reference 
def makeGrayscale(inputImage):

    imagePixel = inputImage.getdata()

    grayscalePixelData = []
    for pixel in imagePixel:
        grayscalePixel = (pixel[0] + pixel[1] + pixel[2]) // 3
        #grayscalePixel = (int(pixel[0]*0.30) + int(pixel[1]*0.59) + int(pixel[2]*0.11))
        grayscalePixelData.append((grayscalePixel,grayscalePixel,grayscalePixel))
    
    inputImage.putdata(grayscalePixelData)
    inputImage.save("/Users/notion/Desktop/CS110/project2/grayscale_image.png")


main()