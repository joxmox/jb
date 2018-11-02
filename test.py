import json
import urllib2

HOST = 'localhost'
PORT = 6661

def req(host, port, meth, url, data):
    url = 'http://{}:{}{}'.format(host, port, url)
    req = urllib2.Request(url, data)
    req.add_header('Content-Type', 'application/json')
    req.add_header('Content-Length', str(len(data)))
    req.get_method = lambda: meth
    resp = urllib2.urlopen(req, timeout=3)
    data = resp.read()
    return data

def req_get(id):
    jdata = req(HOST, PORT, 'GET', '/api/game/{}'.format(id), data='')
    data = json.loads(jdata)
    return data

def req_post(num):
    jdata = json.dumps({'num':num})
    jdata = req(HOST, PORT, 'POST', '/api/game', data=jdata)
    data = json.loads(jdata)
    return data

def main():
    data = req_post(0) #45075 96340
    print data
    id = data['id']
    print id
    data = req_get(id)
    print data
    data = req_get(id)
    hands = data['hands']
    for p in ['north', 'south']:
        print hands[p]['cards'], "  hcp=", hands[p]['hcp']
    while True:
        data = req_get(id)
        action = data['action']
        if action == 'end_game':
            break
        print data['bidder'], data['bid']['name'], "(" + data['bid']['text'] + ")"
    print "end"
    



if __name__ == '__main__':
    main()
