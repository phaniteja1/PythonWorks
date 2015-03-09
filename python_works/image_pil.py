__author__ = 'phaniteja'

# Import the modules to perform operations on Image - PIL is used for operations

from PIL import Image, ImageFilter


def image_operations(user_operation):

    global edited_image

    # changing the user input to upper case for our operations
    operation = user_operation.upper()

    # opening the image file : Best practise to surround with try and except

    try:
        original = Image.open("steve.jpg")

        if operation == "BLUR":
            # Blur the Image
            edited_image = original.filter(ImageFilter.BLUR)

        elif operation == "EMBOSS":
            # Blur the Image
            edited_image = original.filter(ImageFilter.EMBOSS)

        elif operation == "CONTOUR":
            # Blur the Image
            edited_image = original.filter(ImageFilter.CONTOUR)

        elif operation == "ENHANCE":
            # Blur the Image
            edited_image = original.filter(ImageFilter.EDGE_ENHANCE)

        elif operation == "SMOOTH":
            # Blur the Image
            edited_image = original.filter(ImageFilter.SMOOTH)

        elif operation == "SHARPEN":
            # Blur the Image
            edited_image = original.filter(ImageFilter.SHARPEN)

        elif operation == "DETAIL":
            # Blur the Image
            edited_image = original.filter(ImageFilter.DETAIL)

        else:
            edited_image = original

    except FileNotFoundError:
        print("Unable to find file")

    # Display both images
    original.show()
    edited_image.show()

    # save the new image
    edited_image.save("edited_steve.jpg")

    return edited_image


# Getting the operation to be performed on the image and pass it to the function
get_operation = input("Enter the operation on the image : ")
image_operations(get_operation)