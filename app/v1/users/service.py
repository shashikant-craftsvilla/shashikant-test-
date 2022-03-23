from app.v1.users.coordinator import Coordinator
from collections import OrderedDict
class SubApp1Service:
    def __init__(self, params, headers):
        self.params = params
        self.headers = headers
        self.coordinator = Coordinator()

##### 
    def get_static_api_response(self):
        data=self.params
        a=int(data["a"])
        b=int(data["b"])
        c=a+b
        return data, 'success'
####for age 
    def get_static_api_response1(self):
        data = self.params
        age = int(data['age'])
        if age >= 18:
           data['canVote'] = 'yes'
        else:
           data['canVote'] = 'no'
############# work done 

### for api through mysql customer_id

    def get_static_api_response2(self):
        customer_id=self.params.get("customer_id")
        customer_detail=self.coordinator.get_customer_detail(customer_id)
        res={"customer_detail":customer_id,"quotes":customer_detail}
        rvd=OrderedDict(reversed(list(res.items())))
        return res, 'success'