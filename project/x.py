import json
from datetime import datetime
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}

with open("borrowed.json", "r") as file:
    borrowed_data = json.load(file)

with open("resource.json", "r")as file:
    data = json.load(file)

def resource_invet(id, name, category, available_unit):
    found = False
    
    for item in data:
        if item['id'] == id:
            found = True  
            break         
            
    if found:
        print("Id already exists")
        return data
    else:    
        new_resource = {
                "id": id,
                "name": name,
                "category": category,
                "total": available_unit,
                "available": available_unit
            }
    data.append(new_resource)
    with open("resource.json", "w") as file:
          json.dump(data, file, indent=4)
    return("item added succesfully")
    
 



def borrow(fellow_id, resource_id, quantity):
    
    time_borrowed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    matched = None
    for item in data:
        if item['id'] == resource_id:
            matched = item
            break  

    if not matched:
        return "Resource ID does not exist."
    
    if quantity <= 0 or quantity > matched["available"]:
        return f"Too many or low order. Reduce the quantity. We only have {matched['available']} units of '{matched['name']}' now."

    if fellow_id not in fellows:
        return "Fellow ID does not exist."

    matched['available'] -= quantity
    matched['total'] -= quantity
    record = {
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity,
        "time": time_borrowed
    }
    borrowed_data.append(record)

    with open("borrowed.json", "w") as file:
       json.dump(borrowed_data, file, indent=4)

    with open("resource.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"User at ID {fellow_id} borrowed {quantity} '{matched['name']}'. Available {matched['name']} = {matched['available']}")



def Returns(resource_id, fellow_id, quantity, data, borrowed_data, fellows):

    match = None
    for item in data:
        if item['id'] == resource_id:
            match = item
            break 

    if not match:
        return "resource_id doesn't exist"
    
    if fellow_id not in fellows:
        return f"id: {fellow_id} doesn't exist"
        
    if quantity <= 0 or quantity > borrowed_data['quantity']:
        return f"The return is either higher than what you borrowed or negative. You borrowed {borrowed_data['quantity']} and you are returning {quantity}."
    
    match['quantity'] -= quantity   
    match['available'] += quantity  
    borrowed_data['quantity'] -= quantity 

    with open("resource.json", "w") as file:
        json.dump(data, file, indent=4) 

    with open("borrowed.json", "w") as file:
        json.dump(borrowed_data, file, indent=4)  

    print(f"user at id: {fellow_id} returned {resource_id}, {quantity}")
    return "Success"
