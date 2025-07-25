---
title: 그런데 이 서비스의 KPI는 무엇인가요?
slug: kpi
status: public
date: 2025-06-21
---

그날 기획자는 새롭게 개발될 서비스에 추가될 기능에 대한 아이디어를 도출하기 위해 프로젝트에 참여하는 모든 관계자를 불러 모았다. 기획자가 아무 의견이라도 괜찮다고 여러 번 말했으나 회의실에는 침묵만이 자리했다. 그러던 중 누군가가 기획자에게 무심코 물었다.

> 그런데 이 서비스의 KPI는 무엇인가요?

기획자는 짧은 침묵 뒤에 말했다. 

>  글쎄요. 잔존률을 높이고 이탈률을 낮추는 거겠지요. 

그 뒤 놀라운 일이 벌어졌다. 침묵은 사라지고 여기저기서 아이디어가 쏟아졌다.

> - 매일 '오늘의 활동'을 알리는 알림을 보낸다.
> - 로그인 시 ‘오늘의 출석’ 보상(포인트/쿠폰 등)을 제공한다.
> - 레벨업·배지·경험치 등 가벼운 ‘게임화’ 요소를 추가한다.
> - 홈 화면에 “일간/주간 미션”을 항상 노출한다.
> - "당신의 활동이 또래보다 높아요/적어요"

위 언급 중 내가 말한 것도 있는데, 난 그날 내 입이 한 일을 부끄럽게 기억한다. 위 아이디어 중 살아남은 것은 단 하나도 없다. 기획자가 위와 같은 의견을 모두 버린 것은 정말 다행스러운 일이었다.

생각한다. 그날의 침묵은 무엇 때문이었을까? 그 침묵은 왜 '잔존률과 이탈률'이란 단어로 인해 사라졌는가.

## {{ center_h2(content="❃") }}

좋은 서비스는 분명 잔존률이 높고 이탈률이 낮을 것이다. 너무도 당연하기에 우린 그 사실을 알고 있다. 그런데 입으로 '잔존률'과 '이탈률'을 말함으로써 '잔존률'과 '이탈률'이 서비스에서 가장 중요한 요인으로 단숨에 격상했다. 나를 포함한 회의 참석자는 자신도 모른 채 '좋은 서비스'에 대한 생각을 지우고 잔존률을 높이기 위한 방법을 생각했다. 측정을 위한 지표가 목표로 뒤바뀐 것이다. 허나 지표의 달성이 목표가 되면 좋은 것이 나오기 어렵다.

[Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) 에 아래와 같은 문장이 있다.

> 목표가 복잡하고, 미묘할 수록 이를 단순한 지표로 환원하기 어렵다. 이런 목표가 단순한 지표로 구현되면, 작업을 올바르게 수행할 능력이 있는 사람도 지표와 목표를 혼동해 지표를 달성하는 게 마치 궁극적인 목표인 것처럼 행동할 수 있다.
>
> He discusses how systems in general can be [gamed](https://en.wikipedia.org/wiki/Game_the_system), focusing on cases where the goals of a task are complex, sophisticated, or subtle. In such cases, the persons possessing the skills to execute  the tasks properly seek their own goals to the detriment of the assigned tasks. When the goals are instantiated as metrics, this could be seen as equivalent to Goodhart and Campbell's claim.

왜 이런 현상이 발생하는 것일까? 문제의 모든 세부 사항을 고려하면 생각을 계속하기 어렵다. 인간은 오직 추상을 사용해 생각을 계속해나간다. 이때 '추상화'란 잠시 세부 사항을 잊어버리는 것이다. 우린 상황의 본질을 찾아 낸 후 그 본질에만 집중함으로 문제를 해결할 수 있다.

'좋은 서비스'가 무엇인지 생각하는 것은 어렵고 미묘한 일이라 그날 회의실에는 침묵만이 자리했다. 그런데 '잔존률'이란 지표가 언급되자 우린 그것을 자신도 모르게 문제의 본질이라 착각해 그것에만 집중한 것이다. 이건 잘못된 추상화였다. 추상화를 잘 수행하려면 그 안에 내재된 속성과 우연히 나타난 속성을 구분하고 내재한 속성에 집중해야 한다. 잔존률은 우리가 구현하려는 서비스의 내재적 속성이 아니었다. 그건 그냥 측정값일 뿐이다.  [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) 는 측정값이 목표가 되면 그건 더 이상 좋은 측정값이 될 수 없다고 말한다. 측정값을 목표로 정하는 것을 '있다'와 '해야 한다'를 잘못 결합한 것이라고 말한다.

## {{ center_h2(content="❃") }}

추상화를 잘 하려면 문제의 본질이 무엇인지 생각해야  한다. 그게 너무 어려울 때 우린 자기도 모른 채 쉬운 것을 중요한 것으로 착각한다. 중요한 것보다 측정할 수 있는 것에 초점을 맞춘다. 『알고리즘, 인생을 계산하다』는 이에 대한 여러 예시를 **과적합** 장에서 제시하며 이들을 잘못된 것을 무모하고도 영리하게 최적화한 사례라고 설명한다.

- 전자 채점 장비가 펜싱에 도입되자 이 종목의 특성이 바뀌었고, 진지한 결투에서는 별 쓸모가 없는 기술들이 경기에서 중요한 기술이 되었다.
- 취업 알선 회사의 직원들은 구직자 상담 횟수로 성과를 평가하자, 실제로 구직자가 일자리를 찾는 데 도움이 될 만큼 상담 시간을 갖는 대신에 가능한 한 빨리 상담을 끝내려는 쪽으로 동기 부여가 되었다.
- 미 연방 정부의 한 사법기관에서는 수사관들에게 월간 사건 처리량을 할당했는데, 수사관들이 가장 시급한 사건보다는 월말에 쉬운 사건들만 골라서 처리하는 경향을 보였다.

Paul Graham은 [The Origins of Wokeness](https://paulgraham.com/woke.html) 에서 [정치적 올바름](https://en.wikipedia.org/wiki/Political_correctness) 을 같은 방식으로 비판한다. 그는 정치적 올바름을 '사회 정의에 대한 적극적인 성과 중심(An aggressively performative focus on social justice.)'라고 요약한다. 정치적 올바름은 너무도 얕고 복잡한 규칙을 도입했고 그 규칙을 따르지 않는 사람을 올바르지 않은 것으로 섣부르게 규정한다는 게 Paul Graham 의 문제의식이며 나도 이에 동의한다.

Matthew Walther는 [Stock Ownership Is What Really Divides Americans](https://www.nytimes.com/2025/04/12/opinion/stock-market-tariffs.html) 에서 주식 시장이 미국의 건강과 동의어로 받아들여지는 현상을 비판하며 "모든 수치는 현대 사회의 정량화하기 어려운 여러 가지 측면과 함께 고려되어야 한다. 어떤 의미에서 현대 사회의 안 좋은 것, 일종의 병리적 증상은 마켓에는 좋은 것이었다."고 말한다.

## {{ center_h2(content="❃") }}

암묵적인 측정값도 우리에게 큰 영향을 준다. 가령 자본주의는 모든 것을 돈이라는 수치로 환산하려는 태도를 기르게 한다.(내 12살 아들을 보니 정말 그러하다.) 하물며 목표로 격상된 지표는 우리에게 더욱 큰 영향을 주며 대다수는 원치 않는 방식으로 동작한다.

사람은 명확한 것을 좋아한다. 명확해야 참과 거짓을 가르는 선을 그을 수 있다. 생각을 구현하려면 생각을 먼저 명확하게 다듬어야 한다. 그런데 중요한 것일 수록 명확하지 않다. 좋은 서비스가 무엇인지 명확하지 않다. 좋은 삶을 규정하긴 얼마나 어려운가. 우린 이 일이 어렵다는 것을 있는 그대로 받아들여야 한다.

우린 해결하고자 하는 문제가 어려운 것일 수록 지표를 목표로 설정한다. 그것이 옳기 때문이 아니라 그렇게 하는 게 쉽기 때문에. 때로는 오직 그 방법 뿐이기에. 그러나 때때로 지표는 본질을 변질시킨다. 본질을 찾을 수 없다면, 그게 모호하다면 모호한 것을 모호한 채로 두어야 한다. 그래야 우리는 그것에 대해 끊임 없이 생각하고 그것으로 본질에 조금 더 다가갈 수 있다. 

우리가 서로에게 주어야 할 것은 지표가 아니라 '좋음'이 무엇인지 고민하고 성찰하는 시간과 태도이다. 나올 수 있는 것이 오직 침묵 뿐이더라도.
