from PIL import Image, ImageDraw, ImageFont

def main():
    image = Image.open("bfly.jpg")

    draw = ImageDraw.Draw(image)

    draw.rectangle((100, 100, 400, 400), (0,255,255), (255,255,0))
    draw.ellipse((100, 100, 400, 400), (0,255,0), (0,255,0))
    # Polygon by all points...
    # line by all points...
    # draw.arc((800,100,1000,300), 20, 180, "red", width=20)
    # draw.chord((800,100,1000,300), 20, 180, "red", width=20)
    draw.pieslice((800,100,1000,300), 20, 90, "red", width=20)

    # Text
    font = ImageFont.truetype("my_font.ttf", size=80)
    draw.text((1300, 640), "Butterfly!", font=font, fill=(0,255,255))

    image.save("new_image.jpg")

if __name__ == "__main__":
    main()