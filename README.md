# Fam-Fin · 우리집 가계부

부부 공동 가계 및 자산관리 웹앱. v0.99 기반.

## 운영 환경
- main: 승인된 소스 및 운영 페이지. 현재 운영 페이지는 준비 중 안내만 표시합니다.
- develop: 테스트 후보 소스. 수정은 app/index.html에서 진행합니다.
- 테스트: https://tgrlab.github.io/Fam-Fin/test/
- 운영: https://tgrlab.github.io/Fam-Fin/
- 두 주소 모두 Pages 활성화 및 배포 성공 후 사용 가능합니다.

## 최초 배포
1. Settings > Pages > Build and deployment > Source: GitHub Actions 선택.
2. Actions > Build and publish Pages > Run workflow > main 실행.
3. 배포가 성공하면 /test/에서 예시 데이터로 확인합니다.

## 이후 수정
1. develop에서 수정합니다. Preview validation이 JavaScript 문법을 검사합니다.
2. 검증 성공 시 main의 Pages 워크플로가 자동으로 실행됩니다. 운영 페이지는 main에서, 테스트 앱은 develop에서 가져옵니다.
3. 사용자 확인 및 승인 후 PR로 develop 변경사항을 main에 병합합니다.
4. 운영 페이지는 로그인 및 보안 검증을 통과하기 전까지 준비 중 상태를 유지합니다.

## 데이터 보호
실제 금융정보, 개인정보, 카드명세서, JSON 백업, API 비밀키는 저장소에 올리지 않습니다. 테스트용 저장 키를 별도로 사용합니다. Supabase 인증·DB·권한·동시 수정 보호·월 확정 서버 검증 및 PWA는 추후 구축·검증 대상입니다. 실제 시세 API도 아직 연결하지 않았습니다.

## 로컬 빌드
`python3 scripts/build_pages.py` 후 `python3 -m http.server 8000 --directory dist` 실행. http://localhost:8000/test/ 에서 확인.
