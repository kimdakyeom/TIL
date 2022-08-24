### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select *
from playlist_track as A
order by A.PlaylistId desc
limit 5;
```

```sql
PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```
### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select *
from tracks as B
order by B.TrackId
limit 5;
``` 

```sql
TrackId  Name                                     AlbumId  MediaTypeId  GenreId  Composer                                                      Milliseconds  
Bytes     UnitPrice
-------  ---------------------------------------  -------  -----------  -------  ------------------------------------------------------------  ------------  
--------  ---------
1        For Those About To Rock (We Salute You)  1        1            1        Angus Young, Malcolm Young, Brian Johnson                     343719        
11170334  0.99

2        Balls to the Wall                        2        2            1                                                                      342562        
5510424   0.99

3        Fast As a Shark                          3        2            1        F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman           230619        
3990994   0.99

4        Restless and Wild                        3        2            1        F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider &   252051        
4331779   0.99
                                                                                 W. Hoffman


5        Princess of the Dawn                     3        2            1        Deaffy & R.A. Smith-Diesel                                    375418        
6290521   0.99
```
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
select B.PlaylistId, A.Name
from tracks as A 
join playlist_track as B
on A.TrackId = B.TrackId
order by B.PlaylistId desc
limit 10;
```  

```sql
PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls
```
### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select B.PlaylistId, A.Name
from tracks as A 
join playlist_track as B
on A.trackId = B.trackId
where B.PlaylistId = 10
order by A.Name desc
limit 5;
``` 

```sql
PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2
```
### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
select count(*) from tracks as T 
join artists as A
on T.Composer = A.Name;
```

```sql
count(*)
--------
402
```
### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
select count(*)
from tracks as T 
left outer join artists as A
on T.Composer = A.Name;
```

```sql 
count(*)
--------
3503
```
### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
inner join은 양 테이블의 교집합인 데이터만 검색한다.
left join은 왼쪽 테이블에 있는 데이터는 모두 검색하고 오른쪽 테이블의 데이터는 검색 조건에 맞게 출력된다.
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select InvoiceLineId, InvoiceId
from invoice_items
order by InvoiceId
limit 5;
``` 

```sql 
InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2
```
### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select InvoiceId, CustomerId
from invoices
order by InvoiceId
limit 5;
``` 

```sql
InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```
### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select T.InvoiceLineId, T.InvoiceId from invoice_items as T
join invoices as V
on T.InvoiceId = V.InvoiceId
order by V.InvoiceId desc
limit 5;
``` 

```sql
InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2226           411
2227           411
2228           411
2229           411
```
### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select I.InvoiceId, C.CustomerId
from invoices as I
inner join customers C
on I.CustomerId = C.CustomerId
order by I.InvoiceId desc
limit 5;
``` 

```sql
InvoiceId  CustomerId
---------  ----------
284        59
229        59
218        59
97         59
45         59
```
### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select I.InvoiceLineId, I.InvoiceId, C.CustomerId
from invoice_items as I 
    join invoices as V
        on I.InvoiceId = V.InvoiceId
    join customers as C
        on V.CustomerId = C.CustomerId
order by I.InvoiceId desc
limit 5;
```

```sql
InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2239           411        44
2238           411        44
2237           411        44
2236           411        44
```
### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select Z.CustomerId, count(*)
from invoice_items as I
join (select * from invoices as V
    join customers C
    on V.CustomerId = C.CustomerId
) Z
on I.InvoiceId = Z.InvoiceId
group by Z.CustomerId
order by Z.CustomerId
limit 5;
```

```sql
CustomerId  count(*)
----------  --------
1           38
2           38
3           38
4           38
5           38
```