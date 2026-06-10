class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
class Other(BaseModel):
    TYPR = 'OtherModel'

    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other):
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type

    def display_info(self):
        print(f'PK : {self.PK}, TYPE : {self.TYPE}, Extended Type : {self.extended_type}') #pk변수 없으면 mro 순서해서 base에서 가지고 올 것, 노벨-아더-베이스모델 가서 피케이 찾앗다, 본인-노벨-아더 아더 찾앗다
        
    def save(self):
        print('데이터를 확장해서 저장합니다.')

print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
ei = ExtendedModel('소설', '홍길동', '고전 소설', 1618, 1692, '허균', 'Extended Type')
ei.display_info()
ei.save()