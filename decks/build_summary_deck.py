#!/usr/bin/env python3
"""Build ewha_thesis_summary_deck.html from the v11 original."""

src = '/Users/milkyway/Desktop/Dev/deck-maker/decks/ewha_thesis_presentation_deck_v11.html'
dst = '/Users/milkyway/Desktop/Dev/deck-maker/decks/ewha_thesis_summary_deck.html'

with open(src, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []

# ── Part 1: Base CSS (lines 1-131) — class-based styles only, no nth-of-type ──
out.extend(lines[0:131])
out.append('</style></head>\n')

# ── Part 2: Body + Cover + Contents + 서론 + 선행연구 (lines 722-836) ──
out.extend(lines[721:836])

# Close last front-matter section (line 837 in original starts with </section>)
out.append('\n</section>')

# ── Part 3: Summarized slides (연구방법 3 + 연구결과 6 + 결론 2 + closing 1 = 12) ──
SLIDES = r"""
<section class="page">
<div class="side-label"><div class="roman">Ⅲ. 연구 방법</div><div class="alpha">A. 연구 설계 및 참여자</div><div class="num"></div></div>
<header><span class="tag">Section</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>Ⅲ. 연구 방법 — 연구 설계 및 참여자</h2>
<ul class="bullet-list"><li>본 연구는 재난교육을 통한 중학생의 자연재해 인식 변화와 대응 역량 형성 과정을 심층적으로 탐색하기 위하여 <strong>질적 사례 연구</strong>로 설계되었다.</li>
<li>질적 연구는 참여자가 특정 맥락 속에서 어떠한 경험을 하고, 그 경험에 어떠한 의미를 부여하는지를 이해하는 데 적합한 접근이다(Creswell, 2013).</li>
<li>연구 참여자는 <strong>중학생 9명</strong>(1학년 5명, 2학년 3명, 3학년 1명 / 남 7명, 여 2명)이다.</li>
<li>참여 기간: 2022년 5월 7일 ~ 8월 13일, 총 8차시(40시간)</li>
<li>중학생은 자연재해의 원인과 맥락을 구조적으로 이해할 수 있으면서도, 재난에 대한 직관적·경험적 인식이 강하게 나타날 수 있는 시기의 학습자라는 점에서 본 연구의 목적에 적합한 대상이다.</li>
<li>주요 분석 자료: 사전 검사지, 차시별 활동지 1·2·3</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">Ⅲ. 연구 방법 — 연구 설계 및 참여자</div><div class="pg"></div></footer>
</section><section class="page">
<div class="side-label"><div class="roman">Ⅲ. 연구 방법</div><div class="alpha">B. 프로그램 구성</div><div class="num"></div></div>
<header><span class="tag">Table</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>프로그램 구성 및 주요 내용</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th style="width:22%">프로그램 단계</th><th>주요 내용</th></tr></thead><tbody>
<tr><td>사전 검사지</td><td>재난의 정의, 인식, 사전 지식, 경험, 감정, 현재 대응 행동 서술</td></tr>
<tr><td>초기 대응 선택<br/>(활동지 1)</td><td>재난 영상 시청 후 즉각적 대응 선택과 그 근거 서술</td></tr>
<tr><td>자연재해 지식 습득</td><td>교사 강의 — 정의, 발생 원리, 측정·예보 체계, 피해 양상, 대비·대응 방법</td></tr>
<tr><td>최종 대응 선택<br/>(활동지 2)</td><td>재난 영상 재시청 후 최종 대응 선택과 변경 근거 서술</td></tr>
<tr><td>상황별 대응 구성<br/>(활동지 3)</td><td>새로운 상황(지문) 제시 후 대응 선택과 근거 서술</td></tr>
</tbody></table></div>
<ul class="table-summary"><li>총 8차시 구성: 1차시 오리엔테이션, 2~8차시 폭염·지진·태풍·미세먼지·황사·산사태·대설</li>
<li>7가지 자연재해는 우리나라 학생들의 삶과 밀접한 연관이 있는 지구과학 관련 재해로 구성하였다.</li>
<li>상황별 대응 단계에서는 새로운 상황을 영상이 아닌 지문으로 제시하여 보다 정교한 추론 단서를 제공하였다.</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">프로그램 구성 및 주요 내용</div><div class="pg"></div></footer>
</section><section class="page long-page">
<div class="side-label"><div class="roman">Ⅲ. 연구 방법</div><div class="alpha">C. 자료 수집 및 분석</div><div class="num"></div></div>
<header><span class="tag">Part Summary</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>자료 수집 및 분석</h2>
<ul class="bullet-list"><li><strong>핵심 자료:</strong> 사전 검사지(초기 인식 파악) + 차시별 활동지 1(초기 대응)·활동지 2(최종 대응)·활동지 3(상황별 대응) — 총 64부</li>
<li><strong>분석 방법:</strong> 귀납적 범주화와 비교 분석 — 자료 속 반복적 의미 단위와 패턴을 식별하고 범주화(Creswell, 2013; Merriam, 1998)</li>
<li><strong>분석 3단계:</strong><br/>① 전체 자료를 반복적으로 읽으며 학생 응답의 특징을 개방적으로 파악<br/>② 의미 단위를 범주화하고 비교하여 상위 범주로 정리<br/>③ 프로그램 전후 변화와 교육적 의미를 해석</li>
<li><strong>타당도 확보 방안:</strong><br/>① 자료 교차 검증 — 사전 검사지와 활동지 간 대조<br/>② 학생별·재해 유형별·프로그램 전후 반복적 비교 분석<br/>③ 맥락 중심 해석 — 정답 여부가 아닌 사고의 흐름 속에서 해석<br/>④ 범주 점검 및 정교화<br/>⑤ 사례 제시를 통한 해석 타당성 확보</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">자료 수집 및 분석</div><div class="pg"></div></footer>
</section><section class="page">
<div class="side-label"><div class="roman">Ⅳ. 연구 결과</div><div class="alpha"></div><div class="num"></div></div>
<header><span class="tag">Section</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>Ⅳ. 연구 결과 개요</h2>
<ul class="bullet-list"><li>본 연구의 목적은 중학생의 자연재해 교육 프로그램을 개발·적용하여, 프로그램 전 과정에서 드러나는 추론 과정의 흐름과 그 특징을 파악하고 자연재해 교육 프로그램의 의미를 확인하는 것이다.</li>
<li>총 8차시(40시간)의 '자연재해 서바이벌' 프로그램을 개발·실행한 뒤, 수집된 자료를 귀납적으로 분석하여 다음과 같이 정리하였다.</li>
<li><strong>A. 자연재해 유형별 추론 과정의 특징</strong> — 7가지 재난 유형별 추론 양상의 차이</li>
<li><strong>B. 자연재해 교육 프로그램에서 나타난 추론 과정의 흐름</strong> — 5단계 추론 구조와 기존 과학교육 추론과의 비교</li>
<li><strong>C. 자연재해 교육 프로그램에서 나타난 학생의 변화</strong> — 자연재해 이해와 판단 근거의 변화</li>
<li><strong>D. 자연재해 교육 프로그램의 교육적 의미</strong> — 5가지 교육적 의미</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">Ⅳ. 연구 결과 개요</div><div class="pg"></div></footer>
</section><section class="page long-page">
<div class="side-label"><div class="roman">Ⅳ. 연구 결과</div><div class="alpha">A. 자연재해 유형별 추론 과정의 특징</div><div class="num"></div></div>
<header><span class="tag">Subsection</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>A. 자연재해 유형별 추론 과정의 특징</h2>
<ul class="bullet-list"><li>학생들의 추론은 <strong>직관적 반응 → 단서 탐색 → 설명 구성 → 대응 선택 → 정당화</strong>의 순서로 구조화되었다.</li>
<li>그러나 그 시작점과 중심 단서, 설명 방식, 대응 판단의 구조는 재난 유형에 따라 달랐다.</li>
<li><strong>생활 경험이 풍부한 재난(폭염, 대설):</strong> 생활 감각·몸의 경험이 출발점이 되고, "이런 날은 이렇게 해야 한다"는 생활 수준의 설명 구성·정당화로 발전하였다.</li>
<li><strong>교육 경험이 앞서는 재난(지진):</strong> 암기된 대표 수칙("책상 밑으로", "밖으로 나가기")이 출발점이 되고, 이후 공간 판단·조건 판단으로 확장되었다.</li>
<li><strong>위험이 비가시적인 재난(미세먼지, 황사):</strong> 답답함·색감 변화 등 막연한 불편에서 출발하여, 단서 탐색·설명 구성에서 정보·개념 활용 비중이 증가하였다.</li>
<li><strong>결과 장면 충격이 큰 재난(지진, 태풍):</strong> 공포·놀라움 중심 직관에서 출발하여, 공간 위험 식별·우선순위 판단으로 전개되었다.</li>
<li><strong>복합 위험 구조의 재난(태풍, 대설):</strong> 여러 위험의 동시 인식에서 출발하여, 우선순위 판단과 연속적 대응 구성이 나타났다.</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">A. 자연재해 유형별 추론 과정의 특징</div><div class="pg"></div></footer>
</section><section class="page">
<div class="side-label"><div class="roman">Ⅳ. 연구 결과</div><div class="alpha">A. 자연재해 유형별 추론 과정의 특징</div><div class="num">추론 과정의 흐름</div></div>
<header><span class="tag">Figure</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>[그림 Ⅳ-A-1] 자연재해 교육 프로그램에서 나타난 추론 과정의 흐름</h2>
<div class="figure-box"><img alt="추론 과정의 흐름" src="ewha_assets/[그림Ⅳ-A-1].png"/></div>
<ul class="table-summary"><li><strong>직관적 반응:</strong> 재난 장면에 대한 감정적·감각적 반응 ("무섭다", "답답하다", "많이 더워 보인다")</li>
<li><strong>단서 탐색:</strong> 상황 속 핵심 징후·정보·조건을 포착 (낙하물, 침수, 기온, 마스크 종류)</li>
<li><strong>설명 구성:</strong> 단서의 의미를 연결해 위험의 원인과 전개를 설명 (열사병 위험, 감전, 기관지 위해)</li>
<li><strong>대응 선택:</strong> 설명에 근거하여 적절한 행동을 선택 (외출 자제, 높은 곳 대피, KF80 이상 착용)</li>
<li><strong>정당화:</strong> 선택한 행동의 이유를 구체적 위험과 연결 (탈수 예방, 추락·갇힘 방지, 감전 방지)</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">[그림 Ⅳ-A-1] 추론 과정의 흐름</div><div class="pg"></div></footer>
</section><section class="page">
<div class="side-label"><div class="roman">Ⅳ. 연구 결과</div><div class="alpha">B. 추론 과정의 흐름</div><div class="num"></div></div>
<header><span class="tag">Figure</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>[그림 Ⅳ-B-1] 과학교육의 추론 과정과 자연재해 교육 프로그램의 추론 과정</h2>
<div class="figure-box"><img alt="추론 과정 비교" src="ewha_assets/[그림Ⅳ-B-1].jpg"/></div>
<ul class="table-summary"><li>자연재해 교육 프로그램의 추론 과정은 기존 과학교육의 추론 구조(관찰 → 가설 → 증거 → 정당화)와 공통점을 가지면서도, <strong>정서·위험 인식</strong>과 <strong>실제 생활 경험</strong>의 개입이 더 강하게 나타났다.</li>
<li>특히 <strong>대응 선택</strong>이 필수적이고 중심적인 단계로 나타나며, 인지적 판단과 실천적 판단이 결합되는 점에서 기존 과학교육 추론과 차별화된다.</li>
<li>단서 탐색과 설명 구성은 위험 해석과 대응 행동 판단으로 직접 연결되며, 정당화는 행동의 타당성이 핵심이 되었다.</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">[그림 Ⅳ-B-1] 추론 과정 비교</div><div class="pg"></div></footer>
</section><section class="page long-page">
<div class="side-label"><div class="roman">Ⅳ. 연구 결과</div><div class="alpha">C. 학생의 변화</div><div class="num"></div></div>
<header><span class="tag">Subsection</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>C. 자연재해 교육 프로그램에서 나타난 학생의 변화</h2>
<ul class="bullet-list"><li><strong>자연재해 이해의 변화 — 네 가지 방향:</strong></li>
<li>① 결과 장면·현상 이름 중심 이해 → <strong>원인과 조건</strong>을 포함한 구조적 이해</li>
<li>② 감각·정서에 기대던 이해 → <strong>구체적 위험 요소</strong>(낙하물, 탈수, 열사병, 침수, 호흡기 위해 등) 파악</li>
<li>③ 단일 현상·대표 장면 중심 이해 → 재난의 <strong>전개 과정과 복합 위험</strong>을 포함하는 이해</li>
<li>④ 생활과 분리된 재난 이해 → 자신의 <strong>생활세계</strong>(등하교, 외출, 실내 생활 등)와 연결된 이해</li>
<li><strong>판단 근거의 변화 — 네 가지 방향:</strong></li>
<li>① 감정·인상 중심 판단 → <strong>단서와 징후</strong> 기반 판단</li>
<li>② 행동 요령 단순 제시 → <strong>목적과 효과를 설명하는 정당화</strong> 수준으로 발전</li>
<li>③ 단일 행동 중심 대응 → <strong>조건과 우선순위</strong>를 고려한 연속적 대응 구성</li>
<li>④ 즉각적 회피 반응 → <strong>생활 유지와 사전 대비</strong>를 포함한 구조적 대응 판단</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">C. 학생의 변화</div><div class="pg"></div></footer>
</section><section class="page long-page">
<div class="side-label"><div class="roman">Ⅳ. 연구 결과</div><div class="alpha">D. 교육적 의미</div><div class="num"></div></div>
<header><span class="tag">Subsection</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>D. 자연재해 교육 프로그램의 교육적 의미</h2>
<ul class="bullet-list"><li><strong>1. 추론 형성 중심 교육:</strong> 자연재해 교육은 결과 지식 습득이 아니라 사고 형성의 과정이며, 학생을 수동적 수용자가 아닌 의미 구성자로 위치시키고, 설명 가능한 판단을 형성하는 교육이다.</li>
<li><strong>2. 재난 유형별 추론 구조 차이:</strong> 자연재해는 내용이 아니라 사고 구조의 차이로도 구분되어야 하며, 이 차이는 교수·학습 설계의 차이로 이어져야 한다.</li>
<li><strong>3. 대응 역량 형성:</strong> 대응 역량은 수칙 암기보다 상황 판단 능력과 더 깊이 연결되며, 삶의 맥락과 연결될 때 실제성을 가지고, 회복력과 실천 가능성을 함께 길러 준다.</li>
<li><strong>4. 중학생 대상 교육 설계 시사점:</strong> 직관을 배제하기보다 구조화해야 하며, 자료와 과제는 장면·정보·행동 판단을 연결하도록 설계되어야 하고, 평가는 이해와 판단 구조를 드러내는 방식이어야 한다.</li>
<li><strong>5. 지구과학 교육에서의 의미:</strong> 자연재해 교육은 지구과학 개념을 생활세계 속 문제로 전환하고, 설명 중심 교과에서 판단 중심 교과로 확장하며, 과학적 소양과 재난 문해력을 함께 기른다.</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">D. 교육적 의미</div><div class="pg"></div></footer>
</section><section class="page long-page">
<div class="side-label"><div class="roman">Ⅴ. 결론 및 제언</div><div class="alpha">A. 결론</div><div class="num"></div></div>
<header><span class="tag">Section</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>Ⅴ. 결론</h2>
<ul class="bullet-list"><li>본 연구는 폭염, 지진, 태풍, 미세먼지, 황사, 산사태, 대설을 포함하는 총 8차시의 자연재해 교육 프로그램을 구성·운영하고, 중학생의 추론 과정을 질적으로 분석하였다.</li>
<li><strong>결론 1:</strong> 학생들의 추론 과정은 모든 재난에서 동일하게 나타나지 않으며, 자연재해 유형의 성격에 따라 서로 다른 양상으로 조직된다.</li>
<li><strong>결론 2:</strong> 학생들의 추론은 직관적 반응 → 단서 탐색 → 설명 구성 → 대응 선택 → 정당화의 흐름을 따랐으며, 실제 대응 판단을 포함한다는 점에서 기존 과학교육 추론과 차별성을 가진다.</li>
<li><strong>결론 3:</strong> 프로그램 적용 이후 학생들의 자연재해 이해가 보다 구조적이고 생활세계와 연결된 방향으로 변화하였다.</li>
<li><strong>결론 4:</strong> 학생들의 판단 근거가 감정·상식 수준에서 구체적이고 설명 가능한 수준으로 발전하였다.</li>
<li><strong>결론 5:</strong> 본 연구의 자연재해 교육은 추론 형성, 재난 유형별 사고 구조 이해, 대응 역량 형성, 중학생 대상 교육 설계, 지구과학 교육의 확장이라는 측면에서 중요한 교육적 의미를 가진다.</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">Ⅴ. 결론</div><div class="pg"></div></footer>
</section><section class="page">
<div class="side-label"><div class="roman">Ⅴ. 결론 및 제언</div><div class="alpha">B. 제언</div><div class="num"></div></div>
<header><span class="tag">Subsection</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<h2>교육적 제언 및 후속 연구를 위한 제언</h2>
<ul class="bullet-list"><li><strong>교육적 제언 1:</strong> 학교 자연재해 교육은 자연재해 유형별 사고 구조의 차이를 반영하여 설계될 필요가 있다. 생활 경험 풍부 재난은 경험의 구조적 전환, 교육 경험 우위 재난은 수칙의 상황 판단 재구성, 비가시적 재난은 개념·정보 활용 활동, 복합 재난은 우선순위와 연속적 대응 구성 활동이 필요하다.</li>
<li><strong>교육적 제언 2:</strong> 자연재해 교육은 단순한 행동 요령 중심 교육을 넘어 추론 과정 중심 교육으로 확대될 필요가 있다.</li>
<li><strong>교육적 제언 3:</strong> 자연재해 교육의 평가 방식은 정답 여부가 아닌 사고의 흐름과 판단의 구조를 드러내는 방향으로 전환될 필요가 있다.</li>
<li><strong>후속 연구 제언 1:</strong> 초등학생, 고등학생 등 다른 학교급을 포함하거나, 다양한 지역과 학교 환경을 가진 집단을 대상으로 연구를 확장할 필요가 있다.</li>
<li><strong>후속 연구 제언 2:</strong> 학교급 간 비교는 재난교육 내용과 방법의 수준화를 설계하는 데 중요한 시사점을 제공할 수 있다.</li>
<li><strong>후속 연구 제언 3:</strong> 지역사회 연계 교육이나 디지털 기반 시뮬레이션 교육 등 다양한 교수·학습 방법과의 비교 연구도 필요하다.</li></ul>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">교육적 제언 및 후속 연구 제언</div><div class="pg"></div></footer>
</section><section class="page closing">
<header><span class="tag">Closing</span><img alt="Ewha" src="ewha_assets/ewha_wordmark.png"/></header>
<div class="thanks">
<img alt="" src="ewha_assets/ewha_seal.png"/>
<h1>감사합니다</h1>
</div>
<footer><div class="foot-brand"><img alt="" src="ewha_assets/ewha_seal.png"/>이화여자대학교 대학원</div><div class="foot-title">Closing</div><div class="pg"></div></footer>
</section>
"""

out.append(SLIDES)
out.append('\n</body>\n</html>\n')

with open(dst, 'w', encoding='utf-8') as f:
    f.writelines(out)

print(f"Done — wrote {dst}")
# Count slides
with open(dst, 'r', encoding='utf-8') as f:
    content = f.read()
count = content.count('<section class="page')
print(f"Total slides: {count}")
