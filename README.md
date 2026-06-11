# 해상풍력 로프 시장 모니터링 시스템

DSR의 해상풍력(Offshore Wind) 로프 시장 진출을 지원하는 글로벌 시장 모니터링 및 정보 수집 시스템입니다.

## 📊 프로젝트 개요

- **목표:** 해상풍력 로프 시장의 글로벌 트렌드 모니터링
- **주기:** 주 1회 자동 리포트 생성
- **수신자:** CHMIN@DSR.COM
- **언어:** 한국어

## 🏗️ 프로젝트 구조

```
.
├── README.md                          # 프로젝트 개요 (현재 파일)
├── ONBOARDING.md                      # 초기 설정 가이드
├── IMPROVEMENTS.md                    # 시스템 개선점 이슈 목록
├── .claude/                           # Claude Code 설정
│   └── settings.local.json            # 프로젝트 설정
├── memory/                            # 프로젝트 메모리 시스템
│   ├── MEMORY.md                      # 메모리 인덱스
│   ├── user_profile.md                # 사용자 정보
│   └── project_offshore_rope.md       # 프로젝트 정보
├── docs/                              # 프로젝트 문서
├── research/                          # 연구 자료 및 논문
├── reports/                           # 생성된 리포트
├── config/                            # 설정 파일
├── mooring_paper.pdf                  # 해양 관련 연구 자료
└── .github/                           # GitHub 관련 설정
    └── CONTRIBUTING.md                # 기여 가이드
```

## 📋 핵심 기능

### 1. 주간 시장 리포트 (자동화)
**스케줄:** 매주 월요일 오전 9시 (한국 시간)

자동으로 생성되는 리포트 내용:
- 🔬 **재료/기술 개발** - 최신 로프 재료 혁신, 코팅 기술, 내구성 개선
- 📈 **시장 규모/성장률** - 글로벌 시장 현황, CAGR, 지역별 분석
- ⚖️ **규제/인증 표준** - DNV, ABS, GL 등 국제 표준 및 규제 업데이트
- 🏢 **경쟁사 동향** - 주요 로프 제조업체 뉴스 및 신제품 정보

**수신 방식:** 이메일 (CHMIN@DSR.COM)

### 2. 메모리 시스템
프로젝트의 지속성을 위해 다음 정보를 기억합니다:
- 사용자 프로필 및 선호도
- 프로젝트 현황 및 목표
- 참고 자료 위치

**메모리 파일:** `memory/MEMORY.md`에서 확인

### 3. GitHub 이슈 추적
프로젝트 개선점과 할 일을 이슈로 관리합니다.

**현재 이슈:** https://github.com/chulhongmin-dsr/chmin_aiworkshop/issues

## 🚀 빠른 시작

### 1단계: 메모리 시스템 확인
```bash
ls memory/
```
다음 파일들이 있는지 확인:
- `MEMORY.md` - 메모리 인덱스
- `user_profile.md` - 사용자 정보
- `project_offshore_rope.md` - 프로젝트 정보

### 2단계: 초기 설정 확인
`ONBOARDING.md`를 읽고 필요한 설정을 진행하세요.

### 3단계: 주간 리포트 확인
- **매주 월요일 오전 9시**에 자동으로 리포트가 생성됩니다
- 이메일 (CHMIN@DSR.COM)에서 확인

### 4단계: GitHub 이슈 처리
현재 미해결 이슈들을 확인하고 처리합니다:
https://github.com/chulhongmin-dsr/chmin_aiworkshop/issues

## 📚 문서

| 문서 | 설명 |
|------|------|
| [ONBOARDING.md](ONBOARDING.md) | 프로젝트 초기 설정 및 사용 방법 |
| [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) | Git 워크플로우 및 커밋 규칙 |
| [memory/MEMORY.md](memory/MEMORY.md) | 프로젝트 메모리 인덱스 |

## 🔧 기술 스택

- **모니터링 도구:** Claude Code + Claude API
- **저장소:** GitHub (chulhongmin-dsr/chmin_aiworkshop)
- **일정 관리:** Claude Code Scheduled Tasks
- **자동화:** GitHub API + Git

## 📊 시장 정보 수집 출처

**학술 자료:**
- Google Scholar
- ResearchGate

**산업 리포트:**
- Grand View Research
- Allied Market Research
- Mordor Intelligence

**규제/표준:**
- DNV (Det Norske Veritas)
- ABS (American Bureau of Shipping)
- GL (Germanischer Lloyd)

**경쟁사 정보:**
- Samson Rope
- Cortland
- Lankhorst
- Bridon-Bekaert

## 📞 문의 및 지원

프로젝트 관련 문의:
- 담당자: Chulhong Min (CHMIN@DSR.COM)
- 회사: DSR (합성섬유로프 제조)
- 경력: 27년

## 📝 라이선스 및 기여

이 프로젝트에 기여하고 싶으시면 [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md)를 참고하세요.

- 커밋 메시지 규칙 (Conventional Commits)
- 브랜치 명명 규칙
- PR 프로세스

## 🎯 다음 단계

1. ✅ ONBOARDING.md 읽기
2. ✅ Scheduled Task 권한 설정
3. ✅ 첫 번째 주간 리포트 확인
4. ✅ GitHub 이슈 처리 시작

---

**마지막 업데이트:** 2026-06-11  
**프로젝트 상태:** 🟢 Active
