# 버전 관리 시스템의 종류

버전 관리 시스템은 소스 코드나 문서의 변경 이력을 추적하고 관리하는 도구입니다. 대표적인 종류는 다음과 같습니다:

## 1. 로컬 버전 관리 시스템 (Local VCS)
- 사용자가 로컬 컴퓨터에서만 변경 이력을 추적
- 예: RCS(Revision Control System)
- 단점: 협업이 어렵고, 백업이나 복원이 제한적임

## 2. 중앙 집중식 버전 관리 시스템 (Centralized VCS)
- 중앙 서버에 버전 이력을 저장하고 클라이언트가 이를 내려받아 사용
- 예: CVS, Subversion(SVN), Perforce
- 장점: 중앙 집중 관리로 단순함
- 단점: 서버 장애 시 전체 작업이 중단될 수 있음

## 3. 분산 버전 관리 시스템 (Distributed VCS)
- 클라이언트가 전체 리포지터리를 복제(clone)해서 로컬에서도 전체 히스토리 관리 가능
- 예: Git, Mercurial, Bazaar
- 장점: 서버 없이도 작업 가능, 분기 및 병합 기능이 강력함

---

# .git 디렉토리의 역할

`.git` 디렉토리는 Git 프로젝트의 **모든 버전 관리 정보를 저장하는 숨겨진 폴더**로, Git 리포지터리의 핵심 역할을 합니다.

## 주요 역할
- **히스토리 저장**: 커밋, 브랜치, 태그 등의 모든 이력이 저장됨
- **객체 데이터 관리**: Git은 변경된 파일을 객체(Blob, Tree, Commit)로 저장함
- **구성 설정**: 프로젝트 수준의 설정 정보를 담고 있음 (`config`, `HEAD`, `index` 등)

## 주요 구성 파일 및 폴더
| 경로 | 설명 |
|------|------|
| `.git/config` | 해당 리포지터리의 Git 설정 |
| `.git/HEAD` | 현재 체크아웃된 브랜치를 가리킴 |
| `.git/objects/` | Git의 실제 데이터(커밋, 트리, 블롭 등) 저장소 |
| `.git/refs/` | 브랜치와 태그 등의 포인터 정보 |
| `.git/index` | 스테이징 영역 정보(인덱스) |

## 요약
`.git` 디렉토리는 Git 리포지터리의 **중추적인 데이터베이스**로, 이 폴더가 존재해야 Git 명령어를 사용할 수 있습니다. 이 디렉토리를 삭제하면 해당 프로젝트의 Git 이력이 사라집니다.


