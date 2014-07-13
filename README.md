#------READ ME-------
##This software is using for show the simple Json or Json array in console,and provider the restclient for send rest message.
### The Json code like this

```javascript
//json array
{"person":[
{"name":"wang","age":24,"height":"166cm","birthday":"1990-2-23","city":"shenzhen","conutry":"China"},
{"name":"xu","age":25,"height":"175cm","birthday":"1989-5-23","city":"changsha","conutry":"China"},
{"name":"xie","age":22,"height":"180cm","birthday":"1992-3-21","city":"fujian","conutry":"China"}
]}
//the simple json 
{
"dadasdsadsa":"davfssadasdasdsadadas",
"dasdsadsada":"dasxczxcsadasdss",
"fscsarersdas":"caadasdsadsad",
"dasfsddewwsds":"dasdsadsadsa"
}
```

### The result show in the console 


+----+---+------+--------+---------+-------+
|name|age|height|city&emsp;&emsp;   |birthday &nbsp;|conutry|
+----+---+------+--------+---------+-------+
|wang|24 |166cm |shenzhen|1990-2-23|China|
+----+---+------+--------+---------+-------+
|xu  &nbsp;&nbsp;&nbsp;&nbsp;|25 |175cm |changsha|1989-5-23|China|
+----+---+------+--------+---------+-------+
|xie &nbsp;&nbsp;&nbsp;|22&nbsp; |180cm|fujian&nbsp;&nbsp;&nbsp;  |1992-3-21|China &nbsp; |

+----+---+------+--------+---------+-------+  
|name|age|height|city&emsp;&emsp;   |birthday &nbsp;|conutry|  
+----+---+------+--------+---------+-------+  
|wang|24 |166cm |shenzhen|1990-2-23|China|  
+----+---+------+--------+---------+-------+  
|xu  &nbsp;&nbsp;&nbsp;&nbsp;|25 |175cm |changsha|1989-5-23|China|  
+----+---+------+--------+---------+-------+  
|xie &nbsp;&nbsp;&nbsp;|22&nbsp; |180cm|fujian&nbsp;&nbsp;&nbsp;  |1992-3-21|China &nbsp; |  
+----+---+------+--------+---------+-------+

###Example
You can use it to send rest message very easier，but only optimized for json format message. 
```python
client=RestClient("https","localhost",8086)
json_value=client.get(url="/show/book/1")
#TODO
client=RestClient("https","localhost",8086)
client.patch(content,url="/show/book/1")
```
