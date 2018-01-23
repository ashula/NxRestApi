#
#    Module: nx_get_vmdisks.py
#
#    Ver-0.01: 18Jan2018, Initial implementation to get vmdisk info .  from nx_get_vms.py
#    Ver-0.03: 17Jan2018, get vm info with nic and vmdisk info.
#    Ver-0.02: 21Dec2017, get vm info with nic info.
#    Ver-0.01: 05Nov2017, initial nx_get_vms.py from nx_get_image.py Ver-0.05.
#    Ver-0.05: 25Oct2017, get VIP through arguments.
#    Ver-0.04: 25Oct2017, separate port address of PRISM from VIP argument. (due to change of rest_api())
#    Ver-0.03: 24Oct2017, define nx_get_images()
#    Ver-0.02: 10Oct2017, text -> json conversion should be done in nx_rest_api.rest_api().
#    Ver-0.01: 20Oct2017, Initial implementation from nx_images.py and nx_rest_api.py
#
#    $ python ./nx_get_vmdisk.py  VIP VM_Name
#
#    func. nx_get_vms() return REST api
#    func. print_nx_vms_list() prints list of VM_name, container_uuid, vmdisk_uuid, ip_address
#
import os
import sys
import traceback
import json
import requests
import get_argv
import nx_get_vms
import read_credentials
import nx_rest_api

#def  nx_get_vms(VIP):
##    SUB_URL = 'PrismGateway/services/rest/v2.0/images/'
#    SUB_URL = 'api/nutanix/v2.0/vms/?include_vm_disk_config=true&include_vm_nic_config=true'
#
#    payload = {}
#    r = requests.Response()
#    r = nx_rest_api.rest_api(VIP, SUB_URL, payload, 'get')
#    return r

def nx_get_virtual_disks(VIP):
    SUB_URL = 'PrismGateway/services/rest/v2.0/virtual_disks/'

    payload = {}
    r = requests.Response()
    r = nx_rest_api.rest_api(VIP, SUB_URL, payload, 'get')
    return r

def nx_get_virtual_disk_uuid(JSON, VM_NAME):
    num = JSON["metadata"]["total_entities"]
    print >> sys.stderr, "virtual_disks#=%d" % num

    i = 0
    uuid = ""
    while (i < num):
        virtual_disk = JSON["entities"][i]

        if (virtual_disk['attached_vmname']==VM_NAME):
            uuid = virtual_disk['uuid']
            break

        i += 1

    return uuid

def print_nx_virtual_disks_list(JSON):
    num = JSON["metadata"]["total_entities"]
    print >> sys.stderr, "virtual_disks#=%d" % num

    print "vmname,vm_uuid,uuid,storage_container_uuid,disk_capacity(Bytes)"

    i = 0
    while (i < num):
        virtual_disk = JSON["entities"][i]

        print "%s,%s,%s,%s,%d" % (virtual_disk['attached_vmname'], \
                                      virtual_disk['attached_vm_uuid'],\
                                      virtual_disk['uuid'],\
                                      virtual_disk['storage_container_uuid'],\
                                      virtual_disk['disk_capacity_in_bytes']\
                                  )
        i += 1

if (__name__=='__main__'):
    argc, argv = get_argv.get_argv(2)
    VIP = argv[1]

    r = nx_get_virtual_disks(VIP)

    print >> sys.stderr, "Return_code:%d" % r.status_code
    print "%s" % r.text

    print_nx_virtual_disks_list(r.json())

    print "=" * 20

    VM_NAME = 'xREST-1'
    print "%s, %s" % (VM_NAME, nx_get_virtual_disk_uuid(r.json(), VM_NAME))
    # print "%s, %s" %  (VM_NAME, uuid)
