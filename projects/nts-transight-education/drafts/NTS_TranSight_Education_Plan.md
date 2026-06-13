# 국세청 TranSight 교육 운영 계획안

작성일: 2026-06-07  
대상 사업: 국세청 가상자산 탈세대응 거래추적 SW 라이선스 구매  
대상 기관: 서울지방국세청 및 지방국세청  
제안사: 주식회사 보난자팩토리  
교육 도구: TranSight Web

---

## 1. 교육 설계 방향

본 교육은 국세청 조사관이 TranSight Web을 활용하여 가상자산 탈세대응 업무를 독립적으로 수행할 수 있도록 설계한다. 교육 범위는 단순 로그인 및 기능 사용법을 넘어, 가상자산 기본 구조 이해, 자금세탁·범죄 트렌드 파악, 온체인 분석 기법, 브릿지·스왑·믹서 등 추적 회피 구조 해석, 사건형 케이스 분석 및 조사 산출물 작성까지 포함한다.

제안서상 본 사업의 목적은 단순한 도구 구매가 아니라 다음 세 가지 역량을 국세청 내부에 확보하는 데 있다.

1. **분석 역량**  
   온체인 데이터 기반 주소 추적, 클러스터링, 전·후방 자금 출처 추적, 믹서 디믹싱, OSINT 오프체인 데이터 통합 분석 기능을 활용하여 조사관이 독립적으로 분석할 수 있는 역량 확보

2. **증거 구성 역량**  
   분석 결과를 그래프, 보고서, 케이스 파일로 체계화하여 세무조사 및 심리 단계에서 활용 가능한 증거 패키지로 정리하는 역량 확보

3. **역외 협조 역량**  
   해외 가상자산 거래소에 대한 동결 요청 및 KYC·KYT 정보 제공 요청이 필요한 구간을 식별하고, IAAN 프로토콜 기반 협조 요청 흐름을 이해하는 역량 확보

따라서 교육은 다음의 흐름으로 구성한다.

```text
초급: 사용한다
  -> TranSight 접속, 검색, Transaction Map, 기본 리스크 태그, 기본 보고서 출력

중급: 해석한다
  -> UTXO / Account 모델, DEX swap, bridge, mixer, CEX 입출금 후보, off-ramp 후보 해석

고급: 사건으로 판단한다
  -> 실제·유사 케이스를 바탕으로 분석 가설, 자금흐름표, 과세 이벤트 후보표, 자료 요청서, 한계 메모 작성
```

---

## 2. 전체 교육 회차 및 시간 산정

### 2.1 권장 기준

| 구분 | 기준 |
|---|---:|
| 1차시 권장 시간 | 2시간 |
| 1차시 구성 | 강의 70분 + 실습 35분 + 질의응답/정리 15분 |
| 서울지방국세청 과정 | 8차시 |
| 지방국세청 속성 과정 | 기관별 2차시 |
| 지방국세청 대상 기관 수 | 최대 4개 기관 |
| 총 차시 | 16차시 |
| 총 교육 시간 | 32시간 |

> 운영상 1차시를 90분으로 축소할 수 있으나, TranSight 기능 실습과 케이스 분석을 포함하려면 **1차시 2시간 기준**이 가장 적절하다. 특히 중급·고급 과정은 단순 설명형 강의보다 실습형 분석이 중요하므로, 차시당 최소 100분 이상 확보가 필요하다.

### 2.2 총량 배분

| 교육 대상 | 과정 성격 | 차시 | 시간 | 권장 운영 방식 |
|---|---|---:|---:|---|
| 서울지방국세청 | 정규 심화 과정 | 8차시 | 16시간 | 2일 집중 과정 또는 4회 반일 과정 |
| 지방국세청 A | 속성 과정 | 2차시 | 4시간 | 반일 과정 |
| 지방국세청 B | 속성 과정 | 2차시 | 4시간 | 반일 과정 |
| 지방국세청 C | 속성 과정 | 2차시 | 4시간 | 반일 과정 |
| 지방국세청 D | 속성 과정 | 2차시 | 4시간 | 반일 과정 |
| **합계** |  | **16차시** | **32시간** |  |

---

## 3. 과정별 교육 목표

| 과정 | 교육 목표 | 주요 대상 | 종료 시점 역량 |
|---|---|---|---|
| 초급 | TranSight Web 기본 사용 및 가상자산 탈세대응 기초 이해 | 신규 사용자, 일반 조사관 | 주소·TX 검색, Transaction Map 조회, 기본 리스크 태그 해석, CSV·이미지·보고서 출력 |
| 중급 | 온체인 구조와 세탁·은닉 경로 해석 | 실무 조사관, 분석 담당자 | UTXO/Account 모델 구분, DEX·브릿지·믹서·CEX 입출금 후보 해석, 과세 이벤트 후보 분류 |
| 고급 | 사건형 케이스 분석 및 조사 산출물 작성 | 심화 분석 담당자, 과학조사 담당자 | 사건 범위 설정, 자금흐름표 작성, evidence table 작성, 자료 요청서 초안 작성, 분석 한계 정리 |

---

## 4. 서울지방국세청 정규 과정: 8차시 구성

서울지방국세청 과정은 본 사업의 핵심 사용자 그룹을 대상으로 하는 정규 심화 과정으로 구성한다. 초급 3차시, 중급 3차시, 고급 2차시로 설계하여 기능 사용, 분석기법, 케이스 산출물 작성을 모두 포함한다.

### 4.1 서울청 8차시 총괄표

| 차시 | 과정 | 주제 | 핵심 내용 | 방식 | 권장 시간 |
|---:|---|---|---|---|---:|
| 1차시 | 초급 | TranSight 로그인 및 기본 기능 사용 | 계정 로그인, OTP, 검색, 주소·TX 상세, Transaction Map, 저장·내보내기 | 강의+시연+기초실습 | 2시간 |
| 2차시 | 초급 | 가상자산 기본 이해 | 블록체인, 주소, TX, 토큰, 지갑, CEX/DEX, UTXO/Account 개념 입문 | 강의+퀴즈 | 2시간 |
| 3차시 | 초급 | 최근 가상자산 범죄·자금세탁 트렌드 | 역외탈세, 차명·분산 보관, 믹서, 브릿지, OTC, 다크웹, 고위험 엔티티 | 강의+사례토론 | 2시간 |
| 4차시 | 중급 | 분석기법 1: UTXO / Account 모델별 추적 | BTC UTXO, change address, CIOH, ETH/TRON account 모델, 토큰 전송 해석 | 강의+맵 실습 | 2시간 |
| 5차시 | 중급 | 분석기법 2: 브릿징·스왑·믹서 추적 | Bridge, DEX swap, aggregator, mixer, CoinJoin, Tornado Cash, 추적 단절 구간 | 강의+실습 | 2시간 |
| 6차시 | 중급 | 분석기법 3: 중급 분석 응용 | CEX deposit 후보, hot/sweep wallet, OSINT, Auto Trace, evidence table 작성 | 실습+산출물 작성 | 2시간 |
| 7차시 | 고급 | 케이스 분석 1·2 | 사건 intake, seed register, cross-chain flow, 거래소 자료 요청 포인트 | 팀 실습 | 2시간 |
| 8차시 | 고급 | 케이스 분석 3 및 최종 산출물 리뷰 | 자금흐름 요약, 과세 이벤트 후보표, limitation note, 보고서 리뷰 | 팀 발표+피드백 | 2시간 |

---

## 5. 서울청 차시별 세부 커리큘럼

### 1차시. TranSight 로그인, 기능 및 세부 기능 사용 방법

**목표**  
교육생이 TranSight Web에 접속하여 주소·트랜잭션을 검색하고, Transaction Map을 통해 기본 자금 흐름을 확인할 수 있도록 한다.

**주요 내용**

- 기관 계정 로그인 및 Google Authenticator OTP 사용
- 사용자 보안 수칙 및 계정 관리 원칙
- 주소 검색, TX 검색, Entity 검색의 차이
- 주소 상세 화면, TX 상세 화면, Entity 정보 화면 이해
- Transaction Map 기본 조작
- Entity Cluster, Batch/Single View, Force/Tree View 전환
- USD/KRW/Token 단위 전환
- UTC/Local 시간 기준 전환
- 메모, 라벨, 색상 지정
- 그래프 이미지, CSV, 보고서 출력
- 케이스 저장 및 폴더 관리

**실습**

- 샘플 주소 검색
- Transaction Map 생성
- 특정 노드 메모 작성
- CSV 및 이미지 내보내기

**산출물**

- 개인별 샘플 Transaction Map 1개
- 주소 목록 CSV 1개

---

### 2차시. 가상자산에 대한 기본 이해

**목표**  
가상자산 조사에 필요한 최소 기술 개념을 이해하고, 온체인 데이터로 확인 가능한 사실과 외부 자료가 필요한 사실을 구분한다.

**주요 내용**

- 블록체인과 원장 구조
- 주소, 개인키, 지갑, 트랜잭션, 블록의 의미
- Native coin과 token의 차이
- CEX, DEX, DeFi, Bridge, Mixer, OTC 개념
- BTC UTXO 모델 개요
- ETH/TRON/BSC 등 Account 모델 개요
- 토큰 전송과 컨트랙트 호출의 차이
- 온체인에서 보이는 것과 보이지 않는 것
- 세무조사 관점의 핵심 질문
  - 누가 수령했는가?
  - 언제 취득했는가?
  - 언제 처분했는가?
  - 단순 이동인가, 과세 이벤트 후보인가?
  - 원화화 또는 현금화 후보 지점은 어디인가?

**실습**

- 주소 / TX / token transfer 구분
- 단순 transfer와 contract interaction 비교

**산출물**

- 기본 용어 체크리스트
- 온체인 확인 가능 정보 / 추가 요청 필요 정보 구분표

---

### 3차시. 최근 가상자산 범죄 및 자금세탁 트렌드

**목표**  
최근 가상자산 탈세·은닉·자금세탁 유형을 이해하고, TranSight에서 어떤 신호를 확인해야 하는지 파악한다.

**주요 내용**

- 가상자산 탈세대응 주요 유형
  - 변칙 상속·증여
  - 역외탈세
  - 고액 무기명 자산 은닉
  - 차명 지갑 및 분산 보관
  - 해외 거래소 경유 현금화
- 범죄·자금세탁 트렌드
  - Mixer 및 CoinJoin
  - DEX swap 및 aggregator
  - Bridge 기반 cross-chain 이동
  - 다크웹·텔레그램·OTC 브로커 활용
  - 고위험 거래소 및 미신고 VASP 활용
- 조세조사 관점의 위험 신호
  - 반복적 소액 분산
  - 고액 입금 후 단기 분산
  - CEX deposit 후보 반복
  - bridge 이후 추적 단절
  - mixer 또는 sanctioned entity 접촉

**실습**

- 고위험 엔티티 라벨 확인
- 위험 태그 기반 주소 해석

**산출물**

- 위험 신호 체크리스트
- 고위험 엔티티 확인 메모

---

### 4차시. 분석기법 1: UTXO / Account 모델별 추적

**목표**  
체인별 거래 구조 차이를 이해하고, BTC 계열과 ETH/TRON 계열 분석 시 다른 관점으로 접근할 수 있도록 한다.

**주요 내용**

- UTXO 모델 분석
  - input/output 구조
  - change address
  - Common Input Ownership Heuristic
  - sweep transaction
  - CoinJoin 의심 구조
- Account 모델 분석
  - account balance 변화
  - native transfer와 token transfer
  - internal transaction
  - contract call
  - gas fee funder
- 체인별 주의사항
  - BTC
  - ETH / BSC / Polygon / Arbitrum / Optimism
  - TRON
  - XRP destination tag
- Transaction Map에서 모델별 흐름 읽는 법

**실습**

- BTC 샘플 TX에서 input/output 구조 확인
- EVM 샘플 TX에서 token transfer와 contract call 확인

**산출물**

- UTXO 분석 메모
- Account 모델 분석 메모

---

### 5차시. 분석기법 2: 브릿징, 스왑, 믹서

**목표**  
자금세탁과 추적 회피에 자주 활용되는 bridge, swap, mixer 구조를 구분하고, 추적 단절 구간을 evidence 중심으로 정리한다.

**주요 내용**

- DEX swap 분석
  - router
  - pool
  - aggregator
  - input token / output token
  - slippage / fee
- Bridge 분석
  - source chain / destination chain
  - source TX / destination TX
  - recipient address
  - bridge event log
  - cross-chain 추적 시 한계
- Mixer 분석
  - mixer contract
  - CoinJoin
  - Tornado Cash류 구조
  - mixer 이후 자금 흐름 해석 한계
- 세무 관점의 해석
  - token-to-token 교환 후보
  - 단순 이동 후보
  - 처분 후보
  - 추가 자료 요청 필요 구간

**실습**

- DEX swap TX 해석
- bridge 전후 TX 연결
- mixer 접촉 주소의 위험 신호 정리

**산출물**

- swap evidence table
- bridge flow table
- mixer limitation note

---

### 6차시. 분석기법 3: 기타 중급 분석 기법

**목표**  
실무에서 자주 발생하는 CEX 접점, OSINT, Auto Trace, 자료 요청 포인트를 종합적으로 다룬다.

**주요 내용**

- CEX deposit / withdrawal 후보 구분
- deposit address, hot wallet, sweep wallet, omnibus wallet 구조
- CEX 입금과 실제 매도 확정의 차이
- 온체인으로 확인 가능한 정보와 거래소 내부 장부가 필요한 정보
- Auto Trace 활용
  - 금액순
  - 최신순
  - 위험순
  - 기간 필터
  - 노이즈 브랜치 제거
- OSINT 오프체인 데이터 활용
  - 다크웹
  - 텔레그램
  - OTC 브로커
  - 국내 범죄 특화 데이터
- evidence table 작성법
- information request draft 작성법

**실습**

- CEX deposit 후보 추적
- Auto Trace로 endpoint 후보 탐색
- 자료 요청 항목 도출

**산출물**

- exchange contact evidence table
- information request draft

---

### 7차시. 고급 케이스 분석 1·2

**목표**  
여러 주소, 여러 체인, 여러 거래 유형이 섞인 사건을 케이스 단위로 분석하고, 조사 가설과 추적 범위를 설정한다.

**주요 내용**

- Case intake 방법
- seed address / seed TX / chain / token / 기간 범위 설정
- 분석 가설 수립
- 제외 범위 및 한계 설정
- wallet-level timeline 작성
- cross-chain flow 복원
- CEX 접점 후보 정리
- 자료 요청 우선순위 설정

**권장 케이스**

- 케이스 1: 해외 CEX 출금 → 개인 지갑 → DEX swap → 국내 CEX deposit 후보
- 케이스 2: Airdrop claim → swap → bridge → CEX deposit 후보

**실습**

- 팀별 seed register 작성
- 자금흐름 타임라인 작성
- cross-chain flow table 작성

**산출물**

- seed register
- wallet activity timeline
- cross-chain flow table

---

### 8차시. 고급 케이스 분석 3 및 최종 산출물 리뷰

**목표**  
복합 케이스를 바탕으로 국세청 내부 업무에 활용 가능한 분석 메모, 과세 이벤트 후보표, 자료 요청서, 한계 메모를 작성한다.

**주요 내용**

- 사건형 케이스 종합 분석
- 수령 후보 / 처분 후보 / 단순 이동 / off-ramp 후보 / 추가 확인 필요 구간 분류
- 과세 이벤트 후보표 작성
- 자금흐름 요약표 작성
- 거래소·프로젝트 대상 자료 요청서 초안 작성
- confidence / limitation 작성
- 분석 결과 발표 및 피드백

**권장 케이스**

- 케이스 3: Polymarket 또는 유사 prediction market / DeFi 손익 케이스
- 보조 케이스: GMX v2, LP pool, RWA token, NFT trading 등

**실습**

- 팀별 tax investigation memo 작성
- 발표용 1-page summary 작성
- 강사 리뷰 및 보완

**산출물**

- tax investigation memo
- taxable event candidate table
- information request draft
- final limitation note

---

## 6. 서울청 2일 집중 운영안

서울청 8차시는 2일 집중 과정으로 운영하는 것이 가장 효율적이다. 단, 조사관 일정상 2일 연속 교육이 어렵다면 4회 반일 과정으로 분할 운영할 수 있다.

### 6.1 2일 집중 과정

| 일자 | 시간 | 차시 | 주제 |
|---|---:|---:|---|
| 1일차 | 09:30-11:30 | 1차시 | TranSight 로그인 및 기본 기능 사용 |
| 1일차 | 13:00-15:00 | 2차시 | 가상자산 기본 이해 |
| 1일차 | 15:20-17:20 | 3차시 | 최근 범죄·자금세탁 트렌드 |
| 1일차 | 17:20-17:50 | 보충 | 질의응답 및 개인 실습 보완 |
| 2일차 | 09:30-11:30 | 4차시 | UTXO / Account 모델별 추적 |
| 2일차 | 13:00-15:00 | 5차시 | 브릿징·스왑·믹서 추적 |
| 2일차 | 15:20-17:20 | 6차시 | CEX 접점·OSINT·Auto Trace 응용 |
| 2일차 | 별도 반일 | 7~8차시 | 케이스 분석 및 최종 산출물 리뷰 |

> 2일 연속 운영 시 7~8차시까지 모두 포함하려면 일자별 교육 시간이 과도해질 수 있으므로, 실제 운영은 **2일+반일** 또는 **4회 반일** 방식이 더 안정적이다.

### 6.2 4회 반일 과정

| 회차 | 차시 | 구성 | 시간 |
|---:|---|---|---:|
| 1회 | 1~2차시 | 기본 기능 + 가상자산 기본 이해 | 4시간 |
| 2회 | 3~4차시 | 범죄 트렌드 + UTXO/Account 분석 | 4시간 |
| 3회 | 5~6차시 | 브릿지·스왑·믹서 + CEX/OSINT/Auto Trace | 4시간 |
| 4회 | 7~8차시 | 케이스 분석 + 산출물 리뷰 | 4시간 |

**권장안: 4회 반일 과정**  
이 방식은 교육생의 현업 공백을 줄이고, 각 회차 사이에 실제 업무에서 TranSight를 사용해본 뒤 다음 회차에서 질문과 보완을 진행할 수 있다는 장점이 있다.

---

## 7. 지방국세청 속성 과정: 기관별 2차시 구성

지방국세청 과정은 2차시 속성 교육으로 구성한다. 제한된 시간 내에 초급·중급·고급 내용을 모두 다루기 어렵기 때문에, 실무 즉시 활용성이 높은 내용 중심으로 압축한다.

### 7.1 지방청 2차시 총괄표

| 차시 | 주제 | 핵심 내용 | 방식 | 권장 시간 |
|---:|---|---|---|---:|
| 1차시 | TranSight 기본 사용 및 가상자산 탈세대응 기초 | 로그인, 검색, Transaction Map, 주소·TX 상세, 기본 리스크 태그, 가상자산 기본 구조, 최근 트렌드 | 강의+시연 | 2시간 |
| 2차시 | 핵심 분석기법 및 케이스 속성 실습 | UTXO/Account 차이, bridge/swap/mixer, CEX deposit 후보, Auto Trace, 자료 요청 포인트, 미니 케이스 | 강의+실습 | 2시간 |

### 7.2 지방청 1차시 세부 내용

**주제**  
TranSight 기본 사용 및 가상자산 탈세대응 기초

**주요 내용**

- TranSight 로그인 및 OTP
- 주소·TX 검색
- Transaction Map 기본 조회
- Entity 라벨 및 리스크 태그 이해
- 그래프 이미지·CSV·보고서 출력
- 가상자산 기본 구조
- CEX / DEX / Bridge / Mixer 개념
- 최근 가상자산 탈세·자금세탁 트렌드
- 온체인 분석으로 확인 가능한 것과 추가 자료가 필요한 것

**실습**

- 샘플 주소 검색
- Transaction Map 생성
- 리스크 태그 확인

**산출물**

- 기본 분석 화면 캡처
- 샘플 주소 메모

### 7.3 지방청 2차시 세부 내용

**주제**  
핵심 분석기법 및 케이스 속성 실습

**주요 내용**

- UTXO / Account 모델 차이
- token transfer와 contract call 차이
- DEX swap 해석
- bridge 전후 자금흐름 해석
- mixer 접촉 여부 확인
- CEX deposit 후보와 실제 매도 확정의 차이
- Auto Trace 기본 활용
- 자료 요청서 작성 포인트
- 케이스형 미니 실습

**실습**

- CEX deposit 후보 탐색
- bridge 또는 swap TX 해석
- 추가 확인 필요 자료 정리

**산출물**

- 미니 evidence table
- information request memo

---

## 8. 지방청 4개 기관 운영 계획

| 기관 | 차시 | 시간 | 구성 | 비고 |
|---|---:|---:|---|---|
| 지방국세청 A | 2차시 | 4시간 | 기본 사용 + 핵심 분석기법 | 반일 과정 |
| 지방국세청 B | 2차시 | 4시간 | 기본 사용 + 핵심 분석기법 | 반일 과정 |
| 지방국세청 C | 2차시 | 4시간 | 기본 사용 + 핵심 분석기법 | 반일 과정 |
| 지방국세청 D | 2차시 | 4시간 | 기본 사용 + 핵심 분석기법 | 반일 과정 |
| **합계** | **8차시** | **16시간** |  |  |

---

## 9. 초급·중급·고급 과정별 세부 모듈

### 9.1 초급 과정

| 모듈 | 제목 | 주요 내용 | 권장 시간 |
|---:|---|---|---:|
| 초급-1 | TranSight 기본 기능 | 로그인, OTP, 검색, 주소·TX 상세, Transaction Map, 저장·내보내기 | 2시간 |
| 초급-2 | 가상자산 기본 이해 | 블록체인, 주소, 지갑, TX, token, CEX/DEX, UTXO/Account 기본 | 2시간 |
| 초급-3 | 범죄·자금세탁 트렌드 | 역외탈세, 믹서, 브릿지, OTC, 다크웹, 고위험 엔티티 | 2시간 |

### 9.2 중급 과정

| 모듈 | 제목 | 주요 내용 | 권장 시간 |
|---:|---|---|---:|
| 중급-1 | UTXO / Account 분석 | BTC input/output, change, CIOH, EVM token transfer, contract call | 2시간 |
| 중급-2 | 브릿지·스왑·믹서 | DEX swap, bridge source/destination, mixer, CoinJoin, Tornado Cash류 구조 | 2시간 |
| 중급-3 | 중급 분석 응용 | CEX deposit 후보, Auto Trace, OSINT, evidence table, 자료 요청 초안 | 2시간 |

### 9.3 고급 과정

| 모듈 | 제목 | 주요 내용 | 권장 시간 |
|---:|---|---|---:|
| 고급-1 | 케이스 분석 1·2 | seed register, wallet timeline, cross-chain flow, CEX 접점 분석 | 2시간 |
| 고급-2 | 케이스 분석 3 및 산출물 리뷰 | 과세 이벤트 후보표, 자금흐름표, 자료 요청서, limitation note, 발표·피드백 | 2시간 |

---

## 10. 교육 실습 산출물

교육은 강의 종료 후 실제 업무에 활용할 수 있는 산출물을 남기는 방식으로 운영한다.

| 산출물 | 설명 | 적용 차시 |
|---|---|---|
| Transaction Map 캡처 | 분석 대상 주소의 자금 흐름 그래프 | 초급 1차시 |
| 주소 목록 CSV | 주요 주소, Entity, 총 전송액, 입출금 TX 수 정리 | 초급 1차시 |
| 온체인 확인 가능 정보 / 추가 자료 필요 정보 구분표 | 온체인 근거와 외부 요청 자료 분리 | 초급 2차시 |
| 위험 신호 체크리스트 | 믹서, 브릿지, 고위험 엔티티, 분산 패턴 등 | 초급 3차시 |
| UTXO 분석 메모 | input/output, change, cluster 후보 | 중급 1차시 |
| Account 모델 분석 메모 | token transfer, contract call, internal transaction | 중급 1차시 |
| swap evidence table | input token, output token, router, pool, fee 등 | 중급 2차시 |
| bridge flow table | source TX, destination TX, recipient, chain | 중급 2차시 |
| exchange contact evidence table | CEX deposit 후보, hot wallet, 자료 요청 필요성 | 중급 3차시 |
| information request draft | 거래소·프로젝트 대상 요청 자료 초안 | 중급 3차시, 고급 |
| seed register | 사건 분석 시작점 정리 | 고급 1차시 |
| wallet activity timeline | 지갑 단위 수령·이동·처분 후보 타임라인 | 고급 1차시 |
| taxable event candidate table | 수령·처분·단순 이동·off-ramp 후보 분류 | 고급 2차시 |
| final limitation note | 단정 가능 / 단정 불가 / 추가 확인 필요 사항 | 고급 2차시 |
| tax investigation memo | 최종 분석 요약 및 조사 메모 | 고급 2차시 |

---

## 11. 권장 케이스 구성

| 난이도 | 케이스 | 교육 목적 | 적용 과정 |
|---|---|---|---|
| 기초 | 단순 CEX withdrawal → 개인 지갑 | 거래소 출금과 개인 지갑 이동 이해 | 초급 |
| 기초 | 개인 지갑 → CEX deposit 후보 | off-ramp 후보와 실제 매도 확정의 차이 이해 | 초급·중급 |
| 중급 | 기본 DEX swap | token-to-token 교환 후보 분석 | 중급 |
| 중급 | Airdrop claim → swap → deposit 후보 | 수령 원인, 수령 시점, 이후 처분 후보 분류 | 중급 |
| 중급 | Bridge source/destination 연결 | cross-chain 추적과 한계 이해 | 중급 |
| 중급 | 국내 CEX 연계 아비트라지 | 국내 거래소 자료 요청 필요성 이해 | 중급·고급 |
| 고급 | Prediction market / Polymarket류 케이스 | 정산액, 출금액, 실제 손익 차이 이해 | 고급 |
| 고급 | DeFi LP / vault / perp 케이스 | 원금, 수익, 보상, 청산, 수수료 구분 | 고급 |
| 고급 | RWA 또는 token sale 케이스 | 온체인 이전과 오프체인 권리관계 분리 | 고급 |

---

## 12. 교육자료 구성

| 자료 | 형식 | 내용 |
|---|---|---|
| 교육용 슬라이드 | PDF / PPT | 차시별 개념, 화면 캡처, 주요 체크포인트 |
| 실습 주소·TX 목록 | Excel / Markdown | 난이도별 샘플 주소 및 TX |
| TranSight 기능 매뉴얼 | PDF / Web | 로그인, 검색, 맵, 보고서, 케이스 관리 |
| 분석 산출물 템플릿 | Excel / Markdown | evidence table, bridge table, 자료 요청서 등 |
| 용어집 | PDF / Markdown | CEX, DEX, bridge, mixer, UTXO, Account, KYT 등 |
| 케이스 해설지 | PDF / Markdown | 실습 케이스별 정답 예시 및 해석 한계 |

---

## 13. 교육 운영 인력

| 역할 | 주요 업무 |
|---|---|
| 총괄 강사 | 전체 교육 진행, 가상자산 분석 방법론 설명, 고급 케이스 리뷰 |
| 제품 사용 지원 강사 | TranSight 기능 시연, 로그인·검색·맵·보고서 실습 지원 |
| 분석 지원 강사 | 중급·고급 케이스 해설, evidence table 및 자료 요청서 작성 지원 |
| 기술 지원 담당 | 교육 중 계정, 접속, OTP, 네트워크, 화면 오류 대응 |

---

## 14. 교육 운영 방식

### 14.1 사전 준비

- 교육 대상자 명단 수령
- 계정 발급 및 OTP 사전 안내
- 교육장 네트워크 및 접속 가능 여부 확인
- 샘플 주소·TX 및 실습 데이터 사전 준비
- 교육용 계정 또는 샘플 케이스 접근 권한 설정
- 보안상 실제 사건 데이터 사용 여부 사전 협의

### 14.2 교육 중 운영

- 강의 50~60%, 실습 30~40%, 질의응답 10% 비율 권장
- 서울청 과정은 팀별 실습 포함
- 지방청 과정은 시연 중심 + 미니 실습으로 압축
- 실제 사건과 유사한 구조를 사용하되, 민감정보는 제거한 샘플 데이터 활용
- 실습 산출물은 교육 후 회수 또는 공유 범위를 사전 협의

### 14.3 교육 후 지원

- 교육자료 PDF 제공
- 기능별 Q&A 정리본 제공
- 주요 실습 산출물 템플릿 제공
- 교육 후 1~2주 내 follow-up Q&A 세션 권장
- 실제 업무 중 분석 문의는 제안서상 수시 기술 지원 체계와 연계

---

## 15. 최종 권장안

이번 계약의 교육 총량은 **총 16차시, 32시간**으로 설계하는 것이 적절하다.

가장 권장되는 운영 방식은 다음과 같다.

```text
서울지방국세청: 8차시 / 16시간
  - 초급 3차시
  - 중급 3차시
  - 고급 2차시
  - 운영 방식: 4회 반일 과정 권장

지방국세청: 2차시 / 4시간 × 최대 4개 기관
  - 1차시: TranSight 기본 사용 + 가상자산 기초 + 범죄 트렌드
  - 2차시: 핵심 분석기법 + 미니 케이스 실습

총계: 16차시 / 32시간
```

이 구성은 제안서상 교육 훈련 계획의 “사용자 수준별 한국어 교육”, “실제 탈세대응 업무에 활용 가능한 시나리오형 실습”, “주소 검색·거래 흐름 분석·고위험 엔티티 식별·믹서·브릿지·스왑 경로 해석·보고서 작성·케이스 관리”라는 요구를 모두 반영한다.

또한 서울청은 과학조사담당관실 중심의 심화 사용기관이므로 8차시 정규 과정을 통해 독립 분석 역량과 산출물 작성 역량까지 확보하도록 하고, 지방청은 2차시 속성 과정을 통해 기본 사용법과 핵심 위험 신호 식별 능력을 우선 확보하는 방식이 현실적이다.
