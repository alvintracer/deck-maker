# 8. BTC-USDC DeFi Pool / LP Case

## 목적

BTC 계열 token과 stablecoin을 pool에 공급한 LP가 어떤 방식으로 경제적 이익을 얻는지 보여준다.

핵심은 `LP position`, `fee accrual`, `fee collect`, `remove liquidity`, `swap 처분`을 섞지 않고 분리해서 보는 것이다. 이 case는 Uniswap V3 WBTC-USDC pool을 사용한다.

## 핵심 질문

```text
LP 제공자는 어떤 자산을 pool에 넣었고,
LP NFT/share, fee, remove liquidity, swap 처분을 어떻게 구분할 것인가?
```

## 검색 체인

이 문서의 주요 seed는 모두 아래 네트워크에서 검색한다.

```text
Transight search network / chain: Ethereum Mainnet
```

## 경제적 이익 취득 방식

- WBTC와 USDC를 Uniswap V3 WBTC-USDC pool에 공급한다.
- Uniswap V3에서는 LP position이 ERC-721 NFT로 표현된다.
- 거래 수수료는 별도 reward token으로 지급되는 것이 아니라, position에 `tokens owed` 형태로 쌓였다가 `collect` 때 WBTC/USDC로 수령된다.
- `remove liquidity`는 LP position의 원본 자산 회수 후보이고, `collect`는 원본 회수분과 fee owed가 같이 나올 수 있다.
- 회수한 WBTC를 USDC로 swap하면 그 부분은 WBTC 처분 후보로 볼 수 있다.
- 이 case에서는 CEX/off-ramp까지 확정하지 않는다. 확인되는 것은 DEX swap과 새 LP position 생성이다.

## Seed

```text
Protocol
Uniswap V3

Pool
WBTC-USDC 0.30% pool

Transight search network / chain
Ethereum Mainnet

Main lifecycle / rebalance TX
0x67dd4b6bbb62966f0dfe68a3dcd784e21e8a5d121a3d22f1ee4057efad1c8303

Block / time
23147412 / 2025-08-15 15:44:23 UTC

TX sender
0xBb1A1a2773a799D83078ae4d59d9F4B2B6aC50fF

Execution contract (on-chain label: AutoRange)
0x88481E2Fbc98d4a251655B0F1A4422555EA72d9E

Position recipient
0xBA0a91e6C5954A605f8A81ff16F0686a475116FE

Old Uniswap V3 position tokenId
1057021

New Uniswap V3 position tokenId
1059017
```

## 주요 주소

| 구분 | 주소 | Transight 검색 체인 | 비고 |
|---|---|---|---|
| WBTC token | `0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599` | Ethereum Mainnet | token0, 8 decimals |
| USDC token | `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48` | Ethereum Mainnet | token1, 6 decimals |
| Uniswap V3 WBTC-USDC pool | `0x99ac8cA7087fA4A2A1FB6357269965A2014ABc35` | Ethereum Mainnet | fee tier 3000 = 0.30% |
| Uniswap V3 Positions NFT | `0xC36442b4a4522E871399CD717aBDD847Ab11FE88` | Ethereum Mainnet | LP position ERC-721 |
| Uniswap Universal Router | `0x3fc91A3afd70395Cd496C647d5a6CC9D4B2b7FAD` | Ethereum Mainnet | WBTC -> USDC swap route |
| TX sender | `0xBb1A1a2773a799D83078ae4d59d9F4B2B6aC50fF` | Ethereum Mainnet | 실행 요청자 후보 |
| Execution contract | `0x88481E2Fbc98d4a251655B0F1A4422555EA72d9E` | Ethereum Mainnet | on-chain label `AutoRange`. LP range 자동관리 contract 후보 |
| Position recipient | `0xBA0a91e6C5954A605f8A81ff16F0686a475116FE` | Ethereum Mainnet | 새 LP NFT 수령 주소 |

## Main Flow

```text
old Uniswap V3 position tokenId 1057021
  -> liquidity decrease
  -> WBTC/USDC collect
  -> collected WBTC 일부를 USDC로 swap
  -> WBTC + USDC를 다시 WBTC-USDC pool에 add liquidity
  -> new Uniswap V3 position NFT tokenId 1059017 mint
  -> position recipient로 NFT transfer
```

이 TX는 일반적인 단순 입금 TX라기보다 `LP rebalance`에 가깝다. 그래서 강의에서는 "하나의 TX 안에 여러 경제 행위가 들어갈 수 있다"는 점을 보여주는 용도로 쓰는 것이 좋다.

## Evidence Table

| 단계 | Chain | TX / Address | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|
| 1 | Ethereum Mainnet | `0x67dd4b6bbb62966f0dfe68a3dcd784e21e8a5d121a3d22f1ee4057efad1c8303` | old position `1057021`에서 `DecreaseLiquidity` 발생. `0.16525094 WBTC`, `0 USDC` | remove liquidity | LP 원본 자산 회수 후보. NFT burn은 이 TX에서 확인되지 않음 |
| 2 | Ethereum Mainnet | `0x67dd4b6bbb62966f0dfe68a3dcd784e21e8a5d121a3d22f1ee4057efad1c8303` | pool -> execution contract: `0.16574505 WBTC`, `28.846829 USDC` | collect | remove 원본 + 누적 fee owed가 섞여 나올 수 있음 |
| 3 | Ethereum Mainnet | `0x67dd4b6bbb62966f0dfe68a3dcd784e21e8a5d121a3d22f1ee4057efad1c8303` | execution contract -> Universal Router: `0.09298848 WBTC`; WBTC-USDC pool -> execution contract: `10,877.703656 USDC` | realized swap 후보 | WBTC 일부를 USDC로 바꾼 처분 후보. CEX/off-ramp 아님 |
| 4 | Ethereum Mainnet | `0x67dd4b6bbb62966f0dfe68a3dcd784e21e8a5d121a3d22f1ee4057efad1c8303` | execution contract -> pool: `0.07260155 WBTC`, `10,883.506162 USDC` | add liquidity | 새 LP position 생성/증액 |
| 5 | Ethereum Mainnet | `0xC36442b4a4522E871399CD717aBDD847Ab11FE88` | Uniswap V3 Positions NFT `tokenId 1059017` mint | LP share receipt | Uniswap V3 LP share는 ERC-721 NFT |
| 6 | Ethereum Mainnet | `0xBA0a91e6C5954A605f8A81ff16F0686a475116FE` | `tokenId 1059017`이 execution contract에서 recipient로 transfer | LP position 소유 후보 | NFT 수령 주소가 liquidity control 후보. 실소유자는 추가 확인 필요 |

## 금액 분리

### 1. Remove liquidity

```text
Old position tokenId
1057021

DecreaseLiquidity amount
0.16525094 WBTC
0 USDC
```

이 단계는 position의 유동성을 줄인 것이다. 이 자체를 fee 수령이나 매도로 보지 않는다.

### 2. Collect

```text
Collect transfer from pool
0.16574505 WBTC
28.846829 USDC
```

`DecreaseLiquidity` amount와 `Collect` transfer가 다르다. 차액인 `0.00049411 WBTC`와 `28.846829 USDC`는 기존 position에 누적된 fee owed 후보로 설명할 수 있다.

다만 이 차액을 세무상 확정 수익으로 바로 단정하면 안 된다. position별 fee accrual, 이전 collect 여부, contract/UI/API 자료, 당시 가격 자료를 같이 봐야 한다.

### 3. Swap

```text
Swap input
0.09298848 WBTC

Swap output
10,877.703656 USDC
```

이 단계는 WBTC 처분 후보로 볼 수 있다. 단, 같은 TX 안에서 바로 새 LP position에 다시 공급되므로, "현금화"나 "off-ramp"라고 표현하지 않는다.

### 4. Add liquidity / new LP NFT

```text
Add liquidity input
0.07260155 WBTC
10,883.506162 USDC

New LP NFT
Uniswap V3 Positions NFT tokenId 1059017
```

새 NFT 수령은 "경제적 이익 수령"이라기보다 새 LP position 취득/재구성으로 분류한다. 이후 수익 여부는 position 종료, collect, 가격 자료까지 연결해야 판단할 수 있다.

## Transight 확인 포인트

- TX hash `0x67dd...1c8303`를 Ethereum Mainnet에서 검색한다.
- Token transfer에서 WBTC/USDC가 pool, execution contract, Universal Router 사이에 어떻게 이동했는지 본다.
- NFT transfer에서 `tokenId 1059017`이 mint되고 recipient로 넘어가는지 확인한다.
- `DecreaseLiquidity`, `Collect`, `IncreaseLiquidity` event를 분리해서 본다.
- `collect`를 reward claim으로 단순화하지 않는다. Uniswap V3 fee는 별도 reward token이 아니라 pool token으로 collect된다.
- swap output USDC가 새 add liquidity에 재사용되는지 확인한다.
- CEX deposit이나 fiat off-ramp는 이 TX만으로 확정하지 않는다.

## 강의용 해석

```text
이 사람은 WBTC와 USDC를 단순히 송금한 것이 아니라,
Uniswap V3의 BTC-USDC LP position을 관리했다.

old position에서 liquidity를 빼고,
그 과정에서 WBTC/USDC를 collect했고,
WBTC 일부를 USDC로 swap한 뒤,
다시 WBTC-USDC pool에 add liquidity해서 새 LP NFT를 받았다.
```

국세청 관점에서 좋은 질문은 다음과 같다.

- 이 TX의 어느 부분이 원본 자산 회수인가?
- 어느 부분이 fee accrual/fee collect 후보인가?
- 어느 부분이 WBTC 처분 후보인가?
- 새 LP NFT 수령은 수익 실현인가, position 재구성인가?
- position recipient와 실제 납세자가 같은지 어떻게 확인할 것인가?
- CEX/off-ramp 확인이 필요한 경우 어떤 추가자료를 요구할 것인가?

## 보조 seed

메인 TX가 너무 복잡하면 아래 TX를 보조 예시로 쓸 수 있다. 둘 다 Ethereum Mainnet에서 검색한다.

| 용도 | Chain | TX | 관찰 포인트 | 비고 |
|---|---|---|---|---|
| collect + swap + add liquidity | Ethereum Mainnet | `0xaa59e5cc51ad0bda668d716c83c062c754098afd22d59e3ae8725d750816eb0d` | `0.00353185 WBTC`, `664.627279 USDC` collect 후 `0.00195118 WBTC -> 225.053871 USDC` swap, `0.00156388 WBTC + 880.872425 USDC` add | Uniswap V3 Positions NFT `tokenId 1072500` |
| collect + swap + add liquidity | Ethereum Mainnet | `0x520ae9f82aaa3bd8946a43ee76378b1a99b4f5df5c2dc7939b081bce3a2576da` | `0.00206979 WBTC`, `114.252446 USDC` collect 후 `0.00086679 WBTC -> 99.976924 USDC` swap, `0.00118943 WBTC + 212.108287 USDC` add | Uniswap V3 Positions NFT `tokenId 1082970` |

보조 seed는 `remove liquidity`가 명확히 들어간 메인 seed보다 범위가 좁다. 대신 금액이 작고 Uniswap V3 Positions NFT contract와 직접 상호작용해서 초급 설명에는 더 편할 수 있다.

두 보조 TX의 swap leg는 모두 WBTC를 USDC로 바꾸는 방향(WBTC in, USDC out)이고, swap 후 USDC가 같은 TX 안에서 다시 add liquidity로 재사용되므로 메인 seed와 동일하게 off-ramp로 보지 않는다.

보조 TX에서 확인되는 주요 주소(추가 추적용, 모두 on-chain 확인):

| 구분 | 주소 | 비고 |
|---|---|---|
| 보조 TX sender (EOA) | `0x3459c71C18B4BC77c55A7cE10BCC5EA45Cd0649B` | 두 보조 TX 공통 실행 요청자. NFT는 처리 후 이 주소로 회수됨 |
| 보조 실행 contract | `0xB50a397543fB2c7D08c53D5f5331AD8990D3B48f` | on-chain label `SelfCompoundor`. collect/swap/add를 대행하는 자동화 contract 후보 |

메인 seed와 마찬가지로 EOA sender와 실행 contract가 다르므로 실소유자 판단은 추가 확인이 필요하다.

## 국세청 추가 요청자료

- Uniswap position tokenId별 생성/변경/collect 이력
- protocol UI 또는 API의 position snapshot
- fee accrual 산정 자료
- TX 시점 WBTC/USDC 가격 자료
- execution contract와 position recipient의 관계 자료
- 지갑 소유자 확인 자료
- CEX 입금/매도/출금 여부를 보려면 거래소 내부 자료

## 주의점

- LP position 취득을 곧바로 수익으로 단정하지 않는다.
- remove liquidity는 원본 자산 회수 후보이고, collect에는 원본 회수분과 fee owed가 섞일 수 있다.
- fee는 별도 reward token이 아니라 WBTC/USDC로 collect된다.
- WBTC -> USDC swap은 처분 후보지만, 이 case에서는 같은 TX 안에서 다시 LP에 공급되므로 off-ramp로 보지 않는다.
- execution contract, TX sender, NFT recipient가 다르므로 소유자 판단은 추가 확인이 필요하다. 특히 이 execution contract는 on-chain label이 `AutoRange`인 자동화 contract여서, TX 실행 주체와 실제 position 소유자가 분리될 수 있다.
- impermanent loss와 LP 순손익은 단일 TX의 transfer만으로 계산하기 어렵다.

## 출처 링크

- Uniswap 작동 방식 / LP share 구조: https://developers.uniswap.org/docs/get-started/concepts/how-uniswap-works
- Uniswap LP fee 설명: https://support.uniswap.org/hc/en-us/articles/20901935681677-What-is-a-liquidity-provider-LP-fee
- Uniswap LP position NFT 설명: https://support.uniswap.org/hc/en-us/articles/20980786685069-Why-is-liquidity-position-ownership-represented-by-tokens-or-NFTs
- Main TX: https://etherscan.io/tx/0x67dd4b6bbb62966f0dfe68a3dcd784e21e8a5d121a3d22f1ee4057efad1c8303
- WBTC-USDC pool: https://etherscan.io/address/0x99ac8ca7087fa4a2a1fb6357269965a2014abc35
- Uniswap V3 Positions NFT: https://etherscan.io/token/0xc36442b4a4522e871399cd717abdd847ab11fe88
- Execution contract / AutoRange 후보: https://etherscan.io/address/0x88481E2Fbc98d4a251655B0F1A4422555EA72d9E
- Position recipient: https://etherscan.io/address/0xBA0a91e6C5954A605f8A81ff16F0686a475116FE
- Uniswap Universal Router: https://etherscan.io/address/0x3fc91A3afd70395Cd496C647d5a6CC9D4B2b7FAD
- Old position tokenId 1057021: https://etherscan.io/nft/0xC36442b4a4522E871399CD717aBDD847Ab11FE88/1057021
- New position tokenId 1059017: https://etherscan.io/nft/0xC36442b4a4522E871399CD717aBDD847Ab11FE88/1059017
- 보조 TX 1: https://etherscan.io/tx/0xaa59e5cc51ad0bda668d716c83c062c754098afd22d59e3ae8725d750816eb0d
- 보조 TX 2: https://etherscan.io/tx/0x520ae9f82aaa3bd8946a43ee76378b1a99b4f5df5c2dc7939b081bce3a2576da
