CREATE TABLE sales (
    salesdate DATE,
    productid INT,
    region TEXT,
    freeship BOOLEAN,
    discount FLOAT,
    itemssold INT
);

SELECT * FROM sales LIMIT 20;