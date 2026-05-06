# 문재인 정부 부동산 대책의 인과적 효과 분석

- 수행 기간: 2024.05.[^1]

- 수정 기간: 2026.03.

- 구성원: [`Wang,J.`](https://github.com/jayarnim)

## 개요

문재인 정부는 주택을 투자 자산이 아닌 거주재로 재정의한다는 목적 아래, (1) 투기적 수요 억제를 통한 주택 가격 안정, (2) 무주택자, 1주택자 등 실수요자 중심 시장 재편, 최종적으로 (3) 자산 불평등 완화라는 구체적 목표를 설정하였다. 하지만 현재로서는 이 부동산 정책이 효과적이지 못했다는 평가가 중론이다. 본 연구는 코로나 충격 이전 시행되었던 문재인 정부 부동산 대책의 실효성을 투기적 수요 억제 측면에서 확인하고자 하였다.

문재인 정부는 코로나 충격 이전 총 여섯 차례의 부동산 대책을 발표 및 시행하였다. 이 중 2017년 시행되었던 6.19, 9.5, 10.24 대책은 8.2 대책의 시범적 혹은 보완적 성격이 강하다. 또한 2019년 시행된 12.16 대책은 코로나 시국 직전에 시행되었다는 점에서 그 인과적 효과를 식별하기 어렵다. 따라서 본 연구는 2017년 8.2 대책과 2018년 9.13 대책을 중심으로, 투기과열지역 및 이와 유사한 규모의 도시를 대상으로 이중차분법을 적용하여 인과적 효과를 분석하였다.

빈도주의 이중차분모형을 적합하여 분석한 결과, 유의수준 $0.01$ 하에서 두 정책의 인과적 효과는 모두 통계적으로 유의함을 확인할 수 있었다. 추정된 인과적 효과는 $+7.59\\%$(8.2 대책), $+16.37\\%$(9.13 대책) 으로 양(+)으로 발휘되었다. 즉, 효과는 처치군의 주택 가격 상승 추세를 통제군 수준으로 억제하였다고 볼 수 없다. 요컨대 문재인 정부의 주요 부동산 대책은 투기과열지역의 가격 상승 추세를 타 지역 추세와 유사한 수준으로 억제하였다고 볼 수 없다.

한편, 본 연구는 관측 단위를 8개 광역시의 자치구로 설정하였다. 통념상 동일 광역 단위의 자치구 간에는 주택 가격에 유사성이 존재할 수 있다. 빈도주의 접근법은 이 계층 구조를 모형에 반영하기에 제약이 있다. 또한 시점 고정 효과를 처리함에 있어 각 시점을 상호 독립적으로 취급하므로, 모형에 동태적 구조를 반영하지 못한다. 따라서 지역 고정 효과에는 베이지안 계층 모델링(Bayesian Hierarchical Modeling)을, 시점 고정 효과에는 랜덤 워크(Random Walk)를 설정하여 지역 간 계층 구조와 시간 의존성을 명시적으로 반영한 모형을 재설계하였다.

베이지안 이중차분모형을 적합하여 분석한 결과, 인과적 효과는 각각 $+7.47\\%$(8.2 대책), $+16.18\\%$(9.13 대책) 으로 앞서 도출한 결론을 재확인할 수 있었다. 단, 투기과열지역 지정이 주택 가격 수준 및 변화 양상을 고려하여 이루어졌기 때문에, 처치가 완전히 외생적이라고 보기 어렵다. 다만, 평행 추세 가정 점검 결과, 사전 구간에서 유의수준 $0.01$ 하 처치군과 통제군 간 추세에 차이가 통계적으로 유의하다고 볼 수 없음을 확인하였다. 따라서 본 연구 결과는 평행 추세 가정 하에서 해석은 가능하나, 해석 시 처치의 내생성에 유의할 필요가 있다.

## 모형 상세

### 이중차분법

- **이중차분법(`D`ifference-`i`n-`D`ifferences; DiD)**: 평행 추세 가정 하에 정책 시행에 따른 인과적 효과를 반사실과의 추세 차이로써 추정하는 준실험설계법(Quasi-Experimental)

$$\begin{aligned}
Y_{i,t}(D_{i} \times T_{t})
&=\alpha + \beta D_{i} + \gamma T_{t} + \delta(D_{i} \times T_{t}) + \epsilon_{i,t}
\end{aligned}$$

- **평행 추세 가정(Parallel Trends Assumption)**: 관측 불가능한 반사실(counterfactual), 즉 실험군이 실제로 정책이 적용되지 않은 상태를 대리하는 논리적 장치로서, 정책이 없었더라면 실험군의 추세(두 시점 사이 변화량)은 통제군과 동일했을 것이라는 가정

$$\begin{aligned}
\underbrace{\mathbb{E}\left[Y_{i,t}(0)-Y_{i,s}(0) \mid D_{i}=1\right]}_{\text{experimental group}}
&\approx \underbrace{\mathbb{E}\left[Y_{i,t}(0)-Y_{i,s}(0) \mid D_{i}=0\right]}_{\text{control group}}
\end{aligned}$$

- 평행 추세 가정 하 반사실은 다음과 같이 근사될 수 있음:

$$\begin{aligned}
\mathbb{E}\left[Y_{i,t}(0)-Y_{i,s}(0) \mid D_{i}=1\right]
&=\underbrace{\mathbb{E}\left[Y_{i,t}(0) \mid D_{i}=1\right]}_{\text{counterfactual}} - \underbrace{\mathbb{E}\left[Y_{i,s}(0) \mid D_{i}=1\right]}_{\text{factual}}\\
\mathbb{E}\left[Y_{i,t}(0)-Y_{i,s}(0) \mid D_{i}=0\right]
&=\underbrace{\mathbb{E}\left[Y_{i,t}(0) \mid D_{i}=0\right] - \mathbb{E}\left[Y_{i,s}(0) \mid D_{i}=0\right]}_{\text{control group}}\\
\therefore \underbrace{\mathbb{E}\left[Y_{i,t}(0) \mid D_{i}=1\right]}_{\text{counterfactual}}
&\approx \underbrace{\mathbb{E}\left[Y_{i,s}(0) \mid D_{i}=1\right]}_{\text{factual}} + \underbrace{\mathbb{E}\left[Y_{i,t}(0) \mid D_{i}=0\right] - \mathbb{E}\left[Y_{i,s}(0) \mid D_{i}=0\right]}_{\text{control group}}
\end{aligned}$$

- **정책의 인과적 효과(`A`verage `T`reatment effect on the `T`reated; ATT)**: 정책 시행에 따른 실제 결과와 정책 미시행에 따른 반사실적 결과 간 차이

$$\begin{aligned}
\delta
&=\mathbb{E}\left[Y_{i,t}(1)-Y_{i,t}(0) \mid D_{i}=1\right]\\
&=\underbrace{\mathbb{E}\left[Y_{i,t}(1)\mid D_{i}=1\right]}_{\text{factual}} - \underbrace{\mathbb{E}\left[Y_{i,t}(0)\mid D_{i}=1\right]}_{\text{counterfactual}}\\
&\approx \underbrace{\mathbb{E}\left[Y_{i,t}(1)\mid D_{i}=1\right] - \mathbb{E}\left[Y_{i,s}(0) \mid D_{i}=1\right]}_{\text{experimental group}} + \underbrace{\mathbb{E}\left[Y_{i,t}(0) \mid D_{i}=0\right] - \mathbb{E}\left[Y_{i,s}(0) \mid D_{i}=0\right]}_{\text{control group}}
\end{aligned}$$

### 군집 표준오차

- **패널 자료(Penel Data)**: 동일한 개체(Penel Unit)를 여러 시점에 걸쳐 반복적으로 추적 조사하여 획득한 자료

$$\begin{aligned}
\mathcal{D}
&:=\\{x_{i,t}\mid i\in\mathcal{I},t\in\mathcal{T}\\}
\end{aligned}$$

- 패널 자료는 동일 관측 단위를 반복 관측한 자료라는 점에서 샘플들이 서로 독립이라 보기 어렵기 때문에 모형 적합 시 오차 항에 자기 상관이 발생하기 쉬움. 이는 자료가 제공하는 유효 정보량(혹은 유효 표본 크기)($\propto\vert\mathcal{I}\vert$)이 모형 적합 시 가정하는 정보량($\propto\vert\mathcal{D}\vert$)보다 작다는 것을 의미함. 그 결과, 회귀계수의 표준오차($\propto1/\sqrt{n}$)가 과소추정됨.

$$\begin{aligned}
\mathrm{Cov}\left(u_{i,t},u_{i,s}\right)
&\ne 0
\end{aligned}$$

- 계수 $\beta$ 의 추정량:

$$\begin{aligned}
\hat{\beta}
&=(X^{T}X)^{-1}X^{T}y\\
y
&=X\beta+u\\
\therefore\hat{\beta}
&=\beta+(X^{T}X)^{-1}X^{T}u
\end{aligned}$$

- 계수 $\beta$ 의 추정량의 표준오차(Standard Error):

$$\begin{aligned}
\mathrm{Var}(\hat{\beta})
&=(X^{T}X)^{-1}\mathrm{Var}(X^{T}u)(X^{T}X)^{-1}\\
\\
\mathrm{Var}(X^{T}u)
&=\mathrm{Var}(\sum_{i}{x_{i}u_{i}})\\
&=\sum_{i,j}{\mathrm{Cov}(x_{i}u_{i},x_{j}u_{j})}\\
&=\sum_{i,j}{x_{i}x_{j}\mathrm{Cov}(u_{i},u_{j})}\\
&=X^{T}\Sigma X
\end{aligned}$$

- 관측치의 오차항 간 독립성 가정 하 표준오차:

$$\begin{aligned}
\mathrm{Cov}(u_{i},u_{j})
&=\sigma^{2} I\\
\therefore \mathrm{Var}(X^{T}u)
&=\sigma^{2}X^{T} X\\
\therefore \mathrm{Var}(\hat{\beta})
&=\sigma^{2}(X^{T}X)^{-1}
\end{aligned}$$

- 군집 내 관측치의 오차항 간 자기상관 하 군집 표준오차(Cluster Standard Error):

$$\begin{aligned}
\mathrm{Cov}(u_{i},u_{j})
&\ne 0 \quad \mathrm{for}\quad i,j\in g\\
\mathrm{Var}(X^{T}u)
&=\sum_{g}\sum_{i,j}{x_{i}x_{j}\mathrm{Cov}(u_{i},u_{j})}\\
&=\sum_{g}{X^{T}_{g}\Sigma_{g}X_{g}}\\
\therefore \mathrm{Var}(\hat{\beta})
&=(X^{T}X)^{-1}\left(\sum_{g}{X^{T}_{g}\Sigma_{g}X_{g}}\right)(X^{T}X)^{-1}
\end{aligned}$$

### 베이지안 이중차분모형

- 모형 정의:

$$\begin{aligned}
y_{i,t}
&\sim\mathcal{N}(\mu,\sigma^{2})\\
\sigma
&\sim\mathrm{HalfNormal}(2)\\
\\
\mu
&:=\alpha_{i}+\tau_{t}\\
&\quad+\delta_{1}(\mathrm{Treatment}_{i}\times\mathrm{Post1}_{t})\\
&\quad+\delta_{2}(\mathrm{Treatment}_{i}\times\mathrm{Post2}_{t})
\end{aligned}$$

- 지역 고정 효과(Hierarchical Bayesian):

$$\begin{aligned}
\mu_{\alpha}
&\sim\mathcal{N}(0,2^{2})\\
\sigma^{\mathrm{(city)}}
&\sim\mathrm{HalfNormal}(2)\\
\alpha^{\mathrm{(city)}}_{c}
&\sim\mathcal{N}(\mu_{\alpha},\sigma^{\mathrm{(city)}})\\
\sigma^{\mathrm{(region)}}
&\sim\mathrm{HalfNormal}(2)\\
\alpha^{\mathrm{(region)}}_{i}
&\sim\mathcal{N}(\alpha^{\mathrm{(city)}}_{c(i)},\sigma^{\mathrm{(region)}})
\end{aligned}$$

- 시점 고정 효과(Random Walk):

$$\begin{aligned}
\sigma_{\tau}
&\sim\mathrm{HalfNormal}(2)\\
\tau_{t}
&\sim\begin{cases}
\mathcal{N}(0,\sigma^{2}_{\tau}),\quad &t=1\\
\mathcal{N}(\tau_{t-1},\sigma^{2}_{\tau}),\quad &t\ne1
\end{cases}
\end{aligned}$$

- 중심화(centralization):

$$\begin{aligned}
\tau_{t}\longleftarrow\tau_{t}-\frac{1}{T}\sum_{s}{\tau_{s}}
\end{aligned}$$

- 1차 정책 효과:

$$\begin{aligned}
\delta_{1}\sim\mathcal{N}(0,2^{2})
\end{aligned}$$

- 2차 정책 효과:

$$\begin{aligned}
\delta_{2}\sim\mathcal{N}(0,2^{2})
\end{aligned}$$

## 실험 및 결과

### 데이터

데이터는 국토교통부에서 제공하는 실거래가 공개 시스템([`link`](https://rt.molit.go.kr/))에서 수집하였다. 두 대책 사이 약 1년의 기간이 있으므로, 2016년 1월부터 2019년 12월까지를 기간으로 하였다. 처치군은 8.2 대책에서 투기과열지구로 선정된 서울특별시, 세종특별자치시, 경기도 과천시로 설정하였다. 통제군은 처치군과 비슷한 위계인(광역 단위) 광주광역시, 대구광역시, 대전광역시, 부산광역시, 울산광역시, 인천광역시로 설정하였다.

지역 단위는 각 도시의 자치구로 하였다. 단, 경기도 과천시의 경우 해당 단위가 기초자치단체로서 광역 단위의 자치구와 토지 규모가 비슷하므로 지역 단위를 세분화하지 않고, 서울특별시의 하위 단위로 편입하였다. 세종특별자치시는 광역 단위이나 하위 기초자치단체가 부재하다. 다만, 도시 전체를 단일 지역 단위로 설정하기에는 행정 구역인 읍/면/동의 토지 규모가 상당하다. 따라서 해당 도시에 대해서만 예외적으로 행정 구역을 지역 단위로 설정하였다.

데이터 셋은 일자별 체결된 실거래가를 제공한다. 해당 가격을 제곱미터($m^{2}$) 당 가격으로 변환하였다. 또한 주택 가격의 경우 곱셈 구조를 가정하는 것이 표준적이므로, 로그 변환을 적용하였다. 이후 거래 단위에서 발생하는 잡음을 줄이기 위하여 지역 단위에 대하여 월별 평균을 적용하였다. 주요 정책으로 다루고 있는 8.2 대책과 9.13 대책이 시행된 2017년 8월, 2018년 9월을 기준으로, 2016년 1월부터 2017년 7월까지를 사전 구간, 2017년 8월부터 2018년 8월까지를 1차 정책 시행 구간, 2018년 9월부터 2019년 12월까지를 2차 정책 시행 구간으로 구분하였다.

### 평행 추세 가정 검증

![pre_trend](/desc/pre_trend.png)

평행 추세 가정을 검증하기 위하여 우선 사전 구간에 대하여 처치군과 통제군의 시점별 평균을 내어 시각화하였다. 평균적으로 추세가 유사하나 처치군의 경우 상대적으로 기울기가 흔들리는 것을 확인할 수 있다. 따라서 사전 구간에 대하여 모형을 설계하여 적합하였다. 단, 패널 데이터는 동일 관측 단위를 반복 관측한 데이터이기 때문에, 모형 적합 시 잔차 항에 자기상관이 발생하기 쉽다. 이는 회귀계수 추정오차의 과소 추정 문제로 귀결된다. 따라서 회귀계수 추정 시 관측 단위(지역) 간 자기상관을 반영하는 군집 표준오차를 적용하였다.

$$\begin{aligned}
y_{i,s}
&=\beta+\alpha_{i}+\tau_{s}+\delta(\mathrm{Treatment}_{i}\times s)+\epsilon_{i,s}
\end{aligned}$$

위 수식은 평행 추세 가정을 검증하기 위하여 적합한 모형을 나타낸다. 결정계수 $R^{2}$ 는 $0.983$ 으로 모형의 설명력이 확보되었음을 확인하였다. F-검정 결과 $\mathrm{Pr}(F>F_{\mathrm{obs}}\mid H_{0})$ 는 $0$ 에 근사하여 설명변수가 유효함을 확인하였다.[^2] Durbin-Watson 통계량은 $1.797$ 로 잔차 항의 자기상관이 존재한다고 볼 수 없음을 확인하였다.[^3] 적합 결과, 계수 추정치는 $\delta=0.0018$ 로 처치군이 통제군보다 월 $0.18\\%$ 상승하였음을 확인할 수 있었다. 단, p-값이 $0.037$ 로 이 차이는 $0.01$ 유의수준 하에서는 통계적으로 유의하다고 볼 근거가 부족하였다.

### 빈도주의 이중차분법

$$\begin{aligned}
y_{i,t}
&=\beta+\alpha_{i}+\tau_{t}\\
&\quad+\delta_{1}(\mathrm{Treatment}_{i}\times\mathrm{Post1}_{t})\\
&\quad+\delta_{2}(\mathrm{Treatment}_{i}\times\mathrm{Post2}_{t})\\
&\quad+\epsilon_{i,t}
\end{aligned}$$

전체 구간에 대하여 빈도주의 이중차분모형을 적합하였다. 설계한 모형은 위 수식과 같다. 마찬가지로 결정계수 $R^{2}$ 는 $0.976$ 으로 모형의 설명력이 확보되었음을 확인하였다. F-검정 결과 $\mathrm{Pr}(F>F_{\mathrm{obs}}\mid H_{0})$ 는 $0$ 에 근사하여 설명변수가 유효함을 확인하였다. 다만, Durbin-Watson 통계량은 $1.183$ 으로 잔차 항에 양의 자기상관이 존재함을 확인하였다. 적합 결과, 계수 $\delta_{1}=0.0732,\delta_{2}=0.1516$ 으로, 통제군 대비 처치군의 가격 상승 추세는 8.2 대책 이후 $+7.59\\%$, 9.13 대책 이후 $+16.37\\%$ 였음을 확인할 수 있었다. p-값은 모두 $0.000$ 으로, 유의수준 $0.01$ 하 이 인과적 효과는 모두 유의하였다. 종합하자면, 이 결과는 8.2 대책과 9.13 대책은 투기과열지역의 주택 가격 상승 추세를 타 지역과 유사한 수준으로 억제하였다고 볼 수 없음을 시사한다.

### 베이지안 이중차분법

지역 간 계층 구조와 시간 의존성을 명시적으로 반영하기 위하여 지역 고정 효과에는 베이지안 계층 모델링을, 시점 고정 효과에는 랜덤워크를 적용한 베이지안 이중차분모형을 설계하였다. 모형은 `모형 상세` 의 `베이지안 이중차분모형` 에 서술되어 있다. 빈도주의 이중차분모형과 달리, 해당 모형에는 전역 편향이 명시적으로 존재하지 않는다. 이는 지역 고정 효과의 최상위 계층 $\mu_{\alpha}$ 가 암묵적으로 전역 레벨로서 기능하기 때문이다. 모형 적합 시 지역 고정 효과는 레벨(baseline), 시점 고정 효과는 변동성(deviation)으로 역할을 구분하기 위하여 시간 고정 효과를 중심화(centralization)하였다.

![ppc](/desc/ppc.png)

MCMC 를 활용하여 모형을 적합하였다. $4$ 개 체인에 대하여 $15,000$ 번의 샘플링을 통해 총 $60,000$ 개의 샘플을 추출하였다. 샘플 간 자기상관을 줄이기 위하여 초기 $4\times5,000$ 개의 샘플은 제거하였고(tuning), 나머지 $4\times10,000$ 개의 샘플을 분석에 활용하였다. 수렴성을 진단하기 위하여 ESS(Bulk), ESS(Tail)[^4]이  $4\times 100$ 개 미만이거나 Gelman–Rubin 통계량[^5]이 $1.01$ 초과인 모수의 유무를 점검하였다. 점검 결과, 모든 모수가 조건을 충족하였음을 확인하였다. 또한 모형의 예측력과 예측 불확실성의 적절성을 확인하기 위하여 사후 예측 분포(좌)와 PIT[^6] 분포를 시각화하였다. 예측력은 대체로 양호하나 PIT 분포가 중앙에 집중되는 경향을 보여 예측 분산을 과대 추정하고 있음을 확인하였다. 이는 모형이 예측에 보수적인 경향을 보이는 것으로 해석할 수 있다.

<div align="center">
  <img src="/desc/region_fixed_effect_0.png" width="30%" />
  <img src="/desc/region_fixed_effect_1.png" width="65%" />
</div>

지역 고정 효과의 계층 구조 가정이 데이터와 모순되지 않았는지 확인하기 위하여 광역 단위 고정 효과 $\alpha^{(\mathrm{city})}$ 와 기초자치단체 단위 고정 효과 $\alpha^{(\mathrm{region})}$ 의 사후 분포를 시각화하였다. 고정 효과의 사후 분포를 살펴보면, 광역 단위 간 이질성이 존재하며, 광역 단위 내 지역 간에도 이질성이 존재하는 동시에 그 값이 소속 광역시의 평균값으로 수렴하고 있음을 확인할 수 있다.

![region_fixed_effect_sigma](/desc/region_fixed_effect_sigma.png)

위 그림은 광역 단위, 기초자치단체 단위 고정 효과 표준편차의 사후 분포 $\sigma^{(\mathrm{city})}, \sigma^{(\mathrm{region})}$ 를 시각화한 것이다. 광역 단위 간, 광역 단위 내 지역 간 이질성을 살펴보면 다음과 같다. 우선, $\sigma^{(\mathrm{city})}$ 의 사후 평균은 $0.38$ 로, 광역 단위 간 고정 효과에 $46.2\\%$ 의 변동성이 있다. 또한 $\sigma^{(\mathrm{region})}$ 의 사후 평균은 $0.38$ 로, 동일 광역 내 지역 간 고정 효과에는 $46.2\\%$ 의 변동성이 있다. 따라서 지역 고정 효과의 계층화가 데이터의 공간적 구조를 반영하고 있음을 시사한다.

![time_fixed_effect](/desc/time_fixed_effect.png)

이중차분모형에서 정책의 인과적 효과는 정책 시행 시점 전후 변화 양상을 추정함으로써 식별된다. 때문에 계수 $\delta$ 가 공통 시간 충격을 제외한 인과적 효과만을 반영한다는 점을 확인하기 위해서는 시점 고정 효과의 변동 추세를 살펴볼 필요가 있다. 위 그림은 각각 시점 고정 효과의 시간의 흐름에 따른 변화 추세(좌)와 그 표준편차의 사후 분포(우)를 시각화한 것이다. 좌측 그림의 빨간색 선은 8.2 대책과 9.13 대책 시행 시점을, 회색 선은 6.19, 9.5, 10.24, 12.16 대책 시행 시점을 나타낸다. 분석의 대상이 되는 8.2 대책과 9.13 대책 전후 시점 고정 효과의 변화 양상이 급격하지 않음을 확인할 수 있다. 또한 표준편차 사후 분포의 평균은 $0.013$ 으로, 시점 간에는 $1.31\\%$ 의 변동성이 존재한다. 따라서 시점 고정 효과는 정책의 인과적 효과를 제외한 공통 시간 충격만을 반영하고 있다고 볼 수 있다. 이는 후술할 계수 $\delta$ 값이 인과적 효과로서 설득력이 있음을 시사한다.

![att](/desc/att.png)

위 그림은 인과적 효과를 나타내는 계수 $\delta_{1},\delta_{2}$ 의 사후 분포를 시각화한 것이다. 8.2 대책에 대한 인과적 효과의 사후 평균은 $0.072$ 로, 해당 대책 이후 처치군의 주택 가격은 통제군 대비 $+7.59\\%$ 상승하였다. 또한 9.13 대책에 대한 인과적 효과의 사후 평균은 $0.15$ 로, 해당 대책 이후 처치군의 주택 가격은 통제군 대비 $+16.18\\%$ 상승하였다. 이로부터 빈도주의 이중차분모형의 적합 결과와 동일한 결론을 내릴 수 있다. 단, 인과적 효과가 양적으로 발휘되었다고 해서 정책이 투기과열지역의 가격 상승 추세를 부추겼다고 볼 수는 없다. 또한 투기과열지역 지정은 주택 가격 수준 및 변화 양상을 고려하여 이루어졌다. 때문에 평행 추세 가정을 기각할 근거가 부족하다는 것이 확인되었으나, 결과 해석 시 처치가 완전히 외생적이라고 보기 어렵다는 점을 고려할 필요가 있다.

[^1]: 본 연구는 초기 군집 표준오차를 적용하여 평행 추세 가정을 검증하고, 빈도주의 이중차분모형을 적합하여 정책의 인과적 효과를 추정하는 데 그쳤다. 수정 기간 동안 지역 고정 효과에 계층 구조를 반영하고, 시점 고정 효과에 시간 의존성을 반영하는 베이지안 이중차분모형을 설계하여 실험을 재수행하였다.

[^2]: 회귀계수가 모두 0 일 때의 F-통계량 F 가 적합된 모형의 F-통계량 F_obs 보다 높을 확률에 대한 검정. F-통계량은 잔차변동 대비 회귀 변동의 비율을 나타냄.

[^3]: 잔차 항의 1차 자기상관 여부를 측정하는 통계량. 0 < DW < 4 의 범위를 가지며, 2 일 때 자기상관이 없다고 해석하고, 2 보다 작을 때 양의 자기상관이, 2 보다 클 때 음의 자기상관이 존재한다고 해석함.

[^4]: 유효 샘플 수(Effective Sample Size)로서 샘플 간 자기상관을 보정한 정보량. ESS(Bulk) 는 사후 분포 중심부의 샘플 정보량으로서 중심 위치 통계량의 신뢰도를 나타냄. ESS(Tail) 은 사후 분포 주변부의 샘플 정보량으로서 신용구간(Credible Interval) 경계의 신뢰도를 나타냄. 공식 문서에서는 ESS(bulk)가 체인 수의 100배 이상이어야 함을 권고함[(`link`)](https://www.pymc.io/projects/examples/en/latest/diagnostics_and_criticism/Diagnosing_biased_Inference_with_Divergences.html).

[^5]: 체인 간 수렴성 평가 지표로서 체인 내 샘플 간 분산 대비 체인 간 중심 위치의 분산의 비율의 자승근. 공식 문서에서는 R_hat 이 1.01 미만이어야 함을 권고함[(`link`)](https://www.pymc.io/projects/examples/en/latest/bart/bart_introduction.html).

[^6]: 확률 적분 변환(Probability Integral Transform)으로서 사후 예측 분포에서 생성된 값이 실제 관측값 이하일 확률. 모형이 과신할수록 표준화된 관측값은 사후 예측 분포의 평균(0)보다 극단적으로 크거나(PIT=1) 극단적으로 작을 수 있음(PIT=0). 따라서 PIT 분포가 U 곡선이 됨. 반대로 모형이 불확실성을 높게 잡을수록 표준화된 관측값은 사후 예측 분포의 평균(0) 근처에 위치함. 따라서 PIT 분포가 역-U 곡선이 됨.