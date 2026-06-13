# 9. Pharos Vault Case

## 목적

Pharos 생태계의 RWA vault 상품을 소재로, `deposit -> receipt/share token -> vault rate 변경 -> redeem request / operator settlement 또는 bridge/send` 흐름에서 경제적 이익 취득 후보가 어디에 나타나는지 설명한다.

이 케이스는 국세청 교육용 심화 사례다. 수익이 단순한 토큰 전송 1건으로 보이지 않고, share token의 교환비율 또는 vault rate 변경으로 반영될 수 있다는 점을 보여주는 데 초점을 둔다.

## 핵심 질문

```text
USDC를 vault에 예치하면 pALPHA 같은 receipt/share token으로 바뀐다.
이후 vault rate, share price, redeem request, settlement, bridge/send 결과가 변할 때 어느 시점과 금액을
"경제적 이익 취득 후보"로 볼 수 있는가?
```

## 케이스 요약

- 대상 상품: Ember Pharos Alpha / pALPHA
- 성격: USDC 기반 RWA yield vault, pALPHA receipt/share token 발행
- 주요 근거: Etherscan verified contract/event, vaults.fyi 상품 페이지, Trading Strategy vault profile, Yield Network case study
- 교육상 포인트: 예치 원금, share token 수령, vault rate 업데이트, 출금/상환을 분리해 봐야 한다.

## 중요한 한계

Pharos를 이름에 둔 vault이지만, 확인 가능한 핵심 온체인 seed는 현재 `Ethereum Mainnet`의 `Ember Pharos Alpha (pALPHA)` vault 계약이다. vaults.fyi는 pALPHA가 Pharos와 Ethereum 사이에서 LayerZero로 bridge 가능하고 Pharos ecosystem에서 조합 가능하다고 설명하지만, 이 문서에서 확보한 입금, 발행, rate update, redeem request, operator settlement, bridge/send seed 및 실패 withdraw seed는 Pharos chain tx가 아니라 Ethereum tx다.

따라서 본 케이스의 결론은 보수적으로 써야 한다. Pharos ecosystem incentive, points, reward top-up은 과세상 이익 후보가 될 수 있으나, 이 문서의 seed만으로는 개별 지갑별 확정 지급액과 귀속 시점을 단정하지 않는다.

## 경제적 이익 취득 방식

- 사용자가 USDC를 vault에 deposit한다.
- vault는 pALPHA receipt/share token을 mint한다.
- vault의 `VaultRateUpdated` 이벤트 또는 외부 dashboard의 share price 변화로 underlying 가치 변화가 관찰된다.
- redeem/withdraw 요청 자체는 수익 실현으로 단정하지 않는다. 사용자가 받는 USDC, 또는 사용자를 대리하는 정산 계정의 입금과 실제 귀속 자료가 확인될 때 기존 취득가액/원금과의 차이가 경제적 이익 후보가 된다.
- Pharos ecosystem incentive, points, reward가 별도 지급된다면 그 지급 이벤트, claim 내역, 약관, 포인트 산식이 추가로 필요하다.

## Seed

```text
Transight search network / chain
Ethereum / Ethereum Mainnet (chainId 1)

Vault / share token
0xC3AaCb558aFB635307B66FDb405188138576fc4c
Ember Pharos Alpha (pALPHA)

Collateral token
0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
Circle USDC on Ethereum Mainnet

Vault creation TX
0xd9c7f4be449424ca6c37bbcf02da8d308015a21e9f2ef56545bd1d0afa0a9576
status ok. VaultCreated: collateralToken=USDC, 초기 rate=1.0(1e18 scale, rate=1000000000000000000)
operator=0x116046991e3F0B0967723073a87820eF5edB29f2, rateProvider=0x291C3315707A8Ebcd6a6D202cA639002eA4Ff01D
subAccounts=[0xeD8808F1e839be43b448D03184Da3E9CfA19D14e], feePercentage=0, maxTVL=75000000(USDC, raw 75000000000000)

Deposit with permit TX
0x273210e4eb068e206694fcb32d6b2b81f2f600e240fc4b5e72a7f32e67df4d3e
status ok, method=depositWithPermit, depositor=0xF0669Ef23b776Bb5998920647996BB3A137CA52A
USDC 1,011 -> vault, pALPHA 1,010.508872 mint(0x000 -> depositor)

Vault rate update TX
0x15993137cca297f0b1d5cd02eec3bfd2407363d567d20db79e9a84e94b432ff6
status ok, method=updateVaultRate, 호출자=rateProvider(0x291C3315707A8Ebcd6a6D202cA639002eA4Ff01D)
VaultRateUpdated previousRate=0.986504273, newRate=0.985230181 (1e18 scale)
주의: 이 seed에서는 rate가 소폭 하락했다. rate는 오를 수도 내릴 수도 있는 평가/회계 변동 근거이지 현금 지급이 아니다.

Redeem request TX (상환 요청 예시, USDC 수령 아님)
0x2d708d3ff85f6797c718d58bf52825611625f7d142f96e57a7d5f71a92f2c71e
2026-04-12 20:30:47 UTC, status ok, method=redeemShares
owner/receiver=0x74588DD3661781BFA0b497C613aD861B3Dae6F32
pALPHA 50.000000이 owner -> vault로 이동하고, RequestRedeemed sequenceNumber=1030 발생
같은 TX에 USDC 수령은 없다.

Operator settlement / subAccount withdrawal TX (운영 정산 예시, 사용자 직접 수령 아님)
0x954d599e948f02d907b2348d10b3301d02d5fcd2aff69daa979c6bf3f3ab5ab6
2026-05-15 12:01:59 UTC, status ok, method=withdrawFromVaultWithoutRedeemingShares
caller=0x71da2342b11AE27aF0a7E2507eCeF6CC89572738, subAccount=0xeD8808F1e839be43b448D03184Da3E9CfA19D14e
USDC 47.474204가 vault -> subAccount로 이동하고, VaultWithdrawalWithoutRedeemingShares sequenceNumber=4545 발생
이 TX는 정산용 보조 계정으로의 운영 이동이므로 특정 사용자 소득 귀속 근거로 바로 쓰면 안 된다.

pALPHA bridge/send (cross-chain burn) TX
0x5758c4725ba1cac3d1d3be66efe6409fe33655bc974855b20303c016fc56481e
2026-05-27 14:05:11 UTC, status ok, pALPHA 999.514216 소각(-> 0x000)
요청 지갑=0xa9798102cEa07A07e5aFdd55129C584D54c3D9ea, OFT 컨트랙트(0xC6507ef17265B4Eed37aE901D939A6b977C5CbA3, LayerZero OFT adapter — send의 to이자 OFTSent emitter. LayerZero relayer/DVN이 아님) 경유, method=send
실제 구조: LayerZero OFT cross-chain burn(BridgeBurn + OFTSent, dstEid 30407)으로 pALPHA를 소각하고 다른 chain으로 bridge한다. 같은 TX에 USDC 수령은 없다.

Reverted withdraw TX (실패 예시 — status 확인 교육용, 실제 시연 흐름 아님)
0x090cb4f4b8a790e50c2d146c6aa61b6cac4c61b3f8c183588a164389c62ff9fb
status error / Reverted, withdrawFromVaultWithoutRedeemingShares
```

> 주의: `0x5758c472...`는 실제 USDC redeem/withdraw seed가 아니라 LayerZero OFT 방식의 pALPHA bridge/send seed다. pALPHA가 `BridgeBurn`/`OFTSent`로 소각되고 다른 chain으로 이동하는 구조이며, 같은 TX에 USDC 수령은 없다. 따라서 이 TX를 상환 완료나 USDC 수령 근거로 쓰면 안 된다. `0x2d708d...` 같은 `redeemShares` TX도 pALPHA가 vault로 들어가고 `RequestRedeemed`가 남는 상환 요청이지, 같은 TX에서 USDC가 지급되는 구조가 아니다. 실제 경제적 이익 실현 후보는 별도 settlement에서 사용자 또는 사용자 귀속 계정으로 USDC 수령이 확인될 때 판단한다. 온체인 `VaultCreated` 기준 vault의 권한 주소는 operator `0x116046991e3F0B0967723073a87820eF5edB29f2`, rateProvider `0x291C3315707A8Ebcd6a6D202cA639002eA4Ff01D`이며, `0xeD8808F1e839be43b448D03184Da3E9CfA19D14e`는 operator가 아니라 vault의 subAccount(정산용 보조 계정)로 등록돼 있다. 단일 TX에 소각·수령이 같이 보이는 깔끔한 redeem 예시가 필요하면 아래 "대체 가능한 vault-yield seed"의 Spark sDAI 등을 쓴다.

## 추가 온체인 스캔 메모 (2026-06-04)

Ethereum RPC 로그 필터로 vault 생성 block `24314684`부터 block `25243486`까지 확인했다.

- `RequestRedeemed`: 71건. `redeemShares` 호출로 pALPHA가 `owner -> vault`로 이동하고 요청 이벤트가 남는다.
- 표준 ERC-4626 `Withdraw`: 0건. 사용자에게 USDC가 같은 TX에서 바로 나가는 깔끔한 withdraw 이벤트는 확인되지 않았다.
- `VaultWithdrawalWithoutRedeemingShares`: 143건. USDC가 vault에서 subAccount로 이동하는 운영 정산 이벤트이며, 특정 사용자 수익 귀속은 별도 자료가 필요하다.

## 근거 링크

- Vault app/profile: [vaults.fyi - Ember Pharos Alpha](https://app.vaults.fyi/opportunity/mainnet/0xC3AaCb558aFB635307B66FDb405188138576fc4c)
- Explorer vault/token: [Etherscan - pALPHA vault](https://etherscan.io/address/0xC3AaCb558aFB635307B66FDb405188138576fc4c)
- Explorer token tracker: [Etherscan - Ember Pharos Alpha token](https://etherscan.io/token/0xC3AaCb558aFB635307B66FDb405188138576fc4c)
- Deposit tx: [Etherscan - 0x273210e4...](https://etherscan.io/tx/0x273210e4eb068e206694fcb32d6b2b81f2f600e240fc4b5e72a7f32e67df4d3e)
- Vault creation tx: [Etherscan - 0xd9c7f4be...](https://etherscan.io/tx/0xd9c7f4be449424ca6c37bbcf02da8d308015a21e9f2ef56545bd1d0afa0a9576)
- Vault rate update tx: [Etherscan - 0x15993137...](https://etherscan.io/tx/0x15993137cca297f0b1d5cd02eec3bfd2407363d567d20db79e9a84e94b432ff6)
- Redeem request tx: [Etherscan - 0x2d708d3f...](https://etherscan.io/tx/0x2d708d3ff85f6797c718d58bf52825611625f7d142f96e57a7d5f71a92f2c71e)
- Operator settlement tx: [Etherscan - 0x954d599e...](https://etherscan.io/tx/0x954d599e948f02d907b2348d10b3301d02d5fcd2aff69daa979c6bf3f3ab5ab6)
- pALPHA bridge/send tx: [Etherscan - 0x5758c472...](https://etherscan.io/tx/0x5758c4725ba1cac3d1d3be66efe6409fe33655bc974855b20303c016fc56481e)
- Reverted withdraw tx (실패 예시): [Etherscan - 0x090cb4f4...](https://etherscan.io/tx/0x090cb4f4b8a790e50c2d146c6aa61b6cac4c61b3f8c183588a164389c62ff9fb)
- Market/profile reference: [Trading Strategy - Ember Pharos Alpha](https://tradingstrategy.ai/trading-view/vaults/ember-pharos-alpha)
- RWA vault structure background: [Yield Network - Pharos RWA Vault case study](https://www.yieldnetwork.io/blog/pharos-rwa-vault-case-study)
- Pharos official site: [Pharos](https://www.pharos.xyz/)
- Pharos official docs: [About Pharos Network](https://docs.pharosnetwork.xyz/introduction)
- Pharos official entry point: [Pharos Network Linktree](https://linktr.ee/PharosNetwork)

## 예상 Flow

```text
wallet
  -> USDC approve 또는 permit
  -> vault deposit
  -> pALPHA mint
  -> vault rate/share price update
  -> redeemShares로 상환 요청 또는 LayerZero OFT bridge/send
  -> redeem request / bridge/send는 USDC 수령이 아니며, operator settlement / USDC 정산은 별도 TX와 별도 시점 확인 필요
  -> 사용자 또는 사용자 귀속 계정의 USDC 수령이 실제 확인된 뒤에야 swap/CEX deposit 후보 추적
```

## 강의 스토리

1. 수강자에게 "입금 tx 하나만 보면 수익이 보이는가?"라고 질문한다.
2. Deposit tx에서 USDC가 vault로 이동하고 pALPHA가 mint되는 장면을 보여준다. 이 단계는 대체로 자산 형태 변경 후보이지, 수익 실현으로 단정하기 어렵다.
3. Vault creation event와 rate update event를 비교한다. 초기 rate는 `1.0`(1e18 scale)으로 생성되지만, 이후 `VaultRateUpdated`에서 rate가 변경된다. 확인된 rate update seed에서는 rate가 `0.986504273` -> `0.985230181`로 소폭 하락했는데, 이는 rate가 항상 오르지는 않으며 평가/회계 변동 근거일 뿐 현금 지급이 아니라는 점을 보여주는 데 쓸 수 있다.
4. `redeemShares` tx와 실제 USDC settlement를 구분한다. `0x2d708d...`는 pALPHA가 vault로 이동하고 `RequestRedeemed`가 남는 요청 단계이며, 같은 TX에 USDC 수령이 없다.
5. pALPHA bridge/send tx와 withdraw/redeem tx를 구분한다. 이 seed의 `0x5758...`은 pALPHA가 LayerZero OFT로 소각되어 다른 chain으로 이동하는 bridge/send이고, USDC 수령이 같은 TX에 있지 않다. 실제 상환/정산 판단에는 별도 USDC 수령 TX가 필요하다.
6. 결론에서는 "예치 시점", "rate/share price 변화 시점", "redeem request 시점", "USDC settlement 시점", "별도 reward/points claim 시점"을 분리해 판단해야 한다고 정리한다.

## Transight 시연 포인트

- `Ethereum / Ethereum Mainnet (chainId 1)`에서 vault 주소 `0xC3AaCb558aFB635307B66FDb405188138576fc4c`를 검색한다.
- `0x273210e4...` deposit tx를 열어 USDC transfer와 pALPHA mint를 같은 tx 안에서 확인한다.
- 같은 wallet `0xF0669Ef23b776Bb5998920647996BB3A137CA52A` 기준으로 전후 pALPHA balance, USDC balance 변화를 비교한다.
- `0x15993137...` rate update tx의 `VaultRateUpdated` event를 확인하고, 이 event가 직접 지급이 아니라 회계상/가격상 변동 근거라는 점을 설명한다.
- `0x2d708d3f...` redeem request tx를 열어 pALPHA 50.000000이 `owner -> vault`로 이동하고 `RequestRedeemed`가 발생하지만, 같은 TX에 USDC transfer가 없다는 점을 확인한다.
- `0x954d599e...` operator settlement tx를 열어 USDC 47.474204가 `vault -> subAccount`로 이동하는 장면을 보여준다. 이 주소는 사용자 지갑이 아니라 정산용 보조 계정이므로, 이용자별 귀속은 추가 자료가 필요하다고 설명한다.
- `0x5758c472...` bridge/send tx를 열어 pALPHA 소각과 `BridgeBurn`/`OFTSent`를 확인한다. 이 TX는 USDC redeem/withdraw가 아니며, 요청 지갑은 deposit 지갑(`0xF0669Ef2...`)과 다른 `0xa9798102...`임을 함께 확인한다.
- `0x090cb4f4...` reverted withdraw tx도 열어 `status error / Reverted`를 보여주고, "실패 TX는 자산 이동이 없으므로 시연 흐름에 쓰지 않는다"는 점을 강조한다.
- 이후 별도 정산 TX에서 USDC 수령이 확인되는지 먼저 찾고, 확인된 USDC 또는 pALPHA가 DEX, bridge, CEX deposit 주소로 이동하는지 추적한다.

## Evidence Table

| 단계 | Chain | TX / Address | Transight search network / chain | Evidence | 분류 | 비고 |
|---|---|---|---|---|---|---|
| 1 | Ethereum Mainnet | `0xC3AaCb558aFB635307B66FDb405188138576fc4c` | Ethereum / Ethereum Mainnet (chainId 1) | Etherscan token/contract, vaults.fyi profile | vault/share token | Ember Pharos Alpha, pALPHA, ERC-4626 계열 구현 |
| 2 | Ethereum Mainnet | `0xd9c7f4be449424ca6c37bbcf02da8d308015a21e9f2ef56545bd1d0afa0a9576` | Ethereum / Ethereum Mainnet (chainId 1) | status ok, `VaultCreated`, collateralToken USDC, name/symbol, rate, maxTVL | vault 생성 | 초기 rate 1.0(1e18), maxTVL 75,000,000 USDC, fee 0%, operator `0x116046991e...`, rateProvider `0x291C3315...`, subAccount `0xeD8808F1...` |
| 3 | Ethereum Mainnet | `0x273210e4eb068e206694fcb32d6b2b81f2f600e240fc4b5e72a7f32e67df4d3e` | Ethereum / Ethereum Mainnet (chainId 1) | USDC transfer to vault, pALPHA mint from zero address, `VaultDeposit` | deposit/position 생성 | 1,011 USDC 입금, 1,010.508872 pALPHA mint |
| 4 | Ethereum Mainnet | `0x15993137cca297f0b1d5cd02eec3bfd2407363d567d20db79e9a84e94b432ff6` | Ethereum / Ethereum Mainnet (chainId 1) | status ok, `VaultRateUpdated(previousRate=0.986504273, newRate=0.985230181)`, 호출자 rateProvider `0x291C3315...` | valuation/yield 후보 | 직접 지급이 아니라 share/accounting value 변화 후보. 이 seed에서는 rate가 소폭 하락(상승만 가정하지 말 것) |
| 5 | Ethereum Mainnet | `0x2d708d3ff85f6797c718d58bf52825611625f7d142f96e57a7d5f71a92f2c71e` | Ethereum / Ethereum Mainnet (chainId 1) | status ok, `redeemShares`, pALPHA 50.000000 `owner -> vault`, `RequestRedeemed(sequenceNumber=1030)` | redeem request 후보 | 같은 TX에 USDC 수령 없음. 상환 완료가 아니라 요청 단계로 설명 |
| 6 | Ethereum Mainnet | `0x954d599e948f02d907b2348d10b3301d02d5fcd2aff69daa979c6bf3f3ab5ab6` | Ethereum / Ethereum Mainnet (chainId 1) | status ok, `withdrawFromVaultWithoutRedeemingShares`, USDC 47.474204 `vault -> subAccount`, `VaultWithdrawalWithoutRedeemingShares(sequenceNumber=4545)` | operator settlement 후보 | subAccount는 정산용 보조 계정. 사용자 직접 수령 또는 소득 귀속 근거로 단정 금지 |
| 7 | Ethereum Mainnet | `0x5758c4725ba1cac3d1d3be66efe6409fe33655bc974855b20303c016fc56481e` | Ethereum / Ethereum Mainnet (chainId 1) | status ok, pALPHA 999.514216 소각(-> 0x000), `BridgeBurn`/`OFTSent`(dstEid 30407), OFT 컨트랙트 경유 `send` | bridge/send 후보 | 요청 지갑 `0xa9798102...`(deposit 지갑과 다름). 같은 TX에 USDC 수령 없음. 실제 redeem/withdraw 또는 USDC 정산 TX는 별도 확보 필요 |
| 7b | Ethereum Mainnet | `0x090cb4f4b8a790e50c2d146c6aa61b6cac4c61b3f8c183588a164389c62ff9fb` | Ethereum / Ethereum Mainnet (chainId 1) | status error / Reverted, `withdrawFromVaultWithoutRedeemingShares` | 실패 TX (시연 제외) | 자산 이동 없음. status 확인 교육용으로만 사용 |
| 8 | Ethereum Mainnet | `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48` | Ethereum / Ethereum Mainnet (chainId 1) | Circle USDC token | underlying asset | 원금/수익 계산 기준 토큰 |

## 국세청 추가 요청자료

- Deposit 시점 USDC 수량, 원화 환산가, 취득가액
- pALPHA mint 수량과 당시 vault rate/share price
- 각 rate update의 산식, 관리자, oracle 또는 rate provider 권한 자료
- Bridge/send 시점 pALPHA 소각량, 목적 chain, 수령 주소 자료
- Redeem request, operator settlement, 최종 사용자 귀속 USDC 수령량, fee, settlement window 자료
- Pharos ecosystem incentive 또는 points가 있었다면 campaign 약관, 포인트 산식, claim tx, 지급 token 정보
- 프로젝트 dashboard 캡처, account statement, investor report, KYC/subscription agreement
- CEX 내부 매도, 출금, 원화 환전 자료

## 세무상 판단 후보

- Deposit: USDC가 pALPHA로 바뀌는 포지션 생성 후보. 이 단계만으로 과세소득 발생을 단정하지 않는다.
- Vault rate/share price 변동: rate가 오르면 경제적 가치 증가 후보다(확인된 seed에서는 오히려 소폭 하락했으므로 항상 상승을 가정하면 안 된다). 다만 미실현 평가손익인지, 과세 가능한 확정 이익인지는 상품 약관과 권리 확정성을 추가 확인해야 한다.
- Bridge/send: pALPHA가 다른 chain으로 이동하는 자산 이전 후보. 이 TX만으로 USDC 수령이나 수익 실현을 단정하지 않는다.
- Redeem request: 상환 신청/권리 행사 후보. 같은 TX에 USDC 수령이 없으면 수익 실현으로 단정하지 않는다.
- Operator settlement: vault와 subAccount 사이의 정산 후보. 사용자별 귀속 자료가 있어야 실제 소득 판단에 연결된다.
- Final USDC receipt: 실제 사용자 또는 사용자 귀속 계정의 USDC 수령 시점이 경제적 이익 실현 후보. 원금, 수수료, 환율, 취득가액 분리가 필요하다.
- Reward/points: 별도 token 또는 포인트가 claim 가능해졌거나 양도 가능해진 시점이 판단 후보. 단순 dashboard point는 과세상 재산적 가치 확정 여부를 추가 확인해야 한다.

## 주의점

- Pharos chain 자체 tx가 아니라 Ethereum mainnet vault seed를 중심으로 구성한 케이스다.
- vaults.fyi와 Trading Strategy의 APY/TVL 수치는 시간에 따라 바뀐다. 강의 당일 최신 화면을 캡처해 보조자료로 붙인다.
- `VaultRateUpdated`는 직접 현금흐름이 아니다. 이를 곧바로 소득 지급으로 처리하면 과대 판단이 될 수 있다.
- RWA vault는 off-chain 자산, 관리자 권한, settlement window, KYC/약관의 영향을 받는다.
- pALPHA 가격, secondary market 거래, bridge 이동은 수익 실현 또는 처분 후보가 될 수 있으나, 각 tx별 대가 관계를 별도로 확인해야 한다.
- `0x2d708d3f...`는 redeem request seed이며, 실제 USDC 수령 seed가 아니다. 요청 TX 한 건만 보고 "상환 완료"로 단정하지 않는다.
- `0x954d599e...`는 subAccount settlement seed이며, 특정 사용자 직접 수령 seed가 아니다. 운영 정산과 사용자 귀속을 분리한다.
- `0x5758c472...`는 pALPHA bridge/send seed이며, 실제 USDC redeem/withdraw seed가 아니다. 소각 TX 한 건만 보고 "USDC 얼마를 받았다"로 단정하지 않는다.
- 상환 요청 TX는 revert될 수 있다(예: `0x090cb4f4...`). 항상 TX status를 먼저 확인하고, 실패 TX는 자산 이동 근거로 쓰지 않는다.

## 대체 가능한 vault-yield seed

Pharos 관련 공식/온체인 근거가 교육 목적에 충분하지 않다고 판단되면, 아래 seed를 보조 케이스로 사용한다. 모두 실제 과세 판단 전에 최신 explorer와 protocol docs 재검증이 필요하다.

| 대체 케이스 | Chain | 주소 | Transight search network / chain | 사용 이유 | 주의점 |
|---|---|---|---|---|---|
| Spark Savings DAI (sDAI) | Ethereum Mainnet | `0x83F20F44975D03b1b09e64809B757c47f942BEeA` | Ethereum / Ethereum Mainnet (chainId 1) | ERC-4626형 yield-bearing token 설명에 적합 | 현재는 후보 주소만 기재. 대표 deposit/redeem TX를 별도 확보해야 시연 seed로 사용 가능 |
| Yearn USDC yVault v2 | Ethereum Mainnet | `0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9` | Ethereum / Ethereum Mainnet (chainId 1) | 오래된 vault deposit/share price/redeem 교육용 seed | 현재는 후보 주소만 기재. 최신 유동성, vault version, 대표 TX 재검증 필요 |
| Aave V3 aUSDC | Ethereum Mainnet | `0x98C23E9d8f34FEFb1B7BD6a91B7FF122F4e16F5c` | Ethereum / Ethereum Mainnet (chainId 1) | yield-bearing receipt token의 원리 설명에 안정적 | 현재는 후보 주소만 기재. lending receipt token이라 Pharos/RWA vault와 구조가 다르고 대표 TX 확보 필요 |
