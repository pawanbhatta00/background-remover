from transformers import pipeline

image_path = "images/16MB.jpg"
pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
pillow_mask = pipe(image_path, return_mask = True)
pillow_image = pipe(image_path)
pillow_image.save("output.png")