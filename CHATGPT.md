# CHATGPT.md

이 문서는 ChatGPT가 이 프로젝트 repository를 참조할 때 따라야 하는 운영
규칙이다.

## 읽기 순서

ChatGPT는 이 프로젝트를 참조할 때 다음 순서로 읽는다.

1. `START_HERE.md`
2. `AGENTS.md`
3. `index.md`
4. `log.md`
5. 이번 요청과 관련된 `AI-Sessions/wiki/` 문서
6. 필요한 경우 `AI-Sessions/raw/` 원본 자료

## 기본 원칙

- `AI-Sessions/raw/`는 불변 원본 자료로 본다.
- raw 자료는 근거 확인용으로만 사용하고, 임의로 수정하거나 정본처럼 재작성하지
  않는다.
- 실제 업무 맥락은 `AI-Sessions/wiki/`를 우선한다.
- 최신성 판단은 `log.md`, `AI-Sessions/wiki/decisions/`, `status: active` 문서를
  우선한다.
- 확정되지 않은 추측은 사실처럼 말하지 않는다.
- 저장이 필요한 정보는 save 5-filter를 통과해야 한다.
- 민감정보, API key, 비밀번호, 고객 개인정보, 수사 관련 원문, 비공개 계약 원문은
  Wiki에 승격하지 않는다.
- 외부 제출 문서 작성 시에는 approved claims, forbidden claims, project
  decisions를 우선 확인한다.

## 명령어 해석

- “옵시디언에 저장해줘”, “save 해줘”\
  → 저장 가치 판단 후 `AI-Sessions/wiki/` 또는 `AI-Sessions/conversations/`에
  저장할 구조를 제안한다.

- “옵시디언 참조해줘”, “reference 해줘”, “query 해줘”\
  → `index.md`, `log.md`, 관련 wiki 문서를 읽고 현재 작업 맥락을 복원한다.

- “ingest 해줘”\
  → raw 자료를 읽고 source summary, concept, decision, project 문서로 정리한다.

- “lint 해줘”\
  → 구조 위반, 중복 정보, 출처 없는 결정, 오래된 규칙, 민감정보 저장 여부를
  점검한다.
