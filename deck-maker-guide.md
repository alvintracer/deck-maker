# deck-maker-guide.md

# deck-maker 운영 가이드

이 문서는 `deck-maker` 프로젝트를 기준으로, `master-context`에서 최신 프로젝트 컨텍스트를 참조하고, ChatGPT에서 초안을 만들고, 로컬에서 Antigravity / Codex / Claude Code로 HTML, PPTX, DOCX, 이미지 자료를 효과적으로 수정·관리하는 방법을 설명한다.

---

## 1. 기본 전제

이 가이드는 아래 구조가 이미 세팅되어 있다고 가정한다.

```text
상위 작업 폴더/
  master-context/
  deck-maker/
  transight-tr/
  traverse-wallet/
  mom-attention-socialfi/
```

각 repo의 역할은 다음과 같다.

```text
master-context
= 여러 프로젝트의 최신 wiki/context를 모아둔 중앙 참조 저장소

source project
= transight-tr, traverse-wallet, mom-attention-socialfi 등 각 프로젝트의 원본 ContextHub

deck-maker
= HTML, PPTX, DOCX, PDF, 이미지, 템플릿, 스타일, 산출물 제작을 관리하는 실제 작업 repo

ChatGPT Deck-maker 프로젝트
= 초안 생성, 구성 기획, 문장 다듬기, HTML 1차 제작

Antigravity / Codex / Claude Code
= 로컬 deck-maker repo의 실제 파일 수정, asset 연결, 리팩토링, 변환 작업
```

가장 중요한 원칙은 다음과 같다.

```text
내용의 정본 = master-context 또는 source project
산출물의 정본 = deck-maker
초안 생성 = ChatGPT
실제 파일 수정 = 로컬 deck-maker + Antigravity
```

---

## 2. deck-maker가 소유하는 것과 소유하지 않는 것

### 2.1 deck-maker가 소유하는 것

`deck-maker`는 산출물 제작 repo다. 아래 자료는 deck-maker에서 관리한다.

```text
- HTML 제안서
- PPTX 파일
- DOCX 파일
- PDF export
- 공통 로고, 아이콘, 이미지 asset
- 고객사별 deck 작업 폴더
- A4 landscape HTML 템플릿
- PPTX 슬라이드 구조 템플릿
- 제안서 스타일 가이드
- deck 제작 규칙
- 이미지 placeholder 규칙
- output 변환 규칙
- deck 제작 과정에서 얻은 lesson
```

### 2.2 deck-maker가 소유하지 않는 것

아래 정보의 정본은 deck-maker에 두지 않는다.

```text
- TranSight, TR, TTR, TR-OBM 등 제품 정의의 정본
- 가격정책의 정본
- 법무/컴플라이언스 입장의 정본
- 고객사별 최신 협의 맥락의 정본
- 각 source project의 원본 wiki
- 수사자료, 개인정보, 비공개 계약서 원문
```

이런 내용은 `master-context` 또는 각 source project의 `AI-Sessions/wiki/`를 참조한다.

핵심 원칙:

```text
deck-maker는 복사하지 않는다.
deck-maker는 참조한다.
deck-maker는 산출한다.
```

---

## 3. 추천 폴더 구조

`deck-maker`는 아래처럼 구성한다.

```text
deck-maker/
  README.md
  START_HERE.md
  AGENTS.md
  CHATGPT.md
  index.md
  log.md
  source-projects.md
  deck-maker-guide.md

  AI-Sessions/
    raw/
      chatgpt-uploads/
      reference-docs/
      screenshots/
      client-materials/
    wiki/
      deck-patterns/
      style-rules/
      client-guides/
      output-lessons/
      errors/
    conversations/
      handoffs/

  master-context-usage/
    how-to-reference.md
    read-order.md

  style-guides/
    transight-standard.md
    bank-proposal.md
    public-sector.md
    investor-deck.md
    a4-landscape-html.md

  deck-templates/
    one-pager.md
    10-slide-proposal.md
    20-slide-proposal.md
    executive-briefing.md
    product-proposal.md

  output-rules/
    html-output.md
    pptx-output.md
    docx-output.md
    pdf-export.md
    image-placeholder.md

  shared-assets/
    logos/
      transight/
      bonanza/
      traverse/
      client-logos/
    icons/
    diagrams/
    screenshots/
    backgrounds/

  projects/
    project-name/
      README.md
      brief.md
      source-context.md
      deck-outline.md
      visual-plan.md
      assets/
      drafts/
      html/
      pptx/
      docx/
      pdf/
      notes.md

  outputs/
    html/
    pptx/
    docx/
    pdf/

  archive/
```

---

## 4. master-context와 연결하는 방식

`deck-maker`는 source project를 직접 뒤지기보다 `master-context`를 우선 참조한다.

예시:

```text
../master-context/
  core/
  projects/
    transight-tr/
    traverse-wallet/
    mom-attention-socialfi/
```

`deck-maker/source-projects.md`에는 아래 내용을 둔다.

```markdown
# Source Projects

deck-maker는 프로젝트 내용의 정본을 직접 보관하지 않는다.  
내용 정본은 `master-context`를 통해 참조한다.

## Master Context

Local path:

```text
../master-context
```

GitHub repo:

```text
alvintracer/master-context
```

## Read Order

1. `../master-context/index.md`
2. `../master-context/core/`
3. `../master-context/projects/[target-project]/index.md`
4. `../master-context/projects/[target-project]/log.md`
5. `../master-context/projects/[target-project]/AI-Sessions/wiki/`
6. `deck-maker/style-guides/`
7. `deck-maker/deck-templates/`
8. `deck-maker/output-rules/`

## Rule

- 프로젝트 내용의 정본은 master-context에 있다.
- deck-maker는 산출물 제작 규칙과 결과물만 관리한다.
- source project 내용을 deck-maker에 복사해 정본처럼 보관하지 않는다.
```

---

## 5. 새 deck 작업 시작 순서

예를 들어 `hana-stablecoin-proposal` 작업을 만든다고 하자.

### 5.1 master-context 최신화

먼저 source project에서 최신 context를 master-context에 sync한다.

```bash
cd ../transight-tr
./scripts/sync-context-to-master.sh
```

Windows / PowerShell 환경이면 Git Bash에서 실행한다.

```bash
bash scripts/sync-context-to-master.sh
```

### 5.2 deck-maker로 이동

```bash
cd ../deck-maker
```

### 5.3 새 작업 폴더 생성

Antigravity / Codex에게 아래처럼 요청한다.

```text
새 deck 작업 폴더를 만들어줘.

프로젝트명: hana-stablecoin-proposal
source project: transight-tr
목적: 하나은행 스테이블코인 유통 규제준수 제안서
산출물: A4 landscape HTML, PPTX
청중: 디지털자산/AML/컴플라이언스 담당 임원

projects/hana-stablecoin-proposal/ 아래에 다음 구조를 만들어줘.

- README.md
- brief.md
- source-context.md
- deck-outline.md
- visual-plan.md
- assets/
- drafts/
- html/
- pptx/
- docx/
- pdf/
- notes.md
```

---

## 6. deck 작업 폴더 파일 역할

### `README.md`

이 deck 작업의 개요.

```text
- 작업명
- source project
- 산출물 형식
- 현재 상태
- 최종 파일 위치
```

### `brief.md`

ChatGPT와 로컬 에이전트가 읽을 작업 브리프.

```text
- 목적
- 청중
- 핵심 메시지
- 톤앤매너
- 산출물 형식
- 분량
- 반드시 포함할 내용
- 피해야 할 내용
```

### `source-context.md`

master-context에서 어떤 문서를 참조했는지 기록.

```text
- 참조한 master-context 경로
- source project
- core 문서
- 관련 products / partners / legal-compliance 문서
- 최신 결정사항
- 사용 가능한 approved claims
- 피해야 할 forbidden claims
```

### `deck-outline.md`

슬라이드별 구성 또는 HTML 섹션 구조.

```text
- Slide No. 또는 Section No.
- 제목
- 핵심 메시지
- 본문 요지
- 시각 자료 방향
- 참조 source
```

### `visual-plan.md`

이미지, 도식, placeholder 계획.

```text
- 필요한 이미지 목록
- 현재 보유한 이미지
- 생성/수정해야 할 이미지
- placeholder 위치
- 파일명 규칙
- asset 경로
```

### `assets/`

이 deck 작업에만 쓰는 이미지, 캡처, 로고, 도식.

### `drafts/`

중간 텍스트 초안, ChatGPT 출력물, 구조 초안.

### `html/`

HTML 산출물.

### `pptx/`

PPTX 산출물.

### `docx/`

DOCX 산출물.

### `pdf/`

PDF export.

### `notes.md`

작업 메모, 수정 요청, handoff.

---

## 7. ChatGPT에서 초안 만들기

ChatGPT는 주로 아래 작업에 적합하다.

```text
- deck 목적 정리
- 핵심 메시지 도출
- 슬라이드 구조 작성
- HTML 초안 생성
- 문장 톤 정리
- 고객사별 설득 논리 작성
- 발표자료/제안서 카피 개선
```

### 7.1 ChatGPT에 줄 기본 요청

```text
master-context를 기준으로 deck 초안을 만들어줘.

참조 기준:
- master-context/core/
- master-context/projects/transight-tr/index.md
- master-context/projects/transight-tr/log.md
- master-context/projects/transight-tr/AI-Sessions/wiki/
- deck-maker의 style-guides/bank-proposal.md
- deck-maker의 output-rules/html-output.md

작업:
하나은행 스테이블코인 유통 규제준수 제안서용 A4 landscape HTML 초안을 만들어줘.

조건:
- 프로젝트 내용의 정본은 master-context를 기준으로 해줘.
- 불확실한 내용은 단정하지 말고 placeholder로 남겨줘.
- 이미지가 필요한 부분은 placeholder로 표시해줘.
- 나중에 로컬 deck-maker에서 Antigravity로 수정할 수 있게 파일 구조를 명확히 해줘.
```

### 7.2 ChatGPT가 생성한 HTML 저장 위치

ChatGPT에서 받은 HTML은 로컬에 아래 경로로 저장한다.

```text
deck-maker/projects/hana-stablecoin-proposal/html/index.html
```

중간 초안은 다음처럼 저장한다.

```text
deck-maker/projects/hana-stablecoin-proposal/drafts/chatgpt-html-v1.html
```

### 7.3 ChatGPT 출력물을 바로 정본으로 보지 않는다

ChatGPT 출력물은 초안이다.

반드시 로컬에서 확인한다.

```text
- master-context 기준과 충돌하는 내용이 없는가?
- 가격/법무/보안 표현이 과장되지 않았는가?
- 이미지 경로가 실제 파일 구조와 맞는가?
- 고객사명, 제품명, 프로젝트명이 정확한가?
- placeholder가 필요한 곳에 남아 있는가?
```

---

## 8. 로컬에서 Antigravity로 수정하기

Antigravity는 로컬 파일 수정과 구조 정리에 사용한다.

### 8.1 Antigravity 시작 명령

```text
START_HERE.md부터 읽고 reference 해줘.

이 repo는 deck-maker 오케스트레이터야.
master-context를 참조해 산출물을 만드는 프로젝트이고,
프로젝트 내용의 정본은 master-context에 있어.
deck-maker는 HTML/PPTX/DOCX, 이미지 asset, 스타일 가이드, 출력 규칙을 관리해.

현재 작업 대상:
projects/hana-stablecoin-proposal/

먼저 아래 파일을 읽어줘.
- source-projects.md
- projects/hana-stablecoin-proposal/brief.md
- projects/hana-stablecoin-proposal/source-context.md
- projects/hana-stablecoin-proposal/deck-outline.md
- projects/hana-stablecoin-proposal/visual-plan.md
- style-guides/
- output-rules/
```

### 8.2 HTML 정리 명령

```text
projects/hana-stablecoin-proposal/html/index.html을 점검해줘.

해야 할 일:
- asset 경로를 실제 폴더 구조에 맞게 정리
- 이미지 placeholder를 visual-plan.md와 일치시킴
- 중복 CSS 정리
- A4 landscape 출력 기준 점검
- 섹션별 주석 추가
- 모바일 대응보다 PDF/인쇄 품질 우선
- 사용하지 않는 임시 텍스트 제거

수정 후 변경한 파일과 이유를 보고해줘.
```

### 8.3 이미지 연결 명령

```text
projects/hana-stablecoin-proposal/assets/와 shared-assets/를 확인해서
HTML의 이미지 placeholder를 실제 파일 경로로 연결해줘.

규칙:
- 공통 로고는 shared-assets/logos/에서 사용
- 이 deck 전용 이미지는 projects/hana-stablecoin-proposal/assets/에서 사용
- 없는 이미지는 임의 생성하지 말고 visual-plan.md에 TODO로 남김
- 파일명은 영문 소문자와 하이픈으로 정리
```

### 8.4 PPTX 변환 준비 명령

```text
HTML 산출물을 PPTX로 변환하기 위한 slide spec을 만들어줘.

입력:
- projects/hana-stablecoin-proposal/html/index.html
- projects/hana-stablecoin-proposal/deck-outline.md
- projects/hana-stablecoin-proposal/visual-plan.md

출력:
- projects/hana-stablecoin-proposal/pptx/slide-spec.md

각 슬라이드에는 아래를 포함해줘.
- Slide No.
- Title
- Key Message
- Main Text
- Visual
- Asset Path
- Speaker Notes
- Source Context
```

### 8.5 DOCX 변환 준비 명령

```text
HTML 제안서 내용을 DOCX 제안서 구조로 변환하기 위한 문서 명세를 만들어줘.

출력:
- projects/hana-stablecoin-proposal/docx/docx-spec.md

포함할 것:
- 표지
- 요약
- 제안 배경
- 문제 정의
- 솔루션
- 기술 구조
- 컴플라이언스/AML 대응
- 구축 방식
- 가격/상업 조건이 필요한 경우 placeholder
- 다음 단계
```

---

## 9. Git에 올릴 파일 기준

deck-maker는 이미지, PPTX, DOCX, PDF를 다룰 수 있으므로 Git 관리 기준을 분명히 해야 한다.

### 9.1 일반 Git에 올릴 것

```text
- Markdown
- HTML
- CSS
- JS
- JSON
- SVG
- 작은 PNG/JPG
- 작은 로고/아이콘
- deck template
- style guide
- output rule
```

### 9.2 Git LFS에 올릴 것

```text
- PPTX
- DOCX
- PDF
- 대형 PNG/JPG
- ZIP
- MP4/MOV
- PSD
- FIG
```

### 9.3 Git에 올리지 않을 것

```text
- 고객사 비공개 원문
- 계약서 원문
- 수사자료
- 개인정보 포함 자료
- API key
- token
- password
- .env
- 임시 export
- node_modules
- 캐시 파일
```

---

## 10. Git LFS 설정

PPTX, DOCX, PDF, 대형 이미지를 Git에서 관리하려면 Git LFS를 사용한다.

```bash
git lfs install
git lfs track "*.pptx"
git lfs track "*.docx"
git lfs track "*.pdf"
git lfs track "*.zip"
git lfs track "*.psd"
git lfs track "*.fig"
git lfs track "*.mov"
git lfs track "*.mp4"
git lfs track "*.png"
git lfs track "*.jpg"
git add .gitattributes
git commit -m "configure git lfs for deck assets"
```

추천:

```text
PPTX/DOCX/PDF = LFS
큰 이미지 = LFS
SVG/작은 로고/아이콘 = 일반 Git
```

이미지가 많지 않으면 처음에는 Git LFS 없이 시작해도 된다.  
다만 PPTX/DOCX/PDF가 계속 쌓이면 LFS를 쓰는 것이 좋다.

---

## 11. .gitignore 추천

`deck-maker/.gitignore`에 아래를 넣는다.

```gitignore
# dependencies
node_modules/
.env
.env.*

# local system files
.DS_Store
Thumbs.db

# temp files
tmp/
temp/
.cache/
*.tmp

# private or restricted materials
private/
restricted/
raw-private/
AI-Sessions/raw-private/
AI-Sessions/raw/restricted/

# office temp files
~$*.docx
~$*.pptx
~$*.xlsx

# optional: huge exports
outputs/tmp/
outputs/cache/
```

---

## 12. ChatGPT ↔ local deck-maker 작업 흐름

### 12.1 기본 흐름

```text
1. source project의 wiki를 master-context에 sync
2. ChatGPT에서 master-context 기준으로 deck 초안 생성
3. ChatGPT 출력물을 로컬 deck-maker 작업 폴더에 저장
4. Antigravity로 HTML/CSS/assets 수정
5. 필요한 경우 PPTX/DOCX 명세 생성
6. 산출물 export
7. deck-maker에 commit/push
8. 제작 lesson만 deck-maker wiki에 save
```

### 12.2 실제 명령 흐름

```bash
# 1. source project 최신 context sync
cd ../transight-tr
./scripts/sync-context-to-master.sh

# 2. deck-maker 작업
cd ../deck-maker

# 3. 작업 후 변경사항 확인
git status

# 4. commit
git add .
git commit -m "update hana stablecoin proposal deck"
git push
```

---

## 13. deck 작업 후 save 규칙

deck 작업이 끝나면 Antigravity / Codex에게 아래처럼 요청한다.

```text
이번 deck 작업 내용을 save 해줘.

단, source project의 제품/법무/가격 정본은 deck-maker에 저장하지 마.
deck-maker에는 아래 내용만 저장해.

- deck 제작 규칙
- 스타일 개선사항
- asset 구조
- 출력 관련 lesson
- 반복 가능한 slide pattern
- HTML/PPTX/DOCX 변환 과정에서 발견한 주의사항
- 이번 작업의 handoff

source project에 반영해야 할 내용이 있으면 별도로 보고해줘.
```

저장 위치 예시:

```text
AI-Sessions/wiki/output-lessons/
AI-Sessions/wiki/deck-patterns/
AI-Sessions/wiki/errors/
AI-Sessions/conversations/handoffs/
```

---

## 14. deck-maker Completion Report

모든 작업 완료 시 에이전트는 아래 형식으로 보고한다.

```text
deck-maker 작업 완료 보고:

- 작업명:
- 참조한 master-context 경로:
- 참조한 source project:
- 참조한 core context:
- 읽은 주요 파일:
- 생성한 산출물:
- 생성/수정한 deck-maker 파일:
- 사용한 asset:
- 아직 placeholder로 남은 부분:
- source project에 반영해야 할 내용:
- deck-maker에 저장한 제작 규칙:
- 저장하지 않은 정보와 이유:
- 발견한 충돌 또는 리스크:
- 다음 작업 권장사항:
```

---

## 15. deck-maker에서 자주 쓰는 명령 모음

### 15.1 master-context 참조

```text
master-context를 참조해서 [프로젝트명]의 최신 컨텍스트를 불러와줘.
core 공통 문서와 projects/[프로젝트명]/AI-Sessions/wiki를 기준으로 해줘.
```

### 15.2 새 deck 작업 폴더 생성

```text
새 deck 작업 폴더를 만들어줘.

프로젝트명: [작업명]
source project: [source project명]
목적: [목적]
산출물: [HTML/PPTX/DOCX/PDF]
청중: [청중]

projects/[작업명]/ 아래에 README.md, brief.md, source-context.md, deck-outline.md, visual-plan.md, assets/, drafts/, html/, pptx/, docx/, pdf/를 만들어줘.
```

### 15.3 ChatGPT 초안 반영

```text
ChatGPT에서 받은 HTML 초안을 projects/[작업명]/html/에 저장하고,
assets 경로를 shared-assets와 project assets 기준으로 정리해줘.
이미지 placeholder 중 실제 파일이 필요한 부분은 visual-plan.md에 체크리스트로 남겨줘.
```

### 15.4 HTML 수정

```text
projects/[작업명]/html/index.html을 수정해줘.

목표:
- A4 landscape 출력 최적화
- CSS 정리
- asset 경로 정리
- placeholder 정리
- 인쇄/PDF export 품질 개선
```

### 15.5 PPTX 명세 생성

```text
projects/[작업명]/html/index.html과 deck-outline.md를 바탕으로
projects/[작업명]/pptx/slide-spec.md를 만들어줘.
```

### 15.6 DOCX 명세 생성

```text
projects/[작업명]/html/index.html과 deck-outline.md를 바탕으로
projects/[작업명]/docx/docx-spec.md를 만들어줘.
```

### 15.7 작업 저장

```text
이번 deck 작업 내용을 save 해줘.
source project 정본은 복사하지 말고, deck 제작 관련 lesson과 handoff만 deck-maker wiki에 저장해줘.
```

---

## 16. 권장 작업 루틴

처음에는 아래 루틴을 따른다.

```text
1. source project context sync
2. ChatGPT 초안 생성
3. deck-maker 작업 폴더에 초안 저장
4. Antigravity로 HTML/assets 수정
5. deck-outline / visual-plan 업데이트
6. 필요한 경우 PPTX/DOCX spec 생성
7. 산출물 export
8. save
9. git commit/push
```

실제 명령 예시:

```bash
cd ../transight-tr
./scripts/sync-context-to-master.sh

cd ../deck-maker
git status
git add .
git commit -m "update hana proposal deck"
git push
```

---

## 17. 최종 요약

```text
master-context
= 내용 컨텍스트 정본 / project wiki mirror

deck-maker
= 산출물 정본 / HTML, PPTX, DOCX, PDF, 이미지, 템플릿, 스타일

ChatGPT
= 초안 생성 / 구성 기획 / HTML 1차 제작

Antigravity
= 로컬 파일 수정 / asset 연결 / 출력 품질 개선

source project
= 각 프로젝트의 원본 ContextHub
```

핵심 원칙:

```text
내용은 master-context에서 읽는다.
산출물은 deck-maker에서 만든다.
이미지와 파일은 deck-maker에서 관리한다.
ChatGPT 초안은 로컬 deck-maker에 저장한 뒤 수정한다.
제품/법무/가격 정본은 deck-maker에 복사하지 않는다.
제작 노하우만 deck-maker wiki에 저장한다.
```
