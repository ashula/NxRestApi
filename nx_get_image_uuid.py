#
#    module nx_get_image_uuid.py
#
#    Ver-0.01: 24Oct2017, Inital implementation.
#
#    get list of uuids for AHV VM images with specified name.
#    Be careful, image name is not uniue on AHV.
#
import sys
import json
import nx_get_images

def get_image_uuid(JSON,IMAGE_NAME):
      # print >>sys.stderr, "get_image_uuid(): passed name:%s" % IMAGE_NAME
      num = JSON["metadata"]["total_entities"]
      # print >> sys.stderr, "Entities:%d" % num

      image_uuid_list=[]
      i=0
      while (i<num):
          image = JSON["entities"][i]
          # print >>sys.stderr,"%s:%s"  % (image["name"],image["uuid"])
          if (image["name"]==IMAGE_NAME):
              # print >> sys.stderr, "Hit!"
              image_uuid_list.append(image["uuid"])
          i+=1
          # print image_uuid_list

      return image_uuid_list

if (__name__=='__main__'):
    false=False
    test_body = {
      "metadata": {
          "grand_total_entities": 24,
          "total_entities": 24
      },
      "entities": [
      {
          "uuid": "fc14caf7-6d91-4e77-aba8-80accc00a85e",
          "name": "IMG-TEST",
          "deleted": false,
          "storage_container_id": 12246,
          "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
          "logical_timestamp": 2,
          "image_type": "DISK_IMAGE",
          "vm_disk_id": "9e567ff8-fb32-4536-b08a-83135d58bf63",
          "image_state": "ACTIVE",
          "created_time_in_usecs": 1504004814336187,
          "updated_time_in_usecs": 1504004814818358
      },
      {
      "uuid": "fec550e3-f671-4ecc-994c-dd535039f2d4",
      "name": "ISO-CENT7",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "12b47f04-4a2f-48ae-bafd-ba335a7a2be9",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1492996693694688,
      "updated_time_in_usecs": 1492997225717857
    },
    {
      "uuid": "d14da7b9-5fb2-4e22-87f2-7d5f5efc88dd",
      "name": "IMG-DOCKER-HOST",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "2122fda0-8848-4c19-b290-fa6a3abbcf3a",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1493022560757455,
      "updated_time_in_usecs": 1493022561070472
    },
    {
      "uuid": "d5db59d2-6f4f-4487-a3c3-4353b82268e7",
      "name": "ISO-WIN2016",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "2fb4b0dc-32f9-44be-84cc-f4afa405f831",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1493001373769092,
      "updated_time_in_usecs": 1493001374314248
    },
    {
      "uuid": "e9159e96-8e8d-452d-a776-d1e02147af9c",
      "name": "ISO-VIRTIO1.1.1",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "35d2e244-3f7c-4bc7-bf71-84867dcf63bf",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1506580275654901,
      "updated_time_in_usecs": 1506580276191778
    },
    {
      "uuid": "f0683a5b-9376-4b17-8e4c-a8f2a7845536",
      "name": "IMG-CALM",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "cff4ed95-d324-4288-9811-578eb7d77118",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1492998077914478,
      "updated_time_in_usecs": 1492998078336948
    },
    {
      "uuid": "f32f39de-1ab8-41d1-a6e5-1b3af4a1afca",
      "name": "ISO-UBU17",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "46e43e1a-c99a-4667-bcf3-46af12f15d2b",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1492996901265624,
      "updated_time_in_usecs": 1492997214482273
    },
    {
      "uuid": "1741f618-f37f-4194-8cd2-7a5a903f9e8e",
      "name": "IMG-UBU17",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "b2cdcbd4-658d-4b0e-9f27-5e5a874f0869",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1493020064233062,
      "updated_time_in_usecs": 1493020064604127
    },
    {
      "uuid": "2499df4f-64a7-48a0-bfa6-68c3ef5f9948",
      "name": "IMG-PC-HOME",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "6cb53ff5-d16b-4f1e-aaa8-4ae5d455e172",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1493000649331787,
      "updated_time_in_usecs": 1493000654538397
    },
    {
      "uuid": "30db2b84-1e5b-43ce-9b63-5a5742ef5fe8",
      "name": "ISO-VIRTIO",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "6417c5d3-821e-4c5a-b07e-b3573f94181d",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1492996700818534,
      "updated_time_in_usecs": 1492997236142726
    },
    {
      "uuid": "3268ee40-f2d2-4286-affc-24bc36ca90ff",
      "name": "IMG-CENT7",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "09203ca2-1c90-4c8d-bbbf-d4349f661255",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1493020017695629,
      "updated_time_in_usecs": 1493020018234123
    },
    {
      "uuid": "43063416-c7f0-4cc3-8214-5f71dc1e4ea4",
      "name": "ISO-WIN7",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "ed1593d7-a947-42ec-9cac-b3e47dca9baf",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1506579493688884,
      "updated_time_in_usecs": 1506579494174184
    },
    {
      "uuid": "4ecff829-f07f-4cbd-965c-7b283a6bf3bd",
      "name": "Migrated VM image from ESXi",
      "deleted": false,
      "storage_container_id": 11854899,
      "storage_container_uuid": "1194d858-2d9d-46d5-9639-264c79b526b7",
      "logical_timestamp": 1,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "69ef10cf-1e3e-4660-954e-035613dceecc",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1506323245066390,
      "updated_time_in_usecs": 1506323245066390
    },
    {
      "uuid": "55ab50f1-c0b1-4b43-8c5f-4ef97ab61464",
      "name": "IMG-SAG2",
      "deleted": false,
      "storage_container_id": 12247,
      "storage_container_uuid": "deafd50c-8588-4de3-b162-f540583e3bb5",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "55934081-f7e1-4881-a499-3e0cd35ecd91",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1503242091954487,
      "updated_time_in_usecs": 1503242092998053
    },
    {
      "uuid": "66cd2fbc-97fa-44c7-98fc-7b6443224524",
      "name": "ISO-OFFICE2016x86",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "1f5f47dc-19e5-4529-8030-58bd5c512022",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1506582729793503,
      "updated_time_in_usecs": 1506582730485341
    },
    {
      "uuid": "6a0eb732-6d58-46c2-b11e-b28cd3711956",
      "name": "Mallanox NEO",
      "deleted": false,
      "storage_container_id": 12247,
      "storage_container_uuid": "deafd50c-8588-4de3-b162-f540583e3bb5",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "d9560dce-87b1-4393-b3b8-3e17446ba2cd",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1502935288211010,
      "updated_time_in_usecs": 1502935288827101
    },
    {
      "uuid": "83c89978-bde0-4159-9844-0b15024b39bb",
      "name": "ISO-WIN10-1703",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "8f517451-f251-4252-ac5c-90fcf59a09d5",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1508217757869704,
      "updated_time_in_usecs": 1508217759118602
    },
    {
      "uuid": "804dd923-edfc-447a-af63-601b76e9c3f4",
      "name": "COS69",
      "annotation": "CentOS 6.9",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 1,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "5f3dd5ea-4c9a-4045-ab3c-646c4d0d5fca",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1505885183934950,
      "updated_time_in_usecs": 1505885183934950
    },
    {
      "uuid": "90a0068f-238a-452d-8b79-dd69743d9603",
      "name": "xCOS69_ISO",
      "deleted": false,
      "storage_container_id": 15166670,
      "storage_container_uuid": "9a871171-cee7-4139-b5e2-8a7fb07ec7ff",
      "logical_timestamp": 1,
      "vm_disk_id": "377c3a35-0c4e-4d0a-a52b-a78467cfaf7d",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1508752078640320,
      "updated_time_in_usecs": 1508752078640320
    },
    {
      "uuid": "9960cfed-c6d6-42dc-b1f4-e466da22b235",
      "name": "IMG-PC-BOOT",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "a3992fb6-42d0-4908-9d08-ad3809e6071a",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1493000802205237,
      "updated_time_in_usecs": 1493000807427253
    },
    {
      "uuid": "a52f74d0-9a33-46f8-9118-35622fc0f107",
      "name": "ISO-WIN10",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "4435614f-fde5-45d8-a80b-300d942f319b",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1492997282505654,
      "updated_time_in_usecs": 1492997282713802
    },
    {
      "uuid": "bbe1f2d4-f134-4e33-8d64-527651ad5188",
      "name": "ISO-UBU16",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "ISO_IMAGE",
      "vm_disk_id": "0da73ecb-76f1-42e7-bab6-4eb930f9e908",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1492996828492164,
      "updated_time_in_usecs": 1492997205751630
    },
    {
      "uuid": "b8fa6a9b-ed82-4cb8-a8da-5d6536623fcb",
      "name": "IMG-WIN10",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "d66cc3ee-d594-4166-b97a-63ded647acfc",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1493020123765280,
      "updated_time_in_usecs": 1493020124157560
    },
    {
      "uuid": "c6e3f0fe-b2a6-44e1-acc6-8bd9b8972b10",
      "name": "IMG-PC-DATA",
      "deleted": false,
      "storage_container_id": 12246,
      "storage_container_uuid": "e59ca1ff-f8f2-4cdb-9a5a-f7163df008c0",
      "logical_timestamp": 2,
      "image_type": "DISK_IMAGE",
      "vm_disk_id": "5b6dd54c-28c0-4f21-8a44-459762dd6e6e",
      "image_state": "ACTIVE",
      "created_time_in_usecs": 1493000826180616,
      "updated_time_in_usecs": 1493000831396645
    }
  ]
}

VIP = '172.16.2.109:9440'
test_body = nx_get_images.nx_get_images(VIP)
# print >> sys.stderr, test_body.text
uuid_list = get_image_uuid(test_body.json(),"xCOS69_ISO")

print uuid_list
