# 1. LayerZero Airdrop Case

## 목적

기존 UNI airdrop case의 현대판으로 사용한다. 국세청 강의에서는 `디믹싱/추적 기능` 자체보다, Web3 생태계에서 경제적 이익이 발생하는 방식을 보여주는 case로 잡는다.

이 case의 핵심은 `airdrop claim -> 보유/이동 -> DEX swap 또는 cross-chain 처분 후보`를 온체인 evidence로 확인하는 것이다. 현재 seed에서는 CEX deposit이나 실제 fiat off-ramp까지 확정하지 않는다.

## 핵심 질문

```text
이 주소는 LayerZero airdrop으로 어떤 token을 수령했는가?
수령 이후 보유, 지갑 간 이동, DEX swap, cross-chain 이동 후보 중 어디까지 확인되는가?
국세청 입장에서 추가로 요청해야 할 off-chain 자료는 무엇인가?
```

## 경제적 이익 취득 방식

- 과거 LayerZero protocol 사용 이력 또는 eligibility에 따라 ZRO token을 claim한다.
- claim TX에서 `ZRO 수령` evidence가 남는다.
- LayerZero claim은 Proof-of-Donation 구조라 claim TX의 native ETH value와 ZRO 수령액을 분리해서 봐야 한다.
- claim 이후 DEX swap 또는 cross-chain route가 있으면 `처분 후보`로 분류한다.
- CEX deposit, 매도, 원화화는 온체인 라벨과 거래소 자료가 결합되어야 확정할 수 있다.

## 결론 요약

| 구분 | 판단 |
|---|---|
| 메인 실습 후보 | Candidate C |
| 보조 예시 1 | Candidate A, claim 후 다른 지갑으로 전량 이동 |
| 보조 예시 2 | Candidate B, claim 후 WOOFi crossSwap |
| 주요 검색 chain | Arbitrum One |
| CEX/off-ramp 결론 | 이 seed만으로는 확정하지 않음. 이후 trace에서 후보가 나오면 추가 확인 필요 |

## 공통 Seed

```text
Transight search network / chain
Arbitrum One

ZRO token
0x6985884C4392D348587B19cb9eAAf157F13271cd

LayerZero Foundation Proof of Donation Claim 1 / DonateAndClaim
0xB09F16F625B363875e39ADa56C03682088471523

ClaimLocal
0xd6b6a6701303B5Ea36fa0eDf7389b562d8F894DB

USDC on Arbitrum
0xaf88d065e77c8cC2239327C5EDb3A432268e5831

WETH on Arbitrum
0x82aF49447D8a07e3bd95BD0d56f35241523fBab1
```

검증 기준:

- 2026-05-28 기준 Arbitrum Blockscout API v2와 transaction/token transfer record로 확인
- 모든 주요 TX status는 `ok`
- address name은 Blockscout public label 기준이므로 Transight에서 별도 label 확인 필요

## Transight 검색 기준

이 case의 주요 TX는 **Arbitrum One**에서 검색한다.

| 항목 | 검색할 chain/network | 검색값 | 비고 |
|---|---|---|---|
| ZRO token | Arbitrum One | `0x6985884C4392D348587B19cb9eAAf157F13271cd` | LayerZero ERC-20 |
| Claim contract | Arbitrum One | `0xB09F16F625B363875e39ADa56C03682088471523` | DonateAndClaim |
| ClaimLocal | Arbitrum One | `0xd6b6a6701303B5Ea36fa0eDf7389b562d8F894DB` | ZRO transfer source |
| Candidate A wallet | Arbitrum One | `0x1683c5EB3C6Cfe4C25d3044600A2A1542da9e100` | claim 후 외부 지갑 이동 |
| Candidate A claim TX | Arbitrum One | `0x4dc1e95e6b430139234027b9b6c97fc45367010169b805123b0b2d8d07946bcb` | donateAndClaim |
| Candidate A transfer TX | Arbitrum One | `0xb339a681bd11a380ae0912b36adb7fcb89386283364e913c5e0165356b4a924e` | ZRO 전량 이동 |
| Candidate B wallet | Arbitrum One | `0xc45ba68D2640707C0288EB90675ec6b641bB2e10` | claim 후 WOOFi route |
| Candidate B claim TX | Arbitrum One | `0xcbe87f138676e65f7cc2555343664c12f1aa64d35032ddca08d0e5811f5f43bb` | donateAndClaim |
| Candidate B crossSwap TX | Arbitrum One | `0x56ea6db5b6a5add6b2b62e7a5550b0b71ed48279ece13c85c2bf3040ce04ac87` | origin chain TX |
| Candidate C wallet | Arbitrum One | `0x81599529b5E3E5eb7325C7a1dA15af084Eab17A1` | 메인 실습 후보 |
| Candidate C claim TX | Arbitrum One | `0xee614202207f79c1b4390b4f98c70d0429004123772f4992f57acfb12453379b` | donateAndClaim |
| Candidate C swap TX | Arbitrum One | `0xe0412d405217bf00c316bf40a63cb12203237570ea74495d027e87e59d545394` | Uniswap Universal Router |
| Candidate B destination route | 추가 확인 필요 | destination chain TX | WOOFi/Stargate route는 목적지 chain을 별도 추적 |

## Candidate C: claim 후 Uniswap에서 USDC로 처분

강의 난이도: 쉬움-중간  
추천도: 메인 실습 후보

`airdrop 수령 -> DEX swap -> stablecoin 수령`이 명확하다. 국세청 강의에서 경제적 이익의 수령과 처분 후보를 분리해서 설명하기 가장 좋다.

```text
Transight search network / chain
Arbitrum One

Wallet
0x81599529b5E3E5eb7325C7a1dA15af084Eab17A1

Claim TX
0xee614202207f79c1b4390b4f98c70d0429004123772f4992f57acfb12453379b

Post-claim Uniswap swap TX
0xe0412d405217bf00c316bf40a63cb12203237570ea74495d027e87e59d545394
```

확인된 흐름:

```text
2024-06-20 12:00:51 UTC
wallet -> DonateAndClaim
  -> method: donateAndClaim
  -> native ETH value: 0.001099640539277747 ETH
  -> ClaimLocal -> wallet
  -> 39.587059414 ZRO 수령

2024-07-21 00:34:03 UTC
wallet -> Uniswap Universal Router
  -> method: execute
  -> 29.6902945605 ZRO를 UniswapV3Pool로 전송
  -> 9.8967648535 ZRO를 다른 UniswapV3Pool로 전송
  -> wallet이 208.397736 USDC 수령
```

판단:

- claim TX는 `airdrop 수령 후보`
- native ETH value는 `claim 비용/기부성 지출 후보`로 ZRO 수령액과 분리
- Uniswap `execute` TX는 `처분 후보`
- ZRO가 USDC로 전환되어 stablecoin 취득 결과가 명확하다.
- 이후 USDC가 CEX deposit 후보로 이어지는지는 추가 trace 필요

강의에서 보여줄 포인트:

- claim TX의 token transfer tab에서 ZRO 수령 확인
- swap TX에서 ZRO outflow와 USDC inflow를 같은 TX 안에서 확인
- token 수령 시점과 처분 시점을 분리해서 evidence table 작성
- claim value, gas fee, token 수령액, swap 수령액을 서로 다른 항목으로 분리

## Candidate A: claim 후 다른 지갑으로 전량 이동

강의 난이도: 쉬움  
용도: `수령 -> 지갑 간 이동` 기본 예시

```text
Transight search network / chain
Arbitrum One

Wallet
0x1683c5EB3C6Cfe4C25d3044600A2A1542da9e100

Claim TX
0x4dc1e95e6b430139234027b9b6c97fc45367010169b805123b0b2d8d07946bcb

Post-claim transfer TX
0xb339a681bd11a380ae0912b36adb7fcb89386283364e913c5e0165356b4a924e
```

확인된 흐름:

```text
2024-06-20 12:00:49 UTC
wallet -> DonateAndClaim
  -> method: donateAndClaim
  -> native ETH value: 0.002545852058138817 ETH
  -> ClaimLocal -> wallet
  -> 53.502157867 ZRO 수령

2024-06-20 12:06:29 UTC
wallet -> ZRO token contract
  -> method: transfer
  -> wallet -> 0x93Cd9756C5c99dD827C3F794776ed2BF90D39C5D
  -> 53.502157867 ZRO 전량 이동
```

판단:

- claim TX는 `airdrop 수령 후보`
- post-claim transfer는 `단순 이동 후보`
- 수령 직후 전량 이동이므로 manual trace와 cluster로 다음 주소와의 관계를 확인하기 좋다.
- `0x93Cd...9C5D`는 현재 문서 기준 CEX로 확정하지 않는다. 일반 외부 주소 또는 추가 확인 대상 주소로 둔다.

## Candidate B: claim 후 WOOFi crossSwap

강의 난이도: 중간  
용도: `airdrop 수령 -> DEX/cross-chain route -> ETH계 자산 전환 후보`

LayerZero가 multichain protocol이라는 점과 post-claim 처분이 단순 transfer보다 복잡해질 수 있다는 점을 보여주기 좋다. 다만 이 후보는 origin chain TX만으로 최종 destination chain 수령까지 확정하지 않는다.

```text
Transight search network / chain
Arbitrum One

Wallet
0xc45ba68D2640707C0288EB90675ec6b641bB2e10

Claim TX
0xcbe87f138676e65f7cc2555343664c12f1aa64d35032ddca08d0e5811f5f43bb

Post-claim crossSwap TX
0x56ea6db5b6a5add6b2b62e7a5550b0b71ed48279ece13c85c2bf3040ce04ac87
```

확인된 흐름:

```text
2024-06-20 12:00:51 UTC
wallet -> DonateAndClaim
  -> method: donateAndClaim
  -> native ETH value: 0.003201291606861021 ETH
  -> ClaimLocal -> wallet
  -> 115.246497847 ZRO 수령

2024-06-22 07:35:41 UTC
wallet -> WooCrossChainRouterV4
  -> method: crossSwap
  -> wallet -> WooCrossChainRouterV4
  -> 115.246497847 ZRO 투입
  -> WooRouterV2 / UniswapV3Pool route
  -> WETH burn 및 SGETH/Stargate route 발생
```

주요 address label:

| Address | Arbitrum label | 역할 |
|---|---|---|
| `0xCa10E8825FA9F1dB0651Cd48A9097997DBf7615d` | WooCrossChainRouterV4 | crossSwap 진입 |
| `0x4c4AF8DBc524681930a27b2F1Af5bcC8062E6fB7` | WooRouterV2 | swap route |
| `0x4CEf551255EC96d89feC975446301b5C4e164C59` | UniswapV3Pool | ZRO/WETH swap route |
| `0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9` | StargateComposer | Stargate route |
| `0x915A55e36A01285A14f05dE6e81ED9cE89772f8e` | Pool / Stargate Ether Vault-LP | SGETH 관련 pool |

판단:

- claim TX는 `airdrop 수령 후보`
- WOOFi `crossSwap`은 `처분 후보 + bridge/cross-chain 이동 후보`
- origin chain에서 ZRO가 WETH/SGETH route로 들어간 것은 확인된다.
- 목적지 chain, 최종 수령 자산, 최종 수령 주소는 WOOFi/Stargate event와 destination chain TX까지 추가 확인해야 한다.

## 예상 Flow

```text
LayerZero claim contract
  -> wallet이 ZRO claim
  -> token 보유 또는 이동
  -> DEX swap / cross-chain swap 후보
  -> stablecoin 또는 ETH계 자산 전환 후보
  -> CEX deposit/off-ramp 후보는 추가 trace와 거래소 자료로 별도 확인
```

## Transight 확인 포인트

- TX hash 검색 시 network를 Arbitrum One으로 고정
- claim contract interaction
- native ETH value와 ZRO token transfer의 분리
- ClaimLocal -> wallet token transfer
- claim 이후 token movement
- Uniswap/WOOFi/Stargate 등 service address 접점
- Auto Trace로 후보 route를 먼저 보고, 결론은 manual trace와 TX detail로 확정
- CEX deposit 후보가 나와도 실제 매도/원화화는 거래소 내부 자료 없이는 확정하지 않음

## Evidence Table

| 단계 | Chain | TX / Address | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 1 | Arbitrum One | `0xee614202207f79c1b4390b4f98c70d0429004123772f4992f57acfb12453379b` | `donateAndClaim`, 39.587059414 ZRO 수령 | 수령 후보 | Candidate C |
| 2 | Arbitrum One | `0xe0412d405217bf00c316bf40a63cb12203237570ea74495d027e87e59d545394` | Uniswap Universal Router `execute`, ZRO -> USDC, wallet 208.397736 USDC 수령 | 처분 후보 | Candidate C |
| 3 | Arbitrum One | `0x4dc1e95e6b430139234027b9b6c97fc45367010169b805123b0b2d8d07946bcb` | `donateAndClaim`, 53.502157867 ZRO 수령 | 수령 후보 | Candidate A |
| 4 | Arbitrum One | `0xb339a681bd11a380ae0912b36adb7fcb89386283364e913c5e0165356b4a924e` | ZRO 전량 외부 전송 | 단순 이동 후보 | Candidate A |
| 5 | Arbitrum One | `0xcbe87f138676e65f7cc2555343664c12f1aa64d35032ddca08d0e5811f5f43bb` | `donateAndClaim`, 115.246497847 ZRO 수령 | 수령 후보 | Candidate B |
| 6 | Arbitrum One | `0x56ea6db5b6a5add6b2b62e7a5550b0b71ed48279ece13c85c2bf3040ce04ac87` | WOOFi `crossSwap`, ZRO -> WETH/SGETH route | 처분/bridge 후보 | Candidate B |

## 국세청 추가 요청자료

- claim eligibility 또는 campaign 기준
- 납세자 지갑 귀속 자료
- claim 시점 token 시가와 원화 환산 기준
- claim 비용/donation value와 gas fee
- swap 시점 token 시가와 원화 환산 기준
- CEX 계정 귀속, 입금 반영 시각
- CEX 내부 매도/출금/원화 정산 자료

## 주의점

- eligibility 사유는 온체인만으로 완전하게 설명되지 않을 수 있다.
- claim TX의 native ETH value는 donation/claim 비용 후보이고, ZRO 수령액과 별도 항목으로 기록한다.
- CEX deposit은 off-ramp 후보일 뿐 실제 매도/원화화 확정 근거가 아니다.
- cross-chain route는 origin chain TX만으로 최종 목적지까지 확정하지 않는다.
- public label은 explorer/Transight에서 다르게 보일 수 있으므로 라벨 근거를 같이 남긴다.

## Source Links

- Arbitrum Blockscout - ZRO token: https://arbitrum.blockscout.com/address/0x6985884C4392D348587B19cb9eAAf157F13271cd
- Arbitrum Blockscout - DonateAndClaim: https://arbitrum.blockscout.com/address/0xB09F16F625B363875e39ADa56C03682088471523
- Arbitrum Blockscout - ClaimLocal: https://arbitrum.blockscout.com/address/0xd6b6a6701303B5Ea36fa0eDf7389b562d8F894DB
- Candidate C claim: https://arbitrum.blockscout.com/tx/0xee614202207f79c1b4390b4f98c70d0429004123772f4992f57acfb12453379b
- Candidate C swap: https://arbitrum.blockscout.com/tx/0xe0412d405217bf00c316bf40a63cb12203237570ea74495d027e87e59d545394
- Candidate A claim: https://arbitrum.blockscout.com/tx/0x4dc1e95e6b430139234027b9b6c97fc45367010169b805123b0b2d8d07946bcb
- Candidate A transfer: https://arbitrum.blockscout.com/tx/0xb339a681bd11a380ae0912b36adb7fcb89386283364e913c5e0165356b4a924e
- Candidate B claim: https://arbitrum.blockscout.com/tx/0xcbe87f138676e65f7cc2555343664c12f1aa64d35032ddca08d0e5811f5f43bb
- Candidate B crossSwap: https://arbitrum.blockscout.com/tx/0x56ea6db5b6a5add6b2b62e7a5550b0b71ed48279ece13c85c2bf3040ce04ac87
- LayerZero Proof-of-Donation 배경: https://www.theblock.co/post/301043/layerzero-proof-of-donation-zro-claiming-mechanism
