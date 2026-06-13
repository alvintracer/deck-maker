import re

filepath = '/Users/milkyway/Desktop/Dev/deck-maker/decks/knpa_bonanza_traverse_deck_revised_no_base64.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_lines = [
    '<div class="section-head compact"><span class="kicker">Investigation Gap</span><h2>수사관에게 필요한 것은 \u201c툴 조회 결과\u201d가 아닙니다</h2><p>실제 수사는 영장, 거래소 협조, 검찰 송치, 공판 설명까지 이어져야 합니다.</p></div>',
    '<div class="two-flow">',
    '<div class="flow-card muted"><h3>일반 조회 중심 방식</h3><ol><li>주소\u00b7TXID 조회</li><li>그래프 캡처</li><li>위험 라벨 확인</li><li>추가 수사는 수사관이 직접 정리</li></ol><p class="warn">문제: 분석 한계와 후속 조치가 분리되어 실무 활용성이 낮아질 수 있음</p></div>',
    '<div class="flow-card primary"><h3>보난자 컨소시엄 방식</h3><ol><li>의뢰 목적과 사건 맥락 확인</li><li>자금 흐름\u00b7클러스터링\u00b7서비스 식별</li><li>거래소 협조 요청 정보 정리</li><li>보고서\u00b7브리핑\u00b7후속 질의 대응</li></ol><p class="good">효과: 수사관이 바로 활용 가능한 증거화\u00b7공조\u00b7환수 중심 산출물 제공</p></div>',
    '</div>',
]
old_block = '\n'.join(old_lines)

new_block = '''<div class="section-head compact"><span class="kicker">Key Differentiator</span><h2>해외 솔루션 기반 분석 대행사와 보난자 컨소시엄의 차이</h2><p>국내 분석지원 업체 대부분은 Chainalysis, TRM Labs 등 해외 솔루션을 구매하여 분석 업무를 수행합니다. 보난자 컨소시엄은 근본적으로 다릅니다.</p></div>
<div class="two-flow">
<div class="flow-card muted"><h3>해외 솔루션 기반 분석 대행</h3><ol><li>Chainalysis, TRM 등 해외 KYT 툴 라이선스 구매</li><li>툴 제공 라벨·그래프 기반 조회 후 리포트 작성</li><li>신규 토큰·비표준 컨트랙트 등 예외 발생 시 해외 벤더 응답 대기</li><li>한국형 범죄 패턴(보이스피싱, 환전상, OTC 중개책 등) 데이터 부재</li></ol><p class="warn">한계: 분석 도구의 범위 내에서만 대응 가능하며, 알고리즘 개선이 불가능</p></div>
<div class="flow-card primary"><h3>보난자 컨소시엄 (유일한 차별점)</h3><ol><li>TranSight를 직접 개발·운영한 인력이 분석지원에 참여</li><li>업비트 AML 모니터링을 통해 범죄자금 유통 흐름과 트렌드를 가장 먼저 파악</li><li>분석 사건에 필요한 알고리즘이 부족할 경우 자체 설계·개발하여 즉시 반영</li><li>고려대학교 정보보호대학원 협력기관으로서 최고 수준의 연구 역량 보유</li></ol><p class="good">유일한 팀: KYT 솔루션 개발 + 식별 데이터 구축 + 추적 알고리즘 설계 인력이 분석지원을 직접 수행하는 국내 유일의 팀</p></div>
</div>'''

if old_block in content:
    content = content.replace(old_block, new_block)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Page 5 replaced.")
else:
    print("ERROR: Old block not found. Trying line-by-line...")
    # Try just replacing the first line as anchor
    anchor = 'Investigation Gap'
    if anchor in content:
        # Replace lines 97-101
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'Investigation Gap' in line:
                print(f"Found anchor at line {i+1}")
                lines[i] = new_block.split('\n')[0]
                lines[i+1] = new_block.split('\n')[1]
                lines[i+2] = new_block.split('\n')[2]
                lines[i+3] = new_block.split('\n')[3]
                lines[i+4] = new_block.split('\n')[4]
                content = '\n'.join(lines)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("SUCCESS: Page 5 replaced via line-by-line.")
                break
    else:
        print("ERROR: Anchor not found either.")
