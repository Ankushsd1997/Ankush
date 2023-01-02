----EXERCISE 1:
CREATE TABLE PLAYER(
PId INTEGER PRIMARY KEY,
PName VARCHAR2(20) NOT NULL,
Ranking INTEGER)

----EXERCISE 2:
CREATE TABLE Tournament(
TId INTEGER PRIMARY KEY,
TName VARCHAR2(30) NOT NULL,
StartDt DATE NOT NULL,
EndDt DATE NOT NULL,
Prize INTEGER NOT NULL);

----EXERCISE 3:
CREATE TABLE MATCH(
MID INTEGER,
TID INTEGER REFERENCES Tournament(TID),
PLAYER1 INTEGER REFERENCES PLAYER(PID),
PLAYER2 INTEGER REFERENCES PLAYER(PID),
MATCHDT DATE NOT NULL,
WINNER INTEGER REFERENCES PLAYER(PID),
SCORE VARCHAR(30) NOT NULL,
PRIMARY KEY(MID, TID),
CHECK(PLAYER1<>PLAYER2));

----EXERCISE 4:
ALTER TABLE PLAYER ADD (MatchesPlayed NUMBER, MatchesWon NUMBER);

----EXERCISE 7:
ALTER TABLE PLAYER DROP(ContactNo);

----EXERCISE 8:
ALTER TABLE PLAYER RENAME COLUMN PID TO PLAYERID;

----EXERCISE 9:
ALTER TABLE PLAYER MODIFY PNAME VARCHAR2(50);

----EXERCISE 10:
INSERT INTO SALESMAN VALUES(11, 'Elizabeth', 'London');

----EXERCISE 11:
INSERT INTO PRODUCT VALUES(110, 'Bat', 50, 'Sports', NULL);

----EXERCISE 12:
SELECT * FROM PRODUCT;

----EXERCISE 13:
SELECT Prodid, Price, Category FROM PRODUCT;

----EXERCISE 14:
SELECT DISTINCT Category FROM PRODUCT;

----EXERCISE 7:
SELECT Prodid, Pdesc, Category, Discount FROM PRODUCT WHERE Category='Apparel'

----EXERCISE 8:
SELECT Prodid, Pdesc, Category, Discount FROM PRODUCT WHERE Pdesc IS NULL;

----EXERCISE 9:
SELECT Prodid, Pdesc, Category, Discount FROM PRODUCT WHERE Category='Apparel' AND Discount > 5;

Practice Problems : DDL, DML - 1
----(1)
CREATE TABLE BOOK(
BOOKID CHAR(6) PRIMARY KEY,
BTITLE VARCHAR2(50),
ANAME  VARCHAR2(202),
GENRE VARCHAR2(8) CHECK(GENRE IN ('Mystery', 'Thriller')),
PYEAR INTEGER)

----(2)
CREATE TABLE ITEM(
ITEMCODE VARCHAR2(6) CONSTRAINT ITEMCODE_PK PRIMARY KEY,
ITEMTYPE VARCHAR2(30),
DESCR VARCHAR2(50),
PRICE NUMBER(5,2),
CATEGORY CHAR(1));

ALTER TABLE ITEM ADD DISCOUNT NUMBER;
ALTER TABLE ITEM MODIFY DESCR VARCHAR2(45);
ALTER TABLE ITEM MODIFY CATEGORY VARCHAR2(5);
ALTER TABLE ITEM RENAME COLUMN DESCR TO ITEMDESCR;
ALTER TABLE ITEM DROP(ITEMTYPE);
ALTER TABLE ITEM DROP CONSTRAINT ITEMCODE_PK;      *******CONSTRAINT NOT DROP HERE*******

SELECT * FROM ITEM;    // FOR DISPLY PURPOSE ONLY

Collaborative Assignments 2:
CREATE TABLE SHOPPER(
Shopperid NUMBER PRIMARY KEY,
ShopperName VARCHAR2(20) NOT NULL,
Gender CHAR(6) CHECK(Gender IN('Male', 'Female')),
MobileNo NUMBER NOT NULL,
Address VARCHAR2(50));

Collaborative Assignments 3:
ALTER TABLE Shopper MODIFY MobileNo VARCHAR2(15);

Assignment 1:
CREATE TABLE Article(
ArCode CHAR(5)  PRIMARY KEY,
ArName VARCHAR2(30) NOT NULL,
Rate  NUMBER(8,2),
Quantity NUMBER(4)  DEFAULT 0, 
CHECK(Quantity>=0),
CHECK(ArCode LIKE 'A%'),        // if more than one constraint then decide one at table level
Class  CHAR(1) CHECK(Class IN('A','B','C')));

Assignment 5:
CREATE TABLE STORE(
Name VARCHAR2(20) PRIMARY KEY,
Location VARCHAR2(30) NOT NULL,
ManagerName VARCHAR2(30) UNIQUE)

Assignment 6:
ALTER TABLE STORE RENAME COLUMN NAME TO STORENAME;

Assignment 7:
CREATE TABLE BILL(
BillNo NUMBER PRIMARY KEY,
StoreName VARCHAR2(20) REFERENCES STORE(StoreName),
Shopperid NUMBER REFERENCES SHOPPER(Shopperid),
ArCode CHAR(5) REFERENCES ARTICLE(ArCode),
Amount NUMBER,
BillDate DATE,
Quantity NUMBER(4) DEFAULT 1,
CHECK(Quantity>0))

Assignment 8:
CREATE TABLE SUPPLIER(
Supplierid VARCHAR2(6) PRIMARY KEY,
Name VARCHAR2(30),
ContactNo VARCHAR2(15) NOT NULL,
Emailid VARCHAR2(30))	

Assignment 9:
ALTER TABLE SUPPLIER ADD CITY VARCHAR2(10)

Assignment 10:
ALTER TABLE SUPPLIER DROP(Emailid)

Assignment 11:
CREATE TABLE City(
City VARCHAR2(20) UNIQUE)

Assignment 12:
ALTER TABLE City DROP(City);

Assignment 13:
CREATE TABLE Address(
HouseNo NUMBER,
Street VARCHAR2(30),
city VARCHAR2(20) REFERENCES City(city),
zip  NUMBER(6) CHECK(zip>=0),
state VARCHAR2(5),
PRIMARY KEY(HouseNo, Street, city))

Assignment 14:
ALTER TABLE Address MODIFY state VARCHAR2(20);

Assignment 15:
INSERT INTO Shopper VALUES(101, 'Mark Jane', 'Male', 1234567890, 'Allen Street, New York')

Assignment 2:
INSERT INTO Article VALUES('A1001', 'Mouse', 500, 0, 'C')

Assignment 17:
INSERT INTO Store (StoreName, Location, ManagerName) VALUES('Loyal World', 'Infy Campus, Mysore', 'Rohan Kumar')

Assignment 18:
INSERT INTO Bill (BillNo, StoreName, Shopperid,	ArCode,	Amount,	BillDate, Quantity) VALUES(1001, 'Loyal World', 101,'A1001', 1000,'20-OCT-15', 2)

Assignment 19:
INSERT INTO Supplier VALUES('S501', 'Avaya Ltd', 9012345678, 'Mysore')

Collaborative Assignment 43:
SELECT Empid, Salary "Current Salary", ROUND((Salary*1.2), 2) "New Salary", Salary*0.2 "Incremented Amount" From Empdetails WHERE Designation='Manager'

Collaborative Assignment 44:
SELECT Itemcode FROM Item WHERE ABS(Reorderlevel-Qtyonhand)>50

Exercise 31:
Select Prodid, Pdesc, Price "Old_Price", ROUND((Price*0.775), 2) "New_Price" FROM Product WHERE Category='Sports'

Exercise 32:
SELECT Saleid, ROUND((ABS(MONTHS_BETWEEN(Sldate, SYSDATE))), 1) "MONTH_AGED" FROM Sale

Exercise 33:
SELECT ROUND((AVG(Price)), 2) "Avg", MIN(Price) "Min", MAX(Price) "Max", COUNT(Prodid) "Total" FROM Product

Exercise 34:
SELECT ' '||Sname||' is from '||Location||' '  "RESULT" FROM Salesman

Exercise 35:******IMP******
SELECT TO_CHAR((TO_DATE('Jan/10/2015', 'Mon/dd/yyyy')), 'Month') "MONTH", TO_NUMBER('2,50,000', '9,99,999') "AMOUNT" FROM dual

Exercise 36:
SELECT Prodid, Pdesc, Price FROM Product ORDER BY Price DESC, Prodid DESC

Exercise 37:
SELECT Prodid, Pdesc, Price FROM Product ORDER BY Pdesc

Assignment 53:
SELECT Itemcode, Price "Old Price", ROUND((Price*0.745), 2) "New Price" FROM Item WHERE Itemtype='FMCG'

Assignment 54:
SELECT Empid, Empname, Worksin FROM Empdetails WHERE Designation='Billing Staff'

Assignment 8:
SELECT Orderid, Status, NVL(Pymtmode, 'Payment yet not done') "PYMTMODE" FROM Orders

Assignment 56:
SELECT Descr FROM Item WHERE LENGTH(Descr)>15

Assignment 57:
SELECT SUBSTR(Roid, 2,4)  "NUMERICROID" FROM Retailoutlet

Assignment 58:
SELECT TO_CHAR(SYSDATE, 'Mon/DD/YYYY Day') "CURRENTDATE" FROM DUAL

Assignment 9:
SELECT COUNT(Orderid) "TOTALORDERSCOUNT", COUNT(Amountpaid)  "PAIDORDERSCOUNT" FROM Orders

Assignment 60:
SELECT Orderid, ABS(Orderdate-Pymtdate) "NOOFDAYS" FROM Orders

Assignment 61:
SELECT COUNT(DISTINCT(Itemtype)) NOOFITEMTYPES FROM Item

Assignment 10:
SELECT MAX(Salary) "MAXSAL", MIN(Salary) "MINSAL", SUM(Salary) "TOTALSAL", AVG(Salary) "AVGSAL" FROM Empdetails

Assignment 64:
SELECT COUNT(Itemcode) "NOOFITEMS" FROM Item

Assignment 65:
SELECT Orderid, MONTHS_BETWEEN(Orderdate, Pymtdate) "No of Months" FROM Orders

Exercise 11:
SELECT Prodid, SUM(Quantity) "QTY_SOLD" FROM Saledetail WHERE Quantity>1 GROUP BY  Prodid HAVING COUNT(Prodid)>1

EXERCISE 44:
SELECT E.Id, E.Ename, E.Dept, E.Compid, C.Make FROM Employee E INNER JOIN  Computer C ON E.Compid=C.Compid

EXERCISE 13:
SELECT E.Id, E.Ename,E.Compid,C.Make FROM Employee E INNER JOIN Computer C ON E.Compid=C.Compid WHERE C.Model = 'Precision' OR C.Model = 'Edge'

COLLABORATIVE ASSIGNMENT 41:
SELECT TO_CHAR(Qdate, 'Month') "MONTH" , COUNT(Quotationid) "QUOTATIONCOUNT" FROM Quotation GROUP BY TO_CHAR(Qdate, 'Month')

EXERCISE 12:
SELECT Location, COUNT(Sid) "NUMBER_SMAN" FROM Salesman GROUP BY Location

EXERCISE 39:
SELECT Category FROM Product GROUP BY Category HAVING COUNT(Prodid)>1

ASSIGNMENT 11:
SELECT Itemcode, AVG(Qtyavailable) "Average Quantity" FROM Retailstock GROUP BY Itemcode HAVING AVG(Qtyavailable)<75

ASSIGNMENT 46:
SELECT Pymtmode, COUNT(Pymtdate) "PYMTCOUNT" FROM Orders WHERE TO_CHAR(Pymtdate, 'YYYY')<2015  GROUP BY Pymtmode HAVING COUNT(Pymtdate)>1

ASSIGNMENT 12:
SELECT SNAME, AVG(Quotedprice) "Average quoted price" FROM Quotation WHERE Qstatus='Closed' GROUP BY SNAME HAVING AVG(Quotedprice)>500

ASSIGNMENT 48:
SELECT Itemtype, Category, ROUND((AVG(Price)), 2) "Average item price" FROM Item WHERE Itemtype='FMCG' OR Itemtype='Computer' GROUP BY Itemtype, Category HAVING ROUND((AVG(Price)), 2)<2000

ASSIGNMENT 13:
SELECT Job, AVG(Sal) "Average Salary" FROM Emp WHERE Job='MANAGER' OR Job='ANALYST'GROUP BY Job HAVING AVG(Sal)>1500

Assignment 14:
SELECT Job, Deptno, AVG(Sal) "AVGSALARY" FROM Emp WHERE (Deptno=10 OR Deptno=20) AND Sal>2000 GROUP BY Job, Deptno HAVING AVG(Sal)>2500

ASSIGNMENT 63:
SELECT Sname, AVG(Quotedprice) "Average quoted price" FROM Quotation WHERE Quotedprice>1000 AND Qstatus='Closed' GROUP BY  Sname HAVING AVG(Quotedprice)<4500

COLLABORATIVE ASSIGNMENT 67:
SELECT E.ENAME, E.SAL , D.Dname "DNAME" FROM Emp E INNER JOIN Dept D ON E.Deptno=D.Deptno WHERE SAL>2000

COLLABORATIVE ASSIGNMENT 68:
SELECT E.ENAME, D.Dname "DNAME" FROM Emp E INNER JOIN Dept D ON E.Deptno=D.Deptno WHERE Job='MANAGER'
69:
SELECT DISTINCT D.DNAME FROM Emp E INNER JOIN Dept D ON E.Deptno=D.Deptno WHERE Sal>1500 
SELECT I.Itemcode, I.Descr, Q.Sname FROM Quotation Q INNER JOIN Item I ON I.Itemcode=Q.Itemcode
SELECT C.Custid "Customer Id", C.Custname "Customer Name" FROM Customer C INNER JOIN Empdetails E ON C.Emailid=E.Emailid
SELECT I.ITEMCODE, I.DESCR, I.CATEGORY,Q.Quotedprice FROM Item I INNER JOIN Quotation Q ON I.Itemcode=Q.Itemcode WHERE q.Qstatus='Accepted'
SELECT R.ROID, I.DESCR, I.ITEMTYPE, R.UNITPRICE FROM Retailstock R INNER JOIN Item I ON R.Itemcode=I.Itemcode WHERE R.Unitprice>1500
SELECT Q.Itemcode, Q.Sname, SUM(O.Qtyordered) "TOTALQUANTITY" FROM Quotation Q INNER JOIN Orders O ON Q.Quotationid=O.Quotationid GROUP BY Q.Itemcode, Q.Sname HAVING SUM(O.Qtyordered)>=100
SELECT I.Itemcode, I.Descr FROM Item I INNER JOIN Quotation Q ON I.Itemcode=Q.Itemcode WHERE I.Price=Q.Quotedprice GROUP BY I.Itemcode, I.Descr HAVING COUNT(Quotationid)>1
SELECT Q.Sname, Q.Quotationid FROM Quotation Q INNER JOIN Orders O ON Q.Quotationid=O.Quotationid WHERE ABS(Delivereddate-Orderdate)<=5
SELECT C.Custname, P.Billamount FROM Customer C INNER JOIN Purchasebill P ON C.Custid=P.Custid WHERE P.Billamount>5000
SELECT S.Saleid, S.Sldate FROM Sale S INNER JOIN Salesman L ON S.Sid=L.Sid WHERE L.Location='London'
SELECT P1.Prodid, P1.Category, P1.Price FROM Product P1 INNER JOIN Product P2 ON P1.Price=P2.Price WHERE P1.Prodid<>P2.Prodid

SELECT E1.Empname, E1.Designation, E1.Emailid FROM Empdetails E1 INNER JOIN Empdetails E2 ON E1.Worksin=E2.Worksin WHERE E2.Empname = 'George' AND E1.Empid<>E2.Empid

SELECT C1.Custid, C1.Custname FROM Customer C1 INNER JOIN Customer C2 ON C1.Address=C2.Address WHERE C1.Custid<>C2.Custid

SELECT I.Itemcode, I.Descr,R.Roid, R.Qtyavailable FROM Retailstock R INNER JOIN Item I ON R.Itemcode=I.Itemcode

SELECT I.Descr, I.Itemtype, P.Billamount FROM Item I INNER JOIN Purchasebill P ON I.Itemcode=P.Itemcode WHERE P.Roid='R1001'

SELECT C1.Custid, C1.Custname, C1.Custtype FROM Customer C1 INNER JOIN Customer C2 ON C1.Custtype=C2.Custtype WHERE C2.Custid=2004 AND C1.Custid<>C2.Custid

SELECT Saleid, Sldate FROM Sale WHERE Sldate=(SELECT MAX(Sldate) FROM Sale)

SELECT Sname FROM Salesman WHERE Sid IN (SELECT Sid FROM Sale GROUP BY Sid HAVING COUNT(Saleid)>=2);

SELECT Prodid, Pdesc FROM Product WHERE Prodid IN (SELECT Prodid FROM Saledetail GROUP BY Prodid HAVING SUM(Quantity)=(SELECT MIN(SUM(Quantity)) FROM Saledetail GROUP BY Prodid))

SELECT Itemcode, Itemtype, Descr, Category FROM Item WHERE Itemcode IN (SELECT Itemcode FROM Quotation WHERE Quotedprice =(SELECT MIN(Quotedprice) FROM Quotation WHERE Qstatus='Rejected'  ))

SELECT Itemcode, Descr FROM ITEM WHERE Itemcode IN (SELECT Itemcode FROM Quotation WHERE Quotedprice=(SELECT MAX(Quotedprice) FROM Quotation WHERE Qstatus='Closed' OR Qstatus='Rejected' ))

SELECT Itemcode, descr, Price FROM Item WHERE Price= (select MAX(Price) FROM ITEM WHERE PRICE < (SELECT MAX(Price) FROM ITEM))

SELECT Ename, Job FROM Emp WHERE Empno IN (SELECT Empno FROM Empvehicle)

SELECT Ename FROM Emp WHERE Sal =(SELECT MAX(Sal) FROM Emp)































