import json
import requests
import netifaces
from cloudauth import getauth


def update_record(domain_name=None, record_name=None, ip=None):
    token, dns_url = getauth('rax:dns')
    headers = {'x-auth-token': token, 'content-type': 'application/json'}
    if ip is None:
        my_ip_resp = requests.get('http://icanhazip.com/')
        if my_ip_resp.ok:
            ip = my_ip_resp.text
        else:
            resp.raise_for_status()
    if not domain_name and not record_name:
        print ip
        return None
    resp = requests.get("%s/domains" % dns_url, headers=headers)
    if resp.ok:
        for d in json.loads(resp.text)['domains']:
            if d['name'] == domain_name:
                domain_id = d['id']
    else:
        resp.raise_for_status()
    resp = requests.get("%s/domains/%s/records"  % (dns_url, domain_id), headers=headers)
    if resp.ok:
        for r in json.loads(resp.text)['records']:
            if r['name'] == record_name:
                record_id = r['id']
    else:
        resp.raise_for_status()
    if domain_id and record_id:
        data = {
            "name" : record_name,
            "data" : ip,
            "ttl" : 300
        }
        dns_up_uri = '%s/domains/%s/records/%s' % (dns_url, domain_id, record_id)
        dns_up_resp = requests.put(dns_up_uri, data=json.dumps(data), headers=headers)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="dns updater")
    parser.add_argument('-d', dest='domain', help="domain that your record is stored under")
    parser.add_argument('-r', dest='record', help="record you wish to update")
    parser.add_argument('-a', dest='address', default=False, action='store_true', help="use eth0 address")

    args = parser.parse_args()
    if args.address:
        ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
        update_record(args.domain, args.record, ip)
    else: 
        update_record(args.domain, args.record)
