# 프로젝트 초기 설정 가이드

해상풍력 로프 시장 모니터링 시스템의 초기 설정 및 사용 방법입니다.

## 📋 프로젝트 개요

- **이름:** 해상풍력 로프 시장 모니터링 시스템
- **목표:** DSR의 해상풍력 로프 시장 진출 지원
- **주기:** 주 1회 자동 리포트 생성
- **수신자:** CHMIN@DSR.COM

## ✅ 필수 설정

### 1단계: 메모리 시스템 확인

프로젝트의 지속성을 위해 메모리 시스템이 설정되어 있습니다.

**메모리 위치:**
```
~/.claude/projects/chmin_aiworkshop/memory/
```

**확인할 파일:**
```bash
cd ~/.claude/projects/chmin_aiworkshop/memory/
ls -la
```

다음 파일들이 있어야 합니다:
- ✅ `MEMORY.md` - 메모리 인덱스
- ✅ `user_profile.md` - 사용자 정보
- ✅ `project_offshore_rope.md` - 프로젝트 정보

**메모리 내용 확인:**
```bash
cat memory/MEMORY.md
```

### 2단계: Scheduled Task 설정

**주간 리포트 자동화가 설정되어 있습니다.**

**Task 정보:**
- **이름:** offshore-rope-market-weekly-report
- **스케줄:** 매주 월요일 오전 9시 (한국 시간)
- **내용:** 해상풍력 로프 시장 주간 리포트
- **수신자:** CHMIN@DSR.COM

#### 첫 실행 시 권한 설정

Task가 정상적으로 작동하려면 **이메일 권한 설정**이 필요합니다.

**단계:**

1. **Claude Code 앱 실행**
2. **왼쪽 사이드바 하단** → "Scheduled" 섹션 찾기
3. **"offshore-rope-market-weekly-report" 찾기**
4. **마우스 오버 또는 우클릭** → "Run now" 클릭
5. **이메일 계정 인증** (Gmail 또는 Outlook)
   - 계정 선택
   - 권한 승인
6. **테스트 실행 완료** ✅

#### 자동 실행 확인

설정 후 매주 월요일 오전 9시에:
- ✅ 리포트 자동 생성
- ✅ CHMIN@DSR.COM으로 이메일 발송

### 3단계: GitHub 저장소 연동 확인

```bash
git remote -v
```

다음과 같이 표시되어야 합니다:
```
origin  https://github.com/chulhongmin-dsr/chmin_aiworkshop.git (fetch)
origin  https://github.com/chulhongmin-dsr/chmin_aiworkshop.git (push)
```

**확인 안 되면:**
```bash
git remote add origin https://github.com/chulhongmin-dsr/chmin_aiworkshop.git
```

### 4단계: 프로젝트 구조 확인

다음 디렉토리들이 존재하는지 확인:

```bash
ls -la
```

다음이 있어야 합니다:
- ✅ `docs/` - 프로젝트 문서
- ✅ `research/` - 연구 자료
- ✅ `reports/` - 생성된 리포트
- ✅ `config/` - 설정 파일
- ✅ `.github/` - GitHub 설정

## 📅 일일 작업 가이드

### 매주 월요일 오전 9시
자동으로 생성되는 해상풍력 로프 시장 주간 리포트 확인:

**리포트 내용:**
1. 🔬 **재료/기술 개발** 
   - 최신 로프 재료 혁신
   - 코팅 및 표면 처리 기술
   - 내구성 개선 기술

2. 📈 **시장 규모/성장률**
   - 글로벌 시장 현황
   - 예상 성장률 (CAGR)
   - 지역별 시장 분석

3. ⚖️ **규제/인증 표준**
   - DNV, ABS, GL 최신 소식
   - 해양 산업 규제 변화
   - 국제 표준 업데이트

4. 🏢 **경쟁사 동향**
   - 주요 로프 제조업체 뉴스
   - 신제품 출시
   - 주요 계약 소식

**수신:**
- 📧 메일 받을 준비 (CHMIN@DSR.COM)
- 리포트 내용 검토 및 저장

### 수동 업데이트
새로운 정보나 변경사항 발생 시:

```bash
# 1. 변경사항 확인
git status

# 2. 파일 추가
git add <파일명>

# 3. 커밋
git commit -m "docs: Update market research

새로운 정보 추가

Co-Authored-By: Claude Haiku <noreply@anthropic.com>"

# 4. 푸시
git push origin master
```

## 🔧 메모리 시스템 관리

### 메모리 시스템이란?
프로젝트의 맥락과 정보를 지속적으로 기억하는 시스템입니다.

### 메모리 파일 구조

**MEMORY.md** (인덱스)
```markdown
# Memory Index

- [User Profile](user_profile.md) — 사용자 정보
- [Project Info](project_offshore_rope.md) — 프로젝트 정보
```

**user_profile.md** (사용자)
- 이름, 회사, 경력
- 선호 언어
- 역할 및 책임

**project_offshore_rope.md** (프로젝트)
- 프로젝트 목표
- 모니터링 분야
- 주요 일정

### 메모리 업데이트
중요한 정보가 변경되면 메모리도 함께 업데이트:

```bash
# 메모리 파일 편집
nano memory/project_offshore_rope.md

# 변경 후 커밋
git add memory/
git commit -m "docs: Update project memory"
git push origin master
```

## 🐛 문제 해결

### Scheduled Task가 실행되지 않는 경우

**증상:** 월요일 9시에 이메일이 안 옴

**해결 방법:**
1. Claude Code 앱이 **열려있는지** 확인
   - Task는 앱이 열려있어야만 실행됨
   
2. **"Run now"로 수동 실행**
   - Scheduled 섹션 → "Run now" 클릭
   - 이메일 발송 확인

3. **이메일 계정 재인증**
   - Run now 실행 시 계정 재인증
   - Gmail/Outlook 권한 승인

4. **로그 확인**
   - Claude Code 콘솔에서 오류 메시지 확인

### 메모리 파일이 없는 경우

```bash
# 메모리 초기화 스크립트 실행
python init_memory.py
```

### Git 푸시 실패

```bash
# 1. 최신 코드 가져오기
git pull origin master

# 2. 충돌 해결 (있으면)
git status

# 3. 다시 푸시
git push origin master
```

## 📊 모니터링 소스

### 학술 자료
- Google Scholar: https://scholar.google.com
- ResearchGate: https://www.researchgate.net

### 산업 리포트
- Grand View Research
- Allied Market Research
- Mordor Intelligence

### 규제/표준
- DNV GL: https://www.dnvgl.com
- ABS: https://ww2.eagle.org
- Germanischer Lloyd

### 경쟁사
- Samson Rope
- Cortland
- Lankhorst
- Bridon-Bekaert

## 📞 지원

문제가 있으면:
1. 이 가이드 다시 읽기
2. GitHub Issues 확인: https://github.com/chulhongmin-dsr/chmin_aiworkshop/issues
3. 프로젝트 메모리 확인: `memory/MEMORY.md`

## ✨ 다음 단계

- [ ] 메모리 시스템 확인
- [ ] Scheduled Task 권한 설정
- [ ] 첫 번째 "Run now" 실행
- [ ] GitHub 이슈 확인
- [ ] 프로젝트 구조 검토

---

**마지막 업데이트:** 2026-06-11  
**상태:** 🟢 Ready to use
