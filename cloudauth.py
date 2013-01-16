import json
import requests
import personal

def getauth(endpoint_type=None, region=None, echo=False):

    auth_url = "https://auth.api.rackspacecloud.com/v2.0/tokens" 
    auth_data = { 
                    "auth": { 
                        "RAX-KSKEY:apiKeyCredentials": { 
                            "username": personal.CF_USER,
                            "apiKey": personal.CF_KEY
                        }
                    } 
                } 

    resp = requests.post(
                auth_url, data=json.dumps(auth_data), 
                headers={'content-type': 'application/json'})
     
    if resp.ok:
        data = json.loads(resp.text)
        token = data['access']['token']['id']
        expires = data['access']['token']['expires']
        if echo:
            print "token: %s\nexpires: %s\n" % (token, expires)
        for sc in data['access']['serviceCatalog']:
            if echo:
                print "%s (%s)" % (sc['name'], sc['type'])
            if endpoint_type and sc['type'] == endpoint_type:
                return token, [ep for ep in sc['endpoints']][0]['publicURL']
            for ep in sc['endpoints']:
                if echo:
                    if region:
                        if ep.has_key('region') and ep['region'] == region:
                            print "\t%s" % (ep['publicURL'])
                    else:
                        print "\t%s" % (ep['publicURL'])

if __name__ == '__main__':
    getauth(None, None, True)
