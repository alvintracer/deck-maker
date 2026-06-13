# deck-maker

산출물 제작을 관리하는 실제 작업 repo입니다.

HTML / PPTX / DOCX 덱, 이미지 asset, 시각 스타일, 제작 템플릿, 출력 규칙을 관리합니다.

## 역할 분리

| 저장소 | 역할 |
|--------|------|
| **master-context** | 여러 프로젝트의 최신 wiki/context를 모아둔 중앙 참조 저장소 |
| **deck-maker** | 산출물 제작 작업장. HTML, PPTX, DOCX, 이미지, 템플릿, 스타일 관리 |
| **각 source project** | 자기 프로젝트의 원본 ContextHub |

**원칙**: 내용의 정본 = master-context, 산출물의 정본 = deck-maker

## 워크플로우

1. `master-context`에서 최신 컨텍스트를 참조
2. ChatGPT에서 HTML/구성 초안을 생성
3. 로컬 `projects/[작업명]/`에 저장
4. Antigravity로 이미지, 레이아웃, 소스 수정
5. 결과물을 commit/push
6. 제작 노하우를 wiki에 save

## 폴더 구조

```text
deck-maker/
├── AGENTS.md / CHATGPT.md / CLAUDE.md
├── START_HERE.md / README.md
├── index.md / log.md
├── source-projects.md
├── projects/                    ← 고객사별 deck 작업 폴더
│   ├── knpa-bonanza-traverse-deck/
│   ├── hana-stablecoin-proposal/
│   ├── bithumb-proposal/
│   ├── nts-transight-education/
│   ├── ewha-thesis-presentation/
│   ├── kfcpa-bonanza-cooperation/
│   └── transight-general-intro/
├── shared-assets/               ← 공통 로고, 다이어그램
│   ├── logos/ (transight, bonanza, traverse, partners)
│   ├── diagrams/
│   └── icons/ screenshots/ backgrounds/
├── style-guides/                ← 시각 스타일 가이드
├── deck-templates/              ← 덱 구조 템플릿
├── output-rules/                ← 출력 형식 규칙
├── scripts/                     ← Python 유틸리티
├── fonts/                       ← Pretendard, NanumSquare
├── master-context-usage/        ← master-context 참조 가이드
├── outputs/                     ← 최종 납품본
├── archive/                     ← 완료 보관
└── AI-Sessions/
    ├── raw/
    ├── conversations/
    └── wiki/
```

## Git LFS

PPTX, DOCX, PDF, PNG, JPG, WebP, 폰트 파일은 Git LFS로 관리합니다.

```bash
git lfs install
# .gitattributes에 이미 설정됨
```

## 시작하기

1. `START_HERE.md`를 읽습니다.
2. `source-projects.md`에서 master-context 참조 규칙을 확인합니다.
3. `index.md`에서 전체 지도를 확인합니다.
