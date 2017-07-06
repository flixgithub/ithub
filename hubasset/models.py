from django.db import models


class AssetSh(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID")

    asset_id = models.CharField(max_length=20, db_column="ASSET_ID", )
    bams_id = models.CharField(max_length=50, db_column="BAMS_ID", unique=True)
    hostname = models.CharField(max_length=100, db_column="HOSTNAME", db_index=True, unique=True)
    ip_addr = models.CharField(max_length=50, db_column="IP_ADDRESS", db_index=True, unique=True)
    ilom_ip = models.CharField(max_length=50, db_column="ILOM_IP", db_index=True)
    device_type = models.CharField(max_length=50, db_column="DEVICE_TYPE")

    VIRTUAL_INSTANCE = (
        ('p', 'Physical'),
        ('v', 'Virtual'),
    )
    is_Virtual_Instance = models.CharField(max_length=1, choices=VIRTUAL_INSTANCE)
    cpu_num = models.IntegerField(db_column="CPU_No")
    memory = models.IntegerField(db_column="MEMORY")
    usage_catalog = models.CharField(max_length=50, db_column="USAGE_CATALOG")
    os = models.CharField(max_length=100, db_column="OS")
    hub_zone = models.CharField(max_length=50, db_column="HUB_ZONE")
    vlan = models.CharField(max_length=20, db_column="VLAN")
    comment = models.CharField(max_length=300, db_column="COMMENT")
    created_time = models.DateTimeField(db_column="CREATED_TIME", auto_now_add=True)

    dataroom = models.CharField(max_length=20, db_column="DATAROOM")
    row = models.IntegerField("ROW")
    rack = models.IntegerField("RACK")
    ru_no = models.CharField(max_length=20, db_column="RU_No")

    price = models.FloatField(db_column="PRICE")
    product = models.CharField(max_length=50, db_column="PRODUCT")
    pdu = models.CharField(max_length=100, db_column="PDU")

    VM_CHOICES = (
        ('y', 'yes'),
        ('n', 'no'),
    )
    vm_host = models.CharField(max_length=1, choices=VM_CHOICES)

    def __str__(self):
        return self.bams_id


class AssetBj(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID")

    asset_id = models.CharField(max_length=20, db_column="ASSET_ID", )
    bams_id = models.CharField(max_length=50, db_column="BAMS_ID", unique=True)
    hostname = models.CharField(max_length=100, db_column="HOSTNAME", db_index=True, unique=True)
    ip_addr = models.CharField(max_length=50, db_column="IP_ADDRESS", db_index=True, unique=True)
    ilom_ip = models.CharField(max_length=50, db_column="ILOM_IP", db_index=True)
    device_type = models.CharField(max_length=50, db_column="DEVICE_TYPE")

    VIRTUAL_INSTANCE = (
        ('p', 'Physical'),
        ('v', 'Virtual'),
    )
    is_Virtual_Instance = models.CharField(max_length=1, choices=VIRTUAL_INSTANCE)
    cpu_num = models.IntegerField(db_column="CPU_No")
    memory = models.IntegerField(db_column="MEMORY")
    usage_catalog = models.CharField(max_length=50, db_column="USAGE_CATALOG")
    os = models.CharField(max_length=100, db_column="OS")
    hub_zone = models.CharField(max_length=50, db_column="HUB_ZONE")
    vlan = models.CharField(max_length=20, db_column="VLAN")
    comment = models.CharField(max_length=300, db_column="COMMENT")
    created_time = models.DateTimeField(db_column="CREATED_TIME", auto_now_add=True)

    dataroom = models.CharField(max_length=20, db_column="DATAROOM")
    row = models.IntegerField("ROW")
    rack = models.IntegerField("RACK")
    ru_no = models.CharField(max_length=20, db_column="RU_No")

    price = models.FloatField(db_column="PRICE")
    product = models.CharField(max_length=50, db_column="PRODUCT")
    pdu = models.CharField(max_length=100, db_column="PDU")

    VM_CHOICES = (
        ('y', 'yes'),
        ('n', 'no'),
    )
    vm_host = models.CharField(max_length=1, choices=VM_CHOICES)


class AssetNj(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID")

    asset_id = models.CharField(max_length=20, db_column="ASSET_ID", )
    bams_id = models.CharField(max_length=50, db_column="BAMS_ID", unique=True)
    hostname = models.CharField(max_length=100, db_column="HOSTNAME", db_index=True, unique=True)
    ip_addr = models.CharField(max_length=50, db_column="IP_ADDRESS", db_index=True, unique=True)
    ilom_ip = models.CharField(max_length=50, db_column="ILOM_IP", db_index=True)
    device_type = models.CharField(max_length=50, db_column="DEVICE_TYPE")

    VIRTUAL_INSTANCE = (
        ('p', 'Physical'),
        ('v', 'Virtual'),
    )
    is_Virtual_Instance = models.CharField(max_length=1, choices=VIRTUAL_INSTANCE)
    cpu_num = models.IntegerField(db_column="CPU_No")
    memory = models.IntegerField(db_column="MEMORY")
    usage_catalog = models.CharField(max_length=50, db_column="USAGE_CATALOG")
    os = models.CharField(max_length=100, db_column="OS")
    hub_zone = models.CharField(max_length=50, db_column="HUB_ZONE")
    vlan = models.CharField(max_length=20, db_column="VLAN")
    comment = models.CharField(max_length=300, db_column="COMMENT")
    created_time = models.DateTimeField(db_column="CREATED_TIME", auto_now_add=True)

    dataroom = models.CharField(max_length=20, db_column="DATAROOM")
    row = models.IntegerField("ROW")
    rack = models.IntegerField("RACK")
    ru_no = models.CharField(max_length=20, db_column="RU_No")

    price = models.FloatField(db_column="PRICE")
    product = models.CharField(max_length=50, db_column="PRODUCT")
    pdu = models.CharField(max_length=100, db_column="PDU")

    VM_CHOICES = (
        ('y', 'yes'),
        ('n', 'no'),
    )
    vm_host = models.CharField(max_length=1, choices=VM_CHOICES)



