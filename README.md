# pdf_to_image
A script converts a pdf file to an image in PNG or JPEG format.
The generated image has the same name with the pdf file
And the default place to generate is the current folder.

# Examples:
* Call `pdf_to_image png ./test.pdf` will create a new image in PNG format named `test.png` in the current folder.
* Call `pdf_to_image jpg ./test.pdf` will create a new image in JPEG format named `test.jpg` in the current folder.
* Call `pdf_to_image png ./test.pdf /xxx_folder` will create a new image in PNG format named `test.png` in the /xxx_folder.