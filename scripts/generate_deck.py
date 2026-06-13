import os

html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>2026년 가상자산 분석 지원 용역 제안 발표</title>
<style>
@font-face {
  font-family: 'NanumSquare_ac';
  src: url('../fonts/NanumSquare_acL.ttf') format('truetype');
  font-weight: 300;
  font-style: normal;
}
@font-face {
  font-family: 'NanumSquare_ac';
  src: url('../fonts/NanumSquare_acR.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: 'NanumSquare_ac';
  src: url('../fonts/NanumSquare_acB.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: 'NanumSquare_ac';
  src: url('../fonts/NanumSquare_acEB.ttf') format('truetype');
  font-weight: 800;
  font-style: normal;
}
:root{
  --navy: #173A63;
  --navy-dark: #0B1F3A;
  --blue: #1F5F9F;
  --blue-light: #DDEBF7;
  --green: #19733E;
  --green-light: #E7F3EA;
  --red: #8B1E1E;
  --red-light: #F9E6E6;
  --gray-text: #6B7280;
  --gray-line: #C9D1D9;
  --bg: #FFFFFF;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#F7F9FC;color:#102043;font-family:"NanumSquare_ac","NanumSquare","Noto Sans KR","Apple SD Gothic Neo","Malgun Gothic",Arial,sans-serif;}
h1,h2,h3,p{word-break:keep-all;margin:0;}
@page{size:297mm 210mm;margin:0}
.page{width:297mm;min-width:297mm;max-width:297mm;height:210mm;min-height:210mm;max-height:210mm;margin:0 auto 8mm;background:#fff;position:relative;overflow:hidden;padding:15mm 18mm 18mm 18mm;page-break-after:always;box-shadow:0 10px 30px rgba(15,30,60,.10)}
@media print{body{background:#fff}.page{margin:0;box-shadow:none;page-break-after:always}.page:last-child{page-break-after:auto}}
.page:before{content:"";position:absolute;left:0;top:0;width:100%;height:4mm;background:linear-gradient(90deg,var(--navy-dark) 0 50%,var(--navy) 50% 100%)}

.page-footer{position:absolute;left:18mm;right:18mm;bottom:8mm;height:8mm;display:flex;align-items:center;border-top:1px solid var(--gray-line);padding-top:3mm;color:var(--gray-text);font-size:8.5pt;gap:10px}
.footer-brand{display:flex;align-items:center;gap:8px;min-width:70mm}
.footer-logo.bonanza{height:7.5mm;width:auto}
.footer-logo.traverse{height:7.5mm;width:auto}
.sep{height:12px;width:1px;background:var(--gray-line)}
.copyright{flex:1;text-align:center;font-style:italic;}
.page-no{font-weight:700;color:var(--navy-dark);letter-spacing:.06em}

h1{font-size:38pt;line-height:1.2;color:var(--navy-dark);margin-bottom:8mm}
h2{font-size:30pt;line-height:1.3;color:var(--navy);margin-bottom:4mm}
h3{font-size:16pt;color:var(--navy);margin-bottom:2mm}
p{font-size:11pt;line-height:1.6;color:#47566b}

.section-head{margin-bottom:8mm; border-bottom: 2px solid var(--navy); padding-bottom: 4mm;}
.section-head.compact{margin-bottom:6mm;}
.section-head p.kicker{font-size:22pt;color:var(--blue);font-weight:700;margin-top:2mm;}
.section-head.center{text-align:center;margin-top:10mm;border-bottom:none;}

.cover{padding-top:25mm; position:relative;}
.cover-subtitle{font-size:18pt;color:var(--gray-text);margin-top:10mm;line-height:1.5;font-weight:700;}
.cover-logos{position:absolute; right:20mm; bottom: 30mm; display:flex; align-items:center; gap: 8mm;}
.cover-date{font-size: 14pt; color: #4d5b70; font-weight: 800; letter-spacing: 0.05em; margin-top: 5mm;}

.flex-row{display:flex; gap: 8mm; align-items: stretch;}
.flex-col{display:flex; flex-direction: column; gap: 6mm;}

.card{border:1px solid var(--gray-line);border-radius:4mm;padding:6mm;background:#fff;flex:1;}
.card.bg-light{background:#F7F9FC;}
.card h3{margin-bottom: 3mm; font-size: 15pt; border-bottom: 1px solid var(--gray-line); padding-bottom: 3mm;}

.table-styled{width:100%;border-collapse:collapse;font-size:11pt;border:1px solid var(--gray-line); border-radius:4mm; overflow:hidden;}
.table-styled th{background:var(--navy);color:#fff;text-align:left;padding:3mm 4mm;font-weight:700;}
.table-styled td{padding:3mm 4mm;border-bottom:1px solid var(--gray-line);vertical-align:middle;}
.table-styled tr:last-child td{border-bottom:none;}
.table-styled td:first-child{background:var(--blue-light);font-weight:700;}

.process-flow{display:flex;align-items:center;gap:4mm;justify-content:space-between; margin-top: 5mm;}
.process-step{flex:1;background:#fff;border:2px solid var(--blue-light);border-radius:4mm;padding:5mm;text-align:center;position:relative; min-height: 25mm; display:flex; flex-direction:column; justify-content:center;}
.process-step b{display:block;font-size:14pt;color:var(--navy);margin-bottom:2mm;}
.process-step span{font-size:10pt;color:var(--gray-text);}
.process-arrow{color:var(--navy);font-size:20pt;font-weight:bold;}

.img-slot{border:2px dashed #9CA3AF;background:#F3F4F6;display:flex;align-items:center;justify-content:center;flex-direction:column;padding:10px;text-align:center;height:100%;min-height:50mm; border-radius: 4mm;}
.img-slot b{color:var(--navy);font-size:14pt;margin-bottom:4mm;}
.img-slot span{color:var(--gray-text);font-size:10pt;}

.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:8mm;}
.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6mm;}
.grid-2x3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6mm;grid-template-rows:1fr 1fr;}

.roadmap{display:flex;gap:2mm; margin-top: 10mm;}
.roadmap-step{flex:1;padding:5mm;border-radius:4mm;color:#fff;font-weight:700;font-size:12pt;text-align:center;}
.roadmap-step:nth-child(1){background:var(--navy-dark);}
.roadmap-step:nth-child(2){background:var(--navy);}
.roadmap-step:nth-child(3){background:var(--blue);}
.roadmap-step:nth-child(4){background:#4080bf;}
.roadmap-step:nth-child(5){background:var(--green);}

.quote-panel{width:220mm;margin:4mm auto 9mm;border:1px solid #dce5f2;border-radius:6mm;padding:10mm 13mm;background:#F7F9FC;position:relative}
.quote-panel:before{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;background:var(--navy);border-radius:6mm 0 0 6mm}
.quote-panel p{font-size:18pt;line-height:1.55;color:var(--navy-dark);font-weight:700;letter-spacing:-.03em}

ul.bullet-list { margin:0; padding-left:5mm; font-size:11pt; color:#47566b; line-height:1.6; }
ul.bullet-list li { margin-bottom: 2mm; }

</style>
</head>
<body>

<!-- Slide 1 -->
<section class="page cover">
  <div style="font-size:14pt;font-weight:700;color:var(--navy);margin-bottom:5mm;">보난자팩토리 · 트라버스 컨소시엄 / 2026.06</div>
  <h1>2026년 가상자산 분석 지원 용역 제안 발표</h1>
  <div class="cover-subtitle">자체 KYT 솔루션과 실전 수사 지원 인력이 결합된<br/>경찰청 가상자산 범죄 대응 파트너</div>
  
  <div class="cover-logos">
    <div class="img-slot" style="min-width: 45mm; min-height: 20mm; padding: 5px;">
        <b>[IMAGE SLOT]</b><span>Bonanza Factory Logo</span>
    </div>
    <span style="font-size: 20pt; color: #8a95a6;">×</span>
    <div class="img-slot" style="min-width: 45mm; min-height: 20mm; padding: 5px;">
        <b>[IMAGE SLOT]</b><span>Traverse Logo</span>
    </div>
  </div>
  
  <footer class="page-footer" style="bottom: 8mm;">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div>
  </footer>
</section>

<!-- Slide 2 -->
<section class="page">
  <div class="section-head">
    <h2>본 제안의 핵심</h2>
    <p class="kicker">보난자 컨소시엄은 TranSight를 직접 공동 개발·운영한 인력이 경찰청 분석지원에 투입되는 수행체계입니다.</p>
  </div>
  <div class="grid-3" style="margin-top: 15mm;">
    <div class="card" style="text-align:center; border-top: 4px solid var(--navy);">
      <h3 style="border-bottom:none;">자체 KYT 솔루션 TranSight</h3>
      <p>Tool</p>
    </div>
    <div class="card" style="text-align:center; border-top: 4px solid var(--blue);">
      <h3 style="border-bottom:none;">공동개발 인력의 직접 분석지원</h3>
      <p>People</p>
    </div>
    <div class="card" style="text-align:center; border-top: 4px solid var(--green);">
      <h3 style="border-bottom:none;">경찰청 실전 지원·교육·환수 사례</h3>
      <p>Investigation Impact</p>
    </div>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">02</div>
  </footer>
</section>

<!-- Slide 3 -->
<section class="page">
  <div class="section-head">
    <h2>본 사업은 단순 주소 조회가 아니라 수사 실무형 분석지원입니다</h2>
    <p class="kicker">경찰청이 필요로 하는 것은 툴 조회 결과가 아니라, 영장·공조·동결·환수로 이어지는 구조화된 분석 산출물이다.</p>
  </div>
  <div class="process-flow" style="margin-top: 25mm;">
    <div class="process-step"><b>주소/TXID 입력</b></div><div class="process-arrow">→</div>
    <div class="process-step"><b>자금흐름 재구성</b></div><div class="process-arrow">→</div>
    <div class="process-step"><b>주소 클러스터링</b></div><div class="process-arrow">→</div>
    <div class="process-step"><b>거래소·서비스 식별</b></div><div class="process-arrow">→</div>
    <div class="process-step" style="background:var(--blue-light); border-color:var(--navy);">
        <b style="color:var(--navy-dark);">보고서·브리핑<br/>동결·환수 검토</b>
    </div>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">03</div>
  </footer>
</section>

<!-- Slide 4 -->
<section class="page">
  <div class="section-head">
    <h2>TranSight 공동개발 인력이 직접 분석에 참여합니다</h2>
    <p class="kicker">트라버스는 코어 분석 체계, 보난자팩토리는 서비스 개발·운영 체계를 담당하며 TranSight를 공동 개발·운영해 왔다.</p>
  </div>
  <div class="grid-2">
    <div class="flex-col">
        <div class="card" style="border-left: 4px solid var(--navy);">
            <h3>트라버스</h3>
            <p>범죄 데이터 수집 / 추적 알고리즘 / 온체인 분석 방법론 / 사건 분석</p>
        </div>
        <div class="card" style="border-left: 4px solid var(--blue);">
            <h3>보난자팩토리</h3>
            <p>서비스 개발 / 운영 / 기관 제공 / KYT 솔루션화 / 보안·인프라</p>
        </div>
        <div class="card bg-light">
            <h3>경찰청 제공 가치</h3>
            <p>즉시 분석, 즉시 보완, 즉시 보고, 지속 고도화</p>
        </div>
    </div>
    <div class="img-slot">
        <b>[IMAGE SLOT: TranSight Solution Screenshot]</b>
        <span>TranSight 실제 화면 예시 삽입 예정</span>
    </div>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">04</div>
  </footer>
</section>

<!-- Slide 5 -->
<section class="page">
  <div class="section-head">
    <h2>한국형 범죄 데이터를 직접 수집·분석·서비스화했습니다</h2>
    <p class="kicker">TranSight의 강점은 단순 글로벌 라벨링이 아니라 국내 범죄 현장에서 축적한 데이터와 분석 방법론이다.</p>
  </div>
  <div class="flex-col" style="margin-top: 10mm;">
    <div class="card" style="display:flex; align-items:center; padding:0; overflow:hidden;">
        <div style="background:var(--blue-light); padding:8mm; width: 50mm; font-weight:bold; color:var(--navy); font-size:14pt;">1. 데이터 수집</div>
        <div style="padding: 5mm 8mm; font-size: 12pt;">피싱, 마약, 도박, 성범죄, 미신고 VASP, 해외거래소</div>
    </div>
    <div class="card" style="display:flex; align-items:center; padding:0; overflow:hidden;">
        <div style="background:var(--blue-light); padding:8mm; width: 50mm; font-weight:bold; color:var(--navy); font-size:14pt;">2. 분석 알고리즘</div>
        <div style="padding: 5mm 8mm; font-size: 12pt;">클러스터링, 멀티홉 추적, VASP 식별, 리스크 라벨링</div>
    </div>
    <div class="card" style="display:flex; align-items:center; padding:0; overflow:hidden;">
        <div style="background:var(--blue-light); padding:8mm; width: 50mm; font-weight:bold; color:var(--navy); font-size:14pt;">3. 수사지원·서비스</div>
        <div style="padding: 5mm 8mm; font-size: 12pt;">리포트, 브리핑, 거래소 협조, 국세청·경찰청 제공</div>
    </div>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">05</div>
  </footer>
</section>

<!-- Slide 6 -->
<section class="page">
  <div class="section-head">
    <h2>이미 경찰 수사 현장에서 사용된 분석지원 체계입니다</h2>
    <p class="kicker">피싱·마약·불법송금·해외거래소 공조·사이버테러형 자산 탈취 사건에서 실제 수사 지원 경험을 축적했다.</p>
  </div>
  <table class="table-styled">
    <tr>
        <th style="width: 20%;">수사 유형</th>
        <th style="width: 40%;">지원 내용</th>
        <th style="width: 40%;">본 사업 적용 효과</th>
    </tr>
    <tr>
        <td>피싱·보이스피싱</td>
        <td>자금세탁 중개책 주소 추적, 해외거래소 유입 자금 식별</td>
        <td>피해금 흐름과 협조 요청 대상 신속 특정</td>
    </tr>
    <tr>
        <td>마약자금</td>
        <td>판매자 주소와 세탁 중개책 주소 접점 발견, 클러스터링</td>
        <td>인물·주소·통신 단서 결합 분석</td>
    </tr>
    <tr>
        <td>대규모 환전·불법송금</td>
        <td>동일 주체 간 거래 데이터 추출</td>
        <td>대규모 거래 중 의미 있는 거래군 분리</td>
    </tr>
    <tr>
        <td>사이버테러·환수</td>
        <td>국세청 자산 탈취 사건 추적·동결·환수 지원</td>
        <td>발주부서 목적과 직접 연결</td>
    </tr>
  </table>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">06</div>
  </footer>
</section>

<!-- Slide 7 -->
<section class="page">
  <div class="section-head">
    <h2>단순 추적을 넘어 공격 구조와 자금 이동을 함께 분석합니다</h2>
    <p class="kicker">거래소 핫월렛 침해, DeFi exploit, 악성 승인·피싱, 브릿지 세탁 등 기술형 범죄에 대응 가능한 분석 체계이다.</p>
  </div>
  <div class="grid-2">
    <div class="flex-col">
        <ul class="bullet-list">
            <li><b>CEX 핫월렛 침해:</b> 비인가 출금 TX, 중간 세탁 주소, 거래소·브릿지 유입 추적</li>
            <li><b>DeFi exploit:</b> 재진입, 가격·회계 로직 조작, 공격자·반환 지갑 분석</li>
            <li><b>정밀도·반올림 취약점:</b> 반복 호출, 미세 스왑, invariant 계산 왜곡</li>
            <li><b>악성 승인·피싱:</b> 권한 탈취, 승인 트랜잭션, 자금 이동 구조 분석</li>
            <li><b>크로스체인 세탁:</b> Lock/Mint 이벤트, DEX 로그, 시간·금액 상관관계</li>
        </ul>
    </div>
    <div style="background:var(--blue-light); border-radius:50%; width: 90mm; height: 90mm; display:flex; align-items:center; justify-content:center; text-align:center; margin:0 auto; border: 4px solid var(--navy);">
        <b style="font-size: 16pt; color: var(--navy-dark);">Cyber Terror /<br/>Exploit Case<br/>Analysis</b>
    </div>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">07</div>
  </footer>
</section>

<!-- Slide 8 -->
<section class="page">
  <div class="section-head">
    <h2>접수부터 보고·브리핑·공조까지 이어지는 5단계 프로세스</h2>
  </div>
  <div class="process-flow">
    <div class="process-step"><b>1. 의뢰 접수</b><span>보안 확인</span></div><div class="process-arrow">→</div>
    <div class="process-step"><b>2. 초기 트리아지</b><span>방향성 설정</span></div><div class="process-arrow">→</div>
    <div class="process-step"><b>3. 온체인 분석</b><span>심층 추적</span></div><div class="process-arrow">→</div>
    <div class="process-step"><b>4. 보고서 작성</b><span>품질검토</span></div><div class="process-arrow">→</div>
    <div class="process-step"><b>5. 납품·브리핑</b><span>후속지원</span></div>
  </div>
  <div class="img-slot" style="margin-top: 10mm; min-height: 70mm;">
    <b>[IMAGE SLOT: Transaction Map Image]</b>
    <span>자금 흐름 그래프 / 트랜잭션 맵 예시 삽입 예정</span>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">08</div>
  </footer>
</section>

<!-- Slide 9 -->
<section class="page">
  <div class="section-head">
    <h2>RFP 요구 분석항목을 실전 수행 방식으로 대응합니다</h2>
  </div>
  <table class="table-styled">
    <tr>
        <th style="width: 25%;">분석 항목</th>
        <th style="width: 45%;">수행 방식</th>
        <th style="width: 30%;">산출물</th>
    </tr>
    <tr>
        <td>트랜잭션 추적</td>
        <td>Forward/Backward tracing, hop별 경로 분석</td>
        <td>자금 흐름도, TXID 목록</td>
    </tr>
    <tr>
        <td>주소 클러스터링</td>
        <td>CIOH, 체인지 주소, 시간·금액 패턴</td>
        <td>동일 주체 주소 목록</td>
    </tr>
    <tr>
        <td>믹싱·스왑·브릿지</td>
        <td>이벤트 로그, Lock/Mint 매핑</td>
        <td>서비스명, 컨트랙트, 경로</td>
    </tr>
    <tr>
        <td>스마트컨트랙트·NFT·ENS</td>
        <td>배포자, owner 권한, 반복 거래, 도메인 역조회</td>
        <td>사기성·연계성 분석</td>
    </tr>
    <tr>
        <td>프라이버시 코인</td>
        <td>전후 일반 체인, 거래소 입출금, 한계 명시</td>
        <td>후속 영장·공조 방향</td>
    </tr>
  </table>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">09</div>
  </footer>
</section>

<!-- Slide 10 -->
<section class="page">
  <div class="section-head">
    <h2>사건 난이도에 따라 유연하게 분석역량을 배분합니다</h2>
    <p class="kicker">고정 건수보다 난이도와 투입시간을 반영하는 분석 크레딧 방식으로 사업기간 내 유연한 지원이 가능하다.</p>
  </div>
  <div class="grid-2" style="margin-top: 10mm;">
    <div class="card">
        <h3>총 100 Unit 분석지원 풀</h3>
        <ul class="bullet-list" style="margin-top: 4mm;">
            <li><b>일반 분석 (1 Unit):</b> 단순 주소·TXID 분석</li>
            <li><b>심층 분석 (3 Unit):</b> 클러스터링·DEX·브릿지·복수 거래소</li>
            <li><b>고난도 분석 (5 Unit 이상):</b> 믹서·프라이버시 코인·해킹·DeFi exploit</li>
            <li><b>긴급 대응:</b> 24~48시간 집중 대응, 우선순위 협의</li>
        </ul>
    </div>
    <div class="card bg-light" style="border: 2px solid var(--navy); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
        <h3 style="border-bottom:none; color:var(--navy-dark); font-size: 18pt; margin-bottom: 5mm;">최대 4개 TranSight 계정 제공</h3>
        <p style="font-size: 12pt; color: #47566b; line-height: 1.6;">사업기간 중 사이버테러대응과 자체 분석 및<br/>심층 검토를 위해 제공</p>
        <div style="margin-top: 5mm; background: var(--blue-light); padding: 2mm 5mm; border-radius: 20px; font-weight: bold; color: var(--navy);">계정당 연 6천만 원 상당 라이선스 가치</div>
    </div>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">10</div>
  </footer>
</section>

<!-- Slide 11 -->
<section class="page">
  <div class="section-head">
    <h2>분석 결과가 수사 조치로 이어지도록 설계합니다</h2>
  </div>
  <div class="grid-2x3" style="margin-top: 5mm;">
    <div class="card" style="text-align:center;">
        <b style="color:var(--navy); font-size:14pt; display:block; margin-bottom:2mm;">고난도 사건 해결 가능성 제고</b>
        <p style="font-size:10pt;">최신 기술형 범죄 기법에 대응</p>
    </div>
    <div class="card" style="text-align:center;">
        <b style="color:var(--navy); font-size:14pt; display:block; margin-bottom:2mm;">자산 동결·환수 골든타임 확보</b>
        <p style="font-size:10pt;">신속한 추적 및 거래소 협조</p>
    </div>
    <div class="card" style="text-align:center;">
        <b style="color:var(--navy); font-size:14pt; display:block; margin-bottom:2mm;">증거 품질 및 방어력 강화</b>
        <p style="font-size:10pt;">법정 제출 가능한 수준의 리포트</p>
    </div>
    <div class="card" style="text-align:center;">
        <b style="color:var(--navy); font-size:14pt; display:block; margin-bottom:2mm;">수사관 업무부담 경감</b>
        <p style="font-size:10pt;">핵심 분석에 집중할 수 있는 환경</p>
    </div>
    <div class="card" style="text-align:center;">
        <b style="color:var(--navy); font-size:14pt; display:block; margin-bottom:2mm;">현장 활용도 향상</b>
        <p style="font-size:10pt;">실제 수사에 필요한 산출물 제공</p>
    </div>
    <div class="card" style="text-align:center;">
        <b style="color:var(--navy); font-size:14pt; display:block; margin-bottom:2mm;">내부 심층분석 환경 확보</b>
        <p style="font-size:10pt;">라이선스 제공을 통한 자체 역량 배양</p>
    </div>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">11</div>
  </footer>
</section>

<!-- Slide 12 -->
<section class="page">
  <div class="section-head">
    <h2>기존 지원 성과는 본 용역의 실행 가능성을 보여줍니다</h2>
  </div>
  <div class="grid-2">
    <div class="card bg-light">
        <h3 style="color:var(--gray-text); border-bottom:1px solid var(--gray-line);">과거 성과 (경험)</h3>
        <ul class="bullet-list" style="margin-top: 3mm;">
            <li><b>피싱·보이스피싱:</b> 해외거래소 협조 요청 대상 정리</li>
            <li><b>마약자금:</b> 판매자·세탁책 주소 접점 및 클러스터링</li>
            <li><b>불법송금:</b> 동일 주체 거래 데이터 추출</li>
        </ul>
    </div>
    <div class="card" style="border-left: 4px solid var(--navy);">
        <h3 style="color:var(--navy);">이번 사업 적용 효과</h3>
        <ul class="bullet-list" style="margin-top: 3mm;">
            <li><b>본청 직접 지원:</b> 실제 계정 운영 및 현장 피드백 반영</li>
            <li><b>사이버테러대응과:</b> 해외거래소 공조 및 환수 지원 연계</li>
            <li><b>경찰수사연수원:</b> 분석 결과 설명력과 수사관 교육 역량 입증</li>
        </ul>
    </div>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">12</div>
  </footer>
</section>

<!-- Slide 13 -->
<section class="page">
  <div class="section-head">
    <h2>단건 분석 용역을 넘어 경찰청 가상자산 대응 인프라로 확장합니다</h2>
    <p class="kicker">한국형 범죄 데이터 수집, 추적 알고리즘 개발, 수사지원, 솔루션 운영 경험을 경찰청 실무와 연결한다.</p>
  </div>
  <div class="roadmap">
    <div class="roadmap-step">1. 분석지원</div>
    <div class="roadmap-step">2. 현장 피드백 반영</div>
    <div class="roadmap-step">3. DB·룰 고도화</div>
    <div class="roadmap-step">4. 자체 분석 역량 강화</div>
    <div class="roadmap-step">5. 국가 단위 인프라화</div>
  </div>
  <div class="img-slot" style="margin-top: 10mm; min-height: 40mm;">
    <b>[IMAGE SLOT: IAAN / Overseas VASP Cooperation Diagram]</b>
    <span>LEA ↔ TranSight ↔ VASP 공조 구조 삽입 예정 (선택)</span>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">13</div>
  </footer>
</section>

<!-- Slide 14 -->
<section class="page closing">
  <div class="section-head center">
    <h2>보난자 컨소시엄이 최적 수행자인 이유</h2>
  </div>
  <div class="quote-panel">
    <p>직접 만든 솔루션, 직접 축적한 한국형 범죄 데이터, 직접 수행한 경찰청 수사지원 경험을 하나의 팀으로 제공합니다.</p>
  </div>
  <div class="grid-3" style="margin: 0 12mm;">
    <div class="card" style="text-align:center;">
        <b style="display:block; font-size:12pt; color:var(--navy-dark); margin-bottom:2mm;">TranSight + 공동개발 인력</b>
        <span style="font-size:9.5pt; color:var(--gray-text);">자체 개발 솔루션과 인력 직접 투입</span>
    </div>
    <div class="card" style="text-align:center;">
        <b style="display:block; font-size:12pt; color:var(--navy-dark); margin-bottom:2mm;">실전 지원 성과</b>
        <span style="font-size:9.5pt; color:var(--gray-text);">경찰청·국세청·수사기관 협력 경험</span>
    </div>
    <div class="card" style="text-align:center;">
        <b style="display:block; font-size:12pt; color:var(--navy-dark); margin-bottom:2mm;">엔드투엔드 연계</b>
        <span style="font-size:9.5pt; color:var(--gray-text);">분석·보고·브리핑·공조·인프라화 지원</span>
    </div>
  </div>
  <div class="img-slot" style="margin: 10mm auto 0; width: 150mm; min-height: 30mm; border-color: var(--gray-line);">
    <b>[IMAGE SLOT: Final TranSight Dashboard or Visual]</b>
  </div>
  <footer class="page-footer">
    <div class="copyright">CONFIDENTIAL — 무단 공개 금지</div><div class="page-no">14</div>
  </footer>
</section>

<!-- Slide 15 -->
<section class="page thank-you">
  <div style="text-align: center; margin-top: 30mm;">
    <h1 style="font-size: 50pt; font-weight: 800; color: var(--navy-dark); margin-bottom: 4mm; letter-spacing: -0.03em;">Q &amp; A</h1>
    <p style="font-size: 14pt; color: var(--gray-text); margin-bottom: 12mm;">경청해 주셔서 감사합니다.</p>
    
    <div style="display: inline-block; text-align: left; border-top: 1px solid var(--gray-line); padding-top: 8mm; margin-bottom: 10mm;">
        <div style="font-size: 11pt; color: var(--navy-dark); margin-bottom: 3.5mm; display: flex; gap: 3mm;">
            <span style="font-weight: 700; width: 18mm; color: var(--blue);">E-mail</span>
            <span style="color: var(--gray-text);">contact@bonanza-factory.co.kr</span>
        </div>
        <div style="font-size: 11pt; color: var(--navy-dark); margin-bottom: 3.5mm; display: flex; gap: 3mm;">
            <span style="font-weight: 700; width: 18mm; color: var(--blue);">Tel</span>
            <span style="color: var(--gray-text);">02-2632-7774</span>
        </div>
        <div style="font-size: 11pt; color: var(--navy-dark); margin-bottom: 3.5mm; display: flex; gap: 3mm;">
            <span style="font-weight: 700; width: 18mm; color: var(--blue);">Address</span>
            <span style="color: var(--gray-text); line-height: 1.5;">
            서울특별시 영등포구 양평로 12, 정오빌딩 6, 7층<br/>
            <span style="font-size: 9.2pt; color: #8a95a6;">7F, Jeong-Oh Building, 12 Yangpyeong-ro, Yeongdeungpo-gu, Seoul, Republic of Korea</span>
            </span>
        </div>
        <div style="font-size: 11pt; color: var(--navy-dark); display: flex; gap: 3mm; margin-top: 4mm;">
            <span style="font-weight: 700; width: 18mm; color: var(--blue);">Web</span>
            <span style="color: var(--gray-text); font-weight: 700;">www.bonanza-factory.co.kr</span>
        </div>
    </div>
  </div>
  
  <div style="position:absolute; right:20mm; bottom: 25mm; display:flex; align-items:center; gap: 8mm;">
    <div class="img-slot" style="min-width: 40mm; min-height: 15mm; padding: 5px;">
        <b>[IMAGE SLOT]</b><span style="font-size: 8pt;">Bonanza Factory Logo</span>
    </div>
    <span style="font-size: 16pt; color: #8a95a6;">×</span>
    <div class="img-slot" style="min-width: 40mm; min-height: 15mm; padding: 5px;">
        <b>[IMAGE SLOT]</b><span style="font-size: 8pt;">Traverse Logo</span>
    </div>
  </div>
  
  <footer class="page-footer" style="bottom: 8mm;">
    <div class="copyright">Bonanza Factory · Traverse Consortium<br/>CONFIDENTIAL — 무단 공개 금지</div>
  </footer>
</section>

</body>
</html>
"""

with open('/Users/milkyway/Desktop/Dev/deck-maker/decks/KNPA_proposal.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML generated successfully.")
