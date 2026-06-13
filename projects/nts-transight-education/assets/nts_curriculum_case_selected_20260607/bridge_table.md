# Bridge Transfers Table

이미지 파일: `bridge table.png`

테이블명: `common.bridge_transfers`

이 테이블은 bridge source chain에서 발생한 입금/lock/burn 이벤트와 destination chain에서 발생한 출금/mint/release 이벤트를 한 row로 연결하기 위한 매핑 테이블이다.

## Source Side Columns

| column | type | 의미 |
|---|---|---|
| `source_chain` | `LowCardinality(String)` | 출발 체인. 예: `ethereum`, `arbitrum`, `base`, `solana` |
| `source_address` | `String` | 출발 체인에서 bridge를 실행한 원 주소. 보통 depositor/sender/user wallet |
| `tx_hash` | `String` | 출발 체인의 bridge 입금/lock/burn transaction hash |
| `block_timestamp` | `DateTime` | 출발 tx가 포함된 block timestamp |
| `block_number` | `UInt64` | 출발 tx가 포함된 block number |
| `log_index` | `UInt32` | 출발 tx 안에서 bridge event 또는 token transfer event의 log index |
| `token_address` | `String` | 출발 체인에서 이동한 token contract address. native coin이면 별도 sentinel 값 필요 |
| `amount` | `UInt256` | 출발 체인에서 bridge로 들어간 token amount. raw integer 단위 |
| `value_usd` | `Float64` | 출발 amount의 USD 환산값 |

## Destination Side Columns

| column | type | 의미 |
|---|---|---|
| `destination_chain` | `LowCardinality(String)` | 도착 체인 |
| `destination_address` | `String` | 도착 체인에서 asset을 받은 주소. 보통 recipient/user wallet |
| `dest_tx_hash` | `String` | 도착 체인의 출금/mint/release transaction hash |
| `dest_token_address` | `String` | 도착 체인에서 수령한 token contract address. native coin이면 별도 sentinel 값 필요 |
| `dest_amount` | `UInt256` | 도착 체인에서 수령한 token amount. raw integer 단위 |
| `dest_value_usd` | `Float64` | 도착 amount의 USD 환산값 |

## Indexes

| index | column | 목적 |
|---|---|---|
| `idx_src_addr` | `source_address` | 특정 출발 주소가 어떤 bridge를 탔는지 빠르게 검색 |
| `idx_dest_addr` | `destination_address` | 특정 도착 주소로 bridge 수령된 내역 검색 |
| `idx_dest_tx` | `dest_tx_hash` | 도착 tx hash에서 source bridge tx를 역추적 |

## Storage Layout

```sql
ENGINE = ReplicatedReplacingMergeTree(...)
PARTITION BY (source_chain, toYYYYMM(block_timestamp))
ORDER BY (source_chain, tx_hash, log_index)
SETTINGS index_granularity = 8192
```

## 분석할 때 읽는 순서

1. `tx_hash`, `source_chain`으로 source bridge tx를 찾는다.
2. `source_address`, `token_address`, `amount`, `value_usd`로 누가 무엇을 얼마만큼 bridge에 넣었는지 본다.
3. `destination_chain`, `destination_address`, `dest_tx_hash`로 도착 체인 수령자를 확인한다.
4. `dest_token_address`, `dest_amount`, `dest_value_usd`로 실제 수령 asset과 수량을 확인한다.
5. `dest_tx_hash`를 기준으로 destination chain explorer에서 후속 이동을 계속 추적한다.

## 주의점

- `amount`와 `dest_amount`는 raw integer다. token decimals를 적용한 display amount와 구분해야 한다.
- source token과 destination token은 같지 않을 수 있다. 예: `ETH -> SOL`, `USDC.e -> USDC`, wrapped token -> native token.
- bridge fee, relayer fee, slippage 때문에 `amount`와 `dest_amount`의 USD value가 다를 수 있다.
- `source_address`와 `destination_address`가 같지 않을 수 있다. bridge UI에서 다른 recipient를 지정하거나 CEX deposit address로 바로 보내는 경우가 있다.
- `dest_tx_hash`가 비어 있거나 늦게 채워지는 bridge가 있을 수 있다. 이 경우 API/status endpoint 또는 protocol-specific event 매핑이 필요하다.

## Scratch Example Row: Relay Polygon USDC.e -> Ethereum ETH -> Bitget

Source tx: `0xe3c3f2701430b9690b138165048d94c8851124a9bbda41ed790b41163ddc68b5`

Relay request id: `0x7c61139430ca94814658a94a4a19afde21879e63afebae0aa5a2e83f19d918b0`

이 tx는 Polygon에서 `32.744273 USDC.e`를 Relay solver로 보내고, Ethereum에서 `0.009703355477162923 ETH`를 `Bitget: Hot Wallet`로 수령시키는 cross-chain swap/bridge다. 다만 **Legion/FUEL claim recipient와 무관한 별도 스크래치 예시**이므로, 7번 Legion case의 채택 seed로 쓰지 않는다.

### Search Network / Chain

```text
Source side: Polygon PoS
Destination side: Ethereum Mainnet
Relay API: request id 또는 source tx hash로 조회
```

### Bridge Table Row

| column | value | 비고 |
|---|---|---|
| `source_chain` | `polygon` | Relay `originChainId = 137` |
| `source_address` | `0x67C2ec8fB735A2b92A4453D4270aeceAC70cCB5A` | source token transfer sender / Relay metadata `user` |
| `tx_hash` | `0xe3c3f2701430b9690b138165048d94c8851124a9bbda41ed790b41163ddc68b5` | Polygon source tx |
| `block_timestamp` | `2026-01-16 08:54:44` | UTC |
| `block_number` | `81716856` | Polygon block number |
| `log_index` | `862` | USDC.e transfer to Relay solver |
| `token_address` | `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` | Polygon bridged USDC / USDC.e |
| `amount` | `32744273` | 32.744273 USDC.e, 6 decimals |
| `value_usd` | `32.738346` | Relay metadata `currencyIn.amountUsd` 기준 |
| `destination_chain` | `ethereum` | Relay `destinationChainId = 1` |
| `destination_address` | `0x1AB4973a48dc892Cd9971ECE8e01DcC7688f8F23` | Blockscout/eth-labels 기준 `Bitget: Hot Wallet`, `Exchange` |
| `dest_tx_hash` | `0x7a5d936d20a0ee236c71739a1682cfc7d57b3e72cf3dd77a30946efae850c946` | Ethereum destination tx |
| `dest_token_address` | `0x0000000000000000000000000000000000000000` | native ETH sentinel |
| `dest_amount` | `9703355477162923` | 0.009703355477162923 ETH, internal transfer index 33 |
| `dest_value_usd` | `32.156987` | Relay metadata `currencyOut.amountUsd` 기준 |

### Flow Summary

```text
Polygon
0x67C2...cCB5A
  -> Relay Solver 0xf70d...dbEF
  -> 32.744273 USDC.e

Relay request id
0x7c61139430ca94814658a94a4a19afde21879e63afebae0aa5a2e83f19d918b0
  -> status success
  -> source tx 0xe3c3...68b5
  -> destination tx 0x7a5d...c946

Ethereum
Relay Solver / Router
  -> swap route: USDC -> ETH
  -> 0.009703355477162923 ETH
  -> Bitget: Hot Wallet 0x1AB4...8F23
```

### Important Interpretation Notes

- Source tx의 outer `from`은 `0x02A86f...7E23`이고 Blockscout에서 `Polymarket: Relayer`로 보인다. 하지만 bridge table의 `source_address`는 outer relayer가 아니라 USDC.e가 실제 빠져나간 `0x67C2...cCB5A`로 잡는다.
- Destination tx에서 USDC transfer만 보면 최종 수령자를 놓칠 수 있다. 이 케이스는 Ethereum tx 내부에서 USDC가 swap되고, native ETH internal transfer로 Bitget hot wallet에 도착한다.
- `destination_address = Bitget hot wallet`은 CEX 접점이므로 off-ramp 후보로 볼 수 있다. 다만 특정 Bitget 계정 귀속, 내부 매도, 법정화폐 출금은 Bitget 자료 없이는 확정하지 않는다.
- 금액이 작아서 시각 자료의 임팩트는 약하다. 대신 구조는 매우 깔끔하다: `transparent bridge request -> destination tx -> labeled exchange hot wallet`.

### Insert-like Shape

```sql
-- conceptual row; exact native-token sentinel policy should match production ETL
(
  'polygon',
  '0x67C2ec8fB735A2b92A4453D4270aeceAC70cCB5A',
  '0xe3c3f2701430b9690b138165048d94c8851124a9bbda41ed790b41163ddc68b5',
  toDateTime('2026-01-16 08:54:44'),
  81716856,
  862,
  '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
  32744273,
  32.738346,
  'ethereum',
  '0x1AB4973a48dc892Cd9971ECE8e01DcC7688f8F23',
  '0x7a5d936d20a0ee236c71739a1682cfc7d57b3e72cf3dd77a30946efae850c946',
  '0x0000000000000000000000000000000000000000',
  9703355477162923,
  32.156987
)
```

### Source Links

- Relay request API: https://api.relay.link/requests/v2?id=0x7c61139430ca94814658a94a4a19afde21879e63afebae0aa5a2e83f19d918b0
- Relay status API: https://api.relay.link/intents/status/v3?requestId=0x7c61139430ca94814658a94a4a19afde21879e63afebae0aa5a2e83f19d918b0
- Polygon source tx: https://polygon.blockscout.com/tx/0xe3c3f2701430b9690b138165048d94c8851124a9bbda41ed790b41163ddc68b5
- Ethereum destination tx: https://eth.blockscout.com/tx/0x7a5d936d20a0ee236c71739a1682cfc7d57b3e72cf3dd77a30946efae850c946
- Bitget hot wallet address: https://eth.blockscout.com/address/0x1AB4973a48dc892Cd9971ECE8e01DcC7688f8F23
- eth-labels lookup: https://eth-labels.com/accounts?chainId=1&address=0x1ab4973a48dc892cd9971ece8e01dcc7688f8f23

## Bridge-only Candidate: Mayan ETH -> SOL

Source tx: `0x5a944f80bfc46cbb05654fe0f9f37f5faf0e3286df542247a774a46e1d28035c`

Mayan API 기준 이 tx는 Ethereum에서 1.3 ETH를 넣고 Solana 주소 `7wMvii...UibJ`로 23.296308571 SOL을 받은 bridge/swap이다.

비채택 메모: 이 케이스는 source/destination bridge 매핑 자체는 좋지만, Solana recipient가 받은 SOL을 곧바로 CEX로 보내지 않고 Jupiter로 token 매수에 사용했다. 따라서 "bridge 후 off-ramp/CEX 접점" 강의 seed로는 쓰지 않는다.

| column | value | 비고 |
|---|---|---|
| `source_chain` | `ethereum` | Mayan API `sourceChain = 2` |
| `source_address` | `0xa37fAd0C2302ED045d40BA6133514c664fc63979` | Mayan `trader`, Ethereum tx `from` |
| `tx_hash` | `0x5a944f80bfc46cbb05654fe0f9f37f5faf0e3286df542247a774a46e1d28035c` | Ethereum source tx |
| `block_timestamp` | `2024-12-24 03:23:47` | UTC |
| `block_number` | `21469627` | Ethereum block number |
| `log_index` | `167` | Mayan `OrderCreated` event log index |
| `token_address` | `0x0000000000000000000000000000000000000000` | native ETH sentinel |
| `amount` | `1300000000000000000` | 1.3 ETH, 18 decimals |
| `value_usd` | `4395.975397294` | Mayan `fromTokenPrice = 3381.51953638` 기준 |
| `destination_chain` | `solana` | Mayan API `destChain = 1` |
| `destination_address` | `7wMviiScPGZeFMbXYkS2r7eLp3ogANfukSYPFeRHUibJ` | Solana recipient |
| `dest_tx_hash` | `2zF7YUmX46gif2uTam9uJAYXTDumjsifWGiXMoghEEsiPKp42J2CFYqpxFRbt6j6g8Xa8HbbaSUh4C1K4Ve5yedB` | Solana tx where recipient receives SOL |
| `dest_token_address` | `0x0000000000000000000000000000000000000000` | native SOL sentinel. Internal wrapped SOL mint is `So11111111111111111111111111111111111111112` |
| `dest_amount` | `23296308571` | 23.296308571 SOL, 9 decimals |
| `dest_value_usd` | `4386.12058538225010833` | Mayan `toTokenPrice = 188.27534723` 기준 |

### Mayan-specific Mapping

| Mayan field | bridge table column | value |
|---|---|---|
| `sourceTxHash` | `tx_hash` | `0x5a944f80bfc46cbb05654fe0f9f37f5faf0e3286df542247a774a46e1d28035c` |
| `trader` | `source_address` | `0xa37fAd0C2302ED045d40BA6133514c664fc63979` |
| `destAddress` | `destination_address` | `7wMviiScPGZeFMbXYkS2r7eLp3ogANfukSYPFeRHUibJ` |
| `fromTokenAddress` | `token_address` | `0x0000000000000000000000000000000000000000` |
| `fromAmount64` | `amount` | `1300000000000000000` |
| `fulfillTxHash` / settle tx | `dest_tx_hash` | `2zF7YUmX46gif2uTam9uJAYXTDumjsifWGiXMoghEEsiPKp42J2CFYqpxFRbt6j6g8Xa8HbbaSUh4C1K4Ve5yedB` |
| `toTokenAddress` | `dest_token_address` | `0x0000000000000000000000000000000000000000` |
| `toAmount` | `dest_amount` | display amount `23.296308571`; raw amount `23296308571` |
| `redeemTxHash` | not `dest_tx_hash` | `0x44bacb1c07eef7b1211b239f4f89fe3a23eb6104639cc55356166149c3e492bf`; Ethereum-side solver unlock |

### Insert-like Shape

```sql
-- conceptual row; exact native-token sentinel policy should match production ETL
(
  'ethereum',
  '0xa37fAd0C2302ED045d40BA6133514c664fc63979',
  '0x5a944f80bfc46cbb05654fe0f9f37f5faf0e3286df542247a774a46e1d28035c',
  toDateTime('2024-12-24 03:23:47'),
  21469627,
  167,
  '0x0000000000000000000000000000000000000000',
  1300000000000000000,
  4395.975397294,
  'solana',
  '7wMviiScPGZeFMbXYkS2r7eLp3ogANfukSYPFeRHUibJ',
  '2zF7YUmX46gif2uTam9uJAYXTDumjsifWGiXMoghEEsiPKp42J2CFYqpxFRbt6j6g8Xa8HbbaSUh4C1K4Ve5yedB',
  '0x0000000000000000000000000000000000000000',
  23296308571,
  4386.12058538225010833
)
```
