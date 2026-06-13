# 3. GMX V2 PerpDEX Order Lifecycle Case

## 목적

GMX V2에서 PerpDEX 주문이 생성되고 keeper에 의해 실행되는 과정을 보여준다.

이 문서는 기존 V1 seed를 대체하고, 현재 GMX V2의 `ExchangeRouter -> OrderVault -> OrderHandler keeper execution` 구조에 맞춰 정리한다. 아래 Seed A와 Seed B는 각각 `increase 구조`와 `decrease 구조`를 보여주는 별도 예시이며, 하나의 지갑 손익 lifecycle로 연결하지 않는다.

핵심은 아래를 분리하는 것이다.

```text
주문 생성 TX
  -> collateral / execution fee가 vault로 이동
  -> OrderCreated event와 order key 생성

keeper 실행 TX
  -> OrderHandler가 oracle params와 함께 executeOrder
  -> Position increase / decrease / close가 실제 반영
```

## Transight Search Network / Chain

```text
Transight search network / chain
Arbitrum One
```

이 문서의 주요 TX, 지갑, contract는 모두 Arbitrum One에서 검색한다.

## 핵심 질문

```text
GMX V2에서 사용자가 어떤 담보를 넣고 어떤 perp position을 만들었는가?
position close/reduce 때 어떤 token을 돌려받았는가?
온체인만으로 손익을 어디까지 말할 수 있고,
어디서부터 GMX position detail / 거래소 자료 / 가격 자료가 필요한가?
```

## 경제적 이익 취득 방식

- 사용자는 USDC, WETH 등 collateral을 넣고 BTC/USD, ETH/USD 등 perp position을 연다.
- position을 줄이거나 닫으면 collateral 반환, 실현손익, funding/borrowing/position fee가 반영된 정산 후보가 생긴다.
- close/reduce 실행 TX에서 받은 stablecoin이나 ETH는 `수령 후보` 또는 `정산 후보`이지, 곧바로 순수 이익은 아니다.
- 이후 DEX swap, bridge, CEX deposit 후보로 이동하면 처분/off-ramp 후보로 이어서 추적한다.

## GMX V2 공식 / 핵심 주소

아래 주소는 2026-06-01 기준 GMX 공식 문서와 explorer label을 기준으로 정리했다. GMX V2 logic contract는 업그레이드될 수 있으므로 강의 직전 공식 주소 문서에서 재확인한다.

| 구분 | Chain | Address | 메모 |
|---|---|---|---|
| ExchangeRouter | Arbitrum One | `0x1C3fa76e6E1088bCE750f23a5BFcffa1efEF6A41` | 주문 생성, deposit, withdrawal 진입점 |
| OrderVault | Arbitrum One | `0x31eF83a530Fde1B38EE9A18093A333D8Bbbc40D5` | 주문 생성 시 collateral / execution fee 수탁 |
| OrderHandler | Arbitrum One | `0x63492B775e30a9E6b4b4761c12605EB9d071d5e9` | keeper가 executeOrder 호출 |
| EventEmitter | Arbitrum One | `0xC8ee91A54287DB53897056e12D9819156D3822Fb` | `OrderCreated`, `OrderExecuted` event |
| USDC | Arbitrum One | `0xaf88d065e77c8cC2239327C5EDb3A432268e5831` | native USDC |
| WETH | Arbitrum One | `0x82aF49447D8a07e3bd95BD0d56f35241523fBab1` | execution fee / collateral |
| BTC/USD market | Arbitrum One | `0x47c031236e19d024b42f8AE6780E44A573170703` | GMX API 기준 `BTC/USD [WBTC.b-USDC]` (GM market token) |
| BTC/USD index token | Arbitrum One | `0x47904963fc8b2340414262125aF798B9655E58Cd` | market index token(가격 기준). synthetic 주소라 contract code/token transfer 없음. ERC-20처럼 검색하지 않는다 |
| BTC/USD long token | Arbitrum One | `0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f` | market long token. 온체인 ERC-20 symbol은 `WBTC`, GMX 라벨이 `WBTC.b`(bridged WBTC) |
| BTC/USD short token | Arbitrum One | `0xaf88d065e77c8cC2239327C5EDb3A432268e5831` | market short token, USDC (위 USDC와 동일) |

## 메인 Seed A: BTC/USD MarketIncrease Order

사용자가 BTC/USD long position을 여는 예시다.

```text
Transight search network / chain
Arbitrum One

Account
0x1A1ba5cf0dF05c58A64aaBf7733c92F9f0bfA9F3

Create order TX
0xac2f26a545fddc1e679afb7a7d790c46a00b59723686307764529681f6636845

Execution TX
0xb31fb9b0668b23680476eb937f21669b0d3daa7cef37cca11c65670ea7105eed

Order key
0x145138957fafcd7563051ec6e428b606e8c36e1c238e1fcd1f44b5815b38cd7d

Market
BTC/USD [WBTC.b-USDC]
0x47c031236e19d024b42f8AE6780E44A573170703

Collateral token
USDC
0xaf88d065e77c8cC2239327C5EDb3A432268e5831
```

### A-1. 주문 생성

```text
TX
0xac2f26a545fddc1e679afb7a7d790c46a00b59723686307764529681f6636845

Time
2026-05-29 04:00:05 UTC

Method
ExchangeRouter.multicall

Event
OrderCreated

Decoded event 핵심값
orderType = 2
isLong = true
market = BTC/USD [WBTC.b-USDC]
sizeDeltaUsd = 100 USD 후보
initialCollateralDeltaAmount = 10 USDC
```

Token movement:

```text
0x1A1b...A9F3
  -> 10 USDC
  -> OrderVault 0x31eF...40D5

ExchangeRouter
  -> 0.0035 WETH execution fee
  -> OrderVault
```

해석:

- 이 TX는 포지션이 열린 최종 결과가 아니라 `시장가 increase 주문 생성`이다.
- `OrderCreated` event의 `key`가 이후 keeper 실행 TX와 연결되는 핵심 값이다.
- USDC 10개는 collateral 후보이고, WETH는 execution fee 성격이다.

### A-2. Keeper 실행

```text
TX
0xb31fb9b0668b23680476eb937f21669b0d3daa7cef37cca11c65670ea7105eed

Method
OrderHandler.executeOrder

Event
OrderExecuted

Order key
0x145138957fafcd7563051ec6e428b606e8c36e1c238e1fcd1f44b5815b38cd7d
```

Token movement:

```text
OrderVault
  -> 10 USDC
  -> BTC/USD market
```

해석:

- 이 TX에서 keeper가 oracle params와 함께 주문을 실행한다.
- `OrderCreated`와 `OrderExecuted`를 order key로 연결해야 V2 포지션 생성 여부를 확인할 수 있다.
- 이 단계에서는 아직 경제적 이익 실현이 아니라 position 생성이다.

## 메인 Seed B: BTC/USD MarketDecrease Order

포지션을 줄이거나 닫으면서 USDC를 돌려받는 예시다. 이 seed는 Seed A와 같은 사용자나 같은 position이라고 단정하지 않고, `close/reduce 구조`를 보여주는 별도 seed로 사용한다. 따라서 두 seed를 묶어서 한 지갑의 순손익으로 계산하지 않는다.

```text
Transight search network / chain
Arbitrum One

Account
0x4988E8a3E9Be4f0D833816fc91f2fdc5926ed353

Create decrease TX
0x6d0cfabd32ac1996937744e165b224e94937bc6240d7cb84c3894b8cf69f4ce4

Execution TX
0xcd59daef8d801a5cb756fad7965a6f86a1043f8589aa5fe88e3437a9e59eff97

Order key
0x3a3768c9ee434795d55565ac19db0e3d8c0e94a2ed94a3721ba5e09eeeee2536

Market
BTC/USD [WBTC.b-USDC]
0x47c031236e19d024b42f8AE6780E44A573170703
```

### B-1. Decrease 주문 생성

```text
TX
0x6d0cfabd32ac1996937744e165b224e94937bc6240d7cb84c3894b8cf69f4ce4

Time
2026-05-29 04:00:21 UTC

Method
ExchangeRouter.multicall

Event
OrderCreated

Decoded event 핵심값
orderType = 4
isLong = true
market = BTC/USD [WBTC.b-USDC]
sizeDeltaUsd = 약 104.686126947 USD 후보
initialCollateralDeltaAmount = withdraw collateral amount 104.671121 USDC 후보
```

Token movement:

```text
ExchangeRouter
  -> 0.0012 WETH execution fee
  -> OrderVault
```

해석:

- decrease order에서는 새 collateral을 넣는 것이 아니라 기존 position을 줄이거나 닫는 요청이므로, 주문 생성 TX에는 주로 execution fee 이동이 보인다.
- 이때 `initialCollateralDeltaAmount`는 새로 투입한 담보가 아니라 기존 position에서 빼낼 collateral amount 후보로 해석한다.
- 실제 수령 token은 실행 TX에서 확인한다.

### B-2. Decrease 실행 / USDC 수령 후보

```text
TX
0xcd59daef8d801a5cb756fad7965a6f86a1043f8589aa5fe88e3437a9e59eff97

Method
OrderHandler.executeOrder

Event
OrderExecuted

Order key
0x3a3768c9ee434795d55565ac19db0e3d8c0e94a2ed94a3721ba5e09eeeee2536
```

Token movement:

```text
BTC/USD market
0x47c031...0703
  -> 104.671121 USDC
  -> 0x4988...d353
```

해석:

- 이 USDC 수령은 GMX V2 position close/reduce의 정산 후보로 볼 수 있다.
- 다만 `104.671121 USDC` 전체가 이익은 아니다. 원 collateral, PnL, funding fee, borrowing fee, position fee, price impact가 섞인 결과다.
- 손익 계산은 GMX position detail, open/close order 전체, 당시 가격, fee 내역을 같이 봐야 한다.

## Transight 시연 포인트

- `Arbitrum One`에서 TX hash를 직접 검색한다.
- `ExchangeRouter.multicall` 내부에 `createOrder`가 있거나 `OrderCreated` event가 있으면 주문 생성 TX로 본다.
- `OrderCreated` event의 `key`를 확인한다.
- 같은 `key`가 들어간 `OrderExecuted` event를 찾아 keeper 실행 TX와 연결한다.
- `OrderVault`, `OrderHandler`, `EventEmitter`, market token을 cluster/context로 묶는다.
- token transfer만 보지 말고 decoded event의 `orderType`, `isLong`, `market`, `sizeDeltaUsd`, `initialCollateralDeltaAmount`를 같이 본다.
- close/reduce 실행 TX에서 사용자가 받은 token은 `정산 후보`로 표시하고, 순수 이익으로 단정하지 않는다.

## Evidence Table

| 단계 | Chain | TX / Address | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 공식 구조 | Arbitrum One | `0x1C3fa76e6E1088bCE750f23a5BFcffa1efEF6A41` | GMX V2 ExchangeRouter | 주문 생성 진입점 | v2 핵심 router |
| 공식 구조 | Arbitrum One | `0x31eF83a530Fde1B38EE9A18093A333D8Bbbc40D5` | OrderVault | collateral / execution fee 수탁 | 주문 생성 TX에서 확인 |
| 공식 구조 | Arbitrum One | `0x63492B775e30a9E6b4b4761c12605EB9d071d5e9` | OrderHandler | keeper execution | user wallet 발신 아님 |
| Seed A account | Arbitrum One | `0x1A1ba5cf0dF05c58A64aaBf7733c92F9f0bfA9F3` | MarketIncrease 주문자 | 분석 대상 wallet | EOA, label 없음 |
| MarketIncrease 생성 | Arbitrum One | `0xac2f26a545fddc1e679afb7a7d790c46a00b59723686307764529681f6636845` | 10 USDC -> OrderVault, OrderCreated | 포지션 진입 요청 | BTC/USD long seed |
| MarketIncrease 실행 | Arbitrum One | `0xb31fb9b0668b23680476eb937f21669b0d3daa7cef37cca11c65670ea7105eed` | OrderExecuted, 10 USDC -> BTC/USD market | 포지션 진입 실행 | order key로 연결 |
| Seed B account | Arbitrum One | `0x4988E8a3E9Be4f0D833816fc91f2fdc5926ed353` | MarketDecrease 주문자 / USDC 수령 | 분석 대상 wallet | EOA, label 없음. Seed A와 다른 지갑 |
| MarketDecrease 생성 | Arbitrum One | `0x6d0cfabd32ac1996937744e165b224e94937bc6240d7cb84c3894b8cf69f4ce4` | OrderCreated, execution fee 이동, withdraw collateral amount 후보 | 포지션 감소/종료 요청 | 기존 position 기반 |
| MarketDecrease 실행 | Arbitrum One | `0xcd59daef8d801a5cb756fad7965a6f86a1043f8589aa5fe88e3437a9e59eff97` | BTC/USD market -> 104.671121 USDC | 정산 후보 | 순수 이익 아님 |
| Market | Arbitrum One | `0x47c031236e19d024b42f8AE6780E44A573170703` | GMX API 기준 `BTC/USD [WBTC.b-USDC]` | perp market | index/long/short token 확인 |

## 국세청 추가 요청자료

- 납세자 지갑 귀속 자료
- GMX position detail 또는 GMX API 자료
- 해당 account의 전체 open / increase / decrease / close order 내역
- position 방향, size, collateral, entry price, close price
- funding fee, borrowing fee, position fee, price impact, execution fee
- liquidation 또는 ADL 여부
- close/reduce 후 받은 USDC의 DEX swap, bridge, CEX deposit 여부
- CEX 입금이 있으면 거래소 계정 귀속, 내부 매도, 원화 출금 내역

## 판단 기준

- `ExchangeRouter.multicall` + `OrderCreated`는 주문 생성이지, 실행 완료가 아니다.
- `OrderHandler.executeOrder` + `OrderExecuted`까지 연결해야 실제 position 반영을 말할 수 있다.
- `MarketIncrease`는 경제적 이익 실현이 아니라 position 생성 단계다.
- `MarketDecrease` 실행에서 받은 USDC는 정산 후보지만, 원금과 손익이 섞여 있으므로 순수 이익으로 쓰지 않는다.
- 같은 wallet의 이후 swap/bridge/CEX deposit은 자금 사용 후보일 뿐, balance reconciliation 없이 특정 GMX 수령분의 처분이라고 단정하지 않는다.

## 주의점

- Seed A(increase)와 Seed B(decrease)는 서로 다른 account의 다른 position이다. 이 두 seed만으로는 한 position의 실현손익을 계산할 수 없다. 손익은 같은 position의 open/increase/decrease/close 전체와 fee·가격 자료가 있어야 한다.
- decoded event의 `orderType`, `isLong`, `sizeDeltaUsd`는 GMX `EventLog2`의 중첩 `EventUtils` 구조 안에 있어 explorer 기본 화면에서 바로 안 보일 수 있다. `sizeDeltaUsd`는 후보로 표기하고, 확정하려면 event를 직접 디코드한다.
- decrease 실행 TX에서 account가 받은 것은 이 seed에서는 USDC 1건뿐이다. ERC20 transfer와 internal/native trace 기준 별도 execution fee 환급이나 다른 token/native asset의 account 추가 수령은 확인되지 않았다. 그래도 이 USDC는 원금·손익·fee가 섞인 정산 후보이지 순수 이익이 아니다.
- `OrderHandler.executeOrder`는 keeper가 호출한다. 실행 TX의 sender는 사용자 지갑이 아니므로, sender만 보고 소유자를 판단하지 않는다.
- GMX V2 logic contract는 업그레이드될 수 있다. 강의 직전 공식 주소 문서에서 ExchangeRouter/OrderVault/OrderHandler/EventEmitter와 market token을 재확인한다.

## Source Links

- GMX overview: https://docs.gmx.io/docs/intro/
- GMX V2 architecture: https://docs.gmx.io/docs/api/contracts/architecture/
- GMX V2 contract addresses: https://docs.gmx.io/docs/api/contracts/addresses/
- GMX ExchangeRouter docs: https://docs.gmx.io/docs/api/contracts/exchange-router/
- GMX SDK V2 order examples: https://docs.gmx.io/docs/sdk/v2/examples/
- GMX Arbitrum markets API, market name snapshot source: https://arbitrum-api.gmxinfra.io/markets
- Seed A create order: https://arbitrum.blockscout.com/tx/0xac2f26a545fddc1e679afb7a7d790c46a00b59723686307764529681f6636845
- Seed A execution: https://arbitrum.blockscout.com/tx/0xb31fb9b0668b23680476eb937f21669b0d3daa7cef37cca11c65670ea7105eed
- Seed B create decrease: https://arbitrum.blockscout.com/tx/0x6d0cfabd32ac1996937744e165b224e94937bc6240d7cb84c3894b8cf69f4ce4
- Seed B execution: https://arbitrum.blockscout.com/tx/0xcd59daef8d801a5cb756fad7965a6f86a1043f8589aa5fe88e3437a9e59eff97
