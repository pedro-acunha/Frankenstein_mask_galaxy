# Frankenstein_mask_galaxy
Alpha version of a Python code to apply masks to galaxy images. <br />
The code uses SEP, a Python library for Source Extraction and Photometry, and skimage, a image processing package.

In ./test_mask_images, you can find the data used for testing and the final images after a mask is applied.

## Example:
Initial image             |  Image after being cropped and masked
:-------------------------:|:-------------------------:
![Alt text](./test_mask_images/data/11706.jpg?raw=true "Without mask")  |  ![Alt text](./test_mask_images/data_mask/mask_11706.jpg?raw=true "With mask")
![Alt text](./test_mask_images/data/14005.jpg?raw=true "Without mask")  |  ![Alt text](./test_mask_images/data_mask/mask_14005.jpg?raw=true "With mask")
![Alt text](./test_mask_images/data/18220.jpg?raw=true "Without mask")  |  ![Alt text](./test_mask_images/data_mask/mask_18220.jpg?raw=true "With mask")
![Alt text](./test_mask_images/data/11518.jpg?raw=true "Without mask")  |  ![Alt text](./test_mask_images/data_mask/mask_11518.jpg?raw=true "With mask")
