class bill:
  def __init__(self,menu):
    self.menu_list=menu
  def show_menu(self):
    print(self.menu_list)
  def show_bill(self):
    z=[]
    y=[]
    x=[]
    pay=[]
    element=list(map(str,input("ENTER YOU ATE THE DISHES:").split()))
    for i in element:
      if i.isdigit():
        z.append(int(i))
      else:
        y.append(i)
    for i in range(0,len(y)):
      pay.append((self.menu_list[y[i]]*z[i]))
      print(f"{y[i]}\t\t\t  : Rs {z[i]}")
    print("total price(GST inclusive): Rs",sum(pay)*5/100+sum(pay))
    print("----------------thankyou for visiting-----------------")

b=bill({"vada":5,"coffee":10,"tea":10,"idle":6,"poori":30,"pongal":25})
b.show_menu()
b.show_bill()
