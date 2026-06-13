# Agent Work Log

이 파일은 에이전트 작업 로그입니다.

중요한 save, ingest, query, lint 작업이나 구조 변경이 끝나면 한 줄씩 추가합니다.

형식:

```text
YYYY-MM-DD HH:mm | command | summary | linked files
```

## Log

2026-06-13 16:20 | assets | shared-assets/diagrams, shared-assets/logos/partners image assets updated and new files added. Replaced 3 older diagram files. | shared-assets/diagrams, shared-assets/logos/partners
2026-06-13 14:55 | restructure | deck-maker를 산출물 작업용 repo로 구조 전환. .gitignore, Git LFS, .gitattributes 설정. materials/ -> shared-assets/ + projects/*/assets/, decks/ -> projects/*/html/, reference/ -> style-guides/, scripts 통합. HTML 이미지 경로 365건 수정. source-projects.md, master-context-usage/ 생성. CHATGPT.md, AGENTS.md, index.md, README.md 갱신. 프로젝트별 README.md 생성. | index.md, README.md, AGENTS.md, CHATGPT.md, source-projects.md
