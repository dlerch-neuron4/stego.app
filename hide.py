from stegoapp import *

image = base64_to_image(g_image_url)
I = np.array(image)
Is = hide_ext(I, g_message, g_password)
if len(Is)!=0:
    g_b64image = image_to_base64(Is)
else:
    print("ERROR: Cannot hide")
    g_b64image = ''






