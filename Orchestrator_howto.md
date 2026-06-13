# Orchestrator_howto.md

# Orchestrator 프로젝트 운영 가이드

이 문서는 `deck-maker`처럼 여러 프로젝트의 ContextHub를 읽고 산출물을 만드는 상위 오케스트레이터 프로젝트를 어떻게 운영할지 설명한다.

대표 예시:

```text
deck-maker/
```

deck-maker는 독립 제품 프로젝트가 아니라, 여러 source project의 ContextHub를 참조해서 deck, proposal, one-pager, HTML, PPTX, 보고서 등을 만드는 제작 오케스트레이터다.

---

## 1. 핵심 개념

일반 프로젝트와 오케스트레이터 프로젝트는 역할이 다르다.

```text
일반 프로젝트
= 자기 제품/서비스/기획/개발/고객사 맥락의 정본을 가진다.

오케스트레이터 프로젝트
= 여러 프로젝트의 정본을 읽고 산출물을 만든다.
= 대상 프로젝트의 내용을 복사해서 정본처럼 보관하지 않는다.
```

예시 구조:

```text
transight-tr/
= TR / TTR / TR-OBM / Travel Rule 프로젝트 정본

traverse-wallet/
= 지갑 프로젝트 정본

mom-attention-socialfi/
= MOM / SocialFi 프로젝트 정본

bf-context-core/
= 회사/제품/상업/법무 공통 정본

deck-maker/
= 위 프로젝트들을 읽고 deck/proposal/html/pptx를 만드는 오케스트레이터
```

---

## 2. 가장 중요한 원칙

```text
deck-maker는 내용을 소유하지 않는다.
deck-maker는 내용을 참조한다.
deck-maker는 제작 규칙과 산출물 규칙을 소유한다.
```

즉:

```text
프로젝트 지식의 정본
= 각 source project repo

회사/제품 공통 정본
= bf-context-core

덱 제작 방식의 정본
= deck-maker
```

나쁜 구조:

```text
deck-maker/
  transight-tr-copy/
  mom-copy/
  traverse-wallet-copy/
```

이렇게 하면 각 프로젝트 원본이 바뀌었을 때 deck-maker 내부 복사본이 구버전이 되어 혼란이 생긴다.

좋은 구조:

```text
deck-maker/
  source-projects.md
  style-guides/
  deck-templates/
  output-rules/
  examples/
  AGENTS.md
  CHATGPT.md
  index.md
  log.md
```

---

## 3. deck-maker 권장 폴더 구조

```text
deck-maker/
  START_HERE.md
  AGENTS.md
  CLAUDE.md
  CHATGPT.md
  index.md
  log.md
  source-projects.md

  style-guides/
    standard-proposal.md
    executive-briefing.md
    investor-deck.md
    public-sector-proposal.md
    bank-proposal.md

  deck-templates/
    proposal-10p.md
    proposal-20p.md
    one-pager.md
    a4-landscape-html.md
    pitch-deck.md

  output-rules/
    html-output.md
    pptx-output.md
    docx-output.md
    image-placeholder.md
    citation-and-source-rules.md

  examples/
    past-deck-structures/
    layout-samples/
    copywriting-samples/

  AI-Sessions/
    raw/
    wiki/
    conversations/
```

### deck-maker가 가질 수 있는 wiki

deck-maker에도 `AI-Sessions/wiki/`는 둘 수 있다.

다만 여기에 저장되는 것은 프로젝트 내용 정본이 아니라 아래와 같은 제작 지식이다.

```text
- 좋은 덱 구조 패턴
- 고객사용 제안서 톤
- A4 가로 HTML 구성 규칙
- PPTX 생성 규칙
- 이미지 placeholder 규칙
- 발표자료용 문장 길이 규칙
- deck-maker가 자주 실수한 내용
- deck-maker 출력 품질 개선 노트
```

---

## 4. source-projects.md

deck-maker에는 반드시 `source-projects.md`를 둔다.

예시:

```markdown
# Source Projects

deck-maker는 아래 ContextHub repo를 참조해 산출물을 생성한다.

## Core Context

### bf-context-core

Purpose:
- 회사 소개
- 제품 공통 설명
- approved claims
- forbidden claims
- visual identity
- pricing policy
- legal/compliance 공통 입장

Read first:
- index.md
- log.md
- AI-Sessions/wiki/company/
- AI-Sessions/wiki/products/
- AI-Sessions/wiki/commercial/
- AI-Sessions/wiki/legal-compliance/

## Project Contexts

### transight-tr

Purpose:
- TranSight TR / TTR / TR-OBM / Travel Rule 프로젝트 정본

Read first:
- index.md
- log.md
- AI-Sessions/wiki/projects/
- AI-Sessions/wiki/products/
- AI-Sessions/wiki/partners/
- AI-Sessions/wiki/legal-compliance/

### traverse-wallet

Purpose:
- Traverse Wallet 제품/개발/기획 정본

Read first:
- index.md
- log.md
- AI-Sessions/wiki/projects/
- AI-Sessions/wiki/products/
- AI-Sessions/wiki/dev-tasks/

### mom-attention-socialfi

Purpose:
- MOM Attention SocialFi 제품/토큰/리워드/오라클 정본

Read first:
- index.md
- log.md
- AI-Sessions/wiki/projects/
- AI-Sessions/wiki/concepts/
- AI-Sessions/wiki/dev-tasks/

## Rule

deck-maker는 대상 프로젝트의 내용을 자신의 repo에 복사해 정본처럼 보관하지 않는다.
필요한 경우 대상 repo의 index.md, log.md, AI-Sessions/wiki/를 참조한다.
덱 제작 후 생성된 산출물 규칙, 스타일 개선사항, output lesson만 deck-maker에 저장한다.
```

---

## 5. deck-maker의 Read Order

deck-maker는 산출물 작업 전 아래 순서로 문서를 읽는다.

```text
1. deck-maker/START_HERE.md
2. deck-maker/AGENTS.md
3. deck-maker/index.md
4. deck-maker/log.md
5. deck-maker/source-projects.md
6. deck-maker/style-guides/
7. deck-maker/deck-templates/
8. deck-maker/output-rules/
9. 사용자가 지정한 source project의 index.md
10. source project의 log.md
11. source project의 관련 AI-Sessions/wiki/
12. 필요한 경우 source project의 AI-Sessions/raw/
13. 필요한 경우 bf-context-core의 공통 문서
```

---

## 6. deck-maker AGENTS.md에 들어갈 핵심 규칙

아래 내용을 `deck-maker/AGENTS.md` 또는 `START_HERE.md`에 포함한다.

```markdown
# deck-maker Agent Rules

## Role

이 repo는 독립 제품 프로젝트가 아니라, 여러 프로젝트 ContextHub를 참조해 deck, proposal, HTML, PPTX, one-pager를 생성하는 presentation orchestration repo다.

## Source of Truth

- 내용의 정본은 대상 source project repo에 있다.
- 회사/제품 공통 정본은 bf-context-core에 있다.
- deck-maker는 디자인, 구성, 변환 규칙, 산출물 포맷만 정본으로 가진다.
- 대상 프로젝트 내용을 deck-maker 내부에 중복 저장하지 않는다.

## Read Order

작업 전 다음 순서로 읽는다.

1. 이 repo의 START_HERE.md
2. 이 repo의 AGENTS.md
3. 이 repo의 index.md
4. 이 repo의 log.md
5. source-projects.md
6. style-guides/
7. deck-templates/
8. output-rules/
9. 사용자가 지정한 대상 프로젝트 repo의 index.md
10. 대상 프로젝트 repo의 log.md
11. 대상 프로젝트 repo의 관련 AI-Sessions/wiki/
12. 필요한 경우 대상 프로젝트 repo의 AI-Sessions/raw/

## Output Rules

- 덱 생성 전 반드시 대상 프로젝트, 목적, 청중, 산출물 형식을 파악한다.
- 사용자가 명시하지 않으면 대상 프로젝트의 최신 index.md, log.md, decisions/를 기준으로 한다.
- 외부 제출용 문서는 approved claims와 forbidden claims를 확인한다.
- 법무/컴플라이언스 관련 표현은 대상 프로젝트의 legal-compliance/를 우선한다.
- 이미지가 필요한 위치는 placeholder로 남긴다.
- 산출물 생성 후 변경 요약을 log.md에 기록한다.
```

---

## 7. source project에 넣을 deck-maker 연동 문구

각 source project의 `START_HERE.md` 또는 `AGENTS.md`에는 아래 내용을 추가한다.

```markdown
## Deck-maker Integration

이 프로젝트는 deck-maker repo의 source project로 참조될 수 있다.

deck-maker가 이 프로젝트를 참조할 때는 다음 문서를 우선한다.

1. index.md
2. log.md
3. AI-Sessions/wiki/projects/
4. AI-Sessions/wiki/products/
5. AI-Sessions/wiki/partners/
6. AI-Sessions/wiki/commercial/
7. AI-Sessions/wiki/legal-compliance/
8. 필요한 경우 AI-Sessions/raw/

deck-maker는 이 프로젝트의 내용을 복사해 정본처럼 보관하지 않는다.
최신 프로젝트 맥락은 항상 이 repo의 index.md, log.md, AI-Sessions/wiki/를 기준으로 한다.
```

---

## 8. deck-maker 작업 명령어

### 8.1 source project 맥락 읽기

```text
source reference 해줘: [프로젝트명]

deck-maker의 source-projects.md를 읽고, 지정한 source project의 index.md, log.md, 관련 AI-Sessions/wiki/를 참조해줘.

아래 형식으로 정리해줘.

- Source Project Overview
- Current Status
- Key Messages
- Approved Claims
- Forbidden Claims
- Legal/Compliance Notes
- Visual Materials Needed
- Files to Read First
```

예시:

```text
source reference 해줘: transight-tr
```

### 8.2 덱 제작용 컨텍스트 정리

```text
deck context 만들어줘: [프로젝트명] / [목적] / [청중]

source project와 bf-context-core를 참조해서 덱 제작에 필요한 컨텍스트를 정리해줘.

포함할 것:

- 덱 목적
- 청중
- 핵심 메시지
- 문제 정의
- 제안 솔루션
- 제품/기술 설명
- 차별점
- 신뢰 근거
- 법무/컴플라이언스 주의사항
- 가격/상업 조건이 필요한지 여부
- 권장 슬라이드 구성
- 필요한 이미지 placeholder
```

예시:

```text
deck context 만들어줘: transight-tr / 하나은행 제안서 / 디지털자산·컴플라이언스 담당 임원
```

### 8.3 슬라이드 구조 생성

```text
slide outline 만들어줘.

방금 만든 deck context를 바탕으로 슬라이드별 구성을 작성해줘.
각 슬라이드는 아래 형식으로 작성해줘.

- Slide No.
- Slide Title
- Key Message
- Main Content
- Visual Direction
- Source Context
- Notes
```

### 8.4 HTML 제안서 생성

```text
HTML 제안서 생성해줘.

deck context와 slide outline을 바탕으로 A4 landscape 형식의 HTML 제안서를 만들어줘.
style-guides/와 output-rules/html-output.md를 우선 적용해줘.
이미지가 필요한 부분은 placeholder로 남겨줘.
```

### 8.5 PPTX용 명세 생성

```text
PPTX 생성 명세 만들어줘.

slide outline을 바탕으로 deck-maker 또는 PPT 생성 AI가 바로 사용할 수 있는 슬라이드별 명세를 만들어줘.
각 슬라이드에는 제목, 핵심 문장, 본문, 시각 요소, 이미지 placeholder, speaker notes를 포함해줘.
```

### 8.6 결과 저장

```text
save deck 작업내용.

이번 deck 작업에서 장기적으로 재사용할 수 있는 제작 규칙, 스타일 개선사항, 실수 방지 노트만 deck-maker wiki에 저장해줘.
대상 프로젝트의 제품/고객사/법무 내용은 deck-maker에 정본처럼 복사하지 마.
필요하면 source project에 저장해야 할 내용과 deck-maker에 저장해야 할 내용을 분리해서 보고해줘.
```

---

## 9. deck-maker 작업 흐름 예시

### 예시 1: transight-tr 기반 하나은행 제안서

```text
1. source reference 해줘: transight-tr
2. deck context 만들어줘: transight-tr / 하나은행 제안서 / 디지털자산·컴플라이언스 담당 임원
3. slide outline 만들어줘.
4. HTML 제안서 생성해줘.
5. save deck 작업내용.
6. context update commit 준비해줘.
```

### 예시 2: MOM SocialFi 투자자 덱

```text
1. source reference 해줘: mom-attention-socialfi
2. deck context 만들어줘: mom-attention-socialfi / 투자자 피치덱 / Web3 투자자
3. slide outline 만들어줘.
4. PPTX 생성 명세 만들어줘.
5. save deck 작업내용.
```

### 예시 3: Traverse Wallet 제품 소개서

```text
1. source reference 해줘: traverse-wallet
2. deck context 만들어줘: traverse-wallet / 제품 소개서 / 파트너사 기술·사업 담당자
3. slide outline 만들어줘.
4. HTML 제안서 생성해줘.
5. save deck 작업내용.
```

---

## 10. deck-maker가 저장해야 하는 것과 저장하면 안 되는 것

### deck-maker에 저장해야 하는 것

```text
- 덱 제작 규칙
- 스타일 가이드
- 슬라이드 구성 패턴
- 출력 포맷 규칙
- 이미지 placeholder 규칙
- HTML/PPTX 변환 규칙
- 고객사용 제안서 톤앤매너
- deck-maker 작업 중 발견한 제작 관련 실패 사례
```

### deck-maker에 저장하면 안 되는 것

```text
- source project의 최신 제품 설명 정본 복사본
- source project의 법무 입장 복사본
- source project의 가격정책 복사본
- 고객사별 민감 정보 원문
- raw 문서 원본
- 수사자료, 개인정보, 비공개 계약서
```

필요한 경우 deck-maker는 “이 정보는 source project에 저장해야 함”이라고 보고하고, 해당 프로젝트의 `save` 명령으로 넘긴다.

---

## 11. bf-context-core와의 관계

프로젝트가 많아지면 공통 context repo를 둘 수 있다.

```text
bf-context-core/
  company/
  products/
  commercial/
  legal-compliance/
  approved_claims.md
  forbidden_claims.md
  pricing_policy.md
  visual_identity.md
```

deck-maker는 다음 경우에 bf-context-core를 참조한다.

```text
- 회사 소개가 필요한 경우
- Bonanza / Traverse / TranSight 공통 설명이 필요한 경우
- approved claims / forbidden claims가 필요한 경우
- 가격정책이 필요한 경우
- 법무/컴플라이언스 공통 입장이 필요한 경우
- 브랜드 색상, 로고, 톤앤매너가 필요한 경우
```

Read order:

```text
1. source project의 프로젝트별 정본
2. bf-context-core의 공통 정본
3. deck-maker의 스타일/출력 규칙
```

주의:

- 공통 정보와 source project 정보가 충돌하면 임의로 결정하지 않는다.
- source project의 log.md와 decisions/를 확인한다.
- 그래도 충돌하면 사용자에게 보고한다.

---

## 12. 오케스트레이터 완료 보고 형식

deck-maker는 작업 완료 시 아래 형식으로 보고한다.

```text
deck-maker 작업 완료 보고:

- 참조한 source project:
- 참조한 core context:
- 읽은 주요 파일:
- 생성한 산출물:
- 생성/수정한 deck-maker 파일:
- source project에 반영해야 할 내용:
- deck-maker에 저장한 제작 규칙:
- 저장하지 않은 정보와 이유:
- 발견한 충돌 또는 리스크:
- 다음 작업 권장사항:
```

---

## 13. 핵심 요약

```text
source project
= 프로젝트 내용의 정본

bf-context-core
= 회사/제품/상업/법무 공통 정본

deck-maker
= 여러 source project를 읽고 산출물을 만드는 오케스트레이터

deck-maker가 소유하는 것
= 덱 제작 규칙, 스타일, 출력 포맷, 산출물 생성 프로세스

deck-maker가 소유하지 않는 것
= 각 프로젝트의 제품/고객사/법무/가격 정본
```

가장 중요한 원칙:

```text
deck-maker는 복사하지 않는다.
deck-maker는 참조한다.
deck-maker는 산출한다.
``'