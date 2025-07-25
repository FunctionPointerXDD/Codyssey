
---

# 컨테이너 및 관련 기술 문서

## 1. 가상머신(VM)과 컨테이너의 차이

| 구분     | 가상머신(Virtual Machine)         | 컨테이너(Container)                                |
| ------ | ----------------------------- | ---------------------------------------------- |
| 격리 방식  | 하이퍼바이저를 통한 하드웨어 가상화           | 운영체제 커널의 기능(Linux namespaces, cgroups)을 활용한 격리 |
| OS 포함  | 전체 운영체제(Guest OS) 필요          | 호스트 OS와 커널 공유, Guest OS 불필요                    |
| 리소스 사용 | 비교적 무거움(GB 단위 이미지, 느린 부팅)     | 경량(이미지 용량 작음, 빠른 시작)                           |
| 시작 속도  | 수십 초 \~ 수 분                   | 수 초 이내                                         |
| 활용 예시  | 다양한 OS 환경, 완벽 격리 필요 시         | 마이크로서비스, CI/CD, 빠른 배포/확장                       |
| 예시     | VMware, VirtualBox, Hyper-V 등 | Docker, containerd, CRI-O, runc 등              |

**요약:**
가상머신은 하드웨어 전체를 가상화해서 여러 OS를 실행할 수 있지만, 무겁고 느립니다.
컨테이너는 OS 커널을 공유하며, 프로세스 수준에서 격리되어 훨씬 가볍고 빠르며 리소스 효율성이 높습니다.

---

## 2. 컨테이너와 이미지의 차이

| 컨테이너(Container)               | 이미지(Image)                       |
| ----------------------------- | -------------------------------- |
| 이미지로부터 생성된 실행 가능한 인스턴스        | 컨테이너 생성을 위한 읽기 전용 템플릿            |
| 메모리, 네트워크, 파일 시스템 등 런타임 상태 가짐 | 실행 파일, 라이브러리, 설정 등만 포함           |
| 상태 변화 가능 (파일 수정 등)            | 불변(immutable), 직접 실행 불가          |
| 실행/정지/삭제 등 동적으로 관리됨           | 레지스트리에 저장/배포, 빌드/다운로드 대상         |
| 예시: 실행 중인 Ubuntu 컨테이너         | 예시: Ubuntu 이미지 (`ubuntu:latest`) |

**요약:**
이미지는 컨테이너 실행에 필요한 모든 정보를 가진 설계도(정적).
컨테이너는 이미지를 기반으로 실행된 프로세스(동적)로, 상태 변화와 네트워크/스토리지 격리 등을 포함합니다.

---

## 3. 컨테이너 런타임(Container Runtime) 정의

**컨테이너 런타임**은
컨테이너 이미지를 기반으로 실제로 컨테이너를 생성, 실행, 관리하는 소프트웨어 컴포넌트입니다.
컨테이너의 라이프사이클(생성, 시작, 정지, 삭제 등)을 담당하며,
도커, 쿠버네티스와 같은 오케스트레이션 도구와 연동해 컨테이너 인스턴스를 직접 관리합니다.

* 컨테이너 런타임은 이미지에서 컨테이너를 만들고,
  운영체제 커널의 네임스페이스, cgroups, 파일 시스템 계층 등을 설정합니다.
* 런타임은 저수준(Low-level)과 고수준(High-level)으로 구분될 수 있음
  (예: Docker → High-level, runc → Low-level).

---

## 4. CNCF Landscape 기준 컨테이너 런타임 종류(3가지)

### 1. containerd

* 도커에서 분리된 CNCF 프로젝트.
* 컨테이너의 전체 라이프사이클(이미지 풀/푸시, 컨테이너 실행/정지/삭제, 볼륨/네트워크 관리 등)을 담당.
* 쿠버네티스의 기본 런타임 중 하나.

### 2. CRI-O

* 쿠버네티스(Kubernetes)를 위한 경량 컨테이너 런타임.
* OCI(Open Container Initiative) 이미지 및 런타임 표준을 지원.

### 3. runc

* 도커와 containerd 등에서 실제로 컨테이너를 생성/실행하는 저수준 런타임.
* Linux의 네임스페이스, cgroups 등을 사용해 프로세스 격리를 구현.

> 기타 주요 런타임 예시: gVisor, Kata Containers 등

---

## 5. 도커 이미지의 레이어(Docker Image Layers)란?

도커 이미지는 \*\*여러 개의 읽기 전용 레이어(Layer)\*\*로 구성된 파일 시스템 구조입니다.
각 레이어는 Dockerfile의 한 줄(명령어)에 해당하며,
이미지 빌드시 새로운 파일 추가, 수정, 삭제 등이 레이어별로 저장됩니다.

### 주요 특징

* **중복 최소화/캐싱:**
  여러 이미지가 동일한 베이스 레이어를 공유하면,
  해당 레이어는 한 번만 저장되어 효율적입니다.
* **변경 시 레이어 분리:**
  Dockerfile의 특정 명령이 변경되면 그 이후 레이어만 새로 빌드됨.
* **최종 컨테이너:**
  이미지는 읽기 전용이고, 컨테이너 실행 시 최상단에 읽기/쓰기 가능한 레이어가 추가되어
  컨테이너 내에서 파일 변경이 가능해짐.
* **빠른 배포:**
  네트워크로 이미지를 전송할 때,
  변경된 레이어만 전송하여 효율적으로 관리할 수 있음.

### 시각화 예시

```text
[Layer 4: 앱 설치 및 설정]
[Layer 3: 필요 패키지 설치]
[Layer 2: OS 업데이트]
[Layer 1: Base OS (예: ubuntu)]
```

* 위에서 아래로 쌓인 구조
* 컨테이너는 최상단에 추가된 임시(읽기/쓰기) 레이어에서 동작

---

**참고 링크**

* [도커 공식 문서 - What is a Container?](https://docs.docker.com/get-started/overview/)
* [CNCF Cloud Native Landscape](https://landscape.cncf.io/category=container-runtime)
* [도커 이미지 구조 공식 문서](https://docs.docker.com/storage/storagedriver/#docker-image-layers)

---

