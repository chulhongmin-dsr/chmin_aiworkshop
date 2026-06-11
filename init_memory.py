#!/usr/bin/env python3
"""
메모리 시스템 초기화 스크립트

해상풍력 로프 시장 모니터링 프로젝트의 메모리 시스템을 자동으로 초기화합니다.

사용법:
  python init_memory.py
"""

import os
from pathlib import Path
from datetime import datetime


def create_memory_system():
    """메모리 시스템 초기화"""

    # Claude 메모리 디렉토리 확인
    claude_home = Path.home() / '.claude' / 'projects' / 'C--AI-LEADER-WORKSHOP-CHMIN-PRACTICE' / 'memory'

    # 메모리 디렉토리 생성
    claude_home.mkdir(parents=True, exist_ok=True)

    print(f"📁 메모리 디렉토리: {claude_home}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # 1. MEMORY.md 생성
    memory_md = claude_home / 'MEMORY.md'
    memory_content = """# Memory Index

- [User Profile](user_profile.md) — DSR 27년 경력, 해상풍력 로프 시장 진출 담당
- [Offshore Rope Project](project_offshore_rope.md) — 해상풍력 로프 시장 모니터링 및 정보 수집 시스템
"""
    memory_md.write_text(memory_content, encoding='utf-8')
    print(f"✅ 생성: MEMORY.md")

    # 2. user_profile.md 생성
    user_profile = claude_home / 'user_profile.md'
    user_content = """---
name: user-profile-dsr
description: DSR 직원, 27년 경력, 해상풍력 로프 시장 진출 담당
metadata:
  type: user
---

**배경:**
- 회사: DSR (한국 합성섬유로프 제조 회사)
- 경력: 27년
- 위치: 한국
- 언어: 한국어 선호

**역할:**
- 해상풍력(Offshore) 로프 시장 진출 프로젝트 담당
- 글로벌 시장 동향 조사 및 전략 수립

**선호도:**
- 주 1회 자동화 리포트 원함
- 자세한 분석본 선호 (단순 링크 아님)
"""
    user_profile.write_text(user_content, encoding='utf-8')
    print(f"✅ 생성: user_profile.md")

    # 3. project_offshore_rope.md 생성
    project_info = claude_home / 'project_offshore_rope.md'
    project_content = """---
name: project-offshore-rope-market
description: DSR의 해상풍력 로프 시장 진출 프로젝트 및 정보 추적 시스템
metadata:
  type: project
---

**프로젝트:**
- DSR의 해상풍력(Offshore) 및 해상풍력 발전용 로프 시장 진출
- 글로벌 시장 동향 및 기술 모니터링 필요

**모니터링 범위:**
1. **재료/기술 개발** - 최신 로프 재료, 코팅 기술, 내구성 개선 사항
2. **시장 규모/성장률** - 글로벌 해상풍력 로프 시장 규모, CAGR, 지역별 성장
3. **규제/인증 표준** - 국제 표준 (DNV, ABS, GL 등), 해양 관련 규제

**정보 수집 주기:** 주 1회
**정보 형식:** 요약 분석본 + 주요 소스 링크

**추적 대상:**
- 학술논문 (Google Scholar, ResearchGate)
- 산업 리포트 (Grand View Research, Allied Market Research 등)
- 경쟁사 뉴스 (주요 로프 제조업체)
- 규제/표준 기관 뉴스
"""
    project_info.write_text(project_content, encoding='utf-8')
    print(f"✅ 생성: project_offshore_rope.md")

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ 메모리 시스템 초기화 완료!")
    print(f"   위치: {claude_home}")
    print(f"   파일: 3개 (MEMORY.md, user_profile.md, project_offshore_rope.md)")


def main():
    """메인 함수"""
    print("\n🚀 메모리 시스템 초기화")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    try:
        create_memory_system()
        print("\n✨ 성공!")
        print("\n다음 단계:")
        print("1. git add .")
        print("2. git commit -m 'docs: Initialize memory system'")
        print("3. git push origin master")

    except Exception as e:
        print(f"\n❌ 오류: {str(e)}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
