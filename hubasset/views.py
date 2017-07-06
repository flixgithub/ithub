from django.shortcuts import render
from django.http import HttpResponse
from hubasset.models import AssetSh, AssetBj, AssetNj
from django.views.generic import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import searchForm
from django.db.models import Q


def home(request):
    sh_list = AssetSh.objects.all()
    paginator = Paginator(sh_list, 10)
    aseet_sh_list = paginator.page(1)
    return render(request, 'home.html', {'asset_sh_list': aseet_sh_list})


def get_sh_asset(request):
    sh_list = AssetSh.objects.all()
    paginator = Paginator(sh_list, 10)
    page = request.GET.get('page')
    try:
        aseet_sh_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        aseet_sh_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        aseet_sh_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'asset_sh_list': aseet_sh_list})


def get_asset_detail(request):
    hostname = request.GET.get('hostname')
    sh_detail_list = AssetSh.objects.filter(hostname=hostname)

    return render(request, 'assetDetail.html', {'sh_detail_list': sh_detail_list})


def search(request):
    if request.method == 'POST':
        # form = searchForm(request.POST)
        qc = request.POST['searchQ']
        sh_detail_list = AssetSh.objects.filter(Q(asset_id=qc) | Q(bams_id=qc) | Q(hostname=qc)
                                                | Q(ip_addr=qc) | Q(ilom_ip=qc))

        # print(qr)
    return render(request, 'assetDetail.html', {'sh_detail_list': sh_detail_list})




