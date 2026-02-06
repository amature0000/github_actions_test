# file-share webpage build

GitHub Actions 기반의 파일 버전 관리 + 다운로드 웹페이지 자동 생성기입니다.  
`resource/` 폴더의 파일들을 스캔하여 index.html을 자동 생성하고,  
GitHub Pages를 통해 다운로드 페이지로 배포합니다.

---

## features

- 폴더 구조 기반 자동 목록 생성
- 수정일 / 파일 크기 자동 표시
- 수정일 기준 자동 정렬
- 검색 기능
- 비활성 파일(#d) 표시
- GitHub Actions로 index.html 자동 빌드

---

## required directory Structure

```
project/
│
├─ resource/
│   ├─ topic1/
│   │   ├─ 폴더1/
│   │   │   └─ data.zip
│   │   ├─ 폴더2#d/
│   │   │   └─ data.zip
│   │
│   ├─ topic2/
│
├─ makeindex.py
├─ index.html (auto generated)
├─ runme.bat
└─ .github/workflows/build.yml
```

### 규칙

- topic 폴더 → 카테고리
- 폴더1, 폴더2 → 파일 설명
- `#d` suffix → 비활성화 (취소선 표시)
- zip 파일 → 실제 다운로드 대상

---

## How to Use

### 1 파일 추가/수정
`resource/` 폴더에 파일을 추가하거나 수정합니다.

### 2 Push
`runme.bat`을 실행합니다.

---


## Notes
github는 대용량 파일 저장 서비스가 아니며, 명시적인 리포지토리 크기 제한은 없으나 일반적으로 1GB 미만, [최대 5GB 미만](https://docs.github.com/ko/repositories/working-with-files/managing-large-files/about-large-files-on-github)을 유지하라는 권고사항이 존재합니다. 리포지토리의 크기가 지나치게 큰 경우 정정 작업을 수행하라는 경고를 받을 수 있습니다.
