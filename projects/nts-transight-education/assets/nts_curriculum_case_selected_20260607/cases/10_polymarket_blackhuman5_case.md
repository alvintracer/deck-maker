# Polymarket BlackHuman5 Seoul Mayoral Case

## Scope

| Field | Value |
|---|---|
| Base case | `10_polymarket.md` / Candidate B |
| Supporting screening | `10_polymarket_seoul_pnl_screening.md` row 29 |
| Supporting outflow match | `10_polymarket_seoul_redeem_outflow_matches.md` row 29 |
| Public Polymarket profile | `https://polymarket.com/@blackhuman5?tab=activity` |
| Profile display name | `BlackHuman5` |
| Proxy wallet | `0xa89da419310851c4731f24370c25f1e040f9d0a2` |
| Chain for Polymarket activity | Polygon PoS mainnet (chainId 137) |
| Bridge destination chain | BNB Chain (chainId 56) |
| Selected market | `Will Oh Se-hoon win the 2026 Seoul Mayoral Election` |
| Condition ID | `0xc587bda904f031a973ad3cb57128ca011bfab0f45e6cb3734ed2227c4d4be419` |
| Winning position | `Oh Se-hoon YES` |

## Why This Case

이 케이스는 국세청 강의에서 바로 쓰기 좋다.

- 공개 프로필상 `Joined May 2025`, `Biggest Win $9,560.00`, `Predictions 4`라서 시장 참여 규모가 과하지 않고 설명이 단순하다.
- 서울시장 이벤트의 국내 맥락이 직관적이다.
- `YES 10,000 shares`를 `0.044`에 매수하고, 정산 후 `10,000`을 받은 구조라 손익 계산이 깔끔하다.
- 정산 후 Relay를 통해 Polygon에서 BNB Chain으로 이동한 흐름까지 이어져 bridge/off-ramp 후보 설명이 가능하다.
- 다만 BNB Chain 수령 주소가 거래소 입금주소라고 확정된 상태는 아니므로, 강의에서는 `bridge/outflow candidate`로만 둔다.

## Core Story

```text
Polymarket profile @blackhuman5
  -> Polygon proxy wallet 0xa89...d0a2
  -> Oh Se-hoon YES position buy
     10,000 shares bought for 440.00
  -> market resolved
  -> winning position redeem
     10,000.00 received
  -> Relay withdrawal
     12,054.00 USDC.e moved from Polygon to BNB Chain
```

주의할 점은 출금액 `12,054.00`이 서울시장 정산액 `10,000.00`보다 크다는 점이다. 차액 `2,054.00`은 기존 Polymarket 잔고, 다른 시장 매도/정산, rebate 등이 섞였을 가능성이 있으므로 서울시장 이벤트 수익으로 전액 귀속하면 안 된다.

## Seoul Market PnL

| Step | UTC time | Chain | Type | TX | Amount / price | Interpretation |
|---|---|---|---|---|---|---|
| 1 | 2026-06-03 17:19:43 | Polygon PoS | BUY | `0x8a41da06dd274a5af40bcc20f39e7441f42ee4996bd35ed2ab96d9fc5d24c93f` | `10,000` YES at `0.044`, cost `440.00` | position acquisition cost candidate |
| 2 | 2026-06-04 08:45:06 | Polygon PoS | REDEEM | `0xd3dc9358cbe5ef3943ec4197b5c266dce71bbf94fdf9171a27abca2984f412f7` | `10,000.00` | winning position settlement candidate |

```text
Total in  = 440.00
Total out = 10,000.00
PnL       = 9,560.00
ROI       = 2,172.73%
```

## Wallet-Level Activity Summary

이 프로필은 서울시장 이벤트 하나만 한 것이 아니라, 한국 정치 관련 4개 시장을 거래했다. 따라서 지갑 단위 수익을 말할 때는 전체 activity도 같이 보여주는 편이 좋다.

| Market | Total buy cost | Sell proceeds | Redeem proceeds | PnL |
|---|---:|---:|---:|---:|
| Will Lee Jae-myung be elected the next president of South Korea? | 19,236.298000 | 20,000.569800 | 0.000000 | 764.271800 |
| Will Choo Kyung-ho win the 2026 Daegu mayoral election? | 12,144.802301 | 537.140920 | 14,999.995160 | 3,392.333779 |
| Will Kim Boo-kyum win the 2026 Daegu mayoral election? | 327.622760 | 454.930000 | 0.000000 | 127.307240 |
| Will Oh Se-hoon win the 2026 Seoul Mayoral Election | 440.000000 | 0.000000 | 10,000.000000 | 9,560.000000 |
| Total trading PnL | 32,148.723061 | 20,992.640720 | 24,999.995160 | 13,843.912819 |

Maker rebate `7.934400`까지 더하면 wallet-level realized gain 후보는 `13,851.847219`다. 이 값은 Polymarket activity API 기준의 계산값이며, 세무상 확정 소득금액은 수수료, 환율, 귀속자, 인식시점 검토가 필요하다.

## Post-Redeem Relay Flow

서울시장 정산 후 같은 proxy wallet에서 Relay 출금이 발생한다.

| Field | Value |
|---|---|
| Source chain | Polygon PoS mainnet (chainId 137) |
| Source address | `0xa89da419310851c4731f24370c25f1e040f9d0a2` |
| Source token | USDC.e `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` |
| Source amount | `12,054.00` |
| Source tx | `0x17362bd886f50470c5d2caddeafcb03ae91377b1ba0f6bf6780d344fe31c6fa0` |
| Bridge / destination on source chain | RelayDepository `0x4cD00E387622C35bDDB9b4c962C136462338BC31` |
| Relay request id | `0x43cc6964cd88a4bd1929453140d0287eb4a190053a3112223af8bc6cfe0a5dd3` |
| Destination chain | BNB Chain (chainId 56) |
| Destination recipient | `0x44E5F5De33bAE82CC8f80D3D4E4E3fB171aC4950` |
| Destination token | USDC `0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d` |
| Destination amount | `12,054.00` |
| Destination tx | `0x1e7114da58b5557cc02ebc58ddc9ef9179cfb2563a0fd970e890a011fdf6f3dd` |
| Current classification | Relay withdrawal / bridge candidate |

Source tx 안의 토큰 흐름은 아래처럼 읽는다.

```text
0xa89...d0a2
  -> Polymarket USD token / pUSD routing
     PUSD 12,054.00 burn/withdrawal-like movement

0xc417...9db1
  -> 0xa89...d0a2
     USDC.e 12,054.00

0xa89...d0a2
  -> 0x4cD0...BC31 RelayDepository
     USDC.e 12,054.00

Relay API
  -> BNB Chain fill tx
     0xf70d...dbef solver sends 12,054.00 USDC to 0x44E5...4950
```

같은 proxy wallet에는 추가 Relay 출금도 있다.

| Source tx | Created at | Source amount | Destination recipient | Destination tx | Note |
|---|---|---:|---|---|---|
| `0x00aa23b656dd89dd45374479cbf297b854cfd6f043ad70ff5a3c437d214ef6c4` | 2026-06-04 11:12:12 UTC | 13,019.525276 | `0xa136682A468A3ebF114bC635F8f6DF0b19efEaeA` | `0x8015e6b9f11e9330b346177e34d7d34b7a66d01c3ad38498358a4d21e54f019f` | 같은 지갑의 후속 출금. 서울시장 정산금과 직접 1:1 귀속하지 않는다. |

## Transight Demo Script

1. `@blackhuman5` 프로필을 보여주고, `Biggest Win $9,560.00`와 `Predictions 4`를 확인한다.
2. Polygon PoS에서 proxy wallet `0xa89...d0a2`를 검색한다.
3. 서울시장 BUY tx `0x8a41...c93f`를 열어 `10,000 YES`, `440.00` 지출을 확인한다.
4. REDEEM tx `0xd3dc...f412f7`를 열어 winning position 정산 `10,000.00`을 확인한다.
5. 같은 wallet timeline에서 이후 money outflow `0x17362...fa0`를 찾는다.
6. `0x17362...fa0`에서 pUSD burn/withdrawal-like movement와 USDC.e `12,054.00` RelayDepository 이동을 확인한다.
7. Relay API 또는 Relay UI로 source tx와 BNB Chain destination tx `0x1e711...f3dd`를 연결한다.
8. BNB Chain recipient `0x44E5...4950`는 거래소 입금주소로 확정하지 않고, 후속 주소 라벨과 1-hop/2-hop sweep을 추가 조사해야 한다고 설명한다.

## Evidence Table

| Evidence | Chain | Link |
|---|---|---|
| Public profile | Web | https://polymarket.com/@blackhuman5?tab=activity |
| Polymarket activity API | Web/API | https://data-api.polymarket.com/activity?user=0xa89da419310851c4731f24370c25f1e040f9d0a2&limit=100 |
| Seoul BUY tx | Polygon PoS | https://polygon.blockscout.com/tx/0x8a41da06dd274a5af40bcc20f39e7441f42ee4996bd35ed2ab96d9fc5d24c93f |
| Seoul REDEEM tx | Polygon PoS | https://polygon.blockscout.com/tx/0xd3dc9358cbe5ef3943ec4197b5c266dce71bbf94fdf9171a27abca2984f412f7 |
| Relay source tx | Polygon PoS | https://polygon.blockscout.com/tx/0x17362bd886f50470c5d2caddeafcb03ae91377b1ba0f6bf6780d344fe31c6fa0 |
| Relay request API | Web/API | https://api.relay.link/requests/v2?hash=0x17362bd886f50470c5d2caddeafcb03ae91377b1ba0f6bf6780d344fe31c6fa0 |
| Relay destination tx | BNB Chain | https://bscscan.com/tx/0x1e7114da58b5557cc02ebc58ddc9ef9179cfb2563a0fd970e890a011fdf6f3dd |

## Tax / Investigation Notes

- Polymarket profile name과 proxy wallet은 납세자 실명, 거주자성, 계정 귀속의 확정 근거가 아니다.
- 서울시장 market 손익 후보는 `440.00 -> 10,000.00`, 즉 `9,560.00`으로 설명할 수 있다.
- wallet-level activity 기준으로는 다른 한국 정치 시장 손익과 maker rebate까지 합산해야 한다.
- Relay 출금액 `12,054.00`은 서울시장 정산액보다 크므로, 전액을 서울시장 수익 처분으로 단정하지 않는다.
- BNB Chain recipient는 현재 `bridge destination / external wallet candidate`로 둔다. CEX 입금 확정에는 recipient 라벨, 후속 sweep, 거래소 자료, 계정 매칭이 필요하다.
- 세무상 소득 구분과 인식 시점은 prediction market의 법적 성격, 정산 시점, 환율 적용 기준, 실제 환전 여부에 따라 별도 검토한다.
