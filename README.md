# 파이썬 학습 프로젝트

이 프로젝트는 파이썬 학습을 위한 통합 문서화 프로젝트로, 초보자부터 상급자까지 모두가 쉽게 배울 수 있는 환경을 제공합니다.

## 설치 및 설정

### 1. 가상환경 생성

```bash
python -m venv venv
```

### 2. 가상환경 활성화

#### Windows (PowerShell)

```bash
.\venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)

```bash
.\venv\Scripts\activate.bat
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 의존성 추출

```bash
pip freeze > requirements.txt
```

### 5. 프로젝트 실행

```bash
streamlit run app.py
```

## 프로젝트 구조

```
chapter_01/          # Streamlit 기초
├── section_01/      # 텍스트 출력과 기본 위젯
│   └── app.py      # Hello World 앱
├── section_02/      # 레이아웃과 화면 구성
├── section_03/      # 파일 업로드/다운로드
└── section_04/      # 데이터 시각화 기초

chapter_02/          # 실전 프로젝트 1: 주식가격 시각화
├── section_01/      # 데이터 수집 및 전처리
├── section_02/      # 캔들차트 구현
└── section_03/      # 트레이딩 시그널 추가

chapter_03/          # 실전 프로젝트 2: 뉴스 키워드 시각화
├── section_01/      # 웹 크롤링
├── section_02/      # 자연어 전처리
└── section_03/      # 워드클라우드 구현

chapter_04/          # 실전 프로젝트 3: To-Do 앱
├── section_01/      # 기본 UI 구성
├── section_02/      # 데이터 관리
└── section_03/      # 기능 구현

chapter_05/          # 실전 프로젝트 4: 머신러닝 예측
├── section_01/      # 시계열 데이터 처리
├── section_02/      # 모델 학습
└── section_03/      # 예측 결과 시각화

chapter_06/          # 실전 프로젝트 5: 컴퓨터 비전
├── section_01/      # 웹캠 연동
├── section_02/      # 손 인식 모듈
└── section_03/      # 가위바위보 게임
```

## 사용 방법

1. 가상환경을 활성화합니다
2. 원하는 챕터의 파이썬 파일을 실행합니다
3. 예: `python level_01/chapter_03/section_01_01.py`

## 가상환경 비활성화

작업이 끝나면 가상환경을 비활성화합니다:

```bash
deactivate
```
