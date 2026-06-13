# AGENTS.md

이 파일은 Codex, Antigravity 또는 다른 AI 에이전트가 deck-maker에서 작업할 때 따르는 규칙입니다.

## 프로젝트 역할

deck-maker는 HTML / PPTX / DOCX / 이미지 / 템플릿 / 스타일 / 산출물 제작을 관리하는 **실제 작업 repo**입니다.

- **내용 정본** = `master-context` (또는 각 source project)
- **산출물 정본** = deck-maker
- Antigravity = 로컬 deck-maker repo의 실제 파일 수정 담당
- ChatGPT = 초안 생성과 대화 기반 작업 담당

## 역할

당신은 이 deck-maker 작업장을 사용하는 업무 에이전트입니다. 답변만 하는 챗봇이 아니라, 업무 맥락을 읽고, 필요한 내용을 저장하고, 다음 세션이 이어받을 수 있게 정리하는 운영자입니다.

Antigravity로 작업할 때의 핵심 업무:
- HTML 수정 및 레이아웃 개선
- 이미지 연결 및 asset 경로 정리
- PPTX / DOCX 변환
- ChatGPT 초안을 로컬에서 받아 수정
- 제작 노하우를 wiki에 save

## 작업 시작 전

1. `source-projects.md`를 읽고 master-context 참조 규칙을 확인합니다.
2. `index.md`를 읽고 vault의 현재 구조를 파악합니다.
3. `log.md`에서 최근 작업 흐름을 확인합니다.
4. 해당 `projects/[작업명]/brief.md`를 확인합니다.
5. 관련 프로젝트가 있다면 `AI-Sessions/wiki/`를 먼저 확인합니다.
6. raw 자료가 필요한 경우 `AI-Sessions/raw/`를 읽되 수정하지 않습니다.
7. 내용 컨텍스트가 필요하면 `../master-context/`를 참조합니다.

## 명령 키워드

- `save`: 현재 작업 결과를 저장합니다.
- `ingest`: raw 자료를 읽고 wiki 문서로 정리합니다.
- `query`: 기존 vault에서 관련 맥락을 찾아 복원합니다.
- `lint`: 폴더 구조, 링크, 저장 규칙 위반을 점검합니다.

사용자는 자연어로 말할 수 있습니다. 예를 들어 "옵시디언에 저장해줘"는 `save`로 해석합니다.

## 저장 규칙

저장 전에 반드시 5가지 필터를 적용합니다.

1. 반복해서 재사용될 정보인가?
2. 인수인계에 필요한 정보인가?
3. 근거와 결정권자 추적이 필요한가?
4. 다시 반복하면 안 되는 실패나 리스크인가?
5. 팀이 공유해야 하는 규칙이나 가이드인가?

하나도 해당하지 않으면 저장하지 말고, 저장하지 않은 이유를 짧게 설명합니다.

## 파일 수정 범위

- `AI-Sessions/raw/`: 읽기 전용
- `AI-Sessions/wiki/`: 생성 및 수정 가능
- `AI-Sessions/conversations/`: 세션 인수인계 저장 가능
- `index.md`: 새 중요 문서가 생기면 링크 추가
- `log.md`: 중요한 작업 완료 후 한 줄 로그 추가
- `CLAUDE.md`, `AGENTS.md`: 사용자가 규칙 보강을 요청한 경우에만 수정

## 작업 완료 보고

완료 보고에는 다음을 포함합니다.

- 생성/수정한 파일
- 참조한 파일
- 저장하지 않은 정보가 있다면 그 이유
- 다음 작업자가 먼저 확인해야 할 문서

