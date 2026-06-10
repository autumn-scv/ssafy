-- 이미 테이블과 데이터는 이미 모두 생성되어있습니다.
-- 아래 쿼리는 참고용 입니다.

CREATE TABLE User (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Product (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    StockQuantity INTEGER NOT NULL DEFAULT 0,
    CategoryId INTEGER NOT NULL,  -- FK: 어떤 카테고리에 속하는지
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
    -- CategoryId는 Category 테이블의 Id를 참조합니다.
);


CREATE TABLE Purchase (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    UserId INTEGER NOT NULL, -- FK: 어떤 User의 주문인지 식별
    TotalPrice REAL NOT NULL,
    Status TEXT NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE PurchaseItem (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    PurchaseId INTEGER NOT NULL,  -- FK: 어떤 주문에 속하는지
    ProductId INTEGER NOT NULL,   -- FK: 어떤 상품인지
    Quantity INTEGER NOT NULL,    -- 주문 수량
    Price REAL NOT NULL           -- 주문 시점의 상품 가격
);