__author__ = 'wan'
class ShowJsonTable():
    '''the class is suitable for showing the json table like this:
    1.the normal json object,example:
        {"key1":"value","key2":"value2"}
    2.the list style of json array,example:
        {"app":[{"name":"value","style":"normal","color":"read","number":"hhehhe"}]}
    '''  
    def __init__(self,json=None):
        self.json=json

    def create_table(self):
        result=eval(str(self.json))
        for k,v in result.items():
            if isinstance(v,list):
                self.handle_list_component(result)
                return
        self.handle_normal_json(result)


    #parse the normal json
    def handle_normal_json(self,json=dict()):
        keys,values=json.keys(),json.values()
        max_key,max_value=self.get_max_length(arr=keys),self.get_max_length(arr=values)
        self.show_table(keys,values,max_key=max_key,max_value=max_value)

    #parse the json array
    def handle_list_component(self,json=dict):
        cache={}
        for k,v in json.items():
            for item in v:
                for pk,pv in item.items():
                    if not cache.__contains__(pk):
                        cache[pk]=[]
                    cache[pk].append(pv)
        line="+"
        cache_keys,cache_values=cache.keys(),cache.values()
        for k,v in zip(cache_keys,cache_values):
            max_line=max(len(k),self.get_max_length(v))
            v.append(max_line)
            line+=self.get_line(max_line-1)+"+"
        print(line)
        title="|"
        for k,v in zip(cache_keys,cache_values):
            title+=k+self.get_space(list(v)[-1],len(k))+"|"
        print(title)
        
        first_values=list(cache_values)[0]
        for index in range(0,len(first_values)-1):
            v_line="|"
            f_item=first_values[index]
            v_line+=f_item+self.get_space(first_values[-1],len(f_item))+"|"
            for rindex in range(1,len(cache_values)):
                list_item=list(cache_values)
                r_item=list_item[rindex][index]
                v_line+=r_item+self.get_space(list_item[rindex][-1],len(r_item))+"|"
            print(v_line)
        print(line)    


    def get_max_length(self,arr=[]):
        if len(arr)<=0:
            return 0
        try:
            return len(max(arr,key=lambda item:len(item)))
        except Exception as e:
            print("Parse error.%s"(e.msg))
            return 0
        return 0

    def get_header(self):
        return ["Property","Value"]

    def show_table(self,keys,values,max_key=0,max_value=0):
        key,value=self.get_header()
        if len(key)>max_key:
            max_key=len(key)
        if len(value)>max_value:
            max_value=len(value)
        head=line=end="%s+%s"%(self.get_line(max_key),self.get_line(max_value))
        print(head)
        print(self.get_string_line(key,value)(max_key,max_value))
        for k,v in zip(keys,values):
            print(line)
            print(self.get_string_line(k,v)(max_key,max_value))
        print(end)


    def get_line(self,s_len):
        s=""
        for i in range(0,s_len):
            s+="-"
        return s+"-"

    def get_space(self,max_len,actual_len):
        s=""
        for i in range(actual_len,max_len):
            s+=" "
        return s

    def get_string_line(self,p_key,p_value):
        def create_space(max_key=0,max_value=0):
            key,value=self.get_space(max_key,len(p_key)),self.get_space(max_value,len(p_value))
            return "|%s%s|%s%s|"%(p_key,key,p_value,value)
        return create_space

if __name__=="__main__":
    #test_json={"dadasdsadsa":"davfssadasdasdsadadas","dasdsadsada":"dasxczxcsadasdss","fscsarersdas":"caadasdsadsad","dasfsddewwsds":"dasdsadsadsa"}
    test_json={"app":[{"nima":"debi","hahha":"hehhe","nimade":"deca"},{"nima":"debi","hahha":"hehhe","nimade":"deca"},{"nima":"debi","hahha":"hehhe","nimade":"deca"}]}
    p=ShowJsonTable(test_json)
    p.create_table()

