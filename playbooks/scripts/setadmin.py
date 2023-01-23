#!/usr/bin/env python
# 어드민 인증을 설정하기 위한 스크립트
# 세 환경 변수를 사용한다고 가정한다
#
# PROJECT_DIR: 프로젝트 디렉토리(예, ~/projname)
# PROJECT_APP: 프로젝트 애플리케이션 이름
# ADMIN_PASSWORD: 어드민 사용자의 패스워드

import os
import sys

# 시스템 경로에 프로젝트 디렉토리를 추가한다
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

proj_app = os.environ['PROJECT_APP']
os.environ['DJANGO_SETTINGS_MODULE'] = proj_app + '.settings'
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
u, _ = User.objects.get_or_create(username='admin')
u.is_staff = u.is_superuser = True
u.set_password(os.environ['ADMIN_PASSWORD'])
u.save()
