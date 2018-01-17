#
#    Module: nx_get_vms.py
#
#    Ver-0.03: 17Jan2018, get vm info with nic and vmdisk info.
#    Ver-0.02: 21Dec2017, get vm info with nic info.
#    Ver-0.01: 05Nov2017, initial nx_get_vms.py from nx_get_image.py Ver-0.05.
#    Ver-0.05: 25Oct2017, get VIP through arguments.
#    Ver-0.04: 25Oct2017, separate port address of PRISM from VIP argument. (due to change of rest_api())
#    Ver-0.03: 24Oct2017, define nx_get_images()
#    Ver-0.02: 10Oct2017, text -> json conversion should be done in nx_rest_api.rest_api().
#    Ver-0.01: 20Oct2017, Initial implementation from nx_images.py and nx_rest_api.py
#
#    $ python ./nx_get_vms.py  VIP 
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
import read_credentials
import nx_rest_api

def  nx_get_vms(VIP):
#    SUB_URL = 'PrismGateway/services/rest/v2.0/images/'
    SUB_URL = 'api/nutanix/v2.0/vms/?include_vm_disk_config=true&include_vm_nic_config=true'

    payload = {}
    r = requests.Response()
    r = nx_rest_api.rest_api(VIP, SUB_URL, payload, 'get')
    return r

def print_nx_vms_list(JSON):
    # for some reasons, 'total_entities' = 0 in AOS-5.1.0.3
    num = JSON["metadata"]["count"]
    print num

    i = 0
    while (i < num):
        vm = JSON["entities"][i]
        # print >>sys.stderr,"%s:%s"  % (vm["name"],image["uuid"])
        num_disk = (len(vm['vm_disk_info']))
        num_nic  = (len(vm['vm_nics']))

        # print "%s, disks=%d, nics=%d" % (vm['name'], num_disk, num_nic)

        if num_nic == 0 :
            print "%s,%s,%s," %  (vm['name'],vm['vm_disk_info'][1]['storage_container_uuid'],vm['vm_disk_info'][1]['disk_address']['vmdisk_uuid'])
        else:
            exist_ip = vm['vm_nics'][0].has_key('requested_ip_address')
            if exist_ip == True:
                print "%s,%s,%s,%s" %  (vm['name'],vm['vm_disk_info'][1]['storage_container_uuid'],vm['vm_disk_info'][1]['disk_address']['vmdisk_uuid'],vm['vm_nics'][0]['requested_ip_address'])
            else:
                print "%s,%s,%s," %  (vm['name'],vm['vm_disk_info'][1]['storage_container_uuid'],vm['vm_disk_info'][1]['disk_address']['vmdisk_uuid'])

        i += 1


if (__name__=='__main__'):

    argv=get_argv.get_argv(2)
    VIP=argv[1]

    r=nx_get_vms(VIP)

    print >> sys.stderr, "Return_code:%d" % r.status_code
    print "%s" % r.text

    print_nx_vms_list(r.json())

