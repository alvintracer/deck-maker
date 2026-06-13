# Read Order

deck-maker에서 새 deck 작업을 시작할 때 읽는 순서.

## 1단계: deck-maker 내부 규칙 확인

1. `START_HERE.md`
2. `AGENTS.md` / `CHATGPT.md`
3. `source-projects.md`
4. `style-guides/transight-standard.md`
5. 해당 `projects/[작업명]/brief.md`

## 2단계: master-context에서 내용 참조

1. `../master-context/index.md`
2. `../master-context/core/products/` (제품 정의)
3. `../master-context/core/commercial/` (가격, 영업)
4. `../master-context/projects/[대상 프로젝트]/AI-Sessions/wiki/`

## 3단계: 산출물 제작

1. `deck-templates/` 에서 적합한 구조 선택
2. `output-rules/` 에서 출력 형식 규칙 확인
3. `shared-assets/` 에서 공통 이미지/로고 사용
4. 프로젝트별 `assets/` 에서 고유 이미지 사용
