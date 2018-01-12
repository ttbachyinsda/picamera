from sys import stdin
import facetest
import json


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


def gethelp():
    print "help"


def getreport():
    print 'getreport'


def postfacedetail(facetoken, facename):
    print facetoken, facename


if __name__ == '__main__':
    while True:
        c = stdin.readline().strip()
        if c == 'clear':
            #facetest.removeface(facetest.key, facetest.secret, 'testset')
            print 'Cannot remove face in faceset'
            continue
        if c == 'createset':
            #res = facetest.create_set(facetest.key, facetest.secret, 'testset')
            print 'Cannot create faceset'
            continue
        if c == 'help':
            gethelp()
            continue
        if c == 'getreport':
            getreport()
            continue
        if c.split(' ')[0] == 'addface':
            filename = c.split(' ')[1]
            facename = c.split(' ')[2]
            # res1 = facetest.detect_api(facetest.key, facetest.secret, filename)
            # print res1
            # token1 = json.loads(res1)["faces"][0]["face_token"]
            # print facetest.addface(facetest.key, facetest.secret, token1, 'testset')
            token1 = 'API unavailable'
            postfacedetail(token1, facename)
            continue
        if c == 'getdetail':
            #print facetest.getdetail(facetest.key, facetest.secret, 'testset')
            print 'No FaceSet Detail available'
            continue
        if c == 'quit':
            break
        print 'no instruction'
        continue
