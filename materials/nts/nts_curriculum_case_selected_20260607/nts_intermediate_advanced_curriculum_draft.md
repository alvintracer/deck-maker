# 국세청 중급/고급 커리큘럼 구성 초안

작성일: 2026-06-07  
사용처: 2026-06-08 국세청 발표 중 "향후 교육은 이런 구조로 준비할 수 있습니다" 파트

## 목적

이번 발표 이후 이어질 수 있는 국세청 정규 교육을 `중급`과 `고급` 중심으로 제안하기 위한 초안이다.

핵심은 기능 소개가 아니다. 중급은 실제 업무에서 자주 만나는 기본 Web3 거래 구조를 해석하는 방법을 배우고, 고급은 사건형 케이스를 바탕으로 실제 산출물을 작성하는 과정으로 설계한다.

```text
중급: 구조를 해석한다
  -> on-ramp/off-ramp, DEX swap, airdrop claim, CEX 주소 구조를 evidence로 재구성

고급: 사건 안에서 판단한다
  -> 여러 seed와 chain이 섞인 사건을 case study로 풀고 보고서/자료요청서를 작성
```

## 중급 과정 개요

### 과정명

```text
국세청 중급: Web3 경제활동 추적과 세무 evidence 재구성
```

### 대상

- Transight 기본 검색과 Transaction Map을 한 번 이상 사용해 본 교육생
- 주소/TX/token/chain/contract call의 기본 개념은 알고 있으나, DEX/bridge/거래소 입출금 구조 해석 경험이 부족한 교육생
- 세무조사 질문을 온체인 evidence와 자료 요청 항목으로 바꾸는 훈련이 필요한 실무자

### 종료 시점 역량

| 영역 | 할 수 있어야 하는 일 |
|---|---|
| 입출금 구조 이해 | on-ramp, off-ramp, CEX deposit, CEX withdrawal, hot wallet, sweep wallet을 구분한다 |
| 거래 구조 해석 | DEX swap, bridge, airdrop claim, CEX deposit 후보를 구분한다 |
| evidence 확보 | TX detail, token transfer, event log, counterparty label을 근거로 남긴다 |
| tracing | Transaction Map과 Auto Trace로 핵심 경로와 noise branch를 분리한다 |
| 세무 연결 | 수령 후보, 처분 후보, 단순 이동 후보, off-ramp 후보를 분리한다 |
| 자료 요청 | 거래소 내부 장부, 프로젝트 약관, claim 사유, 체결내역 등 추가 요청 항목을 작성한다 |

## 중급 목차안

### 1. On-ramp / off-ramp와 거래소 입출금 구조

핵심 질문:

```text
법정화폐와 가상자산이 만나는 지점은 어디이고, 온체인에서는 무엇만 확인할 수 있는가?
```

내용:

- on-ramp: 법정화폐 또는 거래소 내부 잔고에서 온체인 지갑으로 가상자산이 나오는 구간
- off-ramp: 온체인 자산이 거래소, OTC, 결제, 카드, 은행 등 법정화폐화 가능 지점으로 들어가는 구간
- CEX withdrawal과 CEX deposit의 차이
- deposit address, hot wallet, sweep wallet, omnibus wallet 구조
- CEX 입금이 곧 매도 확정이 아닌 이유
- 거래소 내부 장부, 체결내역, KYC 계정 자료가 필요한 지점

실습 케이스:

- CEX withdrawal 후보에서 개인 지갑으로 이동
- 개인 지갑에서 CEX deposit 후보로 이동

관련 파일:

- `cases/2_arbitrage.md`

### 2. 세무 질문을 온체인 분석 질문으로 바꾸기

핵심 질문:

```text
이 거래는 수령인가, 처분인가, 단순 이동인가, off-ramp 후보인가, 아니면 자료 부족인가?
```

내용:

- 과세 이벤트 후보와 단순 이동 후보 구분
- 취득, 양도, 교환, 대여, reward, airdrop의 온체인 흔적
- on-ramp/off-ramp 후보와 과세 이벤트 확정의 차이
- 큰 출금액, 큰 정산액과 실제 손익의 차이
- market별 `Total in / Total out / PnL`을 먼저 맞추는 원칙
- 온체인으로 보이는 것과 거래소/납세자 자료가 필요한 것의 분리

실습 케이스:

- 간단 DEX swap TX
- CEX deposit 후보 TX
- Polymarket 대형 출금/손실 응용 케이스

### 3. DEX swap과 coin-to-coin 교환

핵심 질문:

```text
토큰이 바뀐 거래를 처분 후보로 볼 때 어떤 evidence가 필요한가?
```

내용:

- swap router, pool, aggregator 구분
- input token, output token, amount, slippage, fee
- swap과 단순 transfer의 차이
- realized gain 계산을 위해 필요한 외부 가격/체결 자료

실습 케이스:

- 기본 token-to-token swap
- swap 이후 CEX deposit 후보

관련 파일:

- `cases/5_meme_coin.md`
- `cases/6_nft_trading.md`

### 4. Airdrop / claim / reward 수령

핵심 질문:

```text
claim TX에서 수령 시점, 수량, 지급 사유, 이후 처분 후보를 어떻게 정리할 것인가?
```

내용:

- airdrop claim contract interaction
- token transfer와 claim event
- 지급 원인: 무상 배포, 활동 보상, quest, referral, bounty
- 수령 후 보유, swap, CEX deposit 후보
- 수령 원인과 대가성은 온체인만으로 확정하지 않는 원칙

실습 케이스:

- LayerZero airdrop

관련 파일:

- `cases/1_layerzero.md`

### 5. 국내 CEX 연계 흐름과 아비트라지

핵심 질문:

```text
해외 또는 DEX에서 취득한 자산이 국내 거래소로 이동했을 때 어디까지 온체인 evidence로 말할 수 있는가?
```

내용:

- 해외 CEX withdrawal / DEX swap / bridge / 국내 CEX deposit 후보 연결
- 국내 거래소 원화마켓 매도는 온체인만으로 확정할 수 없음
- 상장 시점, 입금 시점, 내부 체결내역을 함께 봐야 하는 이유
- off-ramp 후보와 실제 원화화의 구분

실습 케이스:

- 업비트 원화상장 아비트라지

관련 파일:

- `cases/2_arbitrage.md`

### 6. 중급 산출물 작성

핵심 질문:

```text
분석 결과를 국세청 업무 문서로 어떻게 남길 것인가?
```

내용:

- evidence table
- asset flow table
- taxable event candidate table
- PnL reconciliation table
- information request draft
- confidence / limitation 작성법

실습 산출물:

- 한 케이스를 골라 `수령 / 처분 / 단순 이동 / off-ramp 후보 / 추가 확인 필요`로 분류
- `출금액 != 과세소득`, `정산액 != 순이익` 형태의 limitation memo 작성

관련 파일:

- `cases/10_polymarket_seoul_pnl_screening.md`

## 중급 포함 케이스 후보

| 우선순위 | 케이스 | 포함 이유 | 난이도 | 상태 |
|---:|---|---|---|---|
| 1 | 업비트 원화상장 아비트라지 | 국내 거래소 접점, bridge, CEX 내부자료 한계를 설명하기 좋음 | 중 | seed 정리됨 |
| 2 | LayerZero airdrop | 최신 claim/reward 수령 구조를 보여주기 좋음 | 중 | seed 정리됨 |
| 3 | 기본 DEX swap | coin-to-coin 교환과 처분 후보를 설명하기 쉬움 | 중 | `cases/5_meme_coin.md`, `cases/6_nft_trading.md` 활용 |
| 4 | Polymarket 대형 출금/손실 응용 | 큰 출금액이 있어도 market PnL은 손실일 수 있다는 점을 설명하기 좋음 | 중급 응용 | seed 정리됨 |

## 중급 1일 운영 예시

| 시간 | 세션 | 케이스 |
|---:|---|---|
| 09:30-10:10 | on-ramp/off-ramp와 거래소 주소 구조 | CEX 입출금 예시 |
| 10:20-11:00 | 세무 질문을 온체인 질문으로 바꾸기 | 간단 TX |
| 11:10-12:00 | DEX swap과 처분 후보 | 기본 swap TX |
| 13:00-13:50 | airdrop / reward 수령 | LayerZero |
| 14:00-14:50 | 국내 CEX 연계 흐름 | 업비트 아비트라지 |
| 15:00-15:50 | bridge 확인 포인트 | LayerZero / 업비트 아비트라지 보조 해석 |
| 16:00-16:35 | 출금액과 손익 분리 | Polymarket 대형 출금/손실 |
| 16:35-17:10 | 산출물 작성 | evidence table / 자료요청 초안 |

## 고급 과정 개요

### 과정명

```text
국세청 고급: 사건형 케이스 스터디와 세무조사 산출물 작성
```

### 대상

- 기본 tracing과 중급 구조 해석을 수행할 수 있는 교육생
- 실제 사건형 자료를 보고 분석 범위, 가설, evidence, 한계를 정리해야 하는 실무자
- 팀 단위 분석과 보고서 리뷰가 필요한 교육생

### 종료 시점 역량

| 영역 | 할 수 있어야 하는 일 |
|---|---|
| 사건 설계 | seed, 기간, chain, token, 분석 가설을 설정한다 |
| 복합 추적 | 여러 chain, bridge, DeFi, CEX 후보가 섞인 흐름을 재구성한다 |
| 이벤트 분류 | 과세 이벤트 후보, 단순 이동, 자료 부족 구간을 분리한다 |
| 산출물 작성 | 조사 메모, 자료 요청서, 자금흐름표를 작성한다 |
| 방어선 설정 | 단정 가능한 것과 단정 불가능한 것을 구분하고 confidence를 남긴다 |

## 고급 목차안

### 1. Case intake와 seed register 작성

내용:

- 사건 개요 정리
- seed address / tx / chain / token / 기간 범위 설정
- 분석 가설과 제외 범위 작성
- 공개 라벨과 실소유자 단정 금지

산출물:

- seed register
- case scope note

### 2. 지갑 단위 경제활동 타임라인 재구성

내용:

- wallet-level inflow/outflow timeline
- 수령, swap, bridge, deposit 후보의 시간 순 정리
- 같은 지갑의 여러 수익 유형이 섞일 때 귀속 범위 분리

케이스:

- Polymarket `@blackhuman5`
  - 서울시장 YES: 440 투입 -> 10,000 정산
  - 다른 한국 정치시장 PnL
  - Relay 출금액이 정산액보다 큰 이유와 과잉 귀속 금지

관련 파일:

- `cases/10_polymarket.md`
- `cases/10_polymarket_blackhuman5_case.md`
- `cases/10_polymarket_seoul_pnl_screening.md`

산출물:

- wallet activity timeline
- market별 PnL 후보표

### 3. Cross-chain 경로 복원

내용:

- bridge source tx와 destination tx 연결
- Relay / Stargate / CCTP / LayerZero event 비교
- destination recipient와 후속 이동 확인
- bridge 이후 CEX 확정 금지 원칙

케이스:

- Polymarket Relay: Polygon -> BNB Chain
- Stargate + DaimoPay/CCTP routing: BNB -> Arbitrum -> Optimism

관련 파일:

- `bridge_table.md`
- `cases/10_polymarket_blackhuman5_case.md`

산출물:

- cross-chain flow table
- source/destination evidence table

### 4. CEX 접점과 자료 요청서 작성

내용:

- 국내외 CEX deposit 후보
- hot wallet / sweep wallet / deposit address 구분
- CEX 입금과 내부 매도 확정의 차이
- 거래소에 요청할 자료 범위

케이스:

- 업비트 원화상장 아비트라지
- bridge 후 국내외 CEX 접점 후보

관련 파일:

- `cases/2_arbitrage.md`
- `bridge_table.md`

산출물:

- exchange contact evidence table
- information request draft

### 5. DeFi / RWA 심화 해석

내용:

- DeFi 원금과 수익 분리
- LP fee, reward token, vault share, perp PnL
- RWA token과 off-chain 권리관계 분리
- 온체인 event만으로 손익을 확정할 때의 위험

케이스:

- GMX v2
- BTC-USDC pool
- Pharos Vault
- Ondo RWA/STO

관련 파일:

- `cases/3_gmx.md`
- `cases/4_ondo.md`
- `cases/8_btc_usdc_pool.md`
- `cases/9_pharos_vault.md`

산출물:

- DeFi event breakdown
- limitation note

### 6. 경제적 이익 유형별 분류와 과세 이벤트 후보표

내용:

- airdrop, reward, bounty, token sale, NFT sale, prediction market, DeFi yield 비교
- 수령 원인, 대가성, 반복성, 처분 여부
- 온체인 evidence와 외부 자료의 역할 분리

케이스:

- LayerZero airdrop
- Legion token sale
- NFT trading
- Polymarket

관련 파일:

- `cases/1_layerzero.md`
- `cases/7_legion_token_sale.md`
- `cases/6_nft_trading.md`
- `cases/10_polymarket.md`

산출물:

- taxable event candidate table
- crypto income typology map

### 7. 최종 보고서 작성과 리뷰

내용:

- 자금흐름 요약
- 과세 검토 후보
- 단순 이동 후보
- 추가 확인 필요 자료
- confidence / limitation
- reviewer 질문 대응

산출물:

- tax investigation memo
- case study report
- 발표용 1-page summary

## 고급 포함 케이스 후보

| 우선순위 | 케이스 | 고급에서 쓰는 이유 | 산출물 |
|---:|---|---|---|
| 1 | Polymarket `@blackhuman5` | 하나의 지갑에서 market PnL, 정산, bridge, 과잉 귀속 금지까지 설명 가능 | `cases/10_polymarket_blackhuman5_case.md` |
| 2 | 업비트 원화상장 아비트라지 | 국내 CEX 접점과 거래소 자료 요청을 가장 직접적으로 훈련 가능 | `cases/2_arbitrage.md` |
| 3 | GMX v2 / PerpDEX | DeFi 손익을 단순 transfer로 계산하면 안 된다는 고급 논점 | `cases/3_gmx.md` |
| 4 | Ondo RWA/STO | 토큰화 자산의 온체인 이전과 off-chain 권리관계 분리 | `cases/4_ondo.md` |
| 5 | Pharos Vault / BTC-USDC pool | vault share, LP, reward, withdrawal의 구분 훈련 | `cases/9_pharos_vault.md`, `cases/8_btc_usdc_pool.md` |
| 6 | Legion token sale | allocation, vesting, claim, bridge 한계를 설명 | `cases/7_legion_token_sale.md` |

## 고급 1일 운영 예시

| 시간 | 세션 | 산출물 |
|---:|---|---|
| 09:30-10:10 | 사건 개요와 seed register 작성 | seed register |
| 10:20-11:30 | wallet timeline과 주요 TX 선정 | wallet timeline |
| 11:30-12:10 | cross-chain flow 복원 | bridge flow table |
| 13:10-14:20 | 과세 이벤트 후보 분류 | taxable event candidate table |
| 14:30-15:30 | 거래소/프로젝트 자료 요청서 작성 | information request draft |
| 15:40-16:40 | 팀별 case memo 작성 | tax investigation memo |
| 16:40-17:20 | 리뷰와 단정 금지 지점 정리 | final limitation note |
