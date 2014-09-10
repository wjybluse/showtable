###READ ME
####1.Getting start with pretty show
<p>The pretty show is supported to show your json string as table,xml,json formatter and other.
The basic result like this:</p>
```javascript
//show simple json in console
{
    "person": [
        {
            "age": 24, 
            "birthday": "1990-2-23", 
            "city": "shenzhen", 
            "conutry": "China", 
            "height": "166cm", 
            "name": "wang"
        }, 
        {
            "age": 25, 
            "birthday": "1989-5-23", 
            "city": "changsha", 
            "conutry": "China", 
            "height": "175cm", 
            "name": "xu"
        }, 
        {
            "age": 22, 
            "birthday": "1992-3-21", 
            "city": "fujian", 
            "conutry": "China", 
            "height": "180cm", 
            "name": "xie"
        }
    ]
}
```
-->console
<pre>
+----+---+------+--------+---------+-------+
|name|age|height|city    |birthday |conutry|
+----+---+------+--------+---------+-------+
|wang|24 |166cm |shenzhen|1990-2-23|China  |
+----+---+------+--------+---------+-------+
|xu  |25 |175cm |changsha|1989-5-23|China  |
+----+---+------+--------+---------+-------+
|xie |23 | 180cm|fujian  |1992-3-21|China  |
+----+---+------+--------+---------+-------+
|wang|24 |166cm |shenzhen|1990-2-23|China  |
+----+---+------+--------+---------+-------+  
</pre>

####2.Document
<ul>
<li>1.Provided RestClient api to send rest message,we supported post,get,patch,delete,put and head method.<li>
<li>2.Provided the formatter for creating pretty print in console,we supported json,table,xml,yaml now.</li> 
<li>3.Provided parameter parser in future.</li>
</ul>
####3.Example
You can use it to send rest message very easier，but only optimized for json format message. 
```python
client=RestClient("https","localhost",8086)
json_value=client.get(url="/show/book/1")
#TODO
client=RestClient("https","localhost",8086')
client.patch(content,url="/show/book/1")
```
