# 4. Ondo RWA Case

## 목적

Ondo의 OUSG / USDY 사례로 RWA token에서 경제적 이익이 어떻게 온체인에 남는지 설명한다.

핵심은 `token mint/transfer/burn`과 `off-chain 권리관계`를 분리해서 보는 것이다. 온체인에서는 token 수령, wrap, redeem, stablecoin 수령이 보이지만, 실제 법적 권리자, 적격투자자 여부, 약정상 권리, 상환 신청 내역은 issuer/KYC/계약 자료가 있어야 확정된다.

## 강의 포지션

```text
RWA 취득 방식
  -> stablecoin 또는 법정화폐를 issuer/manager 쪽으로 지급
  -> RWA token mint 또는 수령
  -> 보유 중 가격/수량 방식으로 yield 반영
  -> redeem 시 RWA token burn
  -> USDC/PYUSD/RLUSD/USD bank wire 등으로 상환 후보 발생
```

국세청 관점에서는 `디믹싱`보다 이 case가 더 실무적이다. 이유는 온체인만 봐도 다음 질문이 바로 생긴다.

- 이 token 수령이 단순 transfer인지, RWA 취득인지
- yield가 token price 상승형인지, rebasing 수량 증가형인지
- redeem으로 받은 USDC가 처분/상환 대가인지
- 온체인 지갑 소유자와 off-chain 계정/권리자가 일치하는지
- 한국 거주자/법인이 이런 token을 취득할 수 있었는지

## 검색 체인

이 문서의 주요 seed는 모두 아래 네트워크에서 검색한다.

```text
Transight search network / chain: Ethereum Mainnet
```

## 공식 주소

| 구분 | 주소 | Transight 검색 체인 | 근거 / 메모 |
|---|---|---|---|
| OUSG token | `0x1B19C19393e2d034D8Ff31ff34c81252FcBbee92` | Ethereum Mainnet | Ondo 공식 주소 문서의 OUSG Ethereum token |
| OUSG_InstantManager | `0x93358db73B6cd4b98D89c8F5f230E81a95c2643a` | Ethereum Mainnet | OUSG buy/redeem manager |
| OndoIDRegistry | `0xcf6958D69d535FD03BD6Df3F4fe6CDcd127D97df` | Ethereum Mainnet | OUSG를 hold할 수 있는 주소 관리 contract |
| OUSG PYUSD recipient | `0x0317a350b093F8010837d1b844292555d73ebC2c` | Ethereum Mainnet | manual subscription용 PYUSD recipient |
| OUSG manual redemption recipient | `0x72Be8C14B7564f7a61ba2f6B7E50D18DC1D4B63D` | Ethereum Mainnet | manual redemption용 OUSG recipient |
| USDY token | `0x96F6eF951840721AdBF46Ac996b59E0235CB985C` | Ethereum Mainnet | Ondo 공식 주소 문서의 USDY Ethereum token |
| USDY_InstantManager | `0xa42613C243b67BF6194Ac327795b926B4b491f15` | Ethereum Mainnet | USDY instant mint/redeem manager |
| USDC | `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48` | Ethereum Mainnet | USDY/OUSG redeem 수령 token 예시 |

## Seed에서 확인되는 보조 주소

아래 주소는 공식 주소 목록이라기보다, 이 문서의 seed TX token transfer에서 관찰되는 라우터/유동성 출처/보조 contract다. 강의 전 explorer label과 TX transfer를 재확인한다.

| 구분 | 주소 | Transight 검색 체인 | 근거 / 메모 |
|---|---|---|---|
| rOUSG token / wrapper | `0x54043c656F0FAd0652D9Ae2603cDF347c5578d00` | Ethereum Mainnet | Etherscan label 기준 rOUSG token / wrapper |
| OndoTokenRouter | `0x99B8d1D1c17a10CD1A878d1A44c11fd7E4daD7bC` | Ethereum Mainnet | subscribe/redeem 자금이 거치는 internal router (seed에서 확인) |
| BuidlUSDCSource | `0x9F205E1aC7698F59EdbAa0a28C4A4c4ed605b722` | Ethereum Mainnet | OUSG redeem seed에서 USDC source로 관찰되는 labelled contract |
| USDY USDC source SafeProxy | `0x3312cc371Fe0Dd5171878630A1E5cf69778E8fa5` | Ethereum Mainnet | USDY subscribe/redeem seed에서 USDC source/recipient로 관찰되는 SafeProxy |

> 흐름 주의: OUSG subscribe TX에서 PYUSD는 `wallet -> OUSG_InstantManager -> OndoTokenRouter -> PYUSD recipient(0x0317a350...)`로 흐르고, OUSG redeem TX에서 지급 USDC는 `BuidlUSDCSource -> OndoTokenRouter -> OUSG_InstantManager -> wallet`로 흐른다. USDY seed에서는 USDC가 `SafeProxy(0x3312...) -> OndoTokenRouter -> USDY_InstantManager -> wallet` 또는 반대 방향으로 흐른다. 아래 사례 흐름도는 사용자 관점만 단순화한 것이며, 실제 transfer path는 보조 주소를 함께 봐야 한다. (2026-06-01 온체인 확인)

## 사례 A: OUSG subscribe / redeem

가장 추천하는 메인 실습 seed. 같은 지갑이 OUSG를 mint하고, 나중에 일부를 redeem해서 USDC를 받는다.

```text
Transight search network / chain
Ethereum Mainnet

Wallet
0xaDf5e32eB413e62DC072Aa5fd12F19a115aC3c12

OUSG_InstantManager
0x93358db73B6cd4b98D89c8F5f230E81a95c2643a
```

### A-1. OUSG 취득 / mint

```text
TX
0x8c35f208428c39a1d4bde67a90c4e3379bd51cc91780e66622fb2e733c8c418c

Transight search network / chain
Ethereum Mainnet

Block / time
24834938 / 2026-04-08 12:17:59 UTC

Method
subscribe
```

관찰되는 흐름:

```text
wallet
  -> OUSG_InstantManager
  -> PYUSD 303,222.048088 투입
  -> OUSG 2,640.322713906709239181 mint
  -> OUSG가 wallet으로 수령됨
```

강의 포인트:

- 온체인에서는 `PYUSD 지출`과 `OUSG mint`가 같은 TX 안에 보인다.
- OUSG mint는 경제적 이익 취득이라기보다 RWA token 취득/매수 후보로 분류한다.
- 이 TX만으로 법적 권리자, 투자자 적격성, 계약상 권리까지 확정하면 안 된다.

### A-2. OUSG redeem / burn / USDC 수령

```text
TX
0x6d2afb9809a97f1e12350e72f1c92b4c20ed361b5903b109dae5ffe7fd0a0915

Transight search network / chain
Ethereum Mainnet

Block / time
25073169 / 2026-05-11 16:50:59 UTC

Method
redeem
```

관찰되는 흐름:

```text
wallet
  -> OUSG 477.528610584056995384 전송
  -> OUSG_InstantManager
  -> OUSG burn
  -> USDC 55,000 수령
```

강의 포인트:

- `OUSG burn + USDC 수령`은 redemption/상환 후보로 볼 수 있다.
- 이때 USDC 수령은 온체인상 명확하지만, 세무상 처분가액/취득가액/보유기간/yield 인식은 off-chain 기록과 같이 봐야 한다.
- 같은 지갑의 A-1 취득 TX와 A-2 상환 TX를 연결하면 RWA token의 lifecycle을 보여주기 좋다.

## 사례 B: rOUSG wrapper 전환 / redeem

OUSG가 rebasing wrapper인 rOUSG로 바뀌고 다시 USDC로 redeem되는 예시다. "token 하나가 다른 token으로 바뀌었으니 무조건 매도"라고 단정하면 안 되는 case로 좋다.

```text
Transight search network / chain
Ethereum Mainnet

Wallet
0x4D27df39254Feb7b0AEfC23A23D77b7D511B3d33

ENS
windandwaves.eth

rOUSG token / wrapper
0x54043c656F0FAd0652D9Ae2603cDF347c5578d00
```

### B-1. OUSG -> rOUSG wrap

```text
TX
0xc83a124ae29dbf37ff06c66a5cb539d48fcc5a814910010884a5f2a4296615ef

Transight search network / chain
Ethereum Mainnet

Block / time
23840508 / 2025-11-20 13:19:59 UTC

Method
wrap
```

관찰되는 흐름:

```text
wallet
  -> rOUSG wrapper contract
  -> OUSG 44.112077390087414521 전송
  -> rOUSG 4,999.999999999999999919 mint
  -> rOUSG가 wallet으로 수령됨
```

강의 포인트:

- 이건 secondary sale이라기보다 `wrapper 전환`으로 보는 게 안전하다.
- rOUSG 수량은 OUSG와 1:1 가격표시가 아니다. USDY/rUSDY와 비슷하게 wrapper 구조와 기준가 개념을 확인해야 한다.
- 온체인 token transfer만 보고 "OUSG를 팔았다"고 결론 내리면 과잉 해석이다.

### B-2. rOUSG redeem

```text
TX
0x247c8104628121cbfaaadcc4d1bb4070264abc7b2f83ec7530992c728b868904

Transight search network / chain
Ethereum Mainnet

Block / time
23840527 / 2025-11-20 13:23:47 UTC

Method
redeemRebasingOUSG
```

관찰되는 흐름:

```text
wallet
  -> rOUSG 4,999.999999999999999919 전송
  -> OUSG_InstantManager
  -> rOUSG burn
  -> 내부적으로 OUSG 44.112077390087414520 burn
  -> USDC 4,999.999999 수령
```

강의 포인트:

- wrap 직후 redeem까지 이어져서 `RWA token -> rebasing wrapper -> stablecoin` 구조를 설명하기 좋다.
- 단순 token movement가 아니라 product mechanics를 이해해야 한다.

## 사례 C: USDY subscribe / redeem 보조 예시

OUSG보다 금액이 작고 구조가 단순해서 보조 예시로 쓰기 좋다. USDY는 가격 상승형 token이고, rUSDY는 rebasing 방식이라는 점을 설명할 수 있다.

> 주의: 사례 C의 C-1 subscribe 지갑(`0xCcaC6Fcc...`)과 C-2 redeem 지갑(`0x3A68Bf6f...`)은 서로 다른 무관한 지갑이다. 온체인 확인 결과 C-1은 USDY 수령만, C-2는 USDY 상환만 했다(같은 USDY를 round-trip한 한 명이 아님). 사례 A·B는 같은 지갑의 취득→상환 lifecycle이지만, 사례 C는 subscribe 구조와 redeem 구조를 각각 보여주는 별도 예시로만 쓴다.

```text
Transight search network / chain
Ethereum Mainnet

USDY_InstantManager
0xa42613C243b67BF6194Ac327795b926B4b491f15

USDY token
0x96F6eF951840721AdBF46Ac996b59E0235CB985C
```

### C-1. USDC -> USDY subscribe

```text
TX
0x55d884a2f2e18cd66290cd65afdd09558f5a880f3d4a3203ce074a615ecdd7ee

Transight search network / chain
Ethereum Mainnet

Block / time
25187608 / 2026-05-27 15:37:11 UTC

Wallet
0xCcaC6Fcc664A0cC0a3f7d809b92814Be6dDA7A3A

Method
subscribe
```

관찰되는 흐름:

```text
wallet
  -> USDY_InstantManager
  -> USDC 30 지출
  -> USDY 26.450809020477078958 mint
  -> USDY가 wallet으로 수령됨
```

### C-2. USDY -> USDC redeem

```text
TX
0x5113f5dbf77a8fb4ae305569001bd3b3e1ef9598e4b3727fd90b0ae5b1cd8830

Transight search network / chain
Ethereum Mainnet

Block / time
25191758 / 2026-05-28 05:30:23 UTC

Wallet
0x3A68Bf6f4959a62584A37889f862D51eCe948Bd8

Method
redeem
```

관찰되는 흐름:

```text
wallet
  -> USDY 1,000 전송
  -> USDY_InstantManager
  -> USDY burn
  -> USDC 1,134.289220 수령
```

강의 포인트:

- USDY의 경제적 이익은 token 수량 증가가 아니라 기준가 상승 방식으로 나타날 수 있다.
- `1,000 USDY -> 1,134.289220 USDC`처럼 redeem 결과가 보이면, 취득 시점/취득가/보유기간/issuer statement를 같이 확인해야 한다.

## Evidence Table

| 단계 | Chain | TX / Address | Transight search network / chain | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|---|
| 공식 주소 | Ethereum Mainnet | `0x1B19C19393e2d034D8Ff31ff34c81252FcBbee92` | Ethereum Mainnet | Ondo 공식 문서 / Etherscan | OUSG token | 권리관계는 문서/계약 확인 |
| 공식 주소 | Ethereum Mainnet | `0x93358db73B6cd4b98D89c8F5f230E81a95c2643a` | Ethereum Mainnet | Ondo 공식 문서 / Etherscan | OUSG manager | buy/redeem 진입점 |
| 보조 주소 | Ethereum Mainnet | `0x54043c656F0FAd0652D9Ae2603cDF347c5578d00` | Ethereum Mainnet | Etherscan label / seed TX | rOUSG wrapper | 공식 주소 목록이 아니라 seed 보조 주소로 사용 |
| 보조 주소 | Ethereum Mainnet | `0x99B8d1D1c17a10CD1A878d1A44c11fd7E4daD7bC` | Ethereum Mainnet | seed TX token transfer | OndoTokenRouter | 실제 transfer path 확인용 |
| 보조 주소 | Ethereum Mainnet | `0x9F205E1aC7698F59EdbAa0a28C4A4c4ed605b722` | Ethereum Mainnet | seed TX token transfer / explorer label | BuidlUSDCSource | OUSG redeem USDC source 후보 |
| 보조 주소 | Ethereum Mainnet | `0x3312cc371Fe0Dd5171878630A1E5cf69778E8fa5` | Ethereum Mainnet | seed TX token transfer / explorer label | USDY USDC source SafeProxy | USDY subscribe/redeem USDC source/recipient 후보 |
| OUSG 취득 | Ethereum Mainnet | `0x8c35f208428c39a1d4bde67a90c4e3379bd51cc91780e66622fb2e733c8c418c` | Ethereum Mainnet | Blockscout token transfer logs | mint / 취득 후보 | PYUSD 지출 + OUSG mint |
| OUSG 상환 | Ethereum Mainnet | `0x6d2afb9809a97f1e12350e72f1c92b4c20ed361b5903b109dae5ffe7fd0a0915` | Ethereum Mainnet | Blockscout token transfer logs | redeem / 상환 후보 | OUSG burn + USDC 수령 |
| rOUSG wrap | Ethereum Mainnet | `0xc83a124ae29dbf37ff06c66a5cb539d48fcc5a814910010884a5f2a4296615ef` | Ethereum Mainnet | Blockscout token transfer logs | wrapper 전환 | 처분으로 단정 금지 |
| rOUSG redeem | Ethereum Mainnet | `0x247c8104628121cbfaaadcc4d1bb4070264abc7b2f83ec7530992c728b868904` | Ethereum Mainnet | Blockscout token transfer logs | redeem / 상환 후보 | rOUSG/OUSG burn + USDC 수령 |
| USDY 취득 | Ethereum Mainnet | `0x55d884a2f2e18cd66290cd65afdd09558f5a880f3d4a3203ce074a615ecdd7ee` | Ethereum Mainnet | Blockscout token transfer logs | mint / 취득 후보 | USDC 지출 + USDY mint |
| USDY 상환 | Ethereum Mainnet | `0x5113f5dbf77a8fb4ae305569001bd3b3e1ef9598e4b3727fd90b0ae5b1cd8830` | Ethereum Mainnet | Blockscout token transfer logs | redeem / 상환 후보 | USDY burn + USDC 수령 |

## Transight 확인 포인트

- TX hash를 Ethereum Mainnet에서 직접 검색한다.
- `Token Transfer` 탭에서 stablecoin 지출과 RWA token mint를 같이 본다.
- `from = 0x000...000`이면 mint, `to = 0x000...000`이면 burn으로 해석한다.
- manager contract와 token contract를 분리한다.
- 사례 A/B처럼 같은 wallet의 여러 TX일 때만 `취득 -> 보유/전환 -> 상환` lifecycle로 묶는다.
- `Cluster`를 쓰더라도 법적 권리자 확정이 아니라 관련 wallet 후보 정리 정도로 표현한다.

## 실습 질문

1. 이 지갑은 어떤 stablecoin을 지출하고 어떤 RWA token을 받았나?
2. token mint와 issuer subscription을 같은 의미로 봐도 되는가?
3. redeem TX에서 burn된 token과 수령한 USDC의 관계는 무엇인가?
4. rOUSG wrap은 매도인가, 전환인가, 아니면 추가 확인이 필요한가?
5. 한국 거주자/법인이라면 OUSG eligibility 제한을 어떻게 확인해야 하나?
6. 세무 판단을 위해 온체인 외에 어떤 자료를 요청해야 하나?

## 판단 기준

- `mint`: token contract에서 `0x000...000 -> wallet` transfer가 발생하면 온체인상 token 발행/수령으로 본다.
- `redeem`: wallet token이 manager로 들어가고 burn되며 USDC/PYUSD 등이 나오면 상환 후보로 본다.
- `wrap`: OUSG가 wrapper로 들어가고 rOUSG가 mint되면 token 형태 전환으로 본다.
- `secondary sale`: DEX pool, RFQ venue, OTC settlement, counterparty payment가 확인되지 않으면 매도라고 단정하지 않는다.
- `legal ownership`: 지갑 주소와 실질 권리자는 KYC, subscription agreement, issuer statement, custodian statement로 확인한다.

## 국세청 추가 요청자료

- Ondo 계정 가입/KYC 자료
- 적격투자자 확인 자료
- subscription agreement / fund document
- issuer statement 또는 계정명세서
- mint/redeem 신청 내역
- USDC/PYUSD 입출금 원천
- 지갑 소유자 확인 자료
- 회계상 취득가, 평가가, 상환가 산정 자료
- 한국 거주자/법인 여부 및 제한 jurisdiction 관련 검토 자료

## 주의점

- 온체인 token transfer는 법적 권리 이전의 충분조건이 아니다.
- RWA token은 contract address만 보고 일반 ERC-20과 동일하게 처리하면 안 된다.
- OUSG 공식 eligibility 문서에는 한국이 jurisdictional restrictions 목록에 포함되어 있으므로, 한국 거주자/법인 관련 case라면 직접 취득 가능성부터 별도로 확인해야 한다.
- USDY 공식 문서도 미국 등 금지/제한 jurisdiction과 KYC 요건을 둔다.
- `USDC를 받았다`는 사실과 `과세 가능한 처분이 발생했다`는 판단은 구분한다.
- 이 case는 심화 파트에 적합하다. 초급 실습보다는 RWA의 경제적 이익 인식 방식과 추가자료 요청 기준을 보여주는 데 쓴다.

## 근거 링크

- Ondo 공식 contract 주소: https://docs.ondo.finance/addresses
- OUSG mint/redeem 공식 설명: https://docs.ondo.finance/qualified-access-products/minting-and-redeeming
- OUSG eligibility 공식 설명: https://docs.ondo.finance/qualified-access-products/eligibility
- OUSG onboarding/KYC 공식 설명: https://docs.ondo.finance/qualified-access-products/onboarding-and-kyc
- USDY basics 공식 설명: https://docs.ondo.finance/general-access-products/usdy/basics
- USDY eligibility 공식 설명: https://docs.ondo.finance/general-access-products/usdy/eligibility
- USDY_InstantManager 공식 개발 문서: https://docs.ondo.finance/developer-guides/usdy-instant-manager-integration
- rOUSG wrapper / token: https://eth.blockscout.com/address/0x54043c656F0FAd0652D9Ae2603cDF347c5578d00
- OndoTokenRouter: https://eth.blockscout.com/address/0x99B8d1D1c17a10CD1A878d1A44c11fd7E4daD7bC
- BuidlUSDCSource: https://eth.blockscout.com/address/0x9F205E1aC7698F59EdbAa0a28C4A4c4ed605b722
- USDY USDC source SafeProxy: https://eth.blockscout.com/address/0x3312cc371Fe0Dd5171878630A1E5cf69778E8fa5
- OUSG subscribe TX: https://eth.blockscout.com/tx/0x8c35f208428c39a1d4bde67a90c4e3379bd51cc91780e66622fb2e733c8c418c
- OUSG redeem TX: https://eth.blockscout.com/tx/0x6d2afb9809a97f1e12350e72f1c92b4c20ed361b5903b109dae5ffe7fd0a0915
- rOUSG wrap TX: https://eth.blockscout.com/tx/0xc83a124ae29dbf37ff06c66a5cb539d48fcc5a814910010884a5f2a4296615ef
- rOUSG redeem TX: https://eth.blockscout.com/tx/0x247c8104628121cbfaaadcc4d1bb4070264abc7b2f83ec7530992c728b868904
- USDY subscribe TX: https://eth.blockscout.com/tx/0x55d884a2f2e18cd66290cd65afdd09558f5a880f3d4a3203ce074a615ecdd7ee
- USDY redeem TX: https://eth.blockscout.com/tx/0x5113f5dbf77a8fb4ae305569001bd3b3e1ef9598e4b3727fd90b0ae5b1cd8830
