# 10. Polymarket Prediction Market Case

## 목적

Polymarket prediction market에서 `USDC.e`가 CTF outcome position으로 바뀌고, 시장 종료 후 winning position redeem 또는 중도 매도 시 손익 후보가 생기는 구조를 국세청 교육용 케이스로 설명한다.

이 케이스의 핵심은 "베팅 사이트" 설명이 아니라, 온체인에서 다음 흐름을 재현하는 것이다.

```text
Polygon PoS USDC.e
  -> Polymarket proxy wallet
  -> Polymarket CTF Exchange에서 outcome token 매수
  -> market resolution 후 Conditional Tokens에서 USDC.e redeem
  -> 외부/집금 주소로 USDC.e 이동
```

## 핵심 질문

```text
예측시장에 들어간 USDC.e가 어떤 outcome token position으로 바뀌었고,
position 매도 또는 redeem 시 얼마의 USDC.e가 돌아왔으며,
그 차액을 세무상 경제적 이익 취득 후보로 볼 수 있는가?
```

## 강의 스토리

1. 사용자는 Polymarket의 선거 예측시장에 참여한다.
2. Polymarket 계정은 EOA가 아니라 proxy wallet을 통해 거래한다. 사용자는 proxy wallet에 USDC.e를 두고, relayer/relay hub를 통해 gasless 거래를 실행할 수 있다. 따라서 buy/redeem/outgoing tx의 `to`는 proxy wallet이 아니라 Polymarket relayer hub 컨트랙트이며, USDC.e/CTF 토큰의 실제 이동은 그 relayer가 호출하는 내부 호출(internal call)에서 발생한다. tx sender(EOA)도 relayer 운영자이고 proxy wallet 소유자가 아니다.
3. 시장 포지션 매수 시 `USDC.e`가 `Polymarket: CTF Exchange`로 이동하고, 반대 방향으로 ERC-1155 CTF outcome token이 proxy wallet으로 이동한다.
4. 시장이 종료되면 winning outcome token은 Conditional Tokens contract에서 USDC.e로 redeem된다.
5. redeem된 USDC.e가 외부 주소로 이동하면 출금, 집금, OTC, CEX deposit 후보로 분류한다. 다만 수령 주소의 실소유자와 거래소 귀속은 별도 자료로 확인해야 한다.

## 실제 온체인 Seed

### Transight search network / chain

모든 seed는 아래 네트워크로 검색한다.

```text
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)
```

Polymarket legacy USDC.e/CTF 흐름은 Polygon PoS의 `USD Coin (PoS) (USDC.e)`와 `Conditional Tokens (CTF)` ERC-1155 이벤트를 우선 확인한다. 2026년 현재 문서의 V2/pUSD 주소와 2024년 seed의 legacy USDC.e 주소가 다를 수 있으므로, 교육 시점의 market/tx 날짜를 기준으로 주소를 고정해서 설명한다.

### Market

```text
Market page
https://polymarket.com/event/which-party-will-win-the-2024-united-states-presidential-election

Market title
Which party wins 2024 US Presidential Election?

Condition ID
0x26ee82bee2493a302d21283cb578f7e2fff2dd15743854f53034d12420863b55

Resolution rule source shown on market page
National Archives Electoral College results, whitehouse.gov, FEC, and other official/judicial announcements

Transight search network / chain
Polygon / Polygon PoS mainnet (chainId 137)
```

### Wallet / contracts

```text
Trader proxy wallet
0x1F2DD6D473f3e824cd2f8A89d9c69fb96F6aD0CF
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)

USDC.e token
0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)

Polymarket legacy CTF Exchange
0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)

Conditional Tokens (CTF)
0x4D97DCd97eC945f40cF65F87097ACe5EA0476045
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)

Post-redeem USDC.e receiver / collector candidate
0xD36ec33c8bed5a9F7B6630855f1533455b98a418
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)
```

### Transaction seeds

```text
USDC.e inbound / deposit-like top-up TX
0x9103fdf267b77c358dfce213a4ac1f0e9814f3f9ad65d4ef8722dc64a182c442
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)

Position buy TX
0x1606d29d17ac3cb59670850cc95a24bead25f2bfb753f3c5c2d2419b9a40a22c
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)

Redeem TX
0xa4ab20b26fd09e9a2962073d6d10960e20987dbad1b4c3fcb2ef347cb020955f
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)

Post-redeem USDC.e outgoing TX
0xa4cc9829660ec33aa65ef05a5a570cd2f3e76e04bb0943e8ea573aa2f57140a4
Transight search network / chain: Polygon / Polygon PoS mainnet (chainId 137)
```

## 온체인 Flow

```text
0x6545...e7F6 external funding/source candidate
  -> 0x1F2D...D0CF proxy wallet
     USDC.e inbound: 10 USDC.e
     참고: 선택 매수 lot의 직접 재원으로 단정하지 않고, 같은 proxy wallet의 USDC.e 입금/잔고 형성 예시로 사용

0x1F2D...D0CF proxy wallet
  -> 0x4bFb...982E Polymarket CTF Exchange
     (tx.to = relayer hub 0x56c7...e113, gasless; 토큰 이동은 internal call)
     USDC.e spend: 4,783.5776 USDC.e (이 buy tx의 총 fill은 7,047.38 USDC.e, proxy 몫만 4,783.5776)
     CTF ERC-1155 outcome token receive: token id 0x90b0...b630, 7,474.34 unit -> proxy wallet

market resolved

0x1F2D...D0CF proxy wallet
  -> 0x4D97...76045 Conditional Tokens
     (tx.to = relayer hub 0xd216...f494, gasless; 토큰 이동은 internal call)
     winning ERC-1155 outcome token redeem: token id 0x90b0...b630 burn
     USDC.e receive: 76,393.256739 USDC.e
     주의: 선택 buy tx의 수령량 7,474.34 unit보다 redeem 수령액이 훨씬 크므로,
     이 redeem은 같은 token id의 기존 보유분/여러 lot까지 포함한 현재 잔고 정산 후보로 본다.
     선택 buy tx 하나의 손익으로 단정하지 않는다.

0x1F2D...D0CF proxy wallet
  -> 0xD36e...a418 external/collector candidate
     (tx.to = relayer hub 0xd216...f494, gasless; 토큰 이동은 internal call)
     USDC.e outgoing: 6,490,414.98722 USDC.e
     주의: outgoing 금액이 선택 redeem 수령액 76,393.256739 USDC.e보다 훨씬 크므로,
     이 전송은 wallet-level 집금/treasury movement 후보이지 선택 redeem 수령액의 직접 처분으로 단정하지 않는다.
```

## Evidence Table

| 단계 | Chain | TX / Address | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 1 | Polygon PoS mainnet (chainId 137) | Market page: `which-party-will-win-the-2024-united-states-presidential-election` | Polymarket market page shows title, rules, volume, end date, resolver, and official resolution sources. | 시장 식별 | https://polymarket.com/event/which-party-will-win-the-2024-united-states-presidential-election |
| 2 | Polygon PoS mainnet (chainId 137) | `0x1F2DD6D473f3e824cd2f8A89d9c69fb96F6aD0CF` | PolygonScan identifies the address as a `ProxyWallet`; token transfer page shows USDC.e, pUSD, and CTF-related flows. | Polymarket proxy wallet | https://polygonscan.com/address/0x1f2dd6d473f3e824cd2f8a89d9c69fb96f6ad0cf |
| 3 | Polygon PoS mainnet (chainId 137) | `0x9103fdf267b77c358dfce213a4ac1f0e9814f3f9ad65d4ef8722dc64a182c442` | PolygonScan transaction action: `Transfer 10 USDC.e to 0x1F2D...D0CF`; ERC-20 transfer from `0x6545...e7F6` to proxy wallet. | USDC.e 입금/잔고 형성 후보 | 선택 매수 lot의 직접 재원으로 단정하지 않는다. https://polygonscan.com/tx/0x9103fdf267b77c358dfce213a4ac1f0e9814f3f9ad65d4ef8722dc64a182c442 |
| 4 | Polygon PoS mainnet (chainId 137) | `0x1606d29d17ac3cb59670850cc95a24bead25f2bfb753f3c5c2d2419b9a40a22c` | JSON-RPC receipt status `0x1`. tx.to는 proxy wallet이 아니라 relayer hub `0x56c7...e113`(gasless). 같은 tx 안에서 ERC-20 transfer `0x1F2D...D0CF -> 0x4bFb...982E` USDC.e `4,783.5776`(여러 fill 중 proxy 몫)이 확인되고, ERC-1155 TransferSingle로 CTF token id `0x90b0...b630` `7,474.34 unit`이 `0x4bFb...982E -> 0x1F2D...D0CF`로 이동한다. | 포지션 매수 후보 | https://polygonscan.com/tx/0x1606d29d17ac3cb59670850cc95a24bead25f2bfb753f3c5c2d2419b9a40a22c |
| 5 | Polygon PoS mainnet (chainId 137) | `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E` | Polymarket archived CTF Exchange repository says CTF Exchange facilitates atomic swaps between CTF ERC-1155 assets and ERC-20 collateral, with Polygon deployment at this address. PolygonScan labels it `Polymarket: CTF Exchange`. | 거래소 컨트랙트 | https://github.com/Polymarket/ctf-exchange / https://polygonscan.com/address/0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e |
| 6 | Polygon PoS mainnet (chainId 137) | `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` | Polymarket docs explain outcomes are CTF ERC-1155 tokens; core operation includes redeeming winning tokens after resolution. | CTF / 정산 인프라 | https://docs.polymarket.com/trading/ctf/overview |
| 7 | Polygon PoS mainnet (chainId 137) | `0xa4ab20b26fd09e9a2962073d6d10960e20987dbad1b4c3fcb2ef347cb020955f` | JSON-RPC receipt status `0x1`. tx.to는 relayer hub `0xd216...f494`(gasless). ERC-1155 TransferSingle로 token id `0x90b0...b630`이 proxy wallet에서 zero-address로 burn되고, 동시에 ERC-20 transfer로 `Conditional Tokens 0x4D97...76045 -> 0x1F2D...D0CF` USDC.e `76,393.256739`이 확인된다. | redeem / 정산 수령 후보 | 같은 token id 연결은 유효하지만, 선택 buy tx 수령량보다 redeem 규모가 크므로 기존 보유분/여러 lot 포함 가능성을 명시. https://polygonscan.com/tx/0xa4ab20b26fd09e9a2962073d6d10960e20987dbad1b4c3fcb2ef347cb020955f |
| 8 | Polygon PoS mainnet (chainId 137) | `0xa4cc9829660ec33aa65ef05a5a570cd2f3e76e04bb0943e8ea573aa2f57140a4` | JSON-RPC receipt status `0x1`. tx.to는 relayer hub `0xd216...f494`(gasless). ERC-20 transfer로 `0x1F2D...D0CF -> 0xD36e...a418` USDC.e `6,490,414.98722`이 redeem 직후(같은 블록대) 확인된다. 수령 주소 `0xD36e...a418`은 EOA가 아니라 컨트랙트이다. | 출금/집금 후보 | outgoing 금액이 선택 redeem 수령액보다 훨씬 커서 wallet-level treasury movement 후보로 분류. Receiver의 실소유자, 컨트랙트 성격, 내부 대체거래 여부는 추가 확인 필요. https://polygonscan.com/tx/0xa4cc9829660ec33aa65ef05a5a570cd2f3e76e04bb0943e8ea573aa2f57140a4 |

## Transight 시연 포인트

1. `0x9103...c442`를 Polygon PoS에서 검색해 proxy wallet의 USDC.e inbound/top-up 이벤트를 확인한다.
2. `0x1606...a22c`를 Polygon PoS에서 검색한다. 이 tx의 `to`는 proxy wallet이 아니라 relayer hub `0x56c7...e113`이며, 실제 토큰 이동은 internal call/log에서 본다.
3. ERC-20 transfer에서 `0x1F2D...D0CF -> 0x4bFb...982E` USDC.e outflow `4,783.5776`을 확인한다. 같은 tx에 다른 trader의 fill도 섞여 있으므로 proxy wallet이 from/to인 transfer만 골라낸다.
4. 같은 tx의 ERC-1155 transfer에서 CTF token id `0x90b0...b630`(`7,474.34 unit`)가 `0x4bFb...982E -> 0x1F2D...D0CF`로 이동하는지 확인한다. (같은 tx의 다른 token id `0x185a...7438`은 반대편 outcome으로 다른 trader 몫이므로 혼동하지 않는다.)
5. `0xa4ab...955f`를 열어 CTF redeem tx로 전환한다. 이 tx의 `to`도 relayer hub `0xd216...f494`이다.
6. ERC-1155에서 token id `0x90b0...b630`이 proxy wallet에서 burn(zero-address)되고, USDC.e가 Conditional Tokens에서 proxy wallet으로 `76,393.256739` 돌아오는지 확인한다. 같은 token id가 buy와 redeem을 잇는 핵심 연결고리지만, 수량 차이 때문에 선택 buy tx 하나의 결과로 보지 않고 전체 position 잔고 정산 후보로 설명한다.
7. `0xa4cc...40a4`에서 정산 직후 큰 USDC.e가 외부/집금 후보 주소로 이동하는지 확인한다. 금액이 선택 redeem 수령액보다 훨씬 크므로 직접 off-ramp가 아니라 wallet-level 자금 이동 후보로 분류한다.
8. wallet timeline에서 같은 주소의 다른 redeem, merge, reward, transfer가 섞일 수 있으므로 market condition ID와 token ID로 필터링한다.

## 판단 후보

- `0x1606...a22c`의 `4,783.5776 USDC.e` 지출은 해당 market position 취득원가 후보로 볼 수 있다.
- `0x9103...c442`의 `10 USDC.e` 입금은 같은 proxy wallet의 USDC.e 입금/잔고 형성 seed이지만, 선택한 매수 tx의 직접 재원으로 확정하려면 직전 잔고와 전체 입출금 내역이 필요하다.
- `0xa4ab...955f`의 `76,393.256739 USDC.e` 수령은 market resolution 이후 winning position redeem 수령액 후보로 볼 수 있다. 다만 선택 buy tx의 수령량보다 크므로, 같은 token id의 기존 보유분/여러 lot이 포함된 redeem으로 보고 전체 lot 집계를 요구한다.
- 단일 매수 tx와 단일 redeem tx만으로 전체 손익을 확정하면 안 된다. 같은 condition에서 다수 buy/sell/merge/redeem이 존재할 수 있으므로 전체 lot 단위 집계가 필요하다.
- `0xa4cc...40a4`의 외부 송금은 출금/집금/오프램프 후보일 뿐이다. 특히 금액이 선택 redeem 수령액보다 훨씬 크므로, 이 TX를 선택 redeem 수령액의 직접 처분으로 연결하지 않는다. 거래소 입금 또는 원화 환전으로 확정하려면 수령 주소 라벨, 거래소 입금주소 매칭, 이용자 제출자료가 필요하다.
- 세무상 경제적 이익 취득 시점은 `매도 체결`, `redeem 수령`, `법정화폐 환전`, `권리 확정` 중 어떤 기준을 적용할지 법령/사실관계 검토가 필요하다.

## 국세청 추가 요청자료

- Polymarket 계정과 proxy wallet `0x1F2D...D0CF`의 귀속 입증 자료
- 해당 market의 전체 activity export: buy, sell, merge, split, redeem, reward
- condition ID와 CTF token ID별 잔고 변화
- USDC.e 입금 원천: CEX 출금 내역, bridge 내역, 외부 wallet 귀속 자료
- redeem 후 수령 USDC.e의 사용처: `0xD36e...a418` 귀속, CEX deposit memo/내부계정 매칭, 원화 환전 내역
- Polymarket 수수료, maker/taker rebate, reward 내역
- 환율 적용 기준과 수익 인식 시점에 대한 세무 검토 의견

## 주의점

- Polymarket은 2026년 현재 pUSD/V2 문서와 2024년 legacy USDC.e/CTF Exchange 흐름이 혼재한다. 이 케이스는 2024년 Polygon PoS USDC.e seed로 고정한다.
- Polymarket UI activity와 온체인 tx가 1:1로 단순 대응하지 않을 수 있다. 하나의 tx에 여러 fill, split/merge, maker/taker 상대방 token transfer가 섞일 수 있다.
- prediction market의 법적 성격은 관할과 시점별로 달라질 수 있다. 교육에서는 온체인 흐름과 경제적 이익 후보 추적에 집중하고, 도박/파생상품/기타소득 분류는 별도 법률 검토로 분리한다.
- Fredi9999 등 공개 프로필명은 교육용 식별자일 뿐 납세자 실명 또는 거주자성 판단 근거가 아니다.
- 손익은 특정 tx 한두 개가 아니라 같은 시장의 전체 position lifecycle로 계산해야 한다.

## 후보 B: 2026 Seoul Mayoral Election Winner

국내 교육 맥락에는 이 후보가 더 직관적이다. 한국 정치 이벤트라 수강자가 시장 내용을 바로 이해할 수 있고, 목표를 `Polymarket prediction market 참여 -> winning position redeem -> 국내 CEX 입금 후보`로 잡을 수 있다.

다만 2026년 seed는 위 2024년 대선 seed와 구조가 다르다. Polymarket V2/pUSD 구조가 적용되어 `USDC.e가 proxy wallet으로 바로 redeem`되는 단순 흐름이 아니라, `CTF outcome token -> NegRisk adapter -> pUSD/USDC.e 정산 라우팅 -> withdrawal/off-ramp` 구조로 보인다. 따라서 국내 CEX 끝점이 확인되기 전까지는 채택 상태를 `후보`로 둔다.

### Event / market

```text
Event page
https://polymarket.com/event/2026-seoul-mayoral-election-winner

Event title
2026 Seoul Mayoral Election Winner

Gamma API event id
79973

Status
closed / resolved
Polymarket page meta: event_update time 2026-06-04T07:00:01Z, winning outcome Yes

Event volume observed by Gamma API
52,157,070.68030086

Transight search network / chain
Polygon / Polygon PoS mainnet (chainId 137)
```

대표 market은 `Will Oh Se-hoon win the 2026 Seoul Mayoral Election`로 잡는다.

```text
Market id
678929

Condition ID
0xc587bda904f031a973ad3cb57128ca011bfab0f45e6cb3734ed2227c4d4be419

Outcome / token id
Yes: 0x323c46928932f17761025ebd2c0855d070e3e62226ae7ad77ec31b2f2c8179ba
No:  0x98d07fee4edfdef799aae3723059a902d553ce7a2192a3015ea8a1d7f969e61e

Gamma outcome price after resolution
Yes=1, No=0
```

참고: 이 event는 후보별 binary market 66개가 묶인 `negative risk` 이벤트다. 실제 winner market의 `Yes`뿐 아니라 다른 후보 market의 `No`도 winning position이 될 수 있다. 강의에서는 먼저 `Oh Se-hoon Yes` token만 좁혀서 보여주는 편이 안전하다.

### Selected teaching seed

서울시장 이벤트의 실제 시연 케이스는 `@blackhuman5` 공개 프로필 / proxy wallet `0xa89da419310851c4731f24370c25f1e040f9d0a2`로 잡는다.

```text
Selected case file
./10_polymarket_blackhuman5_case.md

Core flow
440.00 USDC-equivalent buy
  -> 10,000.00 redeem
  -> 12,054.00 Relay withdrawal from Polygon to BNB Chain
```

이 케이스는 손익 계산이 단순하고 Relay source/destination까지 연결된다. 다만 Relay destination recipient가 거래소 입금주소로 확정된 것은 아니므로, `off-ramp confirmed`가 아니라 `bridge/outflow candidate`로 설명한다.

### Confirmed redeem seed

```text
Polymarket proxy wallet
0x84571f1bf97a5c710cbe51daff2dd4556cc887fd

Public Polymarket profile metadata
name=ZhangMuZhi.., pseudonym=Tattered-Columnist
주의: 공개 프로필명일 뿐 실명/거주자성/납세자 식별 근거가 아니다.

Redeem TX
0x0c4028ceeb2525d3ff318b84179e0c03ecaa3efd2e4bb01d1e894200ee15159b

Block / time
87900944 / 2026-06-04 07:00:01 UTC

Polymarket activity API
type=REDEEM, title=Will Oh Se-hoon win the 2026 Seoul Mayoral Election,
size=188,777.09, usdcSize=188,777.09
```

전체 `Oh Se-hoon Yes` 정산 txid와 proxy wallet 목록은 별도 파일로 분리했다.

```text
Redeem tx list
./10_polymarket_seoul_redeems.md

Post-redeem outflow list
./10_polymarket_seoul_outflows.md

Scope
block 87900944 to 87954637
redeem rows 415
unknown proxy rows 0
```

온체인 로그상 흐름:

```text
0x8457...87fd proxy wallet
  -> 0xada2005600Dec949baf300f4C6120000bDB6eAab
     CTF TransferBatch

0xada200...eAab
  -> 0xd91e80cf2e7be2e162c6513ced06f1dd0da35296
     CTF TransferBatch

0xd91e80cf...5296 (Polymarket: Neg Risk Adapter)
  -> zero address
     CTF TransferSingle burn
     token id 0x323c...79ba
     amount 188,777.09

0x3a3bd7bb9528e159577f7c2e685cc81a765002e2
  -> 0xada200...eAab
  -> 0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB
  -> 0xc417fd8e9661c0d2120b64a04bb3278c17e99db1
     USDC.e 188,777.09 transfer path
```

해석:

- `0xd91e80cf...5296`는 Polygonscan 기준 `Polymarket: Neg Risk Adapter`로 라벨된다.
- `0xC011a7E...2DFB`는 Polymarket 공식 문서 기준 pUSD collateral token이다.
- `0xada200...eAab`는 Polymarket 공식 문서 기준 `NegRiskCtfCollateralAdapter`다.
- 이 seed는 서울시장 이벤트 winning position 정산을 보여주기 좋다.
- 하지만 `0xc417...9db1`은 개별 사용자 지갑이 아니라 대량 USDC.e outgoing이 발생하는 라우팅/정산 성격의 컨트랙트로 보인다. 첫 5,000 block 범위에서 이 주소의 USDC.e outgoing이 160,000건 이상 잡혔으므로, 이 주소를 그대로 따라가면 개별 납세자 흐름이 아니라 Polymarket 출금 인프라 전체를 보게 된다.

### Domestic CEX endpoint 탐색 상태

목표는 `redeem 후 국내 CEX deposit 후보`까지 잇는 것이다. 현재 공개 라벨 기준으로 확인한 국내 CEX 후보는 아래와 같다.

```text
Upbit: Hot Wallet / Deposit Address
0x4c569c1e541A19132AC893748E0ad54C7c989FF4
Source: PolygonScan / Blockscout label

Korbit 8
0xf0bc8FdDB1F358cEf470D63F96aE65B1D7914953
Source: Blockscout OLI label
```

현재까지의 판단:

- `Oh Se-hoon Yes` token burn/redeem 후보는 충분하다. 2026-06-04 07:00:01 UTC 이후 block `87900944`부터 `87954637`까지 RPC 로그 필터로 `Oh Se-hoon Yes` token burn 415건을 확인했다.
- 다만 `redeem -> domestic CEX`가 한 지갑에서 깔끔하게 이어지는 seed는 아직 채택하지 않았다.
- 최신 pUSD/withdrawal 구조에서는 `proxy wallet -> pUSD/USDC.e routing contract -> external wallet/deposit address`가 섞일 수 있어, 단순히 `redeem TX`의 마지막 USDC.e recipient만 따라가면 안 된다.
- 국내 CEX 입금은 `USDC.e`가 아니라 `POL` 입금일 가능성이 높다. 이 경우 `pUSD/USDC.e -> POL swap/bridge -> Upbit/Korbit hot wallet`까지 찾아야 한다.

### 다음 탐색 방법

1. `Oh Se-hoon Yes` token id `0x323c...79ba`의 burn tx 415건에서 Polymarket proxy wallet과 profile metadata를 수집한다.
2. 각 proxy wallet의 Polymarket activity에서 서울시장 event의 `TRADE`, `CONVERSION`, `REDEEM`을 묶는다.
3. redeem 직후의 withdrawal/off-ramp tx를 찾는다. Polymarket V2에서는 pUSD collateral token `0xC011...2DFB`, `CollateralOfframp`, `PermissionedRamp`, `NegRiskCtfCollateralAdapter`를 같이 봐야 한다.
4. 외부 wallet으로 나온 뒤 `USDC.e`, `pUSD`, `POL`, `WPOL` 이동을 추적한다.
5. 최종 recipient 또는 1-hop/2-hop sweep 주소가 Upbit/Korbit/Bithumb 라벨 주소로 이어지는지 확인한다.
6. 국내 CEX 라벨이 발견되더라도 `off-ramp 후보`로만 적고, 실제 계정 귀속/원화화는 거래소 자료 요청 항목으로 남긴다.

### 참고 링크

- Polymarket event: https://polymarket.com/event/2026-seoul-mayoral-election-winner
- Polymarket Gamma API: https://gamma-api.polymarket.com/events/slug/2026-seoul-mayoral-election-winner
- Polymarket official contract addresses: https://docs.polymarket.com/resources/contract-addresses
- Polymarket bridge status API docs: https://docs.polymarket.com/api-reference/bridge/get-transaction-status
- Upbit hot wallet on Polygon: https://polygonscan.com/address/0x4c569c1e541a19132ac893748e0ad54c7c989ff4
- Korbit 8 on Polygon: https://polygon.blockscout.com/address/0xf0bc8FdDB1F358cEf470D63F96aE65B1D7914953
