# class Salary:
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus

#     def annual_salary(self):
#         return (self.pay*12)+ self.bonus

# class Employee:
#     def __init__(self,name,age,pay,bonus):
#         self.name=name
#         self.age=age
#         self.obj_salary=Salary(pay,bonus)
#     def total_salary(self):
#         return self.obj_salary.annual_salary()

# emp=Employee('max',25,15000,10000)
# print(emp.total_salary())


"""
Q.  Let’s expand a bit on our Clothing classes from the previous in-video question. 
Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of
a given material that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts.
"""


class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
        