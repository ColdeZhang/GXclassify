from apig_sdk import signer
import requests
import base64
import os
import sys
import json
import pycurl

# sig = signer.Signer()
# sig.Key = "QCPZAOV2ZM4F0XPG1ZMI"
# sig.Secret = "R3JOG5NjKwk7LjBteTA3wjl06oofvfpvApEiZpgi"

# r = signer.HttpRequest("POST",
#     "https://1692ab7327d44d489e01d977444bfa12.apig.cn-north-4.huaweicloudapis.com/v1/infers/d95863ea-830b-44f1-bc41-e7a9a2828790",
#     {"x-stage": "RELEASE"},
#      "body")
00
# sig.Sign(r)
curl = pycurl.Curl()
curl.setopt(pycurl.URL, "https://1692ab7327d44d489e01d977444bfa12.apig.cn-north-4.huaweicloudapis.com/v1/infers/d95863ea-830b-44f1-bc41-e7a9a2828790")

def pred_name():
    # f = open('res/or_input_res/seg_pred/image.jpg', 'rb')
    # base64_img = base64.b64encode(f.read())
    # files = {'attach': ('image.jpg', base64_img)}
    # resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body, files = files)
    # print(resp.status_code, resp.reason)
    # print(resp.content)
    data = json.dumps('{"auth": {"identity": {"methods": ["password"],"password": {"user": {"domain": {"name": "hw37522237"},"name": "18758114676","password": "123qwe123"}}},"scope": {"project": {"name": "exeML-ac1f_ExeML_1604802586932936389"}}}}')
    res_token = requests.request("POST", "https://iam.myhuaweicloud.com/v3/auth/tokens", data = data)
    resp = 
    os.system("curl -F 'images=@res/or_input_res/seg_pred/image.jpg' -H 'X-Auth-Token:{}' -X POST https://1692ab7327d44d489e01d977444bfa12.apig.cn-north-4.huaweicloudapis.com/v1/infers/d95863ea-830b-44f1-bc41-e7a9a2828790".format(res_token))
    return resp.predicted_label