#!/usr/bin/env python

# 웹 사이트 도메인을 설정하는 스크립트
# 세 환경 변수를 사용한다고 가정한다
#
# WEBSITE_DOMAIN: 웹 사이트 도메인 (예, www.example.com)
# PROJECT_DIR: 프로젝트의 루트 디렉토리
# PROJECT_APP: 프로젝트 애플리케이션 이름
import os
import sys

# 시스템 경로에 프로젝트 디렉토리를 추가한다
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

proj_app = os.environ['PROJECT_APP']
os.environ['DJANGO_SETTINGS_MODULE'] = proj_app + '.settings'
import django
django.setup()
from django.conf import settings
from django.contrib.sites.models import Site
domain = os.environ['WEBSITE_DOMAIN']
Site.objects.filter(id=settings.SITE_ID).update(domain=domain)
Site.objects.get_or_create(domain=domain)
