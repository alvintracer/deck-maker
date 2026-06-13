import os

html_path = '/Users/milkyway/Desktop/Dev/deck-maker/decks/knpa_bonanza_traverse_deck_revised.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Table
old_table = """<table class="std-table small"><thead><tr><th>역할</th><th>소속/직위</th><th>주요 담당 업무</th></tr></thead><tbody>
<tr><td>총괄 PM</td><td>트라버스 / 대표</td><td>국내 가상자산 거래소 커뮤니케이션 및 전체 프로젝트 관리</td></tr>
<tr><td>책임연구원</td><td>트라버스 / 과장</td><td>가상자산 범죄 자금흐름 분석 총괄, 주요 사건 추적·검증</td></tr>
<tr><td>선임연구원</td><td>트라버스 / 과장</td><td>범죄 연관 주소 식별, 자금세탁 패턴 분석, 수사지원 자료 작성</td></tr>
<tr><td>연구원</td><td>트라버스 / 대리</td><td>온체인 데이터 수집·정제, 거래내역 분석, 주소 클러스터링 지원</td></tr>
<tr><td>기술지원 PM</td><td>보난자팩토리 / 이사</td><td>TranSight 기술지원 총괄</td></tr>
<tr><td>고도화·백엔드</td><td>보난자팩토리 / 기획·개발</td><td>TranSight 커스터마이제이션, 서비스 고도화, 백엔드 개발 지원</td></tr>
</tbody></table>"""

new_table = """<table class="std-table small" style="font-size:0.82em;"><thead><tr><th>역할</th><th>성명</th><th>소속·직위</th><th>주요 담당 업무</th></tr></thead><tbody>
<tr><td>총괄 PM</td><td>한태우</td><td>트라버스 / 대표</td><td>국내 가상자산 거래소 커뮤니케이션 및 전체 프로젝트 관리, 정보통신기획평가원 국책과제 사업 총괄</td></tr>
<tr><td>책임연구원<br/><span style="font-size:0.8em;color:#888;">(수석 분석가)</span></td><td>정도현</td><td>트라버스 / 과장</td><td>가상자산 범죄 자금흐름 분석 총괄, 주요 사건 추적·검증. 경찰청 사이버테러대응과 국세청 자산탈취 추적·환수 지원.<br/>국수본·경기북부·충남·서울 강남경찰서 수사지원. Lazarus 해킹자금 추적, 다중 네트워크 분석 및 추적 알고리즘 개발.</td></tr>
<tr><td>선임연구원</td><td>이금강</td><td>트라버스 / 과장</td><td>범죄 연관 주소 식별, 자금세탁 패턴 분석, 수사지원 자료 작성. 빅데이터분석기사·ADsP·정보처리기사 보유.<br/>믹싱 AI 알고리즘 개발. 고려대 수학과.</td></tr>
<tr><td>연구원</td><td>이승주</td><td>트라버스 / 대리</td><td>온체인 데이터 수집·정제, 거래내역 분석, 주소 클러스터링 지원. 마약·보이스피싱·Lazarus 해킹 분석 지원.</td></tr>
<tr><td>대체 PM</td><td>KIM<br/>MINJAE</td><td>트라버스 / 이사</td><td>글로벌 커뮤니케이션 및 분석 프로젝트 관리, 총괄 PM 부재 시 즉시 대무.</td></tr>
<tr><td>기술지원 PM</td><td>정규환</td><td>보난자팩토리 / 이사</td><td>TranSight 기술지원 총괄.</td></tr>
<tr><td>고도화 기획</td><td>신민재</td><td>보난자팩토리 / 대리</td><td>TranSight 고도화 및 커스터마이제이션 기획. 분석 실무 발견 신규 기법 즉시 반영.</td></tr>
<tr><td>기술지원<br/>(백엔드)</td><td>이상진</td><td>보난자팩토리 / 부장</td><td>TranSight 고도화 백엔드 개발. 미지원 항목 발견 시 크롤링 로직 즉시 보완.</td></tr>
<tr><td>기술지원<br/>(백엔드)</td><td>이한주</td><td>보난자팩토리 / 과장</td><td>TranSight 고도화 백엔드 개발.</td></tr>
</tbody></table>"""

if old_table in content:
    content = content.replace(old_table, new_table)
    print("Table replaced successfully.")
else:
    print("Failed to find old_table.")

# Replace Step
old_step = "착수 2주 내 운영 체계를 확정하고, 계약 종료일까지 분석 의뢰 건별 Step 1~4 사이클을 반복합니다."
new_step = "착수 2주 내 운영 체계를 확정하고, 계약 종료일까지 분석 의뢰 건별 Step 1~5 사이클을 반복합니다."
if old_step in content:
    content = content.replace(old_step, new_step)
    print("Step text replaced successfully.")
else:
    print("Failed to find old_step text.")

# Add Contact Details
contact_html = """<div class="contact-info" style="margin-top: 40px; display: flex; justify-content: space-between; font-size: 0.9rem; color: #555; text-align: left; border-top: 1px solid #e0e0e0; padding-top: 20px; line-height: 1.6; max-width: 1000px; margin-left: auto; margin-right: auto;">
    <div style="flex: 1;">
        <strong style="color:#000; font-size:1.1rem; display:block; margin-bottom:8px;">보난자팩토리</strong>
        <b>Email</b> contact@bonanza-factory.co.kr<br/>
        <b>Tel</b> 02-2632-7774<br/>
        <b>Web</b> www.bonanza-factory.co.kr<br/>
        <b>Address</b> 서울특별시 영등포구 양평로 12, 정오빌딩 6, 7층
    </div>
    <div style="flex: 1; padding-left: 20px;">
        <strong style="color:#000; font-size:1.1rem; display:block; margin-bottom:8px;">트라버스</strong>
        <b>Email</b> contact@traverse.kr<br/>
        <b>Tel</b> 010-5403-9150<br/>
        <b>Web</b> www.traverse.kr<br/>
        <b>Address</b> 서울특별시 영등포구 양평로 12, 정오빌딩 6층
    </div>
</div>
</div>
<footer class="page-footer">"""

closing_page_marker = """<div class="closing-tags"><span>자체 개발</span><span>실전 분석</span><span>증거화</span><span>공조 지원</span><span>인프라화</span></div>\n</div>\n<footer class="page-footer">"""

if closing_page_marker in content:
    content = content.replace(closing_page_marker, """<div class="closing-tags"><span>자체 개발</span><span>실전 분석</span><span>증거화</span><span>공조 지원</span><span>인프라화</span></div>\n""" + contact_html)
    print("Contact info added to closing page.")
else:
    print("Failed to find closing page marker.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

