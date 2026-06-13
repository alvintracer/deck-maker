# 5. 밈코인 트레이딩 케이스

## 목적

밈코인 매매를 통해 다음을 짧고 직관적으로 보여준다.

- DEX에서 밈코인을 취득하는 구간
- 같은 토큰을 다시 ETH/WETH 또는 스테이블코인으로 처분하는 구간
- 실현손익 판단 시 필요한 추가자료
- CEX deposit이 붙는 경우와 붙지 않는 경우의 차이

## 핵심 질문

```text
이 지갑은 어떤 밈코인을 언제 취득했고,
어떤 TX에서 처분했으며,
그 결과 자산이 어떤 형태로 바뀌었는가?
```

## 메인 실습 Seed: PEPE 단기 DEX 매매

이 case의 모든 주요 TX와 주소는 **Ethereum Mainnet**에서 검색한다.

```text
토큰
PEPE

Transight search network / chain
Ethereum Mainnet

PEPE 토큰
0x6982508145454Ce325dDbE47a25d4ec3d2311933

트레이더 지갑
0x8DF79cD8695921a2dE2616105D761b65Ce6CEf4f

실행 라우터
0xb300000b72DEAEb607a12d5f54773D1C19c7028d

PEPE/WETH Uniswap V2 pool
0xA43fe16908251ee70EF74718545e4FE6C5cCEc9f

PEPE/WETH Uniswap V3 pool
0x11950d141EcB863F01007AdD7D1A342041227b58

매수 TX
0xef71c686c56757d19d80c4b28600359d56d63335d4fad2ff7acda00bce2fa6d4

매도 TX
0x624b8dfc89d368ebec22630dd638d1762f2b25d559aed59b59a0d393c198c6b5
```

## 왜 이 seed를 쓰는가

- PEPE는 Ethereum Mainnet의 대표적인 밈코인이라 설명 비용이 낮다.
- EOA가 DEX router를 통해 PEPE를 사고 파는 구조가 보인다.
- PEPE 토큰, Uniswap pool, router, wallet, TX를 모두 같은 체인에서 검색하면 된다.
- CEX deposit이 붙지 않은 순수 DEX 매매 예시라 초급 실습에 적합하다.
- 다만 이 지갑은 여러 밈코인을 반복 매매하므로, 손익 계산은 반드시 토큰별 기간 필터링이 필요하다.

## 예상 Flow

```text
0x8DF79...Ef4f
  -> Diamond router
  -> ETH/WETH로 PEPE buy
  -> PEPE 보유
  -> PEPE sell
  -> WETH/ETH 계열 자산으로 전환
```

## Evidence Table

| 단계 | Chain | TX / 주소 | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 1 | Ethereum Mainnet | `0x8DF79cD8695921a2dE2616105D761b65Ce6CEf4f` | 트레이더 지갑 | 분석 대상 | EOA, 거래소 라벨 없음 |
| 2 | Ethereum Mainnet | `0x6982508145454Ce325dDbE47a25d4ec3d2311933` | PEPE 토큰 컨트랙트 | 대상 토큰 | 검증된 밈코인으로 설명 가능 |
| 3 | Ethereum Mainnet | `0xef71c686c56757d19d80c4b28600359d56d63335d4fad2ff7acda00bce2fa6d4` | 약 305.026M PEPE 수령 | 취득 후보 | PEPE/WETH V2, V3 route가 함께 사용됨 |
| 4 | Ethereum Mainnet | `0x624b8dfc89d368ebec22630dd638d1762f2b25d559aed59b59a0d393c198c6b5` | 약 305.026M PEPE 처분 | 처분 후보 | WETH/ETH 계열로 전환되는 sell route |
| 5 | Ethereum Mainnet | `0xb300000b72DEAEb607a12d5f54773D1C19c7028d` | Diamond router | 실행 경유지 | DEX/aggregator router 성격으로 보고 TX Detail 확인 |
| 6 | Ethereum Mainnet | `0xA43fe16908251ee70EF74718545e4FE6C5cCEc9f` | PEPE/WETH V2 pool | DEX pool | buy/sell route의 핵심 pool |
| 7 | Ethereum Mainnet | `0x11950d141EcB863F01007AdD7D1A342041227b58` | PEPE/WETH V3 pool | DEX pool | buy TX에서 일부 route 사용 |

## TX별 상세 메모

### 매수 TX

```text
체인
Ethereum Mainnet

TX
0xef71c686c56757d19d80c4b28600359d56d63335d4fad2ff7acda00bce2fa6d4

시각
2026-05-28 05:51:23 UTC

송신
0x8DF79cD8695921a2dE2616105D761b65Ce6CEf4f

수신
0xb300000b72DEAEb607a12d5f54773D1C19c7028d

주요 토큰 이동
WETH -> PEPE/WETH pools
PEPE/WETH pools -> 0x8DF79...Ef4f

PEPE 수령량
305,026,271.845567435908288865 PEPE

수령량 route 분할 (온체인 확인)
V2 pool(0xA43fe169...) -> 274,524,531.085006709375344446 PEPE
V3 pool(0x11950d14...) ->  30,501,740.760560726532944419 PEPE
두 leg 합 = 305,026,271.845567435908288865 PEPE (문서 수령량과 일치)
```

### 매도 TX

```text
체인
Ethereum Mainnet

TX
0x624b8dfc89d368ebec22630dd638d1762f2b25d559aed59b59a0d393c198c6b5

시각
2026-05-28 06:04:47 UTC

송신
0x8DF79cD8695921a2dE2616105D761b65Ce6CEf4f

수신
0xb300000b72DEAEb607a12d5f54773D1C19c7028d

주요 토큰 이동
0x8DF79...Ef4f -> PEPE
PEPE -> PEPE/WETH pool
PEPE/WETH pool -> WETH/ETH route

PEPE 처분량
305,026,271.845567435908288865 PEPE

처분 결과 (온체인 확인)
PEPE -> Diamond -> V2 pool(0xA43fe169...) -> WETH 0.509915916387919297
WETH는 마지막 leg에서 0x0으로 burn 되며 ETH로 unwrap 추정 (internal/native trace 병행 확인)

라운드트립 확인 (온체인)
매수 wallet과 매도 wallet 동일: 0x8DF79...Ef4f
매수 수령량과 매도 처분량이 wei 단위까지 동일(305,026,271.845567435908288865 PEPE)하여
이 tx pair 기준 동일 수량 라운드트립 후보로 볼 수 있음
단, PEPE는 fungible token이므로 같은 wallet의 다른 PEPE 입출금과 잔고를 함께 확인해야
특정 취득분이 그대로 처분됐다고 최종 확정할 수 있음
```

## 강의에서 보여줄 포인트

- `TX hash`로 먼저 검색하고, `Token Transfer`에서 PEPE 수량 변화를 확인한다.
- buy TX와 sell TX를 같은 wallet 기준으로 묶어서 본다.
- 같은 토큰 수량이 매수 후 매도되는지 확인하되, fungible token은 전체 잔고와 다른 입출금도 같이 본다.
- router 주소와 pool 주소를 분리해서 본다.
- WETH가 ETH로 unwrap되는 경우, token transfer만 보지 말고 native/internal trace도 같이 확인한다.
- 이 seed만으로는 CEX off-ramp를 말하지 않는다.

## 보조 예시: PEPE whale의 CEX deposit 후보

메인 실습 case에 CEX deposit이 없으므로, off-ramp 후보 설명이 필요하면 아래를 별도 예시로 붙인다.

이 보조 예시의 모든 주요 TX와 주소도 **Ethereum Mainnet**에서 검색한다.

```text
지갑
0x2daabb7d7d8114EE334D5A141A97ef181e565e69

PEPE deposit 후보 주소
0xF45De557A63B2Cf2C17449B15840f03A1336BF6a

Deposit 후보 TX 1
0x8075349ca187f85663e21588cd04941fe7f200bcad97736c531348e3595a9cd9

Deposit 후보 TX 2
0x6a01417dc912e91dd70599e3d4d10c758672313c77af677da3a47d841dd4c651
```

| 단계 | Chain | TX / 주소 | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 1 | Ethereum Mainnet | `0x2daabb7d7d8114EE334D5A141A97ef181e565e69` | PEPE whale wallet | 보조 분석 대상 | Lookonchain 공개 분석에서 언급 |
| 2 | Ethereum Mainnet | `0x8075349ca187f85663e21588cd04941fe7f200bcad97736c531348e3595a9cd9` | 250B PEPE transfer | CEX deposit 후보 | Coinbase 입금 주장 존재, Transight label 확인 필요 |
| 3 | Ethereum Mainnet | `0x6a01417dc912e91dd70599e3d4d10c758672313c77af677da3a47d841dd4c651` | 250B PEPE transfer | CEX deposit 후보 | 같은 수신 주소로 추가 250B PEPE |
| 4 | Ethereum Mainnet | `0xF45De557A63B2Cf2C17449B15840f03A1336BF6a` | PEPE 수신 주소 (whale로부터 2회 x 250B PEPE 수신, 온체인 확인) | deposit 주소 후보 | EOA, 거래소 라벨 없음. 직접 서명한 outbound PEPE sweep tx가 있어 단순 수신 전용 주소는 아님. 거래소 내부 계정 여부는 label/cluster 없이는 확정하지 않음 |

보조 예시는 강의에서 이렇게 표현한다.

```text
공개 분석에서는 Coinbase 입금으로 설명되지만,
교육자료에서는 CEX deposit 후보로만 표현한다.
Transight label, exchange clustering, subpoena 자료가 있어야 실제 계정/처분 여부를 확정할 수 있다.
```

## Transight 확인 포인트

- `Ethereum Mainnet` 선택 여부
- TX hash 검색
- wallet 기준 토큰 잔액 변화
- PEPE 토큰 이동의 `from`, `to`, `amount`
- DEX router와 pool 주소 구분
- PEPE -> WETH/ETH 전환 구간
- CEX deposit 후보는 label과 cluster 근거를 별도로 확인
- 실현손익은 buy/sell 한 쌍만 보고 단정하지 않고 전체 취득원가와 수수료를 다시 계산

## 국세청 추가 요청자료

- 납세자 지갑 귀속 자료
- 전체 PEPE 취득 및 처분 내역
- DEX swap 당시 가격 산정 기준
- gas fee, aggregator fee, slippage 자료
- CEX 입금 후보가 있을 경우 거래소 계정 귀속 및 내부 매도 내역
- 같은 wallet의 다른 밈코인 반복 거래 내역

## 주의점

- 밈코인 case는 자극적으로 보일 수 있으므로 `투자 성공담`이 아니라 `경제적 이익 취득 방식`으로 설명한다.
- PEPE 자체는 대표 밈코인이지만, 주변 dust token이나 scam token은 강의에서 굳이 다루지 않는다.
- router 또는 aggregator를 사용하면 토큰 이동이 여러 pool로 쪼개질 수 있다.
- CEX deposit 후보는 `거래소 입금으로 보이는 접점`까지만 말하고, 원화화/fiat off-ramp는 거래소 자료 없이는 확정하지 않는다.
- 특정 TX의 손익은 전체 포지션, 선입선출/이동평균 등 세무상 계산 방식, 수수료 반영 여부에 따라 달라진다.

## 온체인 소스

- PEPE 토큰: https://eth.blockscout.com/address/0x6982508145454Ce325dDbE47a25d4ec3d2311933
- 트레이더 지갑: https://eth.blockscout.com/address/0x8DF79cD8695921a2dE2616105D761b65Ce6CEf4f
- 매수 TX: https://eth.blockscout.com/tx/0xef71c686c56757d19d80c4b28600359d56d63335d4fad2ff7acda00bce2fa6d4
- 매도 TX: https://eth.blockscout.com/tx/0x624b8dfc89d368ebec22630dd638d1762f2b25d559aed59b59a0d393c198c6b5
- PEPE/WETH V2 pool: https://eth.blockscout.com/address/0xA43fe16908251ee70EF74718545e4FE6C5cCEc9f
- PEPE/WETH V3 pool: https://eth.blockscout.com/address/0x11950d141EcB863F01007AdD7D1A342041227b58
- PEPE whale wallet: https://etherscan.io/address/0x2daabb7d7d8114EE334D5A141A97ef181e565e69
- PEPE deposit 후보 TX 1: https://etherscan.io/tx/0x8075349ca187f85663e21588cd04941fe7f200bcad97736c531348e3595a9cd9
- PEPE deposit 후보 TX 2: https://etherscan.io/tx/0x6a01417dc912e91dd70599e3d4d10c758672313c77af677da3a47d841dd4c651
- PEPE deposit 후보 수신 주소: https://etherscan.io/address/0xF45De557A63B2Cf2C17449B15840f03A1336BF6a
- Lookonchain 보조 근거: https://x.com/lookonchain/status/1856899988221227162
