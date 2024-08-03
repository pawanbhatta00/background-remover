# from transformers import pipeline
from time import perf_counter
import os
from glob import glob
from functools import wraps
from loguru import logger



def perf_counter_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start =  perf_counter()
        func(*args, **kwargs)
        logger.info(f"It took {perf_counter() - start} to process {os.path.basename(args[0])}")
        
    return wrapper
    
@perf_counter_wrapper
def process_image(image):
    # pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
    # pillow_mask = pipe(image, return_mask = True)
    # pillow_image = pipe(image)
    # pillow_image.save("output.png")
    print(image)

if __name__ == "__main__":
    images = glob(os.path.join(os.getcwd(), "images", "*jpg"))
    # print(images)
    # [print(image) for image in images]
    process_image(images[0])
    [process_image(image) for image in images]