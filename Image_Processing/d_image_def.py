from PIL import Image, ImageOps

def main():
    image = Image.open("bfly.jpg")

    new_image = ImageOps.deform(image, Deformer())
    new_image.show()
    # new_image.save("new_image.jpg")

class Deformer():
    def getmesh(self, img):
        w,h = img.size
        # source_shape = (0,0, 0,h, w,h, w,0)
        # target_rect = (100, 100, 500, 500)
        # source_shape = (0,0, 0,h, w-1000,h, w,0)
        # target_rect = (100, 100, w-100, h-100)
        # return [(target_rect, source_shape)]

        # left = ((0, 0, w//2, h), (0, 0, 0, h, w//2, h, w//2, 0))
        # right = ((w//2, 0, w, h), (w//2, 0, w//2, h, 0, h, 0, 0))
        # return [left, right]

        top_left = ((0, 0, w//2, h//2), (0, 0, 0, h//2, w//2, h//2, w//2, 0))
        top_right = ((w//2, 0, w, h//2), (w//2, 0, w//2, h//2, 0, h//2, 0, 0))
        b_left = ((0, h//2, w//2, h), (0, h//2, 0, 0, w//2, 0, w//2, h//2))
        b_right = ((w//2, h//2, w, h), (w//2, h//2, w//2, 0, 0, 0, 0, h//2))
        return [top_left, top_right, b_left, b_right]

if __name__ == "__main__":
    main()