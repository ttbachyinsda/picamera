import json
import urllib2
import time
key = "rqm-AimGRLABYcAleZ3NOQB--WUlG-kl"
secret = "k8M75QQkdp_XXlDpMjnSLYm8VsjydGlZ"
filepath = r"d:/a.jpg"
filepathface = r"d:/aa.jpg"
# filepath1 = r"d:/a.jpg"
# filepath2 = r"d:/b.jpg"
# filepath3 = r"d:/cc.jpg"
# filepath4 = r"d:/bb.jpg"
def detect_api(key, secret, filepath):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr=open(filepath,'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
    data.append('1')
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
    data.append("gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
    data.append('--%s--\r\n' % boundary)
    http_body='\r\n'.join(data)
    #buld http request
    req=urllib2.Request(http_url)
    #header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        #req.add_header('Referer','http://remotserver.com/')
        #post data to server
        resp = urllib2.urlopen(req, timeout=5)
        #get response
        qrcont=resp.read()
        return qrcont

    except urllib2.HTTPError as e:
        return e.read()


def compare_api(key, secret, filepath1, filepath2):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr = open(filepath1, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file1')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    fr = open(filepath2, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file2')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)
    http_body = '\r\n'.join(data)
    # buld http request
    req = urllib2.Request(http_url)
    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        # req.add_header('Referer','http://remotserver.com/')
        # post data to server
        resp = urllib2.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        return qrcont

    except urllib2.HTTPError as e:
        return e.read()


def create_set(key, secret, setname):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
    data.append(setname)
    data.append('--%s--\r\n' % boundary)
    http_body = '\r\n'.join(data)
    # buld http request
    req = urllib2.Request(http_url)
    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        # req.add_header('Referer','http://remotserver.com/')
        # post data to server
        resp = urllib2.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        return qrcont

    except urllib2.HTTPError as e:
        return e.read()


def addface(key,secret,token,setname):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
    data.append(setname)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'face_tokens')
    data.append(token)
    data.append('--%s--\r\n' % boundary)
    http_body = '\r\n'.join(data)
    # buld http request
    req = urllib2.Request(http_url)
    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        # req.add_header('Referer','http://remotserver.com/')
        # post data to server
        resp = urllib2.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        return qrcont

    except urllib2.HTTPError as e:
        return e.read()


def removeface(key,secret,setname):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
    data.append(setname)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'face_tokens')
    data.append('RemoveAllFaceTokens')
    data.append('--%s--\r\n' % boundary)
    http_body = '\r\n'.join(data)
    # buld http request
    req = urllib2.Request(http_url)
    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        # req.add_header('Referer','http://remotserver.com/')
        # post data to server
        resp = urllib2.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        return qrcont

    except urllib2.HTTPError as e:
        return e.read()


def search(key, secret, filepath, setname):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr = open(filepath, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
    data.append(setname)
    data.append('--%s--\r\n' % boundary)
    http_body = '\r\n'.join(data)
    # buld http request
    req = urllib2.Request(http_url)
    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        # req.add_header('Referer','http://remotserver.com/')
        # post data to server
        resp = urllib2.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        return qrcont

    except urllib2.HTTPError as e:
        return e.read()


def getdetail(key, secret, setname):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'outer_id')
    data.append(setname)
    data.append('--%s--\r\n' % boundary)
    http_body = '\r\n'.join(data)
    # buld http request
    req = urllib2.Request(http_url)
    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        # req.add_header('Referer','http://remotserver.com/')
        # post data to server
        resp = urllib2.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        return qrcont

    except urllib2.HTTPError as e:
        return e.read()


# res1 = detect_api(key,secret,filepath)
# res2 = detect_api(key,secret,filepathface)
# print res1
# print res2
# token1 = json.loads(res1)["faces"][0]["face_token"]
# token2 = json.loads(res2)["faces"][0]["face_token"]
# print addface(key,secret,token1,'testset')
# print addface(key,secret,token2,'testset')


# print compare_api(key,secret,filepath1,filepath2)
# print create_set(key, secret, 'testset')

# print search(key,secret,filepath2,'testset')
# print search(key,secret,filepath3,'testset')
# print search(key,secret,filepath4,'testset')
# print getdetail(key,secret,'testset')