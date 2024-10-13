from stegoapp import *

try:
    image = base64_to_image(g_image_url)
    I = np.array(image)

    g_message = extract(I, g_password)
except Exception as e:
    print(e)





