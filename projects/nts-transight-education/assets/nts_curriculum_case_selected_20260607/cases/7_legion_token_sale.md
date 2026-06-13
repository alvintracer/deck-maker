# 7. Legion Token Sale Case

## 목적

Token sale 참여를 통해 `투자금 납입 -> allocation -> vesting/unlock -> claim -> 처분 후보` 흐름을 보여준다.

Airdrop과의 차이는 명확하다. Airdrop은 선행 지급대가가 희미하거나 별도 활동 보상 성격이 강한 반면, token sale은 온체인에서 USDC/USDT 등 투자금 납입이 먼저 확인된다. 따라서 수령 token만 보는 것이 아니라 `투자금`, `배정`, `vesting`, `claim`, `처분`을 분리해서 봐야 한다.

## 메인 Case

```text
Case
Fuel Network FUEL sale on Legion

Transight search network / chain
Ethereum Mainnet

Status
부분 채택: token sale claim/swap 교육용. off-ramp까지 이어지는 seed는 교체 필요
```

Fuel은 공식 글에서 FUEL을 Ethereum Mainnet ERC-20로 설명하고, community expansion effort를 Legion, Impossible Finance, Bitget과 함께 진행한다고 밝혔다. Legion 공식 문서상 pre-liquid sale은 투자금 납입, allocation 처리, refund, raised capital withdrawal, token distribution/vesting 흐름으로 구성된다.

이 문서의 모든 주요 TX와 주소는 `Ethereum Mainnet`에서 검색한다.

## 핵심 질문

```text
이 주소는 token sale에 얼마를 납입했는가?
그 납입액이 어떤 token allocation으로 이어졌는가?
vesting이 있었는가, 아니면 즉시 claim 가능한 구조였는가?
claim 이후 swap 또는 deposit contract 전송이 있었는가?
```

## 경제적 이익 취득 방식

- USDC로 Legion sale contract에 투자금을 납입한다.
- sale contract가 investor별 allocation을 Merkle proof 기반으로 검증한다.
- 이 케이스는 vesting duration이 0으로 확인되어, 해당 public sale claim은 즉시 수령 구조로 본다.
- claim 후 FUEL을 USDT로 swap하고, USDT를 외부 deposit contract로 전송한다.
- 마지막 deposit contract 전송은 처분/플랫폼 입금 후보이지, fiat off-ramp 확정은 아니다.

## Seed

```text
Sale / Project
Fuel Network FUEL sale on Legion

Transight search network / chain
Ethereum Mainnet

Participant Wallet
0x09bB75b11B33D6DA0e43854A135cF45c8ed9444e

Legion Sale Contract
0x97802F38A37E1D789eba194513E3Eb7E918d34Df

FUEL Token
0x675B68AA4d9c2d3BB3F0397048e62E6B7192079c

USDC Token
0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48

USDT Token
0xdAC17F958D2ee523a2206206994597C13D831ec7

Deposit TX
0x1646dfd3770210e7ffa8cd0f58d6d734feb1388d199358d6a3c4090eaaf042a7

Claim TX
0x906fe7a831908f0798b65212abf13e5b74c1848ac7900ebc8d39b63a604f08ea

Secondary Sale / Swap TX
0x2d9836353bf263b2e9447a2c232f8aede1e5eefa34d7b73d846b69836e1e4f38

Post-swap Deposit Contract TX
0x30ce909663f7fb7f4851496f897116250d339c3fcd5a4bf9848450998efa79ad
```

## 예상 Flow

```text
0x09bB...9444e
  -> Legion sale contract에 250 USDC 납입
  -> Merkle proof 기반 allocation 확정
  -> vesting 없음 / 100% claim 가능 구조
  -> 12,500 FUEL claim
  -> MetaSwap 진입 / 1inch route (FUEL -> WETH -> USDT 2-hop)로 FUEL 전량 swap
  -> gross 217.217763 USDT 중 fee 1.902444 USDT 차감, net 215.315319 USDT 수령
  -> DVFDepositContract로 215.315273 USDT deposit
```

## 단계별 해석

### 1. Deposit / 투자금 납입

```text
Transight search network / chain
Ethereum Mainnet

Wallet
0x09bB75b11B33D6DA0e43854A135cF45c8ed9444e

TX
0x1646dfd3770210e7ffa8cd0f58d6d734feb1388d199358d6a3c4090eaaf042a7

Method
invest(uint256 amount, uint256 saftInvestAmount, uint256 tokenAllocationRate, bytes32 saftHash, bytes32[] proof)

Token Movement
250 USDC
from 0x09bB...9444e
to   0x9780...34Df
```

해석: 해당 주소가 Legion sale contract에 USDC를 납입한 투자금 납입 단계다. 이 단계만으로 token 수령이 확정되는 것은 아니고, allocation/claim 단계와 연결해야 한다.

### 2. Allocation / 배정

```text
Transight search network / chain
Ethereum Mainnet

Allocation 확인 방식
claimAskTokenAllocation(bytes32[] proof)
```

이 케이스에서 개별 allocation은 별도 dashboard 화면이 아니라 claim TX의 Merkle proof와 실제 FUEL transfer로 확인한다.

투자금 250 USDC가 claim 단계에서 12,500 FUEL 수령으로 이어진다. 단순 계산상 250 / 12,500 = 0.02 USDC per FUEL이다. 다만 allocation이 어떤 심사/계정 기준으로 확정되었는지는 온체인만으로는 확정하지 않는다.

### 3. Vesting / Unlock

```text
Transight search network / chain
Ethereum Mainnet

Sale creation TX
0x930f7498bee750e9132559e9aa9d607e40c322a9184f111877e31e91ae370b69

Legion PreLiquidSale config
vestingDurationSeconds = 0
vestingCliffDurationSeconds = 0
tokenAllocationOnTGERate = 100%
```

> 주의: 이 sale creation TX의 top-level method는 `createPreLiquidSale`가 아니라 `LegionAccessControl`을 경유한 `functionCall(address target, bytes data)`로 보인다. `createPreLiquidSale` 호출과 위 vesting config는 그 내부 calldata에 들어 있으므로, Transight에서 method 이름만으로 검색하면 안 잡힐 수 있다. decoded input 또는 internal call까지 펼쳐서 확인한다.

해석: 이 participant case는 vesting contract로 장기 release되는 구조가 아니라, claim 시점에 전량 수령되는 구조로 본다. Legion protocol 자체는 vesting release 기능을 지원하지만, 이 FUEL sale seed에서는 vesting release TX를 핵심 흐름으로 쓰지 않는다.

### 4. Claim / Token 수령

```text
Transight search network / chain
Ethereum Mainnet

TX
0x906fe7a831908f0798b65212abf13e5b74c1848ac7900ebc8d39b63a604f08ea

Method
claimAskTokenAllocation(bytes32[] proof)

Token Movement
12,500 FUEL
from 0x9780...34Df
to   0x09bB...9444e
```

해석: 이 지점에서 token sale 참여자가 실제 경제적 이익의 대상인 FUEL을 수령한다. 세무상 취득가액/취득시점/처분시점 논의는 법적 판단이 필요하므로, 강의에서는 온체인 사실관계까지만 분리한다.

> 참고: 이 claim TX에는 sale contract에서 wallet으로 가는 12,500 FUEL transfer 외에, 별도 주소(`0x15E9E260...`)로 가는 `0 FUEL`(0 value) ERC-20 transfer log가 함께 잡힌다. 실제 수령 수량은 12,500 FUEL이며, 0-value log는 참여자 수령액에 영향을 주지 않는다.

### 5. Secondary Sale / Swap

```text
Transight search network / chain
Ethereum Mainnet

TX
0x2d9836353bf263b2e9447a2c232f8aede1e5eefa34d7b73d846b69836e1e4f38

From
0x09bB75b11B33D6DA0e43854A135cF45c8ed9444e

To
0x881D40237659C251811CEC9c364ef91dC08D300C

To Label
MetaSwap

Route Labels
0x74de5d4FCbf63E00296fd95d33236B9794016631 = Spender (1inch)
0xC7eC87AEB9D1129C42123859220C525aBa1ca617 = UniswapV3Pool (FUEL/WETH)
0xc7bBeC68d12a0d1830360F8Ec58fA599bA1b0e9b = UniswapV3Pool (WETH/USDT)
0x1111111254EEB25477B68fb85Ed929f73A960582 = AggregationRouterV5

Token Movement (사용자 관점 요약)
12,500 FUEL out
215.315319 USDT in
```

> 흐름 주의: 이 swap은 FUEL/USDT 직접 pool 단일 hop이 아니라 `FUEL -> WETH -> USDT` 2-hop으로 라우팅된다. 실제 transfer path는 다음과 같다. ① 12,500 FUEL이 `wallet -> Spender(0x74de...) -> UniswapV3Pool(FUEL/WETH, 0xC7eC...)`로 이동하고, ② 그 pool이 0.07932591 WETH를 `AggregationRouterV5(0x1111...)`로 보내며, ③ WETH가 두 번째 UniswapV3Pool(WETH/USDT, 0xc7bB...)에서 USDT로 교환된다. 두 번째 pool이 내보낸 gross 금액은 **217.217763 USDT**이고, 이 중 **1.902444 USDT**가 swap fee로 1inch fee 수취 주소(GnosisSafe `0x2aCf35C9...`)에 차감된 뒤, **순액 215.315319 USDT**가 wallet으로 들어온다. 즉 doc의 `12,500 FUEL -> 215.315319 USDT`는 순액(net) 표기이며, WETH 경유 hop과 gross/fee는 보조 주소를 함께 봐야 드러난다. (2026-06-01 온체인 확인)

해석: claim 받은 FUEL 전량이 swap되어 USDT를 수령한다. 이 단계는 처분 후보로 볼 수 있다. 정확한 세무상 처분금액은 가격, 수수료, 집계 기준을 별도로 확인해야 한다. 특히 gross 217.217763 USDT와 net 215.315319 USDT 중 어느 쪽을 처분가액으로 볼지, swap fee 1.902444 USDT를 비용으로 인정할지는 별도 판단이 필요하다.

### 6. Post-swap Deposit Contract

```text
Transight search network / chain
Ethereum Mainnet

TX
0x30ce909663f7fb7f4851496f897116250d339c3fcd5a4bf9848450998efa79ad

Method
depositWithId(address token, uint256 amount, uint256 commitmentId)

To
0xBCA3039a18c0d2f2F84BA8a028c67290bc045AFa

To Label
TransparentUpgradeableProxy / DVFDepositContract

Token Movement
215.315273 USDT
from 0x09bB...9444e
to   0xBCA3...5AFa
```

해석: swap으로 받은 USDT 대부분이 deposit contract로 이동한다. 이는 platform deposit 후보로 볼 수 있지만, CEX 매도나 fiat off-ramp 확정은 아니다. 플랫폼 내부 계정, 매도 여부, 원화/법정화폐 환전 여부는 추가자료가 필요하다.

## 7.1 보조 사례: 투명 브릿지(Relay.link)로 끝까지 따라가지는 cross-chain 이동

메인 흐름의 6단계(rhino.fi/DVF)는 프라이버시형 브릿지라 목적지 추적이 끊긴다(아래 7.2 참조). 대조군으로, 같은 FUEL sale 참여자 중 **투명 브릿지(Relay.link)**를 쓴 cross-chain 이동을 둔다. 투명 브릿지는 source와 destination이 공개 API로 1:1 연결되어, 제3자도 목적지 체인 tx·수취인·금액을 확정할 수 있다.

### Seed

```text
Transight search network / chain
Arbitrum One (source) / Ethereum Mainnet (destination)

Participant Wallet (FUEL sale claimer)
0x54Bc2fd9E260CF69577Ea4820dC3F03FF9696E01

FUEL Claim TX (Ethereum Mainnet)
0xc3f2b49381cf433af62134cb9b5b44cceb448452b9894e98ac16cae6834fe834
-> 100,000 FUEL 수령

Bridge source TX (Arbitrum One)
0x332b14b19216bc282b8af7d6ae00457fa0de488aa9c9605c5bd0fd61b1297146
2025-04-04 13:50:24 UTC, method swapAndStartBridgeTokensViaRelay (LI.FI Diamond 0x1231DEB6...)
-> 5,006.535592 USDC가 Relay route로 진입

Bridge destination TX (Ethereum Mainnet)
0x6ab29d051c4c68264c139d83eef006e7328c4fc467d4f52d32c583136e997f03
-> 5,005.646105 USDC -> 0x54Bc2fd9E260... (동일 수취인, 온체인 확인)

Relay request id
0xb5e31ca0d3091054022668497b0988e348aaaef085e0fe89ab0786abe31a2004
```

### 추적 방법 (핵심)

Relay는 공개 API로 source↔destination을 연결해준다. 인증·commitmentId 없이 누구나 조회 가능하다.

```text
GET https://api.relay.link/requests/v2?user=0x54Bc2fd9E260CF69577Ea4820dC3F03FF9696E01
-> status:    success
-> recipient: 0x54Bc2fd9E260...
-> inTxs:     Arbitrum One 0x332b14b1...   (소스)
-> outTxs:    Ethereum     0x6ab29d05...   (목적지)
```

즉 소스 tx → request id → 목적지 tx·수취인·금액·fee를 공개 데이터만으로 확정한다. (이 케이스는 Legion 앱의 LI.FI 통합 경유로 라우팅됐고, source tx decoded calldata에 `legion-lifi-integration` 태그가 들어 있다.)

### 메인 case와의 대조 (브릿지 유형 분류)

| 구분 | rhino.fi/DVF (메인 6단계) | Relay.link (이 7.1) |
|---|---|---|
| 유형 | 프라이버시형 / custodial-break | 투명 브릿지 |
| source↔destination 온체인 링크 | 없음 (`commitmentId` ≠ 목적지 `withdrawalId`, off-chain 매핑) | 있음 (request id로 공개 조회) |
| 제3자 추적 | 불가 (rhino.fi VASP 자료요청 필요) | 가능 (공개 API로 목적지 확정) |
| 세무조사 다음 단계 | 플랫폼/계정 자료 요청 | 목적지 체인에서 바로 이어서 추적 |

### 주의점 / 판단

- 이 Relay 브릿지(2025-04-04)를 FUEL claim/처분 대금과 동일 자금이라고 단정하지 않는다. 같은 참여자의 별도 cross-chain 이동이며, 자금 귀속은 balance reconciliation이 필요하다. **이 seed의 교육 포인트는 자금 귀속이 아니라 "브릿지 유형에 따라 추적 가능성이 갈린다"는 점이다.**
- 수취인이 동일 지갑임은 목적지 tx에서 확인된다(USDC 5,005.646105 -> 0x54Bc...).
- 투명 브릿지라도 목적지 수령 이후의 최종 처분/off-ramp는 목적지 체인에서 별도로 이어 추적한다.

### 국세청 시사점

- "브릿지를 거쳤으니 추적 불가"는 틀린 전제다. 먼저 **브릿지 유형을 식별**해야 한다.
  - 투명 브릿지(Relay/Across/Stargate 등): 공개 데이터로 목적지 확정 가능 → 바로 이어서 추적.
  - 프라이버시형/custodial-break(rhino.fi 등): 온체인 단절, 플랫폼(VASP) 자료요청 필요.
  - 비수탁 믹서(Tornado 등): 암호학적 단절, 통계·제재 라벨로 접근.

### Source Links (7.1)

- Relay status API: https://api.relay.link/requests/v2?user=0x54Bc2fd9E260CF69577Ea4820dC3F03FF9696E01
- FUEL claim TX: https://eth.blockscout.com/tx/0xc3f2b49381cf433af62134cb9b5b44cceb448452b9894e98ac16cae6834fe834
- Bridge source (Arbitrum One): https://arbitrum.blockscout.com/tx/0x332b14b19216bc282b8af7d6ae00457fa0de488aa9c9605c5bd0fd61b1297146
- Bridge destination (Ethereum): https://eth.blockscout.com/tx/0x6ab29d051c4c68264c139d83eef006e7328c4fc467d4f52d32c583136e997f03

## 7.2 대체 Seed 검토

### 결론

FUEL/Legion 안에서 `claim -> bridge -> CEX/off-ramp`까지 강의 중에 자신 있게 따라갈 수 있는 seed는 아직 비채택한다.

이 케이스는 `투자금 납입 -> allocation -> claim -> DEX 처분 후보`를 설명하는 데는 쓸 수 있다. 다만 국세청 강의에서 "처분대금이 어디로 갔는가"까지 보여주려면 마지막 구간이 끊긴다. 특히 Rhino.fi/DVF deposit은 source chain tx만으로 destination chain/recipient/withdraw tx가 확정되지 않고, Rhino history API 권한이 필요하다.

2026-06-04 추가 스캔 결과:

- FUEL sale contract `0x9780...34Df`의 FUEL transfer 로그에서 claim recipient 613개를 재확인했다. 이는 Blockscout token-transfer 25페이지 기준이며, 교육 seed 탐색용 표본이다.
- 해당 recipient의 Relay request 145건을 확인했지만, destination recipient가 eth-labels 기준 CEX로 라벨링되는 건은 0건이었다.
- 같은 표본에서 LI.FI `analytics/transfers`는 1건만 잡혔고 CEX destination hit는 0건이었다.
- Socket bridge activity와 deBridge/DLN orders는 해당 표본에서 0건이었다.
- 일부 Relay request에서 `Binance` 문자열이 보이는 경우가 있었지만, 대부분 BSC native asset명 `Binance Coin` 또는 `jumper.exchange` 같은 route/app 문자열에서 나온 false positive였다. CEX 판단은 문자열 검색이 아니라 destination recipient 주소 라벨 또는 deposit/sweep 패턴으로 해야 한다.
- Relay destination이 Ethereum인 flow는 일부 있었지만, 공개 라벨 기준 destination 자체가 CEX인 케이스는 없었다. destination 지갑 이후 CEX 입금까지 이어지는지는 별도 address-history 스캔이 필요하며, 현재까지 강의용으로 채택 가능한 clean seed는 확인하지 못했다.

### 후보 A: `0x7f1e...3EEE`

```text
Wallet
0x7f1e6ee54c539068e5E6A6bB73361E47fb2b3EEE

Claim TX
0x4ba8b324219d5ee2b59a4339d7cb50f046b5f90420cf076a8bc3f5c2685e62c3

Claim amount
100,000 FUEL

Swap TX
0x946e9710f20b761de7365cc4501e146884e13ad568b6de451baccfa868c31c98

Swap route
100,000 FUEL -> Uniswap V3 FUEL/WETH pool
0.079417253619512768 WETH -> UniversalRouter
0.000198543134048781 WETH -> FeeCollector
0.079218710485463987 WETH unwrap/burn

Post-swap ETH transfer
0xde64ddc285659664f75e616470ec7ee6eff48893d60dec8e214a2c5062c711ca
0.097660115001620737 ETH -> 0x6908Cc437c8BEA5c19A81e487A1528635EC2b197
```

비채택 사유: claim 직후 swap은 매우 선명하다. 하지만 ETH 수취 주소 `0x6908...b197` 주변에 유사 prefix/suffix 주소와 0-value/fake token transfer가 많아 address-poisoning 또는 노이즈 가능성이 있다. CEX deposit 또는 fiat off-ramp로 확정할 수 없으므로 교육용 off-ramp seed로 쓰기 어렵다.

### 후보 B: `0xdb2046...5587`

```text
Wallet
0xdB20465F12ecaa54a60E8375f90b63Aa73595587

Claim TX
0x3970a6aadd5478f770ec1765ecfa0bd2fd395c42eaaccf93a6e9c1b506d73300

Claim amount
50,000 FUEL

FUEL transfer after claim
0x7fff96c1fabddad24a923a45b1651bf0743f49e3ba03a0dfbd840205168fac52
50,000 FUEL -> 0xa2882269347a0113D89A2C42A6563F5159572fF3

Later CEX-like deposit pattern
0x41b143de6b8da87d5f8fe440818814024621584160065d1659b495f98de49c14
4,000 USDC -> 0x1939B61024389e9f0215ae25E94AfAa8d4Adc523

Deposit address sweep
0x67720e7b6f05b026a98828439e499c467f1bbd0aab233d3ec847f700130e85af
4,000 USDC -> 0x9642b23Ed1E01Df1092B92641051881a322F5D4E
```

비채택 사유: `0x1939... -> 0x9642...` 구간은 CEX deposit/sweep 패턴으로 보기 좋다. 그러나 이 4,000 USDC는 FUEL claim proceeds와 직접 연결되지 않는다. FUEL은 claim 다음 날 `0xa288...`로 이동했고, 2025-10-03의 4,000 USDC 출금은 다른 Legion sale refund/투자금 회수 흐름과 섞여 있다. 따라서 "FUEL 처분대금의 off-ramp" 예시로 쓰면 오해 소지가 크다.

### 7.2 운영 판단

- FUEL/Legion은 `token sale과 airdrop의 차이`, `선행 USDC 납입`, `Merkle proof claim`, `DEX 처분` 설명에는 적합하다.
- 그러나 `처분대금이 CEX/off-ramp로 이동하는 장면`까지 한 번에 보여주기에는 적합하지 않다.
- 강의에서 follow-through가 중요하면 7번은 token sale acquisition/claim/swap 케이스로만 쓰고, off-ramp는 별도 케이스에서 보여주는 편이 낫다.
- `7.2`로 새 seed를 찾을 때는 sale token 처분 직후 stablecoin 또는 ETH가 labeled CEX deposit/hot wallet로 들어가는 케이스를 우선한다.

## Evidence Table

| 단계 | Chain | TX / Address | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 0 | Ethereum Mainnet | `0x930f7498bee750e9132559e9aa9d607e40c322a9184f111877e31e91ae370b69` | Legion sale contract 생성 | sale setup | top-level method는 `LegionAccessControl` 경유 `functionCall`, 내부에 `createPreLiquidSale` + vesting config. bid token USDC |
| 0 | Ethereum Mainnet | `0x97802F38A37E1D789eba194513E3Eb7E918d34Df` | FUEL Legion sale contract | sale contract | Transight에서 sale hub로 검색 |
| 0 | Ethereum Mainnet | `0x675B68AA4d9c2d3BB3F0397048e62E6B7192079c` | FUEL ERC-20 | sold token | symbol `FUEL`, decimals 9 |
| 1 | Ethereum Mainnet | `0x1646dfd3770210e7ffa8cd0f58d6d734feb1388d199358d6a3c4090eaaf042a7` | 250 USDC -> sale contract | deposit / 투자금 납입 | 선행 투자금 확인 |
| 2 | Ethereum Mainnet | `0x906fe7a831908f0798b65212abf13e5b74c1848ac7900ebc8d39b63a604f08ea` | `claimAskTokenAllocation` + Merkle proof | allocation / claim | allocation 산정근거 자체는 off-chain 가능 |
| 3 | Ethereum Mainnet | `0x930f7498bee750e9132559e9aa9d607e40c322a9184f111877e31e91ae370b69` | vesting duration 0, cliff 0, TGE rate 100% | vesting / unlock | 이 seed는 즉시 claim 구조 |
| 4 | Ethereum Mainnet | `0x906fe7a831908f0798b65212abf13e5b74c1848ac7900ebc8d39b63a604f08ea` | 12,500 FUEL 수령 | token claim | 실제 token 취득 확인 |
| 5 | Ethereum Mainnet | `0x2d9836353bf263b2e9447a2c232f8aede1e5eefa34d7b73d846b69836e1e4f38` | 12,500 FUEL -> 215.315319 USDT (net) | secondary sale / swap 후보 | MetaSwap 진입, 1inch route. 실제 `FUEL->WETH->USDT` 2-hop. gross 217.217763 USDT, fee 1.902444 USDT 차감 |
| 6 | Ethereum Mainnet | `0x30ce909663f7fb7f4851496f897116250d339c3fcd5a4bf9848450998efa79ad` | 215.315273 USDT -> DVFDepositContract | deposit 후보 | fiat off-ramp 확정 아님 |
| 보조 주소 | Ethereum Mainnet | `0x881D40237659C251811CEC9c364ef91dC08D300C` | swap TX `to` / explorer label | swap entry | MetaSwap (`swap(string aggregatorId,...)` 진입점) |
| 보조 주소 | Ethereum Mainnet | `0x74de5d4FCbf63E00296fd95d33236B9794016631` | swap TX token transfer / explorer label | 1inch Spender | FUEL 수취 + net USDT 정산 주소 |
| 보조 주소 | Ethereum Mainnet | `0xC7eC87AEB9D1129C42123859220C525aBa1ca617` | swap TX token transfer / explorer label | UniswapV3Pool (FUEL/WETH) | 1-hop: FUEL -> WETH |
| 보조 주소 | Ethereum Mainnet | `0xc7bBeC68d12a0d1830360F8Ec58fA599bA1b0e9b` | swap TX token transfer / explorer label | UniswapV3Pool (WETH/USDT) | 2-hop: WETH -> USDT, gross 217.217763 USDT |
| 보조 주소 | Ethereum Mainnet | `0x2aCf35C9A3F4c5C3F4c78EF5Fb64c3EE82f07c45` | swap TX token transfer / explorer label | 1inch fee 수취 (GnosisSafe) | swap fee 1.902444 USDT 차감 |

## Transight 확인 포인트

- `Ethereum Mainnet`에서 participant wallet `0x09bB...9444e` 검색
- sale contract `0x9780...34Df`와의 `invest` TX 확인
- `USDC -> sale contract` transfer를 투자금 납입으로 분류
- `claimAskTokenAllocation` TX에서 Merkle proof 기반 claim과 FUEL transfer 확인
- vesting이 있는지 sale config와 token transfer 구조를 분리해서 확인
- claim 이후 FUEL 전량 swap route 확인
- USDT deposit contract 이동을 처분 이후 자금 이동 후보로 분류

## 강의 포인트

- Token sale은 airdrop보다 `취득 원가` 질문이 먼저 나온다.
- 같은 token claim이라도 `airdrop claim`과 `sale allocation claim`은 경제적 실질이 다르다.
- allocation은 온체인 proof로 claim 가능 여부를 확인할 수 있지만, 왜 그만큼 배정되었는지는 off-chain 계정/KYC/심사 자료가 필요할 수 있다.
- vesting이 있으면 `allocation`, `claim 가능 수량`, `실제 release`가 모두 다를 수 있다.
- swap은 처분 후보로 볼 수 있으나, 세무상 확정 처분가액은 수수료와 가격 산정 기준을 별도로 정해야 한다.
- deposit contract 전송은 platform 입금 후보일 뿐, 법정화폐 off-ramp 확정은 아니다.

## 국세청 추가 요청자료

- Legion/Fuel sale 참여 약관
- participant의 Legion 계정, KYC, allocation dashboard 자료
- 투자금 출처와 USDC 취득 내역
- allocation 확정 통지 또는 sale result 자료
- claim dashboard 캡처
- swap 당시 가격, 수수료, route 자료
- DVF 또는 관련 플랫폼 내부 입금/매도/출금 자료

## 주의점

- 이 사례에서 `FUEL claim = 무상수령`으로 표현하면 안 된다. 선행 USDC 납입이 확인된다.
- claim TX만 보면 airdrop처럼 보일 수 있으므로 반드시 deposit TX와 연결해야 한다.
- allocation 산정 기준은 온체인만으로 확정하지 않는다.
- vesting이 없는 seed지만, Legion protocol 자체에는 vesting/release 기능이 있으므로 다른 sale에 일반화하지 않는다.
- DVFDepositContract 전송은 platform deposit 후보이며, CEX 매도 또는 fiat off-ramp 확정 표현은 피한다.

## 출처 링크

- Legion official docs: https://legion-1.gitbook.io/legion
- Legion Pre-Liquid Open Application Sale docs: https://legion-1.gitbook.io/legion/smart-contracts/pre-liquid-open-application-sale/
- Legion website: https://legion.cc/
- Fuel official post: https://paragraph.com/@fuel-labs-2/fuel-genesis-is-coming
- Ethereum Blockscout sale contract: https://eth.blockscout.com/address/0x97802F38A37E1D789eba194513E3Eb7E918d34Df
- Ethereum Blockscout participant wallet: https://eth.blockscout.com/address/0x09bB75b11B33D6DA0e43854A135cF45c8ed9444e
- Deposit TX: https://eth.blockscout.com/tx/0x1646dfd3770210e7ffa8cd0f58d6d734feb1388d199358d6a3c4090eaaf042a7
- Claim TX: https://eth.blockscout.com/tx/0x906fe7a831908f0798b65212abf13e5b74c1848ac7900ebc8d39b63a604f08ea
- Swap TX: https://eth.blockscout.com/tx/0x2d9836353bf263b2e9447a2c232f8aede1e5eefa34d7b73d846b69836e1e4f38
- Deposit contract TX: https://eth.blockscout.com/tx/0x30ce909663f7fb7f4851496f897116250d339c3fcd5a4bf9848450998efa79ad
- MetaSwap entry: https://eth.blockscout.com/address/0x881D40237659C251811CEC9c364ef91dC08D300C
- 1inch Spender: https://eth.blockscout.com/address/0x74de5d4FCbf63E00296fd95d33236B9794016631
- 1inch AggregationRouterV5: https://eth.blockscout.com/address/0x1111111254EEB25477B68fb85Ed929f73A960582
- FUEL/WETH Uniswap V3 pool: https://eth.blockscout.com/address/0xC7eC87AEB9D1129C42123859220C525aBa1ca617
- WETH/USDT Uniswap V3 pool: https://eth.blockscout.com/address/0xc7bBeC68d12a0d1830360F8Ec58fA599bA1b0e9b
- 1inch fee 수취 주소: https://eth.blockscout.com/address/0x2aCf35C9A3F4c5C3F4c78EF5Fb64c3EE82f07c45
- DVFDepositContract: https://eth.blockscout.com/address/0xBCA3039a18c0d2f2F84BA8a028c67290bc045AFa
