from apig_sdk import signer
import requests


sig = signer.Signer()
sig.Key = ""
sig.Secret = ""

r = signer.HttpRequest("POST",
    "https://1684994b180244de9d141c00d3e52c73.apig.exampleRegion.huaweicloudapis.com/v1/infers/exampleServiceId",
    {"x-stage": "RELEASE"},
     "body")
sig.Sign(r)

def pred_name():
    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
    print(resp.status_code, resp.reason)
    print(resp.content)
    return resp.content