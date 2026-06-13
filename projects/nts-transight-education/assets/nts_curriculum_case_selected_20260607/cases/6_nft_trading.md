# 6. NFT Trading Case

## 목적

NFT 단일 token ID의 매수와 매도를 기준으로 취득가, 처분가, marketplace fee, royalty 후보를 분리해 보여준다.

## 핵심 질문

```text
NFT 매수와 매도 TX를 기준으로 취득가, 처분가, 수수료, royalty 후보를 어떻게 구분할 것인가?
```

## 경제적 이익 취득 방식

- NFT를 mint하거나 marketplace에서 매수한다.
- 같은 NFT를 marketplace에서 매도하면 처분 후보가 된다.
- 매도 TX의 payment split을 보면 seller 수령액, marketplace fee, royalty 후보를 분리할 수 있다.
- NFT 거래는 token transfer만 보면 가격을 놓치기 쉽다. ERC-20 transfer, native ETH value, Seaport decoded input을 같이 봐야 한다.

## 강의 구성

NFT 케이스는 하나의 고난도 사건으로 만들기보다, marketplace별 체결 방식 차이를 보여주는 네 개의 작은 패턴으로 구성한다.

| 순서 | 패턴 | 핵심 포인트 | 강의 상태 |
|---:|---|---|---|
| 1 | OpenSea 일반 구매 | 구매자가 컨트랙트를 실행하고 ETH로 결제한다 | 사용 가능 |
| 2 | OpenSea 비딩 체결 | 판매자가 컨트랙트를 실행하고 WETH로 결제된다 | 사용 가능 |
| 3 | Blur 일반 구매 | 구매자 중심 map, Blur는 fee 구조가 OpenSea와 다르다 | tx hash 교체 필요 |
| 4 | Blur 비딩 체결 | 판매자 중심 map, Blur bid payment token을 확인한다 | 후보 |

교육 목표는 NFT 자체 설명이 아니라 아래 세 가지를 익히는 것이다.

- `NFT transfer`와 `payment transfer`를 같은 거래로 묶어 읽는다.
- 구매자, 판매자, marketplace, fee recipient, royalty recipient를 분리한다.
- Transight map이 경제적 주체가 아니라 `컨트랙트 실행자` 중심으로 보일 수 있음을 설명한다.

## Seed

```text
Transight search network / chain
Ethereum Mainnet

Collection
Bored Ape Yacht Club / BAYC

BAYC contract
0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D

Token ID
5928

대상 wallet / trader
0x556697364A2DF758073e55C0F8062F8D1349e5B3

Buy TX
0xbb3ca600f483be9b89da00d804deabc9a08f3df94cb1438139eb6a6c7532c3f1

Sell TX
0x4f1b6e3b7582107364a201cb1d1d30ee2ab721c918825d76466738e4911686d5

Marketplace contract
OpenSea Seaport
0x0000000000000068F116a894984e2DB1123eB395

WETH token
0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2

OpenSea fee recipient 후보
0x0000a26b00c1F0DF003000390027140000fAa719
```

## Google Doc 기반 보강 Seed

2026-06-08 설명 문서의 NFT 파트에서 가져온 교육용 seed다. 모두 **Ethereum Mainnet**에서 검색한다.

| 패턴 | TX | 문서 기준 금액/특징 | 강의에서 볼 것 | 상태 |
|---|---|---|---|---|
| OpenSea 일반 구매 | `0x7faeeb2d4fd0d68556c21c0fb10848ad9fbfe434cdf638b8e2cd8088f22979df` | buyer `0x42b1...`가 `11.75 ETH` 지급, 약 `$25,574`; OpenSea fee 약 `$255.74` | buyer가 Seaport를 실행하고 seller에게 NFT가 넘어오는 구조 | 사용 |
| OpenSea 비딩 체결 | `0xb4a3370961b7bd19271587f3ac2f998bd18d3781665caf985ace4c839a52678d` | seller `0x1abc...`가 실행, bidder `0x63a6...`가 `12.25 WETH` 지급, OpenSea fee와 Yuga Labs royalty 각각 약 `$280` | 비딩 체결은 seller 중심 map으로 보이며 WETH 결제와 royalty가 나온다 | 사용 |
| Blur 일반 구매 | 문서상 `0xb4a337...`로 기재되어 있으나 OpenSea 비딩 TX와 중복 | buyer `0xeae4...`가 약 `$22,313` 지급, seller `0x03b6...`가 NFT 전송, Blur fee 없음 | Blur fixed-price sale의 buyer-centered map | seed 교체 필요 |
| Blur 비딩 체결 | `0x9bf927b3babe601f99f491f1e4328a7bfc1f744e128ffe9a2ffce40140301cc8` | seller가 실행, bidder가 Blur bid payment token으로 지급 | Blur bid는 ETH/WETH가 아니라 Blur 쪽 payment token으로 보일 수 있다 | 후보 |

문서상 Blur 일반 구매 TX는 OpenSea 비딩 TX와 같은 hash로 적혀 있어 그대로 시연 seed로 쓰면 안 된다. 발표 전 Blur 일반 구매 seed는 별도로 하나 더 확정한다.

## Transight 검색 기준

이 case의 모든 주요 TX와 주소는 **Ethereum Mainnet**에서 검색한다.

| 항목 | 검색할 chain/network | 검색값 |
|---|---|---|
| BAYC contract | Ethereum Mainnet | `0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D` |
| BAYC #5928 | Ethereum Mainnet | contract + token ID `5928` |
| 대상 wallet / trader | Ethereum Mainnet | `0x556697364A2DF758073e55C0F8062F8D1349e5B3` |
| Buy TX | Ethereum Mainnet | `0xbb3ca600f483be9b89da00d804deabc9a08f3df94cb1438139eb6a6c7532c3f1` |
| Sell TX | Ethereum Mainnet | `0x4f1b6e3b7582107364a201cb1d1d30ee2ab721c918825d76466738e4911686d5` |
| Seaport | Ethereum Mainnet | `0x0000000000000068F116a894984e2DB1123eB395` |
| WETH | Ethereum Mainnet | `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` |
| OpenSea fee recipient 후보 | Ethereum Mainnet | `0x0000a26b00c1F0DF003000390027140000fAa719` |

## 시나리오별 설명안

### A. OpenSea 일반 구매

핵심 질문:

```text
구매자가 ETH를 내고 NFT를 받는 거래에서 seller 수령액과 platform fee를 어떻게 분리할 것인가?
```

흐름:

```text
buyer 0x42b1...
  -> OpenSea / Seaport contract 실행
  -> 11.75 ETH 지급
  -> NFT 수령

seller 0x45b0...
  -> NFT 이전
  -> OpenSea fee 차감 후 매도대금 수령

OpenSea fee recipient
  -> 약 $255.74 fee 수령
```

분류:

- buyer 기준: NFT 취득 후보
- seller 기준: NFT 처분 후보
- OpenSea fee: 처분 관련 수수료 후보
- royalty: 이 seed에서는 별도 확인 필요

### B. OpenSea 비딩 체결

핵심 질문:

```text
판매자가 bid를 accept한 거래에서 왜 ETH가 아니라 WETH가 움직이고, 왜 판매자 중심 map으로 보이는가?
```

흐름:

```text
seller 0x1abc...
  -> OpenSea / Seaport bid accept 실행
  -> NFT를 bidder에게 이전

bidder 0x63a6...
  -> 12.25 WETH 지급

OpenSea fee recipient
  -> platform fee 약 $280 수령

Yuga Labs
  -> creator royalty 약 $280 수령
```

분류:

- seller 기준: NFT 처분 후보
- bidder 기준: NFT 취득 후보
- WETH payment: bid 체결 대금
- Yuga Labs payment: creator royalty 후보
- map 중심: 판매자가 bid accept를 실행했기 때문에 판매자 중심으로 보일 수 있음

### C. Blur 일반 구매

핵심 질문:

```text
OpenSea와 Blur의 일반 구매는 무엇이 같고 무엇이 다른가?
```

문서 기준 흐름:

```text
buyer 0xeae4...
  -> Blur contract 실행
  -> 약 $22,313 지급
  -> NFT 수령

seller 0x03b6...
  -> NFT 이전
  -> 매도대금 수령
```

강의 포인트:

- 일반 구매는 구매자 중심 map으로 잡히는 구조가 OpenSea와 유사하다.
- 문서 기준으로 Blur는 platform fee가 없는 케이스로 설명한다.
- 단, 현재 문서의 tx hash가 OpenSea 비딩 TX와 중복되어 있어 실제 시연용 hash는 교체해야 한다.

### D. Blur 비딩 체결

핵심 질문:

```text
Blur bid 거래에서 payment token이 ETH/WETH처럼 보이지 않을 때 어떻게 해석할 것인가?
```

흐름:

```text
seller
  -> Blur bid accept 실행
  -> NFT를 bidder에게 이전

bidder
  -> Blur bid payment token 지급
```

강의 포인트:

- 비딩 체결은 판매자가 실행하므로 판매자 중심 map으로 보일 수 있다.
- Blur bid payment token은 ETH와 1:1 가치 연동되는 결제 토큰으로 설명하되, token contract와 wrapping/unwrapping 흐름은 별도 evidence로 확인한다.
- OpenSea 비딩과 비교하면 `WETH bid`와 `Blur payment token bid`의 차이를 설명하기 좋다.

## 추천 Case: BAYC #5928 단기 매수/매도

강의 난이도:

- 중간
- NFT transfer와 payment transfer를 함께 읽는 연습에 좋음
- 단일 NFT라 bundle/wash trading 설명 없이 취득가/처분가/fee 분리가 가능함

확인된 흐름:

```text
2026-05-25 21:29:47 UTC
OpenSea Seaport / fulfillAdvancedOrder

0x5566...e5B3
  -> 8.55 WETH 지급
  -> BAYC #5928 수령

0xf762...b126
  -> BAYC #5928 이전
  -> 8.55 WETH 수령
  -> 0.0855 WETH를 OpenSea fee recipient 후보로 지급
```

```text
2026-05-27 19:05:47 UTC
OpenSea Seaport / fulfillBasicOrder_efficient_6GL6yc

0x5566...e5B3
  -> BAYC #5928 매도
  -> seller amount 8.6031 ETH 수령 후보

0x7dae...89B1
  -> 8.69 ETH 지급
  -> BAYC #5928 수령

OpenSea fee recipient 후보
  -> 0.0869 ETH 수령 후보
```

계산 포인트:

```text
취득가 후보
8.55 WETH

처분 gross price 후보
8.69 ETH

처분 seller net 후보
8.6031 ETH

매도 marketplace fee 후보
0.0869 ETH

단순 차익 후보 (gas fee, WETH/ETH wrapper, 시점별 원화 환산 제외)
8.6031 ETH - 8.55 WETH = 0.0531 ETH
```

판단:

- `Buy TX`는 대상 wallet의 NFT 취득 후보로 본다.
- `Sell TX`는 대상 wallet의 NFT 처분 후보로 본다.
- WETH와 ETH는 1:1 wrapper 관계지만, 회계/세무 판단에서는 token 종류와 환산 시점을 별도로 기록한다.
- Buy TX의 0.0855 WETH marketplace fee는 seller가 부담한 fee로 보이며, 대상 wallet의 추가 취득가로 단순 합산하지 않는다.
- 이 seed에서는 creator royalty로 분리되는 추가 recipient가 명확히 보이지 않는다.
- OpenSea fee recipient 후보는 marketplace fee로 분류하되, 최종 수수료 성격은 marketplace order detail 또는 추가 자료로 확인한다.

## 예상 Flow

```text
대상 wallet
  -> OpenSea Seaport에서 BAYC #5928 매수
  -> NFT transfer 수령
  -> OpenSea Seaport에서 BAYC #5928 매도
  -> ETH payment 수령 후보
  -> marketplace fee 차감
  -> 취득가/처분가/fee/차익 후보 계산
```

## Transight 확인 포인트

- NFT transfer: BAYC #5928이 누구에게서 누구에게 이동했는지 확인
- ERC-20 payment transfer: buy TX에서 WETH 8.55가 대상 wallet에서 seller로 이동했는지 확인
- Native ETH payment: sell TX의 `value`와 decoded input에서 seller amount와 fee recipient 확인
- Marketplace contract: `Seaport` interaction인지 확인
- Fee recipient: `0x0000a26b...Aa719`가 OpenSea fee recipient 후보인지 확인
- Royalty: 추가 recipient가 있는지 확인하고, 없으면 "이 seed에서는 royalty 미식별"로 기록

## Evidence Table

| 단계 | Chain | TX / Address | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 0 | Ethereum Mainnet | `0x556697364A2DF758073e55C0F8062F8D1349e5B3` | Buy TX에서 BAYC #5928 수령 + Sell TX에서 동일 token 매도 (동일 wallet round-trip 확인) | 분석 대상 wallet | EOA (contract 아님) |
| 1 | Ethereum Mainnet | `0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D` / `5928` | BAYC #5928 단일 ERC-721 token (contract label BoredApeYachtClub / symbol BAYC) | 분석 대상 NFT | token ID 고정 |
| 2 | Ethereum Mainnet | `0xbb3ca600f483be9b89da00d804deabc9a08f3df94cb1438139eb6a6c7532c3f1` | BAYC #5928이 `0xf762...b126`에서 `0x5566...e5B3`로 이동 | 취득 후보 | OpenSea Seaport `fulfillAdvancedOrder` |
| 3 | Ethereum Mainnet | `0xbb3ca600f483be9b89da00d804deabc9a08f3df94cb1438139eb6a6c7532c3f1` | `0x5566...e5B3`가 `0xf762...b126`에게 8.55 WETH 지급 | 취득가 후보 | ERC-20 transfer |
| 4 | Ethereum Mainnet | `0xbb3ca600f483be9b89da00d804deabc9a08f3df94cb1438139eb6a6c7532c3f1` | `0xf762...b126`가 `0x0000a26b...Aa719`에 0.0855 WETH 지급 | marketplace fee 후보 | 매수 TX의 seller-side fee. 대상 wallet의 추가 취득가로 단순 합산하지 않음 |
| 5 | Ethereum Mainnet | `0x4f1b6e3b7582107364a201cb1d1d30ee2ab721c918825d76466738e4911686d5` | BAYC #5928이 `0x5566...e5B3`에서 `0x7dae...89B1`로 이동 | 처분 후보 | OpenSea Seaport `fulfillBasicOrder` |
| 6 | Ethereum Mainnet | `0x4f1b6e3b7582107364a201cb1d1d30ee2ab721c918825d76466738e4911686d5` | TX `value` 8.69 ETH, internal tx에서 Seaport가 `0x5566...e5B3`에 8.6031 ETH 지급 (decoded consideration base 8.6031 ETH와 일치) | 처분가 후보 | native ETH payment, seller net |
| 7 | Ethereum Mainnet | `0x0000a26b00c1F0DF003000390027140000fAa719` | internal tx에서 Seaport가 0.0869 ETH 지급 (decoded `additionalRecipients` 단일 entry와 일치) | marketplace fee 후보 | OpenSea fee recipient 후보 |
| 8 | Ethereum Mainnet | Sell TX decoded input | `additionalRecipients`는 OpenSea fee 단일 entry(0.0869 ETH)뿐, creator royalty용 추가 recipient 없음 | royalty 미식별 | royalty 설명은 별도 사례로 보강 가능 |

## 근거 링크

- BAYC #5928 transfer history: https://eth.blockscout.com/token/0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D/instance/5928
- Buy TX: https://eth.blockscout.com/tx/0xbb3ca600f483be9b89da00d804deabc9a08f3df94cb1438139eb6a6c7532c3f1
- Sell TX: https://eth.blockscout.com/tx/0x4f1b6e3b7582107364a201cb1d1d30ee2ab721c918825d76466738e4911686d5
- OpenSea asset page: https://opensea.io/assets/ethereum/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/5928
- OpenSea fee docs: https://docs.opensea.io/docs/opensea-fees
- OpenSea fee update: https://docs.opensea.io/changelog/opensea-fee-update

## 국세청 추가 요청자료

- 납세자 지갑 귀속 자료
- Marketplace 주문/체결 자료
- OpenSea 또는 aggregator의 실제 order detail
- WETH/ETH 환산 기준과 원화 환산 가격 자료
- gas fee 부담 주체와 수수료 처리 기준
- royalty 또는 creator earnings가 별도 정산되었는지에 대한 marketplace 자료

## 주의점

- NFT transfer만 보고 가격을 확정하지 않는다. payment token transfer와 native ETH value를 같이 확인한다.
- Sell TX는 native ETH payment라 ERC-20 transfer 목록에는 처분 대금이 보이지 않을 수 있다.
- Seaport order의 `consideration` 또는 `additionalRecipients`를 확인해야 seller 수령액과 fee가 분리된다.
- 이 case는 bundle 거래가 아니라 단일 NFT 거래로 사용한다.
- 단순 차익 후보는 gas fee, WETH/ETH 환산 시점, 원화 환산 기준을 반영하기 전의 교육용 1차 계산이다.
- 과거 token history에는 loan 관련 TX가 있을 수 있으나, 초급 실습에서는 대상 wallet의 매수/매도 두 TX만 사용한다.
- Wash trading 여부는 이 seed에서 단정하지 않는다. 동일 주체/자전거래 의심은 별도 cluster와 marketplace 자료가 필요하다.
