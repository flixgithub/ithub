# -*- coding:utf8 -*-
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ithub.settings")
django.setup()
from hubasset.models import AssetSh, AssetNj, AssetBj


if __name__ == '__main__':
    asset_sh = AssetSh.objects.create(
        asset_id='4012871',
        bams_id='bams-1001473739',
        hostname='ecnshux1014.sh.cn.ao.ericsson.se',
        ip_addr='147.128.73.34',
        ilom_ip='147.128.73.34',
        device_type='DL360 G6',
        is_Virtual_Instance='p',
        cpu_num=16,
        memory=72,
        usage_catalog='ClearCase',
        os='Solaris 10u6',
        hub_zone='INTR_BASE_PROD_Z0012',
        vlan='121',
        comment='',
        # created_time,
        dataroom='Primary',
        row=1,
        rack=2,
        ru_no='2',
        price=2372.5,
        product='CLEARCASE VIEW & VOB server',
        pdu='ALLUSE',
        vm_host='n',
    )
