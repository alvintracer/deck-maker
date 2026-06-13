# How to Reference master-context

deck-maker에서 산출물을 만들 때 master-context의 정본 내용을 참조하는 방법.

## ChatGPT에서 참조할 때

ChatGPT에게 요청 시 아래처럼 지시한다:

```text
master-context의 [프로젝트명]과 core 문서를 기준으로,
deck-maker 스타일 규칙에 맞춰 [산출물 설명] 초안을 만들어줘.
```

필요한 경우 추가:

```text
현재 deck-maker의 style-guides/transight-standard.md와
projects/[작업명]/brief.md를 참고해줘.
```

## Antigravity에서 참조할 때

Antigravity는 로컬 파일시스템에서 직접 읽을 수 있다:

```text
../master-context/projects/[프로젝트명]/AI-Sessions/wiki/
../master-context/core/
```

## 원칙

- 내용 컨텍스트는 master-context에서 읽는다.
- deck-maker에는 산출물만 남긴다.
- master-context의 내용을 deck-maker에 복사하지 않는다.
