# Rwanda administrative division
## Source 
https://datacatalog.worldbank.org/search/dataset/0041453

## Db opener
https://www.dbfopener.com/

## Data preparation and import 

```
LOAD DATA LOCAL INFILE 'file.csv' INTO TABLE t1 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  
(@col1,@col2,@col3,@col4) set name=@col4,id=@col2 ;
```