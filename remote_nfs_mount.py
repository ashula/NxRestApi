#
#  NFS mount at remote linux host
#
import os

#TARGET_USER='nutanix'
#TARGET_HOST_IP ='172.16.251.66'
#TARGET_MOUNT_POINT ='/mnt/poc08'

#VIP='172.16.8.109'
#VM_CONTAINER='POC08_CTR01'

VM_IMG_SUB_DIRECTORY='.acropolis/vmdisk'

def remote_nfs_mount(
        TARGET_USER,
        TARGET_HOST_IP,
        TARGET_MOUNT_POINT,
        VIP,
        VM_CONTAINER
    ):

    VM_SUB_DIRECTORY = '.acropolis/vmdisk/'

    CMD_MOUNT="/usr/bin/ssh " \
              + TARGET_USER \
              + "@"\
              + TARGET_HOST_IP\
              + " sshpass -p 'nutanix/4u' sudo mount -t nfs "\
              + VIP\
              + ":/"\
              + VM_CONTAINER\
              + " "\
              + TARGET_MOUNT_POINT

    print CMD_MOUNT
    os.system(CMD_MOUNT)

def remote_nfs_ls(
        TARGET_USER,
        TARGET_HOST_IP,
        TARGET_MOUNT_POINT,
        VIP,
        VM_CONTAINER
    ):

    CMD_LS="/usr/bin/ssh "  \
           + TARGET_USER \
           + "@" \
           + TARGET_HOST_IP \
           + " ls "\
           + TARGET_MOUNT_POINT \
           + "/" \
           + VM_IMG_SUB_DIRECTORY

    print CMD_LS
    os.system(CMD_LS)

def remote_nfs_umount(
        TARGET_USER,
        TARGET_HOST_IP,
        TARGET_MOUNT_POINT,
        VIP,
        VM_CONTAINER
    ):

    CMD_UMOUNT="/usr/bin/ssh "\
               + TARGET_USER\
               + "@"\
               + TARGET_HOST_IP\
               + " sshpass -p 'nutanix/4u' sudo umount "\
               + TARGET_MOUNT_POINT

    print CMD_UMOUNT
    os.system(CMD_UMOUNT)

def remote_scp_to_esxi_datastore(
          TARGET_USER,
          TARGET_HOST_IP,
          TARGET_MOUNT_POINT,
          SRC_FILE_NAME,
          DST_ESXI_IP,
          DST_ESXI_PWD,
          DST_ESXI_DATASTORE,
          DST_ESXI_SUB_DIR,
          DST_ESXI_FILE_NAME
    ):

    # VM_SUB_DIRECTORY = '.acropolis/vmdisk/'

    CMD_SCP="/usr/bin/ssh " \
             + TARGET_USER \
             + "@" \
             + TARGET_HOST_IP \
             + " sshpass -p " \
             + "'" \
             + DST_ESXI_PWD \
             + "'" \
             + " " \
             + "scp " \
             + TARGET_MOUNT_POINT \
             + "/" \
             + VM_IMG_SUB_DIRECTORY \
             + "/" \
             + SRC_FILE_NAME \
             + " root@" \
             + DST_ESXI_IP \
             + ":/vmfs/volumes/" \
             + DST_ESXI_DATASTORE \
             + "/" \
             + DST_ESXI_SUB_DIR  \
             + "/" \
             + DST_ESXI_FILE_NAME

    print CMD_SCP
    os.system(CMD_SCP)

if __name__ == '__main__':



    TARGET_HOST_IP = '172.16.251.66'
    TARGET_USER    ='nutanix'
    TARGET_MOUNT_POINT='/mnt/poc08'
    VIP = '172.16.8.109'
    VM_CONTAINER='POC08=CTR01'

    SRC_FILE_NAME = 'fd28afd5-47bb-4876-bace-ec30d39a841c',
    DST_ESXI_IP = '172.16.254.10',
    DST_ESXI_PWD = 'nutanix/4u',
    DST_ESXI_DATASTORE = 'datastore2',
    DST_ESXI_SUB_DIR = 'moritsugu/AHV_VM',
    DST_ESXI_FILE_NAME = "TEST.qcow2"

    remote_nfs_mount(
            TARGET_USER,
            TARGET_HOST_IP,
            TARGET_MOUNT_POINT,
            VIP,
            VM_CONTAINER
        )

    remote_nfs_ls(
            TARGET_USER,
            TARGET_HOST_IP,
            TARGET_MOUNT_POINT,
            VIP,
            VM_CONTAINER
        )

    remote_scp_to_esxi_datastore(
            TARGET_USER,
            TARGET_HOST_IP,
            TARGET_MOUNT_POINT,
            SRC_FILE_NAME,
            DST_ESXI_IP,
            DST_ESXI_PWD,
            DST_ESXI_DATASTORE,
            DST_ESXI_SUB_DIR,
            DST_ESXI_FILE_NAME
        )

    remote_nfs_umount(
            TARGET_USER='nutanix',
            TARGET_HOST_IP='172.16.251.66',
            TARGET_MOUNT_POINT='/mnt/poc08',
            VIP='172.16.8.109',
            VM_CONTAINER='POC08_CTR01'
        )

