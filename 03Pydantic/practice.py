#learned pydantic BAseModel and VAlidationError
from pydantic import BaseModel, ValidationError, EmailStr ,field_validator


class User(BaseModel):
    id:int
    name:str
    email:EmailStr

user_data={"id":2,"name":"shurem","email":"shurem@gmail.com"}
users=User(**user_data)

print(users)   
print(users.model_dump()) #model convert to dictinary

try :
    invalid_data={"id":"123","name":"shurem","email":"shurem@gmail.com"} 
    user2=User(**invalid_data)
    print(user2)
except ValidationError as e :
    print(e)

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User_data(BaseModel):
    id :int
    name:str
    email:EmailStr
    addresses:list[Address]

    @field_validator("name")
    
    def name_validation(cls,valid_name):
        if len(valid_name) < 3:
            raise ValueError("name must be at least 3 char long")
        return valid_name

data={
    "id":123,
    "name":"shurem",
    "email":"shurem@gmail.com",
    "addresses":[
        {"street" : "#1 mainroad " ,"city" : "Hyderabad" ,"zip_code" : "71000",},
        {"street" : "#34 main st ", "city" : "Karachi", "zip_code" : "2000","country":"pk",},
        ]
}
user=User_data.model_validate(data)
print(user.model_dump())
try: 
    data={
    "id":123,
    "name":"sma",
    "email":"shurem@gmail.com",
    "addresses":[
        {"street" : "#1 mainroad " ,"city" : "Hyderabad" ,"zip_code" : "71000",},]
    }
    user=User_data.model_validate(data)
    print(user.model_dump())
except ValidationError as e:
    print(e)    