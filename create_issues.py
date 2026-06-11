import subprocess
import json
from datetime import datetime

# 개선점 목록
improvements = [
    {
        "title": "README.md 추가 필요",
        "body": "## 문제\n프로젝트에 README 문서가 없어서 새로운 사용자가 프로젝트 목적과 구조를 이해하기 어렵습니다.\n\n## 해결책\n다음 내용을 포함한 README.md 작성:\n- 프로젝트 개요 (해상풍력 로프 시장 진출)\n- 디렉토리 구조\n- 메모리 시스템 설명\n- 스케줄된 작업 목록\n- 사용 방법\n\n## 우선순위\n높음"
    },
    {
        "title": "프로젝트 초기 설정 가이드 필요",
        "body": "## 문제\nScheduled task 실행 시 권한 승인 프로세스가 명확하지 않습니다.\n\n## 해결책\nONBOARDING.md 작성:\n- 프로젝트 설정 단계\n- 첫 실행 시 필요한 권한\n- 이메일 계정 연동 방법\n- 스케줄 확인 방법\n\n## 우선순위\n중간"
    },
    {
        "title": "프로젝트 구조 표준화",
        "body": "## 문제\n프로젝트 디렉토리 구조가 명확하지 않습니다.\n\n## 해결책\n다음과 같은 구조로 정리:\n- /docs - 프로젝트 문서\n- /research - 연구 자료\n- /reports - 생성된 리포트\n- /config - 설정 파일\n\n## 우선순위\n중간"
    },
    {
        "title": "메모리 시스템 초기화 스크립트 추가",
        "body": "## 문제\n메모리 시스템이 수동으로 만들어져 있어서 재사용성이 낮습니다.\n\n## 해결책\ninit_memory.py 스크립트 작성:\n- 자동으로 메모리 디렉토리 생성\n- 기본 템플릿 파일 생성\n- MEMORY.md 자동 생성\n\n## 우선순위\n낮음"
    },
    {
        "title": "깃 워크플로우 가이드 추가",
        "body": "## 문제\nGit 커밋 메시지 형식과 푸시 규칙이 정의되어 있지 않습니다.\n\n## 해결책\n.github/CONTRIBUTING.md 작성:\n- 커밋 메시지 규칙 (Conventional Commits)\n- 브랜치 명명 규칙\n- PR 프로세스\n\n## 우선종료\n낮음"
    }
]

# 이슈 생성 (마크다운 저장용)
issues_md = """# 생성된 GitHub Issues

"""

for i, issue in enumerate(improvements, 1):
    issues_md += f"## {i}. {issue['title']}\n{issue['body']}\n\n---\n\n"

# 파일에 저장
with open("IMPROVEMENTS.md", "w", encoding="utf-8") as f:
    f.write(issues_md)

print("✅ 개선점 이슈 생성 완료!")
print(f"📋 생성된 이슈: {len(improvements)}개")
for i, issue in enumerate(improvements, 1):
    print(f"  {i}. {issue['title']}")
