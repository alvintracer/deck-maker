#!/usr/bin/env python3
"""Apply all hanabank proposal edits."""

filepath = '/Users/milkyway/Desktop/Dev/deck-maker/decks/hanabank_transight_kyt_tr_proposal.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

c = 0

# ─── PAGE 1: Title change ───
content = content.replace(
    '스테이블코인 유통 규제준수를 위한<br/>TranSight KYT 및 TTR 제안',
    '스테이블코인 유통 규제준수를 위한<br/>TranSight 컴플라이언스 패키지 제안')
c += 1; print('✅ P1: Title changed')

# PAGE 1: Upbit/Bithumb Rail → Upbit Direct Rail
content = content.replace('Upbit/Bithumb Rail', 'Upbit Direct Rail')
c += 1; print('✅ P1: Chip → Upbit Direct Rail')

# PAGE 1: Delete hero-card (70/30/1 Rail box)
old_hero = '''    <div class="hero-card">
      <div class="metric"><b>70%</b><span>KYT 중심: 입출금 전수 모니터링·RBA·STR 연계</span></div>
      <div class="metric"><b>30%</b><span>TR PoC: 거래소 직접 연결 채널 및 금융망 기반 브릿지 검증</span></div>
      <div class="metric"><b>1 Rail</b><span>KYT + Travel Rule + 감사증적을 하나의 준법 인프라로 통합</span></div>
    </div>'''
content = content.replace(old_hero, '')
c += 1; print('✅ P1: Hero card removed')

# PAGE 1: Bonanza logo size 70%
content = content.replace(
    '.cover-logos img{height:9mm;width:auto}',
    '.cover-logos img{height:6.3mm;width:auto}')
c += 1; print('✅ P1: Bonanza logo 70%')

# ─── PAGE 2: 핵심 제안 ───
content = content.replace(
    '핵심 제안: KYT는 즉시 공급, TR은 PoC로 선점',
    '핵심 제안: KYT는 즉시 구축 및 고도화, 트래블룰은 PoC로 선점')
c += 1; print('✅ P2: Subtitle changed')

# ─── PAGE 4: note text ───
content = content.replace(
    'KYT 전수검사와 거래소 TR 브릿지를 먼저 구축해 시장 표준을 선점하는 전략이 필요합니다.',
    'KYT 기반 온체인 AML 모니터링 체계와 거래소 TR 브릿지를 먼저 구축해 대한민국 금융기관의 디지털 자산 유통 컴플라이언스 표준을 선점하는 전략이 필요합니다.')
c += 1; print('✅ P4: Note text changed')

# ─── PAGE 5: Add compliance model message ───
old_p5 = '</table>\n    </div>\n    <div class="card blue">\n      <h3>TranSight가 제공하는 차세대 보완 구조</h3>'
new_p5 = '</table>\n    </div>\n    <div class="card blue">\n      <h3>TranSight가 제공하는 차세대 보완 구조</h3>'
# Add note at the end of page 5
old_p5_footer = '  <footer class="footer"><img src="../materials/bonanza_Factory_logo.jpg"/><span class="sep"></span><span class="copy">Copyright ⓒ 2026 Bonanza Factory. All rights reserved.</span><span class="page-no">05</span></footer>'
new_p5_footer = '  <div class="note" style="margin-top:5mm"><b>보난자팩토리의 제안 비전</b> 은행권 최초의 디지털 자산 시대 통합 컴플라이언스 모델 설계를 하나은행과 함께 만들어가겠습니다. KYC·KYT·Travel Rule·STR을 하나의 아키텍처로 연결하는 것은 하나은행이 대한민국 디지털 금융의 컴플라이언스 리더로 자리매김하는 핵심 기반이 됩니다.</div>\n  <footer class="footer"><img src="../materials/bonanza_Factory_logo.jpg"/><span class="sep"></span><span class="copy">Copyright ⓒ 2026 Bonanza Factory. All rights reserved.</span><span class="page-no">05</span></footer>'
content = content.replace(old_p5_footer, new_p5_footer)
c += 1; print('✅ P5: Compliance model message added')

# ─── PAGE 7: Title change ───
content = content.replace(
    'TranSight는 API 전수검사와 Web 심층분석을 함께 제공합니다',
    'TranSight는 실시간 온체인 AML 모니터링과 Web 심층분석을 함께 제공합니다')
c += 1; print('✅ P7: Title changed')

# ─── PAGE 8: Title change + FIU 미신고 VASP + bottom message ───
content = content.replace(
    '한국형 범죄 데이터 기반 KYT가 필요한 이유',
    '한국형 범죄 및 제재대상 데이터 기반 KYT가 필요한 이유')
c += 1; print('✅ P8: Title changed')

# 미신고 VASP → FIU 미신고 VASP (in page 8 only - specific context)
content = content.replace('미신고 VASP·DEX·개인지갑 경유 세탁 확대', 'FIU 미신고 VASP·DEX·개인지갑 경유 세탁 확대')
content = content.replace('<b>미신고 VASP</b>', '<b>FIU 미신고 VASP</b>')
c += 1; print('✅ P8: 미신고 VASP → FIU 미신고 VASP')

# Add bottom message to page 8
old_p8_footer = '  <footer class="footer"><img src="../materials/bonanza_Factory_logo.jpg"/><span class="sep"></span><span class="copy">Copyright ⓒ 2026 Bonanza Factory. All rights reserved.</span><span class="page-no">08</span></footer>'
new_p8_footer = '  <div class="note" style="margin-top:5mm"><b>보난자팩토리의 위치</b> 보난자팩토리는 국내 유일, 아시아 최고 수준의 KYT 솔루션 및 데이터 인텔리전스를 인정받고 있으며, 국세청·경찰청·국정원 등 정부기관 가상자산 거래 제한 대상 DB의 표준이 되어가고 있습니다.</div>\n  <footer class="footer"><img src="../materials/bonanza_Factory_logo.jpg"/><span class="sep"></span><span class="copy">Copyright ⓒ 2026 Bonanza Factory. All rights reserved.</span><span class="page-no">08</span></footer>'
content = content.replace(old_p8_footer, new_p8_footer)
c += 1; print('✅ P8: Bottom message added')

# ─── PAGE 9: Add compliance builder message ───
old_p9_note = '<div class="note"><b>TranSight 대응</b> Deposit n-Hop Analysis와 Withdrawal n-Hop Analysis를 통해 직접 주소뿐 아니라 후속 자금 흐름을 모니터링하여 RBA 재평가와 STR 후보화에 활용합니다.</div>'
new_p9_note = '<div class="note"><b>TranSight 대응</b> Deposit n-Hop Analysis와 Withdrawal n-Hop Analysis를 통해 직접 주소뿐 아니라 후속 자금 흐름을 모니터링하여 RBA 재평가와 STR 후보화에 활용합니다.</div>\n      <div class="note" style="margin-top:3mm;border-left-color:var(--blue)"><b>컴플라이언스 빌더로서의 역량</b> 거래소와 금융기관 모두 수탁형 지갑 시스템을 넘어, 고객이 직접 등록하거나 기관이 생성하는 비수탁 지갑(개인지갑)을 통한 규제 우회 리스크를 사전에 파악해야 합니다. 보난자팩토리는 이러한 새로운 유형의 위험을 선제적으로 감지하고, 이에 대응하는 서비스를 설계·구축하는 <b>컴플라이언스 빌더</b>로서 하나은행의 디지털자산 유통 준비를 함께합니다.</div>'
content = content.replace(old_p9_note, new_p9_note)
c += 1; print('✅ P9: Compliance builder message added')

# ─── PAGE 12: Add key differentiators ───
old_p12_strip = '''  <div class="summary-strip">
    <div class="strip-card"><b>매출 220억</b><span>2025년 말 기준</span></div>
    <div class="strip-card"><b>영업이익 87억</b><span>외감법인 핀테크 기업</span></div>
    <div class="strip-card"><b>총자산 420억</b><span>안정적 운영 기반</span></div>
    <div class="strip-card"><b>ISMS</b><span>금융권 수준 보안성</span></div>
  </div>'''
new_p12_strip = '''  <div class="four-col" style="margin-top:5mm">
    <div class="card hana"><h3>이미 준비된 파트너</h3><p>하나은행은 <b>업비트-하나은행 원화입출금(TranSafer)</b>를 보난자팩토리와 공동 개발하고, <b>전용선까지 구축</b>한 유일한 은행입니다. 금융권 망분리 환경·인프라·정보보호체계 호환 이슈를 이미 해결한 상태입니다.</p></div>
    <div class="card blue"><h3>Be-Ready 최속 지원</h3><p>KYT도, 트래블룰도 금융권 망분리·보안·정보보호 인프라와의 호환이 핵심입니다. <b>보난자팩토리는 하나은행의 Be-Ready를 그 누구보다 빠르게 지원할 수 있는 유일한 파트너</b>입니다.</p></div>
    <div class="card"><h3>업비트의 핵심 엔진</h3><p>보난자팩토리는 <b>업비트의 핵심 KYT 엔진이자 입출금 검증 엔진</b>을 운영하고 있습니다. 하나은행과 업비트를 연결하는 인프라의 중심에 이미 보난자팩토리가 있습니다.</p></div>
    <div class="card"><h3>하나와 하나 되다</h3><p>TranSafer로 은행-거래소를 연결하고, TranSight로 온체인 위험을 통제하며, TTR로 Travel Rule까지 — <b>하나은행의 디지털자산 컴플라이언스 파트너는 보난자팩토리</b>입니다.</p></div>
  </div>
  <div class="summary-strip">
    <div class="strip-card"><b>매출 220억</b><span>2025년 말 기준</span></div>
    <div class="strip-card"><b>영업이익 87억</b><span>외감법인 핀테크 기업</span></div>
    <div class="strip-card"><b>총자산 420억</b><span>안정적 운영 기반</span></div>
    <div class="strip-card"><b>ISMS</b><span>금융권 수준 보안성</span></div>
  </div>'''
content = content.replace(old_p12_strip, new_p12_strip)
c += 1; print('✅ P12: Key differentiators added (TranSafer partnership, Be-Ready, 업비트 엔진)')

# ─── PAGE 13: Recommendation change ───
content = content.replace(
    'KYT 공급 제안: Compliance Pro 우선 권장',
    'KYT 공급 제안: Basic 또는 Compliance Pro 단계별 도입 권장')
c += 1; print('✅ P13: Title → Basic or Compliance Pro')

content = content.replace(
    '<b>하나은행 권장안</b> 초기 3개월은 Compliance Pro 기반으로 실시간 API 전수검사, Web 5개 계정, 심층 분석 리포트 체계를 운영하고, 유통량·거래량 확정 후 Enterprise Unlimited 전환 여부를 검토하는 구조를 권장합니다.',
    '<b>하나은행 단계별 도입 권장안</b> 규제 준비 단계에서는 <b>Basic 또는 Compliance Pro</b>를 도입하여 내부 AML·컴플라이언스 팀의 KYT 역량을 강화하고, 디지털자산 규제준수 관련 교육 및 통합 모델 설계를 함께 진행합니다. 이후 실제 규제가 시행되고 VASP 라이선스를 취득하여 스테이블코인을 유통하는 시점에 <b>Enterprise Unlimited</b>로 전환하는 단계적 도입 구조를 권장합니다.')
c += 1; print('✅ P13: Recommendation note → staged adoption')

# ─── PAGE 14: Roadmap reflect staged adoption ───
content = content.replace(
    '<div class="phase"><span class="label">Phase 1</span><h3>정책·연동 설계</h3><p>입금/출금/계정반영 전후 KYT 포인트, Risk Code별 조치 기준, 보류·차단·심사 정책 정의</p></div>',
    '<div class="phase"><span class="label">Phase 1</span><h3>Basic/Compliance Pro 도입</h3><p>내부 AML·컴플라이언스 팀 대상 KYT 교육, 정책·연동 설계, 디지털자산 규제준수 통합 모델 설계 착수</p></div>')
c += 1; print('✅ P14: Phase 1 → Basic/Pro 도입')

content = content.replace(
    '<div class="phase"><span class="label">Phase 4</span><h3>운영 전환</h3><p>전수검사, 사후 n-hop 모니터링, 월간 리스크 리포트, 계정·정책 확장 검토</p></div>',
    '<div class="phase"><span class="label">Phase 4</span><h3>Enterprise 전환</h3><p>VASP 라이선스 취득·스테이블코인 유통 시점에 Enterprise Unlimited 전환, 전수검사, 사후 n-hop 모니터링, 월간 리스크 리포트</p></div>')
c += 1; print('✅ P14: Phase 4 → Enterprise 전환')

# ─── PAGE 15: Travel Rule PoC ───
old_p15_note = '<b>제안 포지션</b> KYT는 본공급 제안, TR은 PoC 제안입니다. 즉, 하나은행은 먼저 KYT 운영체계를 확보하고, 동시에 TTR PoC로 시장 선점형 Travel Rule 인프라를 검증할 수 있습니다.'
new_p15_note = '<b>왜 보난자·하나은행·업비트만 가능한가</b> 현재 VerifyVASP·CODEVASP 등 기존 TR 솔루션은 은행 계정계나 내부망에 바로 연결하기 어려운 구조입니다. 보난자팩토리는 KYT와 패키지로 준비 중인 <b>금융기관형 트래블룰 브릿지(TTR)</b>를 통해 업비트-하나은행뿐 아니라 해외 VASP·타 금융기관으로도 확장 가능합니다. 이미 <b>실명계정 기반 원화입출금 중개 인프라(TranSafer)를 구축 완료</b>한 상태에서, 가장 효율적으로 Travel Rule을 수행할 수 있는 구조입니다. <b>KYT는 다른 은행도 도입할 수 있지만, 이 구조는 보난자팩토리·하나은행·업비트만 할 수 있습니다.</b>'
content = content.replace(old_p15_note, new_p15_note)
c += 1; print('✅ P15: Travel Rule note → exclusive partnership message')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n🎯 Total: {c} changes applied')
