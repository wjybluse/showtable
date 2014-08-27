##READ ME
###1.Getting start with pretty show

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

### The result show in the console 

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

###Example
You can use it to send rest message very easier，but only optimized for json format message. 
```python
client=RestClient("https","localhost",8086)
json_value=client.get(url="/show/book/1")
#TODO
client=RestClient("https","localhost",8086')
client.patch(content,url="/show/book/1")
```
