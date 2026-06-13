# 2. Upbit KRW Listing Arbitrage: ARB on Arbitrum

## 목적

국세청 실무 관심도가 높은 `해외 CEX 취득/출금 -> 국내 CEX 입금 후보 -> 원화마켓 매도 자료 요청` 흐름을 보여준다.

이 파일의 메인 seed는 `ARB 업비트 KRW/BTC 마켓 추가` 직후 Arbitrum One에서 관찰되는 CEX 간 이동이다. bridge 자체가 보이는 케이스는 아니고, 업비트 공지가 ARB 입금을 `Arbitrum 네트워크만 지원`한다고 안내한 케이스라서 모든 주요 TX는 Arbitrum One에서 검색한다.

## 핵심 질문

```text
해외 CEX에서 확보한 token이 국내 CEX로 이동했고,
원화상장 이후 매도 후보로 볼 수 있는 흐름이 있는가?
```

## 경제적 이익 취득 방식

- 해외 CEX와 국내 원화마켓 사이의 가격 차이, 유동성 차이, 상장 직후 수요를 이용한다.
- 해외 CEX에서 token을 확보하거나 출금한 뒤 국내 거래소 deposit/hot wallet 후보까지 보낸다.
- 국내 원화마켓 매도는 온체인이 아니라 거래소 내부 장부, 주문, 체결 자료로 확인한다.

## Seed

```text
Token / Listing event
ARB / Arbitrum
업비트 KRW, BTC 마켓 추가 공지: 2023-03-30
거래지원 개시 예정: 2023-03-30 15:00 KST = 2023-03-30 06:00 UTC
입금 지원 network: Arbitrum only

Transight search network / chain
Arbitrum One

해외 CEX 출금 후보
Binance 54 labeled address:
0xB38e8c17e38363aF6EbdCb3dAE12e0243582891D

중간 주소
0x250ec7BFf0d4D2DEb3fA1147bbD682577b848716

국내 CEX deposit/hot wallet 후보
Upbit labeled address:
0xAAC8eD1aE0b18D6C943a6A285452Eac78397B7E8

Main flow TX 1
0x86ac8507ac5c02bac7b6b63cc40b6439b3d017b5f8a8e0bb5c0fce62ac6c7dea

Main flow TX 2
0x7aa9051b1966fc7aadfcc9dfb83b2ac436252e6cd0f906578c9d543a3be5046e
```

## 자료 이미지

![Upbit ARB listing notice](./assets/2_arbitrage/01_upbit_arb_listing.png)

## 예상 Flow

```text
Binance labeled wallet
  -> intermediate wallet
  -> Upbit labeled wallet
  -> Upbit 내부 KRW/BTC 마켓 매도 여부는 자료 요청
```

## 메인 케이스: Binance -> Upbit 후보

### Transight 검색 기준

```text
Chain / Network: Arbitrum One
Token: ARB
Token contract: 0x912CE59144191C1204E64559FE8253a0e49E6548
```

### Flow

```text
2023-03-31 07:45:24 UTC
Binance 54
0xB38e8c17e38363aF6EbdCb3dAE12e0243582891D
  -> 39,999.7 ARB
  -> 0x250ec7BFf0d4D2DEb3fA1147bbD682577b848716

2023-03-31 07:48:17 UTC
0x250ec7BFf0d4D2DEb3fA1147bbD682577b848716
  -> 39,999.7 ARB
  -> Upbit
     0xAAC8eD1aE0b18D6C943a6A285452Eac78397B7E8
```

### 해석

- 같은 수량 `39,999.7 ARB`가 약 3분 간격으로 `Binance labeled wallet -> 중간 주소 -> Upbit labeled wallet`로 이동한다.
- 업비트 ARB 원화마켓 거래지원 개시 이후 약 25시간 뒤의 이동이다.
- 강의에서는 `해외 CEX에서 국내 CEX로 들어온 상장 아비트라지 후보`로 설명한다.
- 다만 이 흐름만으로는 실제 원화 매도, 계정 귀속, 체결 가격을 확정하지 않는다.

## 보조 케이스: 상장 직후 소액 exact-sum 후보

상장 직후 시간대에 더 가까운 흐름이다. 금액은 작지만 합산 관계가 깔끔해서 실습용으로 좋다.

```text
Transight search network / chain: Arbitrum One

2023-03-30 06:55:34 UTC
Binance 54
0xB38e8c17e38363aF6EbdCb3dAE12e0243582891D
  -> 9.7 ARB
  -> 0x1B3BcA0e71DA06782851B7fAC504EB176a6AEdC4
TX: 0xcaa6b3e5743a6f5d507fe987a8b80c4ffe8601bf740943a82dfc6a9d8cb29581

2023-03-30 07:09:57 UTC
Binance 54
0xB38e8c17e38363aF6EbdCb3dAE12e0243582891D
  -> 49.1835 ARB
  -> 0x1B3BcA0e71DA06782851B7fAC504EB176a6AEdC4
TX: 0x8e8b2bb9a1f9c471b5b95f1609d306413f3c99c84b4419e4a7d785ae8fdde92c

2023-03-30 07:13:38 UTC
0x1B3BcA0e71DA06782851B7fAC504EB176a6AEdC4
  -> 58.8835 ARB
  -> Upbit 2
     0x68b299451bb795f63D95532da20B3CBFa22200De
TX: 0x1bc01165b634a704902447872aeeb69f5c4cbb9e4b64f36f1fed46ce7a183efc
```

해석 포인트는 단순하다. `9.7 + 49.1835 = 58.8835 ARB`이고, 최종 수취 주소가 Arbiscan 기준 `Upbit 2`로 표시된다. 다만 동일인이 중간 주소를 통제했는지, 업비트 계정에서 실제 매도했는지는 추가 확인이 필요하다.

## 보조 관찰: Upbit hot wallet 후보 cluster

0xScope는 2023-03-31에 `0xf7F468B184A48f6ca37EeFFE12733Ee1c16B6E26` 주소가 ARB를 대량 수집했고 활동상 Upbit hot wallet일 수 있다고 언급했다. 이 주소는 상장 직후 `0xF383...`, `0xAAC8...`, `0x68b...` 등과 ARB를 주고받는다.

```text
Transight search network / chain: Arbitrum One

Upbit hot wallet 후보
0xf7F468B184A48f6ca37EeFFE12733Ee1c16B6E26

관련 Upbit labeled address
0xAAC8eD1aE0b18D6C943a6A285452Eac78397B7E8
0x68b299451bb795f63D95532da20B3CBFa22200De
```

이 부분은 cluster/label 기능을 보여주는 보조 소재로만 사용한다. 공개 강의에서는 `Upbit hot wallet 확정`이 아니라 `Upbit 관련 wallet cluster 후보`로 말하는 편이 안전하다.

## Transight 확인 포인트

- 해외 CEX labeled address에서 출금된 token movement
- 중간 주소가 받은 수량과 보낸 수량이 같은지
- 국내 CEX deposit/hot wallet labeled address 접점
- CEX deposit address / hot wallet / sweep wallet 구조
- token 이동 시점과 상장 시점의 관계
- bridge가 실제로 있는지 여부

## Evidence Table

| 단계 | Chain | TX / Address | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 0 | off-chain | Upbit notice `id=3420` | ARB KRW/BTC 마켓 추가, Arbitrum network 입금만 지원 | 상장 이벤트 | 2023-03-30 15:00 KST 거래지원 예정 |
| 1 | Arbitrum One | `0xB38e8c17e38363aF6EbdCb3dAE12e0243582891D` | explorer label: Binance 54 | 해외 CEX wallet | 라벨은 Transight에서도 재확인 |
| 2 | Arbitrum One | `0x86ac8507ac5c02bac7b6b63cc40b6439b3d017b5f8a8e0bb5c0fce62ac6c7dea` | Binance 54 -> `0x250ec...`, `39,999.7 ARB` | 해외 CEX 출금 후보 | 2023-03-31 07:45:24 UTC |
| 3 | Arbitrum One | `0x250ec7BFf0d4D2DEb3fA1147bbD682577b848716` | 받은 수량과 보낸 수량 동일 | 중간 주소 | 개인/계정 귀속 불명 |
| 4 | Arbitrum One | `0x7aa9051b1966fc7aadfcc9dfb83b2ac436252e6cd0f906578c9d543a3be5046e` | `0x250ec...` -> Upbit, `39,999.7 ARB` | 국내 CEX 입금 후보 | 2023-03-31 07:48:17 UTC |
| 5 | Arbitrum One | `0xAAC8eD1aE0b18D6C943a6A285452Eac78397B7E8` | explorer label: Upbit | 국내 CEX wallet | deposit/hot/sweep 세부 구조는 추가 확인 |
| 6 | off-chain | Upbit 계정 장부 | 원화/BTC 마켓 주문, 체결, 입금 반영 | 추가 확인 필요 | 온체인만으로 매도 확정 불가 |

## Source Links

- Upbit notice: https://www.upbit.com/service_center/notice?id=3420
- Upbit notice mirror: https://economybloc.com/article/6812/
- ARB token on Arbitrum: https://arbitrum.blockscout.com/address/0x912CE59144191C1204E64559FE8253a0e49E6548
- Binance 54 address: https://etherscan.io/address/0xB38e8c17e38363aF6EbdCb3dAE12e0243582891D
- Upbit address: https://arbiscan.io/address/0xAAC8eD1aE0b18D6C943a6A285452Eac78397B7E8
- Upbit 2 address: https://arbiscan.io/address/0x68b299451bb795f63D95532da20B3CBFa22200De
- Main TX 1: https://arbitrum.blockscout.com/tx/0x86ac8507ac5c02bac7b6b63cc40b6439b3d017b5f8a8e0bb5c0fce62ac6c7dea
- Main TX 2: https://arbitrum.blockscout.com/tx/0x7aa9051b1966fc7aadfcc9dfb83b2ac436252e6cd0f906578c9d543a3be5046e
- 0xScope/Upbit hot wallet 후보 관련 기사: https://www.blocktempo.com/korean-crypto-exchange-upbit-listing-arbitrum/

## 국세청 추가 요청자료

- 국내 CEX 계정 귀속 자료
- 입금 반영 시각
- 원화마켓 주문/체결 내역
- 수수료, 출금, 원화 정산 내역
- 해외 CEX 입출금 내역
- 해외 CEX 계정 귀속 자료
- travel rule 또는 VASP 간 송수신 정보
- 동일 시각 ARB/KRW, ARB/BTC, 해외 ARB/USDT 가격 자료

## 주의점

- 특정 사용자의 업비트 계정 귀속은 온체인만으로 확정하지 않는다.
- `CEX deposit = 원화 매도 확정`으로 쓰지 않는다.
- 공개 case에서는 주소 귀속을 단정하지 않는다.
- 이 seed에서는 bridge TX를 확인하지 못했다. 핵심은 `Arbitrum One 네트워크에서 CEX 간 token 이동`이다.
- explorer label은 교육용 seed 선별 근거로만 쓰고, 최종 판단에서는 Transight label, 거래소 회신, 내부 장부를 교차 확인한다.
