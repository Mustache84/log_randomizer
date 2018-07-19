This script runs through a document and searches for variables, which are listed in the replace string towards the end
It then replaces all variables with random selections from whatever list is being called for that
variable.  

Known variables with lists already created:

~~~~IP Addresses and subnets.
_IP_ = private IP for workstation devices. 10.1.x.x
_IP1_ = different list for when lines have 2 private IP devices on one line 10.1.x.x
_IP2_ = same as IP1 but for more selections 10.1.x.x
_SRC192_ was used for a script that had 192 addresses but I changed them to a different 10.1.2 for variety
_DST192_  another 10.1.2.x list
_DCIP_ is for domain controller/server IPs on a separate subnet 10.2.x.x
_DCIP2_ is another selection of DCIP IPs. 10.2.x.x
_REMIP_ = public IP addresses
_EXTIP_ == _REMIP_
_INTIP_ == _IP_ in case you wanted to add variety 10.1.x.x
_INTIP2 == _IP2_ for variety 10.1.x.x
_FW_ = firewall IP addresses. 10.5.x.x
_VPNIP_ = addresses on the VPN subnet 10.7.x.x

~~~~Users
_USER_NAME_ = basic user names.
_NIX_USER_ = linux users.
_TARGET_USER_NAME_ = a list of users that normal users can impersonate.
    for example >> where a default user, User.A, remotes to a machine as UserA.Admin.
    It's also random from the same primary user list for various results.
    
~~~~Device Names
_WORSTATION_ = workstation names. Endpoint names.
_DC_ = Server Names. Domain Controllers.
_FWNAME_ = firewall names.

~~~~Random Names of things
_NT_ = Active Directory root name. ADROOT
_SRCZONE_ = random zone names for sources
_DSTZONE_ = random zone names for destinations.
