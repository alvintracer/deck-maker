# Obsidian_Github_howto.md

# Obsidian + GitHub + AI ContextHub 사용 가이드

이 문서는 프로젝트별 Obsidian AI 업무 위키 / ContextHub를 어떻게 만들고, Obsidian에서 어떻게 보고, GitHub에 어떻게 push하며, Codex / Antigravity / Claude Code / ChatGPT 같은 AI 에이전트가 어떻게 같은 컨텍스트를 공유하게 할지 설명한다.

---

## 1. 핵심 개념

이 시스템의 목적은 단순 메모 정리가 아니다.

목표는 다음과 같다.

```text
프로젝트 폴더
+ Obsidian Wiki 구조
+ GitHub 버전관리
+ AI 에이전트 운영 규칙
= 여러 AI 에이전트가 같은 프로젝트 맥락을 공유하는 ContextHub
```

각 프로젝트는 하나의 ContextHub로 운영한다.

예시:

```text
transight-tr/
traverse-wallet/
mom-attention-socialfi/
deck-maker/
```

각 프로젝트 폴더 안에는 다음과 같은 구조가 들어간다.

```text
START_HERE.md
AGENTS.md
CLAUDE.md
CHATGPT.md
index.md
log.md
prompts/
AI-Sessions/
  raw/
  wiki/
  conversations/
```

---

## 2. Obsidian은 왜 쓰는가?

Obsidian은 AI 실행 엔진이 아니다.

Obsidian은 사람이 Markdown 기반 ContextHub를 보기 쉽게 해주는 위키 UI다.

역할을 나누면 다음과 같다.

```text
GitHub
= 중앙 저장소, 버전관리, 에이전트 공유

Obsidian
= 사람이 읽고 수정하는 위키 화면

Codex / Antigravity / Claude Code
= 프로젝트 폴더를 읽고 작업하는 AI 에이전트

ChatGPT
= GitHub 또는 업로드된 ContextHub 문서를 참조해 답변하는 AI 에이전트
```

Obsidian 없이도 Markdown 파일과 GitHub만으로 운영은 가능하다.  
다만 Obsidian을 쓰면 다음이 편해진다.

- `index.md`를 목차처럼 보기
- `[[문서 링크]]`를 클릭해서 이동하기
- `AI-Sessions/wiki/` 문서를 위키처럼 탐색하기
- `log.md`로 작업 이력 확인하기
- 프로젝트 문서 관계를 그래프 뷰로 보기
- 회의 중 빠르게 메모 작성하기

---

## 3. Vault란 무엇인가?

Obsidian에서 말하는 Vault는 그냥 Markdown 파일들이 들어 있는 폴더다.

즉, 아래 프로젝트 폴더 하나하나가 모두 Vault가 될 수 있다.

```text
transight-tr/ = 하나의 Obsidian vault
traverse-wallet/ = 하나의 Obsidian vault
mom-attention-socialfi/ = 하나의 Obsidian vault
deck-maker/ = 하나의 Obsidian vault
```

특별한 파일 형식이 필요한 것이 아니다.  
기존 프로젝트 폴더를 그대로 Obsidian에서 열면 된다.

---

## 4. Obsidian 설치 및 열기

### 4.1 설치

1. Obsidian 공식 사이트에서 앱을 다운로드한다.
2. Windows 또는 Mac용 앱을 설치한다.
3. Obsidian을 실행한다.

### 4.2 프로젝트 폴더를 Vault로 열기

1. Obsidian 실행
2. `Open folder as vault` 선택
3. 기존 프로젝트 폴더 선택

예시:

```text
C:\Projects\transight-tr
```

또는

```text
/Users/username/projects/transight-tr
```

열면 왼쪽 파일 탐색기에 `START_HERE.md`, `index.md`, `log.md`, `AI-Sessions/`가 보인다.

---

## 5. 프로젝트별 ContextHub 기본 구조

각 프로젝트에는 다음 구조를 둔다.

```text
project-name/
  START_HERE.md
  AGENTS.md
  CLAUDE.md
  CHATGPT.md
  index.md
  log.md
  prompts/

  AI-Sessions/
    raw/
    wiki/
    conversations/
```

### 5.1 `AI-Sessions/raw/`

원본 자료 저장소다.

예시:

```text
AI-Sessions/raw/meetings/
AI-Sessions/raw/emails/
AI-Sessions/raw/documents/
AI-Sessions/raw/screenshots/
AI-Sessions/raw/external-sources/
```

규칙:

- raw는 불변 원본이다.
- AI 에이전트는 raw를 직접 수정하지 않는다.
- 회의록, 원본 문서, 이메일, 외부 자료, 스크린샷 등을 저장한다.

### 5.2 `AI-Sessions/wiki/`

정리된 업무 지식 저장소다.

예시:

```text
AI-Sessions/wiki/projects/
AI-Sessions/wiki/sources/
AI-Sessions/wiki/concepts/
AI-Sessions/wiki/decisions/
AI-Sessions/wiki/errors/
AI-Sessions/wiki/design/
AI-Sessions/wiki/dev-tasks/
```

프로젝트 성격에 따라 아래 폴더를 추가할 수 있다.

```text
AI-Sessions/wiki/company/
AI-Sessions/wiki/products/
AI-Sessions/wiki/partners/
AI-Sessions/wiki/commercial/
AI-Sessions/wiki/legal-compliance/
AI-Sessions/wiki/operations/
AI-Sessions/wiki/deliverables/
```

규칙:

- wiki에는 검증된 업무 지식만 저장한다.
- 일회성 답변, 중간 생각, 검증되지 않은 추측은 저장하지 않는다.
- 중요한 의사결정, 프로젝트 맥락, 반복 재사용 가능한 설명, 금지 표현, 실패 사례 등을 저장한다.

### 5.3 `AI-Sessions/conversations/`

세션 인수인계와 작업 기록 저장소다.

예시:

```text
AI-Sessions/conversations/chatgpt/
AI-Sessions/conversations/codex/
AI-Sessions/conversations/claude/
AI-Sessions/conversations/handoffs/
```

규칙:

- 다음 에이전트가 이어받을 수 있도록 handoff 문서를 저장한다.
- wiki에 승격할 정도는 아니지만 맥락 보존이 필요한 세션 기록을 둔다.

---

## 6. 가장 먼저 봐야 할 파일

Obsidian에서 프로젝트를 열면 아래 순서로 확인한다.

```text
1. START_HERE.md
2. index.md
3. log.md
4. AI-Sessions/wiki/
5. AI-Sessions/raw/
6. AI-Sessions/conversations/
```

### `START_HERE.md`

이 프로젝트의 ContextHub 사용법과 에이전트 명령어가 들어 있는 시작 문서다.

### `index.md`

프로젝트 전체 지도다.

들어가야 할 내용:

```text
Project Overview
Current Status
Key Documents
Decisions
Sources
Open Questions
Next Actions
Agent Commands
```

### `log.md`

중요 작업 기록이다.

권장 형식:

```text
YYYY-MM-DD HH:mm | command | summary | linked files
```

예시:

```text
2026-06-13 15:20 | ingest | added Bybit IAAN legal questions | AI-Sessions/wiki/projects/bybit-iaan.md
```

---

## 7. 기존 프로젝트에 템플릿 적용하기

### 7.1 기존 프로젝트 백업

프로젝트 폴더에서 먼저 Git 상태를 확인한다.

```bash
git status
```

현재 상태를 백업 커밋한다.

```bash
git add .
git commit -m "backup before adding context hub"
```

Git repo가 아니라면 먼저 초기화한다.

```bash
git init
git add .
git commit -m "initial project backup"
```

### 7.2 템플릿 복사

`AI-Agent-Wiki-Template-v1.0.0`의 주요 파일과 폴더를 기존 프로젝트 루트에 복사한다.

복사할 것:

```text
START_HERE.md
AGENTS.md
CLAUDE.md
CHATGPT.md
index.md
log.md
prompts/
scripts/
AI-Sessions/
TEMPLATE_MANIFEST.md
```

기본 템플릿에 `CHATGPT.md`가 없다면 새로 만든다.

### 7.3 `.gitignore` 점검

민감 자료가 GitHub에 올라가지 않도록 `.gitignore`에 다음을 추가한다.

```gitignore
# private raw materials
AI-Sessions/raw-private/
AI-Sessions/raw/restricted/
AI-Sessions/raw/**/secrets/
AI-Sessions/raw/**/*secret*
AI-Sessions/raw/**/*password*
AI-Sessions/raw/**/*token*
AI-Sessions/raw/**/*apikey*
AI-Sessions/raw/**/*api-key*

# environment files
.env
.env.*

# Obsidian local workspace
.obsidian/workspace.json
.obsidian/workspace-mobile.json
```

주의:

- `.obsidian/` 전체를 무조건 ignore하지 않아도 된다.
- 팀과 공유할 Obsidian 설정이 있으면 유지할 수 있다.
- 개인 workspace 파일만 ignore하는 것이 보통 안전하다.

---

## 8. 1차 세팅 명령

템플릿을 복사한 뒤 Antigravity, Codex, Claude Code 중 하나를 프로젝트 폴더에서 실행하고 아래 명령을 입력한다.

```text
setup check 해줘.

이 프로젝트의 ContextHub 구조가 올바르게 구성되어 있는지 확인해줘.

확인할 것:

- AGENTS.md 존재 여부
- CLAUDE.md 존재 여부
- CHATGPT.md 존재 여부
- START_HERE.md 존재 여부
- index.md 존재 여부
- log.md 존재 여부
- prompts/ 존재 여부
- AI-Sessions/raw/ 존재 여부
- AI-Sessions/conversations/ 존재 여부
- AI-Sessions/wiki/ 존재 여부
- save / ingest / query / reference / lint / handoff 규칙 존재 여부
- 민감정보 정책 존재 여부
- .gitignore에 raw-private, restricted, secrets 관련 규칙 존재 여부

부족한 것이 있으면 생성하거나 수정해줘.
작업 후 수정한 파일과 다음 확인사항을 보고해줘.
```

---

## 9. 자주 쓰는 에이전트 명령어

### 9.1 맥락 복원

새 에이전트를 연결했거나 이전 작업을 이어가려면:

```text
reference 해줘.

START_HERE.md, AGENTS.md, CHATGPT.md, CLAUDE.md, index.md, log.md를 읽고,
AI-Sessions/wiki/에서 관련 문서를 찾아 현재 프로젝트 맥락을 복원해줘.

아래 형식으로 보고해줘.

- Project Overview
- Current Status
- Key Decisions
- Important Source Documents
- Open Questions
- Next Actions
- Files I should read first
```

짧은 버전:

```text
옵시디언 참조해줘. 이 프로젝트의 현재 상태와 다음 액션을 복원해줘.
```

### 9.2 raw 자료 정리

새 회의록, 문서, 이메일, 스크린샷을 `AI-Sessions/raw/`에 넣은 뒤:

```text
ingest 해줘.

AI-Sessions/raw/에 새로 추가된 자료를 읽고, raw 원본은 절대 수정하지 마.
필요한 경우 AI-Sessions/wiki/sources/, concepts/, decisions/, projects/에 요약과 연결 문서를 만들어줘.

작업 후 index.md와 log.md를 업데이트해줘.
```

### 9.3 작업 저장

세션에서 나온 중요한 결정이나 재사용 가능한 내용을 저장할 때:

```text
save 해줘.

이번 작업 내용 중 장기적으로 재사용할 가치가 있는 정보만 저장해줘.
저장 전 반드시 아래 5가지 필터를 적용해.

1. 반복해서 재사용될 정보인가?
2. 인수인계에 필요한 정보인가?
3. 근거와 결정권자 추적이 필요한가?
4. 다시 반복하면 안 되는 실패나 리스크인가?
5. 팀이 공유해야 하는 규칙이나 가이드인가?

위 조건 중 하나라도 만족하는 정보만 AI-Sessions/wiki/에 저장해.
조건을 만족하지 않는 정보는 wiki에 저장하지 말고 필요하면 conversations에만 남겨.

작업 후 index.md와 log.md를 업데이트해줘.
```

### 9.4 특정 주제 검색

```text
query 해줘: [찾고 싶은 주제]

index.md와 log.md를 먼저 확인하고, AI-Sessions/wiki/ 아래에서 관련 문서를 찾아줘.
필요하면 AI-Sessions/raw/ 원본도 근거 확인용으로만 참조해줘.

아래 형식으로 정리해줘.

- 관련 문서
- 현재 유효한 정보
- 오래되었거나 superseded 된 정보
- 충돌하는 내용
- 이번 작업에 적용해야 할 기준
```

### 9.5 위키 품질 점검

```text
lint 해줘.

index.md, log.md, AI-Sessions/wiki/를 점검해줘.
아래 항목을 확인해줘.

- 중복 정보
- 출처 없는 결정
- 오래된 규칙
- superseded 되었는데 active로 남은 문서
- 검증되지 않은 추측
- raw에만 있어야 할 민감정보가 wiki에 올라간 경우
- API key, 비밀번호, 토큰, 개인정보, 수사자료, 비공개 계약 원문 노출 여부
- index.md에 링크되지 않은 중요 문서
- log.md에 기록되지 않은 중요 변경

문제별로 Issue, Risk, Affected Files, Recommended Fix를 보고해줘.
```

### 9.6 다음 에이전트에게 인수인계

```text
handoff 작성해줘.

현재 작업 상태를 다음 에이전트가 바로 이어받을 수 있게 정리해줘.
AI-Sessions/conversations/ 아래에 handoff 문서를 만들고, 필요하면 index.md와 log.md를 업데이트해줘.

반드시 포함해줘.

- 작업 목표
- 지금까지 완료한 것
- 아직 남은 것
- 중요한 결정사항
- 주의해야 할 맥락
- 다음 에이전트가 먼저 읽어야 할 파일
- 절대 건드리면 안 되는 파일 또는 정보
```

---

## 10. GitHub에 push하기

ContextHub 변경사항을 GitHub에 반영하기 전, 먼저 에이전트에게 점검을 시킨다.

```text
context update commit 준비해줘.

이번 변경사항을 확인하고, ContextHub 관련 변경만 정리해줘.
민감정보가 포함되었는지 먼저 점검해줘.

문제가 없으면 적절한 git commit message를 제안해줘.

보고 형식:

- Changed Files
- Added Files
- Sensitive Info Check
- Suggested Commit Message
- Push Readiness
```

이상이 없으면 터미널에서 실행한다.

```bash
git status
git add .
git commit -m "update project context hub"
git push
```

상황별 commit message 예시:

```text
update project context hub
ingest new source materials into wiki
update decisions and project status
lint context hub and fix stale references
add handoff notes for next agent
```

---

## 11. 민감정보 운영 원칙

GitHub가 private repo라도 모든 raw를 무조건 올리면 안 된다.

GitHub에 올려도 되는 것:

```text
- 정리된 wiki 문서
- index.md
- log.md
- AGENTS.md
- CLAUDE.md
- CHATGPT.md
- prompts/
- 민감정보가 제거된 source summary
```

주의해야 하는 것:

```text
- 실제 API key
- 비밀번호
- 토큰
- 고객 개인정보
- 수사자료 원문
- 비공개 계약서 원문
- 민감 사건의 지갑주소/트랜잭션 원문
- 외부 공개 불가 이메일 원문
```

추천 구조:

```text
AI-Sessions/raw/
  public-safe/
  internal/
  restricted/

AI-Sessions/raw-private/
  # gitignore 대상
```

민감도가 높은 원본은 `AI-Sessions/raw-private/` 또는 `AI-Sessions/raw/restricted/`로 분리하고 GitHub push 대상에서 제외한다.

---

## 12. 프로젝트 여러 개 운영 방식

프로젝트별로 하나의 ContextHub를 둔다.

```text
transight-tr/
  AI-Sessions/
  START_HERE.md
  AGENTS.md
  index.md
  log.md

traverse-wallet/
  AI-Sessions/
  START_HERE.md
  AGENTS.md
  index.md
  log.md

mom-attention-socialfi/
  AI-Sessions/
  START_HERE.md
  AGENTS.md
  index.md
  log.md
```

각 프로젝트는 자기 프로젝트의 정본 컨텍스트를 가진다.

공통 회사/제품/가격/법무 정보가 많아지면 별도 core context repo를 둘 수 있다.

```text
bf-context-core/
  company/
  products/
  commercial/
  legal-compliance/
  approved_claims.md
  forbidden_claims.md
  pricing_policy.md
```

---

## 13. 최소 운영 루틴

처음에는 아래 루틴만 지키면 된다.

```text
1. raw에 새 자료 넣기
2. 에이전트에게 ingest 요청
3. Obsidian에서 wiki 결과 확인
4. 필요한 작업 수행
5. save 요청
6. lint 요청
7. context update commit 준비
8. git commit & push
```

짧게 말하면:

```text
raw에 넣고
→ ingest
→ 작업하고
→ save
→ lint
→ push
```

---

## 14. 에이전트 완료 보고 형식

모든 에이전트는 작업 완료 시 아래 형식으로 보고한다.

```text
작업 완료 보고:

- 읽은 주요 파일:
- 생성한 파일:
- 수정한 파일:
- raw로 유지한 자료:
- wiki로 승격한 정보:
- 저장하지 않은 정보와 이유:
- 발견한 리스크:
- 다음 에이전트가 먼저 읽어야 할 문서:
- 권장 다음 작업:
```

---

## 15. 핵심 요약

```text
Obsidian
= 사람이 보는 위키 UI

GitHub
= ContextHub를 저장하고 에이전트들이 공유하는 중앙 저장소

AI-Sessions/raw/
= 원본 자료. 수정 금지.

AI-Sessions/wiki/
= 검증된 업무 지식.

AI-Sessions/conversations/
= 세션 인수인계와 handoff.

index.md
= 전체 지도.

log.md
= 작업 이력.

reference
= 맥락 복원.

ingest
= raw 자료 정리.

save
= 중요한 작업 결과 저장.

query
= 특정 주제 검색.

lint
= 위키 품질 점검.

handoff
= 다음 에이전트 인수인계.
```

