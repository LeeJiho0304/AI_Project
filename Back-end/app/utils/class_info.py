with open("./yolo_model/obj.names", "rt",encoding = "UTF8") as f:
    classes = [line.strip() for line in f.readlines()]
dictionary = {i:string for i,string in enumerate(classes)}
class_name = dictionary


class_dict={0: 'blt샌드위치', 1: '갈비구이', 2: '갈비찜', 3: '갈비탕', 4: '감자스프', 5: '감자칩', 6: '감자튀김', 7: '게장', 8: '고등어구이', 9: '고로케', 10: '고추장아찌', 11: '군고구마', 12: '군만두', 13: '김구이', 14: '김밥', 15: '김치볶음밥', 16: '김치찌개', 17: '낙지볶음', 18: '냉면', 19: '단호박', 20: '달걀말이', 21: '달걀볶음밥', 22: '닭가슴살구이', 23: '닭가슴살샐러드', 24: '닭갈비', 25: '닭강정', 26: '닭찜', 27: '돼지갈비찜', 28: '돼지고기볶음', 29: '된장찌개', 30: '두부', 31: '떡국', 32: '떡볶이', 33: '라면', 34: '라자냐', 35: '랍스타', 36: '리조또', 37: '마늘장아찌', 38: '마르게리타피자', 39: '만두', 40: '메쉬드포테이토', 41: '모듬초밥', 42: '배추김치', 43: '베이컨구이', 44: '보쌈', 45: '볶음밥', 46: '봉골레파스타', 47: '부대찌개', 48: '부침개', 49: '비빔밥', 50: '비엔나소시지', 51: '삶은 고구마', 52: '삶은달걀', 53: '삼겹살구이', 54: '삼계탕', 55: '상추샐러드', 56: '새우구이', 57: '새우튀김', 58: '생선구이', 59: '생선초밥', 60: '송편', 61: '쇠고기볶음', 62: '숙주나물', 63: '순대', 64: '스크램블드에그', 65: '스테이크', 66: '스파게티', 67: '쌀국수', 68: '쌀밥', 69: '양념치킨', 70: '어묵탕', 71: '연어구이', 72: '오므라이스', 73: '육회', 74: '잔치국수', 75: '짜장면', 76: '짬뽕', 77: '쭈꾸미볶음', 78: '참치통조림', 79: '채소죽', 80: '총각김치', 81: '치즈볼', 82: '치즈피자', 83: '치킨', 84: '치킨너겟', 85: '카레라이스', 86: '컵라면', 87: '콤비네이션피자', 88: '콩나물', 89: '퀘사디아', 90: '크림파스타', 91: '페퍼로니피자', 92: '함박스테이크', 93: '해물덮밥', 94: '해물볶음', 95: '해장국', 96: '햄볶음밥', 97: '후라이드치킨', 98: '훈제오리', 99: '훈제치킨'}

