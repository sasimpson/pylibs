pylibs
======

My Python Libraries
-------------------

these are some libraries i use for python.  some of them are to interact with the rackspace cloud

in order to use these you need to create a library file personal.py which will have two constants defined:

    CF_USER = xxxxxxxxx
    CF_KEY = xxxxxxxxxx

cloudauth.py
------------

    getauth(endpoint, region, echo)

    endpoint: which service you need the endpoint for
        'object-store'
        'compute'
        etc, echo for all of them

    region: which rackspace cloud region you want endpoint for. some services don't care about regions.
        'ord'
        'dfw'
        'lon'

    echo: print out auth data
        True

dnsupdate.py
------------

    dnsupdate.py -d DOMAIN -r RECORD -a

        -d DOMAIN
            the top-level domain your record is under, ie. foo.com
        -r RECORD
            the actual record you want to update, ie. host1.foo.com
        -a 
            use the address from eth0 and not what is visible from the internet.  default is to use the ip see from http://icanhazip.com

