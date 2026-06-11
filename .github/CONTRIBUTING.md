# 기여 가이드

해상풍력 로프 시장 모니터링 시스템 프로젝트에 기여하기 위한 가이드입니다.

## 📋 개요

이 프로젝트는 DSR의 해상풍력 로프 시장 진출을 지원하는 시스템입니다.
모든 팀원이 동일한 규칙을 따라 협업합니다.

## 📝 커밋 메시지 규칙 (Conventional Commits)

### 형식

```
<type>(<scope>): <subject>

<body>

Co-Authored-By: Name <email@example.com>
```

### Type (필수)

메인 커밋 타입:

- **feat**: 새로운 기능 추가
- **fix**: 버그 수정
- **docs**: 문서 수정 (README, 가이드 등)
- **style**: 코드 스타일 변경 (공백, 들여쓰기 등)
- **refactor**: 코드 리팩토링 (기능 변화 없음)
- **test**: 테스트 추가 또는 수정
- **chore**: 빌드, 의존성, 설정 파일 변경
- **perf**: 성능 개선
- **ci**: CI/CD 관련 변경

### Scope (선택)

변경 영역을 명시합니다:

- `memory` - 메모리 시스템
- `docs` - 문서
- `task` - 스케줄 작업
- `market-report` - 시장 리포트
- `offshore-rope` - 해상풍력 로프
- `github` - GitHub 관련

### Subject (필수)

- 명령형으로 작성 (한국어 또는 영어)
- 첫 글자 대문자 (영어인 경우)
- 마침표 없음
- 50자 이내

### Body (선택)

- 변경의 **이유**를 설명
- **어떻게** 변경했는지 설명
- 한국어 선호

### Co-Authored-By (권장)

AI 또는 팀원과 함께 작업한 경우:

```
Co-Authored-By: Claude Haiku <noreply@anthropic.com>
Co-Authored-By: Team Member <member@dsr.com>
```

### 예시

#### 예시 1: 새로운 기능
```
feat(market-report): Add weekly offshore rope market monitoring

주간 해상풍력 로프 시장 리포트 자동화 기능 추가
- 재료/기술 개발 동향 모니터링
- 시장 규모/성장률 분석
- 규제/인증 표준 추적
- 경쟁사 동향 분석

Scheduled task로 매주 월요일 오전 9시에 자동 실행됩니다.

Co-Authored-By: Claude Haiku <noreply@anthropic.com>
```

#### 예시 2: 문서 수정
```
docs(offshore-rope): Update project overview in README

프로젝트 개요 섹션 업데이트
- 목표 및 범위 명확화
- 기술 스택 추가
- 출처 정보 업데이트

Co-Authored-By: Claude Haiku <noreply@anthropic.com>
```

#### 예시 3: 버그 수정
```
fix(memory): Fix memory system initialization

메모리 시스템 초기화 오류 수정
- MEMORY.md 인코딩 문제 해결
- 디렉토리 경로 정정
- 파일 생성 실패 문제 해결

Co-Authored-By: Claude Haiku <noreply@anthropic.com>
```

#### 예시 4: 메모리 업데이트
```
docs(memory): Update project memory for Q2 2026

프로젝트 메모리 최신화
- 최신 시장 진출 현황 반영
- 새로운 경쟁사 정보 추가
- 규제 변화 사항 업데이트

Co-Authored-By: Claude Haiku <noreply@anthropic.com>
```

## 🌿 브랜치 명명 규칙

브랜치는 작업 타입과 설명으로 구성합니다:

```
<type>/<description>
```

### 예시

- `feature/readme-generation` - README 자동 생성 기능
- `fix/memory-encoding` - 메모리 인코딩 버그 수정
- `docs/market-research` - 시장 조사 문서 작성
- `chore/update-dependencies` - 의존성 업데이트

### 규칙

- 소문자만 사용
- 단어는 하이픈으로 구분
- 작업 완료 후 삭제

## 🔄 PR (Pull Request) 프로세스

### 1단계: 브랜치 생성
```bash
git checkout -b feature/my-feature
```

### 2단계: 변경 및 커밋
```bash
# 파일 수정
git add .
git commit -m "feat(scope): description"
```

### 3단계: 푸시
```bash
git push origin feature/my-feature
```

### 4단계: PR 생성
GitHub에서 Pull Request 생성:
- 제목: 커밋 메시지의 subject 사용
- 설명: 변경 내용, 이유, 테스트 방법 포함

### 5단계: 검토 및 승인
- 코드 리뷰 진행
- 피드백 반영
- 승인 후 merge

### 6단계: 정리
병합 후 브랜치 삭제:
```bash
git branch -d feature/my-feature
```

## 📊 파일 구조 규칙

### 문서 파일
- 위치: `docs/` 또는 루트 (`README.md`, `ONBOARDING.md`)
- 형식: 마크다운 (`.md`)
- 인코딩: UTF-8
- 한국어 선호

### 연구 자료
- 위치: `research/`
- 형식: PDF, HTML, TXT 등
- 이름: 영문 + 날짜 (예: `market_analysis_20260611.pdf`)

### 리포트
- 위치: `reports/`
- 형식: 마크다운 또는 PDF
- 이름: 년-월 (예: `2026-06-market-report.md`)

### 설정 파일
- 위치: `config/`
- 형식: JSON, YAML, INI 등
- 주석: 한국어

### 스크립트
- 위치: 루트 또는 `scripts/`
- 형식: Python (`.py`), Shell (`.sh`) 등
- 주석: 한국어

## 🔍 코드 스타일

### Python

PEP 8 준수:
```python
# 좋음
def create_memory_system():
    """메모리 시스템 초기화"""
    memory_dir = Path.home() / '.claude'
    memory_dir.mkdir(parents=True, exist_ok=True)

# 안 좋음
def CreateMemorySystem():
    memory_dir=Path.home()/'\.claude'
```

### 주석

한국어로 작성:
```python
# 메모리 디렉토리 생성
memory_dir.mkdir(parents=True, exist_ok=True)
```

### 변수명

영어 사용, 명확한 이름:
```python
# 좋음
market_report = load_report('offshore_rope_market')

# 안 좋음
mr = load_report('orm')
```

## ✅ 체크리스트

커밋하기 전에 확인:

- [ ] 브랜치 이름이 규칙을 따르는가?
- [ ] 커밋 메시지가 Conventional Commits를 따르는가?
- [ ] 파일이 올바른 위치에 있는가?
- [ ] UTF-8 인코딩을 사용했는가?
- [ ] 불필요한 파일을 추가하지 않았는가? (`.pyc`, `__pycache__` 등)
- [ ] 메모리 파일을 업데이트했는가? (필요하면)

## 🚫 금지 사항

다음은 하지 마세요:

- ❌ `git push --force` (강제 푸시)
- ❌ main/master 브랜치에 직접 커밋
- ❌ 민감한 정보 커밋 (API 키, 패스워드 등)
- ❌ 대용량 파일 (.exe, `.zip` 등)
- ❌ 포맷되지 않은 코드

## 🤝 협업 규칙

### 리뷰 요청
PR 작성 시 명확한 설명 포함:
- 변경 내용
- 이유
- 테스트 방법
- 관련 이슈 번호

### 피드백 대응
- 빨리 응답하기 (24시간 이내)
- 건설적인 피드백 환영
- 질문이 있으면 댓글로 물어보기

### 병합 기준
- [ ] CI/CD 통과
- [ ] 코드 리뷰 승인
- [ ] 충돌 해결

## 📞 문의

문제가 있으면:
1. GitHub Issues에 질문하기
2. 가이드 다시 읽기
3. 팀원에게 물어보기

---

**감사합니다! 함께 성장하는 프로젝트를 만들어갑시다.** 🚀

마지막 업데이트: 2026-06-11
