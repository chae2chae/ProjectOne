#Begin Phyton Code
import requests
from requests.auth import HTTPDigestAuth
import cv2
import numpy as np
from mask_rcnn import *

mrcnn = MaskRCNN()

url = 'http://192.168.1.1/osc/commands/execute'
username = "THETAYL12100859"
password = "12100859"

payload = {
    "name": "camera.getLivePreview",

    "optionNames": [
        "iso",
        "isoSupport"
    ]
}
headers = {
    "Content-Type": "application/json;charset=utf-8"
}

response = requests.post(url, auth=HTTPDigestAuth(username, password), json=payload, headers=headers, stream=True)

if response.status_code == 200:
    bytes_ = bytes()
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            bytes_ += chunk
            a = bytes_.find(b'\xff\xd8')
            b = bytes_.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes_[a:b+2]
                bytes_ = bytes_[b+2:]
                img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                # cv2.imshow("Preview", img)

                # Get object mask
                boxes, classes, contours, centers = mrcnn.detect_objects_mask(img)

                # Show depth info of the objects
                result_img = mrcnn.draw_object_mask(img)
                cv2.imshow("draw_object", result_img)

                if cv2.waitKey(1) == 27:
                    break
else:
    print("Error: ", response.status_code)

cv2.destroyAllWindows()
#End Python Code