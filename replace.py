
'''This script runs through a document and searches for variables, which are listed in the replace string towards the end
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
'''



import random

'''Opens all the files that contain lists which can be edited, but are set for now to generate different IP sets, names, usernames, etc
for the script to randomize and throw into the main log files supplied.
this will open each file, read each line of the file and add that data to a string. This allows the script to later go through
that string and pull random data out to insert into the variables listed above.
'''

IPS1 = open('IPLIST1.txt', 'r')
iplist1 = IPS1.readlines()

IPS2 = open('IPLIST2.txt', 'r')
iplist2 = IPS2.readlines()

IPS3 = open('IPLIST3.txt','r')
iplist3 = IPS3.readlines()

IP192S = open('subnet192.txt','r')
ip192list1 = IP192S.readlines()

IP192SS = open('subnet192.2.txt','r')
ip192list2 = IP192SS.readlines()

VIP1 = open('vpn1.txt','r')
vip1l = VIP1.readlines()

VIP2 = open('vpn2.txt','r')
vip2l = VIP2.readlines()

DCIPS = open('dcip.txt','r')
dcipl = DCIPS.readlines()

DCIPS2 = open('dcip2.txt','r')
dcipl2 = DCIPS2.readlines()

NAMES = open('usernames.txt','r')
unlist = NAMES.readlines()

EXIPS = open('extip.txt', 'r')
exiplist = EXIPS.readlines()

DCS = open('dclist.txt', 'r')
dclist = DCS.readlines()

FWS = open('fwlist.txt', 'r')
fwlist = FWS.readlines()

FWIPS = open('fwips.txt','r')
fwipl = FWIPS.readlines()

ZONES1 = open('zones.txt', 'r')
zlist1 = ZONES1.readlines()

ZONES2 = open('zones01.txt','r')
zlist2 = ZONES2.readlines()

NUS = open('nixusers.txt', 'r')
nixu = NUS.readlines()

EPS = open('workstations.txt', 'r')
eplist = EPS.readlines()


#Random list of timestamps. Just a reference as I used this for a specific application.
#DATES = open('dates.txt','r')
#dtlist = DATES.readlines()


NT = 'ADROOT'


#Target file to search through for variables to replace.
searchfile = open("cisco.edited.txt", "r")

for line in searchfile:
    #Randomizes the lists above and replaces variables inside the files
        rip1 = random.choice(iplist1).strip()
        rip2 = random.choice(iplist2).strip()
        rip3 = random.choice(iplist3).strip()
        rvip1 = random.choice(vip1l).strip()
        rvip2 = random.choice(vip2l).strip()
        rdcip = random.choice(dcipl).strip()
        rdip2 = random.choice(dcipl2).strip()
        rip1921 = random.choice(ip192list1).strip()
        rip1922 = random.choice(ip192list2).strip()
        rnames = random.choice(unlist).strip()
        rexips = random.choice(exiplist).strip()
        rdcs = random.choice(dclist).strip()
        rfw = random.choice(fwlist).strip()
        rfwip = random.choice(fwipl).strip()
        rz1 = random.choice(zlist1).strip()
        rz2 = random.choice(zlist2).strip()
        rnixu = random.choice(nixu).strip()
        rep = random.choice(eplist).strip()
        #rdate = random.choice(dtlist).strip() #used for dates commented out above.

        #The output will store all the data placed at locations indicated by the variables in ' ' after replace(
        output = line.replace('_IP_', rip1).replace('_IP2_', rip2).replace('_IP3_', rip3).replace('_SRC192_',rip1921).replace('_DST192_',rip1922).replace('_DCIP_', rdcip).replace('_DCIP2_', rdip2)\
            .replace('_REMIP_', rexips).replace('_INTIP_', rip1).replace('_INTIP2_', rip2).replace('_EXTIP_', rexips).replace('_FW_', rfwip).replace('_VPNIP_', rvip1).replace('_VPNIP2_', rvip2)\
            .replace('_TARGET_USER_NAME_', rnames).replace('_USER_NAME_', rnames).replace('_WORKSTATION_', rep).replace('_NIX_USER_', rnixu)\
            .replace('_DC_', rdcs).replace('_FWNAME_', rfw).replace('_SRCZONE_', rz1).replace('_DSTZONE_', rz2).replace('_NT_', NT).strip()
        #prints output as I currently use the file by running it in terminal.
    #example usage:
        #   python replace.py > output.txt
        print output


#Closes all opened files above. If you do not close the files, it does bad things. Trust me.
IPS1.close()
IPS2.close()
IPS3.close()
IP192S.close()
IP192SS.close()
DCIPS.close()
DCIPS2.close()
VIP1.close()
VIP2.close()
FWIPS.close()
ZONES1.close()
ZONES2.close()
FWS.close()
NAMES.close()
searchfile.close()
EXIPS.close()
DCS.close()
NUS.close()
EPS.close()
#DATES.close()