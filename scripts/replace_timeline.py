import os

html_path = '/Users/milkyway/Desktop/Dev/deck-maker/decks/knpa_bonanza_traverse_deck_revised_no_base64.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_timeline = """<div class="timeline">
<div><span>착수 단계<br/>계약 후 ~2주</span><b>PM 지정·연락체계 수립</b><p>담당 수사관·본청 담당자 연락처 확보, 의뢰 접수 채널 일원화</p></div>
<div><span>착수 단계</span><b>의뢰 접수·보안 체계 수립</b><p>분석 의뢰서 양식 확정, 보안 준수사항 교육, 자료관리대장 준비</p></div>
<div><span>수시 대응 구간</span><b>건별 분석 사이클</b><p>의뢰 접수 → 트리아지 → 온체인 분석 → 보고서 작성 → 납품·브리핑</p></div>
<div><span>종료 단계<br/>~12.20</span><b>최종 보고·보안 처리</b><p>전체 분석 결과보고서 제출, 분석 파일 삭제, 자료관리대장 최종 정리</p></div>
</div>"""

new_table = """<table class="std-table small" style="text-align: center; margin-top: 10px;">
<colgroup>
    <col style="width: 25%;">
    <col style="width: 55%;">
    <col style="width: 20%;">
</colgroup>
<thead><tr><th>단계</th><th>세부 내용</th><th>기간</th></tr></thead><tbody>
<tr><td><b>착수 단계 ①:</b><br/>PM 지정·연락체계 수립</td><td style="text-align: left;">담당 수사관 및 본청 담당자 연락처 확보, 의뢰 접수 채널 일원화, 대체 PM 체계 수립</td><td>계약 후 ~2주</td></tr>
<tr><td><b>착수 단계 ②:</b><br/>의뢰 접수 프로세스·<br/>보안 체계 수립</td><td style="text-align: left;">분석 의뢰서 양식 확정, 보안 준수사항 교육 실시, 자료관리대장 양식 확정·준비</td><td>계약 후 ~2주</td></tr>
<tr><td><b>수시 대응 구간:</b><br/>건별 분석 사이클</td><td style="text-align: left;">의뢰 접수 → 트리아지 → 온체인 분석 → 보고서 작성 → 납품·브리핑 반복</td><td>계약일 ~<br/>2026.12.20.</td></tr>
<tr><td><b>종료 단계 ①:</b><br/>최종 결과보고서 제출</td><td style="text-align: left;">전체 분석 결과를 종합한 사업 종료 보고서 제출 (수행 건수, 유형별 분석 결과, 주요 성과)</td><td>~2026.12.20.</td></tr>
<tr><td><b>종료 단계 ②:</b><br/>보안 처리</td><td style="text-align: left;">참여 인력 PC 내 분석 파일 전체 삭제, 자료관리대장 최종 정리 후 경찰청 제출</td><td>~2026.12.20.</td></tr>
</tbody></table>"""

if old_timeline in content:
    content = content.replace(old_timeline, new_table)
    print("Timeline replaced with table successfully.")
else:
    print("Failed to find old timeline.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

