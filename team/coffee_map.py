#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import map_draw

def parse_data():
    df_map    = pd.read_csv('dataFile/area_map.csv')
    df_struct = pd.read_csv('dataFile/area_struct.csv')
    df_cat    = pd.read_csv('dataFile/area_category.csv')
    
    # 2) category 파일 컬럼명 정리
    df_cat.columns = df_cat.columns.str.strip()  # ['category', 'struct']
    df_cat = df_cat.rename(columns={'struct': 'name'})  # ['category', 'name']
    
    # 3) 지도 데이터 + 구조물 정보 병합 (x, y 기준)
    df = pd.merge(df_map,
                  df_struct,
                  on=['x', 'y'],
                  how='left')
    
    # 4) 구조물 이름 매핑 (category 기준)
    df = pd.merge(df,
                  df_cat,
                  on='category',
                  how='left')
    
    # 5) area 기준 정렬 및 area 1에 속하는 부분만 출력
    df = df.sort_values('area').reset_index(drop=True)
    print(df[df['area'] == 1])

    
    # 6) 결과 저장
    output_file = 'dataFile/mas_map.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"{output_file} 저장 완료 (행 수: {len(df)})")
    return df

if __name__ == "__main__":
    df_combined = parse_data()
    map_draw.draw_map()