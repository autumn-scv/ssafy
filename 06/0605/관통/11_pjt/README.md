### 서버 실행

```
cd 11-pjt
npm install chart.js
npm run dev
```

### 데이터 구조

```
{
  "pet_type": "개",
  "breed": "말티즈",
  "age_years": 3,
  "adoption_cost_krw": 200000,
  "monthly_care_cost_krw": 240000,
  "health_status_score": 95,
  "animal_name": "초코"
}
```

### 차트 종류 & 구조

|주제|타입|비고|
|:---:|:---:|:---:|
|펫 타입별 나이별 한 달 비용|2차원, 표||
|펫 타입별 건강점수별 한 달 비용|3차원||
|펫 타입별 나이별 건강점수 평균 차트|2차원||


### 앱 구조
```
components
    ├ ┬─ AgeCharTable.vue       ── 펫 타입별 나이별 한 달 비용
    │ ├─ AgeChar2d.vue          ── 펫 타입별 나이별 한 달 비용
    │ ├─ HealthStatusChar3d.vue ── 펫 타입별 건강점수별 한 달 비용
    │ └─ AgeHealthStatus2d.vue  ── 펫 타입별 나이별 건강점수 평균 차트
    │
  views
    └─┬─ TwoDGraphView.vue
      ├─ ThreeDGraphView.vue
      └─ TableView.vue
```

```
황순철
초기 화면 구성부터 디테일한 디자인까지 직접 스타일링하며, 막연했던 프론트엔드 영역과 깊이 교감할 수 있었습니다. 내 손으로 직접 사용자 인터페이스를 완성해 나가는 과정에서 큰 성취감을 느꼈고, 프론트엔드 개발의 진정한 재미를 알게 된 뜻깊은 프로젝트였습니다.
```
