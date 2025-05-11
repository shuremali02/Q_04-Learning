
from typing import Annotated
from fastapi import FastAPI, Depends, Query, HTTPException,status
 
app=FastAPI()
def get_simple_goal():
    return{"goal":"Here is my goal building AI Agents"}

@app.get("/get-simple-goal")
def simple_goal(response:Annotated[dict, Depends(get_simple_goal)]):
    return response

def get_username(user:str):
    return {"This is username":user}
@app.get("/get-username")
def get_user(response:Annotated[dict, Depends(get_username)]):
    return response 

def login_check(phone_number:str = Query(None),password:str = Query(None)):
    if phone_number and password == "1234":
        return {"message":"login successful"}
    else:
        return {"message":"login failed"}
    
@app.get("/signin")
def login_api(user:Annotated[dict,Depends(login_check)]):
    return user    


#Multiple Dependency

def multiple_dependency_func1(num):
    num=int(num)
    num+=1
    return num
def multiple_dependency_func2(num):
    num=int(num)
    num +=2
    return num

@app.get("/sum/{num}")
def get_output(num:int,num1:Annotated[dict,Depends(multiple_dependency_func1,)],num2:Annotated[dict,Depends(multiple_dependency_func2)]):
    total= num + num1 + num2
    return f"Total_Numbers: {total}"

# classes

blogs={
    "1":"GenAi",
    "2":"FastAPI",
    "3":"Pydantic"
}

users={
    "6":"Ali",
    "7":"Raza"
}

class Get_objector404:
    def __init__(self,model):
        self.model=model
    def __call__(self,id:str):
        obj=self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj 
blog_dependency=Get_objector404(blogs)

@app.get("/blog/{id}")
def get_blogs(blog_name:Annotated[dict,Depends(blog_dependency)]):
    return blog_name

user_dependency=Get_objector404(users)
@app.get("/user/{id}")
def get_blogs(user_name:Annotated[dict,Depends(user_dependency)]):
    return user_name