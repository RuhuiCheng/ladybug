# Test Case Guideline  
## Demo Case Running
> ### unit case   
> 1. range match with hive timeout   
     ladybug case=ladybug_dw-demo1

> 2. range match with mysql timeout   
     ladybug case=ladybug_dw-demo2

> 3. range match with oracle timeout   
     ladybug case=ladybug_dw-demo3

> 4. exactly match failed   
     ladybug case=ladybug_dw-demo4

> 5. exactly match success   
     ladybug case=ladybug_dw-demo5

> 6. exactly match for schemal check   
     ladybug case=ladybug_dw-demo6

> ### case group   
> 1. run group_demo1   
     ladybug group=group_demo1
> 2. run group_demo2   
     ladybug group=group_demo2
> 3. run group_demo3   
     ladybug group=group_demo3

> ### case scenarios   
> 1. run case scenarios   
     ladybug scenarios=ladybug_scenarios_demo1
## Comparation Option List:
1. __> Rowcount (Primary key change)__
2. __> Data row duplicate check(by per table unique key )__
3. __> Table structure match (oracle vs hive)__
4. Key measure(sum, avg, money)
## Test Object:
1. __DimTable__
2. __FactTable__
3. __DMTable__
4. Job
5. Report

## Naming rule
|Category|Nameing|Demo|
|--------|-------|----|
| case | [count,schema,measure] . [dim,fact,dm,job,report] . [db] . [table] . [name] | count.dim.ladybug_dw.dim_hotel_base.clc_categroy_distinct |
| group | [hive,mysql,oracle].[db].[name] | hive.ladybug_dw.hote_agreement |
| scenarios | [name] | hotel

## Note:
| ID | Comment |
| ------ | ------- |
| 1 | data row with out order by |
| 2 | data column is order sensitive |
| 3 | test case duration must be reasonable |
| 4 | every column should have name |
| 5 | avoid one big test case (use several small test case to instead of big one)|
