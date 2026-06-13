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
