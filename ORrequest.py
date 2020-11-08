from apig_sdk import signer
import requests


sig = signer.Signer()
sig.Key = "QCPZAOV2ZM4F0XPG1ZMI"
sig.Secret = "R3JOG5NjKwk7LjBteTA3wjl06oofvfpvApEiZpgi"

r = signer.HttpRequest("POST",
    "https://1692ab7327d44d489e01d977444bfa12.apig.cn-north-4.huaweicloudapis.com/v1/infers/d95863ea-830b-44f1-bc41-e7a9a2828790",
    {"x-stage": "RELEASE"},
     "body")
sig.Sign(r)

def pred_name():
    files = {'attach': ('image.jpg', open('file:///home/pi/Desktop/GXclassify/res/or_input_res/seg_pred/', 'rb'))}
    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body, files = files)
    print(resp.status_code, resp.reason)
    print(resp.content)
    return resp.predicted_label