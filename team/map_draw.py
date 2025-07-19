
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


def draw_map(input_file='dataFile/mas_map.csv', output_file='img/map.png'):
    # 데이터 로드
    df = pd.read_csv(input_file)

    # 좌표 범위 설정
    x_min, x_max = int(df['x'].min()), int(df['x'].max())
    y_min, y_max = int(df['y'].min()), int(df['y'].max())

    # 플롯 설정
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(x_min - 0.5, x_max + 0.5)
    ax.set_ylim(y_min - 0.5, y_max + 0.5)
    ax.invert_yaxis()  # (1,1)이 좌측 상단이 되도록
    ax.set_xticks(range(x_min, x_max + 1))
    ax.set_yticks(range(y_min, y_max + 1))
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal')

    # 구조물별 스타일 정의: category_id -> marker, 크기, 색상, 레이블, zorder
    category_styles = {
        1: {'marker': 'o', 's': 100, 'color': 'brown', 'label': 'Apartment', 'zorder': 3},
        2: {'marker': 'o', 's': 100, 'color': 'brown', 'label': 'Building', 'zorder': 3},
        4: {'marker': 's', 's': 150, 'color': 'green', 'label': 'BandalgomCoffee', 'zorder': 4},
        3: {'marker': '^', 's': 150, 'color': 'green', 'label': 'MyHome', 'zorder': 5},
    }

    # 1) 아파트, 빌딩, 반달곰 커피, 내 집 그리기
    for cat_id, style in category_styles.items():
        subset = df[df['category'] == cat_id]
        if not subset.empty:
            ax.scatter(subset['x'], subset['y'], **style)

    # 2) 건설 현장: 마지막에 그려서 우선시 (겹침 허용)
    if 'ConstructionSite' in df.columns:
        const = df[df['ConstructionSite'] == 1]
        if not const.empty:
            ax.scatter(const['x'], const['y'],
                       marker='s', s=200, color='lightgray',
                       label='under_construction', zorder=2)

    # 범례: 플롯 영역 밖 오른쪽에 배치
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0, fontsize='small')

    # 축 레이블 및 타이틀
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Local map')

    # 이미지 저장
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"{output_file} 저장 완료")

