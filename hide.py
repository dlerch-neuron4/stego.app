import sys
from stegoapp import *

image = base64_to_image(g_image_url)
I = np.array(image)

if capacity(I.shape) < len(encode(g_message)):
    print("ERROR: Message too long")
    g_b64image = 'ERR_TOO_LONG'
    sys.exit(0)

Is = hide_ext(I, g_message, g_password)
if len(Is)!=0:
    g_b64image = image_to_base64(Is)
else:
    print("ERROR: Cannot hide")
    g_b64image = 'ERR_EMB'






