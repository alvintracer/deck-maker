# deck-maker 운영 가이드

이 문서는 deck-maker 프로젝트의 운영 방법을 설명한다.  
master-context에서 컨텍스트를 참조하고, ChatGPT로 초안을 만들고, Antigravity로 로컬 수정하는 전체 워크플로우를 다룬다.

---

## 1. 역할과 원칙

### 각 repo의 역할

| 저장소 | 역할 |
|--------|------|
| **master-context** | 여러 프로젝트의 최신 wiki/context를 모아둔 중앙 참조 저장소 |
| **source project** | transight-tr, traverse-wallet 등 각 프로젝트의 원본 ContextHub |
| **deck-maker** | HTML, PPTX, DOCX, PDF, 이미지, 템플릿, 스타일, 산출물 제작 작업장 |
| **ChatGPT** | 초안 생성, 구성 기획, 문장 다듬기, HTML 1차 제작 |
| **Antigravity** | 로컬 deck-maker repo의 실제 파일 수정, asset 연결, 변환 작업 |

### 핵심 원칙

- **내용의 정본** = master-context 또는 source project
- **산출물의 정본** = deck-maker
- **초안 생성** = ChatGPT
- **실제 파일 수정** = 로컬 deck-maker + Antigravity
- deck-maker는 내용을 복사하지 않고 **참조**한다. 산출물만 **소유**한다.

---

## 2. deck-maker가 소유하는 것 / 소유하지 않는 것

### 소유하는 것 (deck-maker에 보관)

- HTML / PPTX / DOCX / PDF 산출물
- 공통 로고, 아이콘, 이미지 asset
- 고객사별 deck 작업 폴더
- 템플릿, 스타일 가이드, 출력 규칙
- deck 제작 과정에서 얻은 lesson

### 소유하지 않는 것 (master-context에서 참조)

- 제품 정의 (TranSight, TR, TTR 등)
- 가격정책, 법무/컴플라이언스 입장
- 고객사별 최신 협의 맥락
- 수사자료, 개인정보, 비공개 계약서

---

## 3. 폴더 구조

```text
deck-maker/
├── AGENTS.md / CHATGPT.md / CLAUDE.md    ← 에이전트 규칙
├── START_HERE.md / README.md
├── index.md / log.md / source-projects.md
├── deck-maker-guide.md                   ← 이 문서
│
├── projects/                             ← 고객사별 deck 작업 폴더
│   └── [project-name]/
│       ├── README.md / brief.md / source-context.md
│       ├── deck-outline.md / visual-plan.md / notes.md
│       ├── assets/ / drafts/
│       └── html/ / pptx/ / docx/ / pdf/
│
├── shared-assets/                        ← 공통 asset
│   ├── logos/ (transight, bonanza, traverse, partners)
│   ├── diagrams/ / icons/ / screenshots/ / backgrounds/
│
├── style-guides/                         ← 시각 스타일 가이드
├── deck-templates/                       ← 덱 구조 템플릿
├── output-rules/                         ← 출력 형식 규칙
├── scripts/                              ← Python 유틸리티
├── fonts/                                ← Pretendard, NanumSquare
├── master-context-usage/                 ← master-context 참조 가이드
├── outputs/                              ← 최종 납품본
├── archive/                              ← 완료 보관
└── AI-Sessions/
    ├── raw/ / conversations/
    └── wiki/ (deck-patterns, style-rules, client-guides, output-lessons)
```

---

## 4. master-context 참조 방식

deck-maker는 source project를 직접 뒤지기보다 master-context를 우선 참조한다.  
상세 규칙은 [`source-projects.md`](source-projects.md)에 정의되어 있다.

**Read Order:**

1. `../master-context/index.md`
2. `../master-context/core/`
3. `../master-context/projects/[target-project]/AI-Sessions/wiki/`
4. `deck-maker/style-guides/`
5. `deck-maker/deck-templates/`
6. `deck-maker/output-rules/`

---

## 5. 새 deck 작업 시작 순서

### Step 1: master-context 최신화

```bash
cd ../transight-tr
# source project의 context를 master-context에 sync
# (각 프로젝트의 sync 방식에 따라 실행)
```

### Step 2: 새 작업 폴더 생성

Antigravity에게 요청:

```text
새 deck 작업 폴더를 만들어줘.

프로젝트명: hana-stablecoin-proposal
source project: transight-tr
목적: 하나은행 스테이블코인 유통 규제준수 제안서
산출물: A4 landscape HTML, PPTX
청중: 디지털자산/AML/컴플라이언스 담당 임원

projects/hana-stablecoin-proposal/ 아래에 README.md, brief.md,
source-context.md, deck-outline.md, visual-plan.md, assets/,
drafts/, html/, pptx/, docx/, pdf/, notes.md를 만들어줘.
```

### Step 3: 프로젝트 파일 역할

| 파일 | 역할 |
|------|------|
| `README.md` | 작업 개요, 상태, 최종 파일 위치 |
| `brief.md` | 목적, 청중, 핵심 메시지, 톤, 산출물 형식, 반드시/피해야 할 내용 |
| `source-context.md` | 참조한 master-context 경로, approved/forbidden claims |
| `deck-outline.md` | 슬라이드별 구조 (제목, 핵심 메시지, 시각 자료, 참조 source) |
| `visual-plan.md` | 필요 이미지 목록, 보유/미보유, placeholder 위치, 파일명 규칙 |
| `notes.md` | 작업 메모, 수정 요청, handoff |
| `assets/` | 이 deck 전용 이미지 |
| `drafts/` | 중간 초안 (ChatGPT 출력물 포함) |
| `html/` `pptx/` `docx/` `pdf/` | 산출물 |

---

## 6. ChatGPT에서 초안 만들기

ChatGPT에게 아래처럼 요청한다:

```text
master-context를 기준으로 deck 초안을 만들어줘.

참조:
- master-context/core/
- master-context/projects/transight-tr/AI-Sessions/wiki/
- deck-maker의 style-guides/ 와 output-rules/

작업: [고객사] 제안서용 A4 landscape HTML 초안 생성

조건:
- 프로젝트 내용은 master-context 기준
- 불확실한 내용은 placeholder로 남겨줘
- 이미지 필요 부분은 placeholder 표시
```

### 초안 저장 위치

- 최종 HTML → `projects/[작업명]/html/index.html`
- 중간 초안 → `projects/[작업명]/drafts/chatgpt-html-v1.html`

### 초안 검증 체크리스트

ChatGPT 출력물은 **초안**이다. 로컬에서 반드시 확인:

- [ ] master-context 기준과 충돌하는 내용이 없는가
- [ ] 가격/법무/보안 표현이 과장되지 않았는가
- [ ] 이미지 경로가 실제 파일 구조와 맞는가
- [ ] 고객사명, 제품명, 프로젝트명이 정확한가
- [ ] placeholder가 필요한 곳에 남아 있는가

---

## 7. 로컬에서 Antigravity로 수정하기

### 시작 명령

```text
START_HERE.md부터 읽고 reference 해줘.
현재 작업 대상: projects/[작업명]/
brief.md, source-context.md, deck-outline.md, visual-plan.md를 읽어줘.
```

### 주요 작업 명령

**HTML 정리:**

```text
projects/[작업명]/html/index.html을 점검해줘.
- asset 경로를 실제 폴더 구조에 맞게 정리
- 이미지 placeholder를 visual-plan.md와 일치
- CSS 정리, A4 landscape 출력 기준 점검
- PDF/인쇄 품질 우선
```

**이미지 연결:**

```text
assets/와 shared-assets/를 확인해서 HTML의 이미지 placeholder를
실제 파일 경로로 연결해줘.
- 공통 로고 → shared-assets/logos/
- 전용 이미지 → projects/[작업명]/assets/
- 없는 이미지는 visual-plan.md에 TODO로 남김
```

**PPTX/DOCX 명세 생성:**

```text
HTML과 deck-outline.md를 바탕으로 slide-spec.md (또는 docx-spec.md)를 만들어줘.
각 슬라이드에 Title, Key Message, Visual, Asset Path, Speaker Notes 포함.
```

---

## 8. Git 관리

### 현재 설정 (이미 적용됨)

- `.gitignore` — .DS_Store, 임시파일, 민감 폴더, Python 캐시 제외
- `.gitattributes` — Git LFS로 PPTX, DOCX, PDF, PNG, JPG, WebP, 폰트 관리

### Git에 올리지 않는 것

- 고객사 비공개 원문, 계약서, 수사자료, 개인정보
- API key, token, password, `.env`
- 임시 export, `node_modules`, 캐시 파일

---

## 9. 작업 완료 후 save 규칙

deck 작업이 끝나면:

```text
이번 deck 작업 내용을 save 해줘.

source project 정본은 복사하지 말고,
deck 제작 관련 lesson과 handoff만 deck-maker wiki에 저장해줘.
```

**deck-maker wiki에 저장할 것:**

- deck 제작 규칙, 스타일 개선사항
- asset 구조, 출력 관련 lesson
- 반복 가능한 slide pattern
- HTML/PPTX/DOCX 변환 주의사항

**저장 위치:**

| 카테고리 | 위치 |
|----------|------|
| 제작 노하우 | `AI-Sessions/wiki/output-lessons/` |
| 레이아웃 패턴 | `AI-Sessions/wiki/deck-patterns/` |
| 실패/주의사항 | `AI-Sessions/wiki/errors/` |
| 인수인계 | `AI-Sessions/conversations/handoffs/` |

---

## 10. 작업 완료 보고 형식

```text
deck-maker 작업 완료 보고:

- 작업명:
- 참조한 master-context 경로:
- 참조한 source project:
- 생성한 산출물:
- 생성/수정한 파일:
- 아직 placeholder로 남은 부분:
- source project에 반영해야 할 내용:
- deck-maker wiki에 저장한 제작 규칙:
- 저장하지 않은 정보와 이유:
- 다음 작업 권장사항:
```

---

## 11. 권장 작업 루틴 (요약)

```text
1. source project context → master-context sync
2. ChatGPT에서 master-context 기준으로 deck 초안 생성
3. 로컬 deck-maker 작업 폴더에 초안 저장
4. Antigravity로 HTML/CSS/assets 수정
5. deck-outline / visual-plan 업데이트
6. 필요 시 PPTX/DOCX spec 생성 → 변환
7. 산출물 export
8. 제작 lesson만 deck-maker wiki에 save
9. git add → commit → push
```

---

## 12. 자주 쓰는 명령 요약

| 목적 | 명령 |
|------|------|
| master-context 참조 | `master-context를 참조해서 [프로젝트명]의 최신 컨텍스트를 불러와줘.` |
| 새 작업 폴더 | `새 deck 작업 폴더를 만들어줘. 프로젝트명: [name], source: [project], 목적: [desc]` |
| ChatGPT 초안 반영 | `ChatGPT에서 받은 HTML 초안을 projects/[name]/html/에 저장하고 경로 정리해줘.` |
| HTML 수정 | `projects/[name]/html/을 A4 landscape 기준으로 점검하고 수정해줘.` |
| 이미지 연결 | `assets/와 shared-assets/를 확인해서 placeholder를 실제 경로로 연결해줘.` |
| PPTX 명세 | `HTML과 deck-outline.md를 바탕으로 slide-spec.md를 만들어줘.` |
| 작업 저장 | `이번 deck 작업 내용을 save 해줘. 제작 lesson만 저장해줘.` |

---

## 13. 핵심 요약

| 무엇을 | 어디서 |
|--------|--------|
| 내용 읽기 | master-context |
| 산출물 만들기 | deck-maker |
| 초안 생성 | ChatGPT |
| 파일 수정 | Antigravity (로컬) |
| 이미지/asset 관리 | deck-maker |
| 제작 노하우 저장 | deck-maker wiki |
| 제품/법무/가격 정본 | master-context (복사 금지) |
