class Pizza:
    ingredients = {1:"Ham", 2:"Sausage", 3:"Bacon", 4:"Beef", 5:"Meatball",
    6:"Spinach", 7:"Olive", 8:"Mushroom", 9:"Tomato",
    10:"Eggplant", 11:"Garlic", 12:"Cheese", 13:"Pineapple",
    14:"Onion", 15:"Caper"}
    flavors = {"Hawaiian": [1, 13], "Garden Feast": [6, 7, 8, 9, 10],
    "Meat Festival": [2, 3, 4, 5], "Carbonara": [3, 12],
    "Custom": []}

    def __init__(self, flavor, custom_ingreds=[]):
        self.flavor= flavor
        self.ingreds=[]
        if flavor == "Custom":
            id= custom_ingreds
        if flavor != "Custom":
            id = Pizza.flavors[flavor]
        for i in id:
            self.ingreds.append(Pizza.ingredients[i])
        self.ingreds = ', '.join(map(str, self.ingreds))
        Summary=list(flavor+(" (")+self.ingreds+(")"))
        self.ingreds = ''.join(Summary)
    
    def __str__(self):
        return self.ingreds

class PizzaOrder:
    total_orders=0
    def __init__(self):
        self.order= self.total_orders +1
        self.pizza_list= []

    @staticmethod
    def select_menu(self):
        ans = "y"
        PizzaOrder.total_orders +=1
        print("Pizza order {}:".format(PizzaOrder.total_orders))
        while ans == "y":
            print("1. Hawaiian\n2. Garden Feast\n3. Meat Festival\n4. Carbonara\n5. Custom")
            choice = 0
            choice=int(input("Select a flavor: "))
            if choice == 1:
                self.pizza_list.append(Pizza("Hawaiian",None))
            if choice == 2:
                self.pizza_list.append(Pizza("Garden Feast",None))
            if choice == 3:
                self.pizza_list.append(Pizza("Meat Festival",None))
            if choice == 4:
                self.pizza_list.append(Pizza("Carbonara",None))
            if choice == 5:
                print("1: Ham, 2: Sausage, 3: Bacon, 4: Beef, 5: Meatball\n6: Spinach, 7: Olive, 8: Mushroom, 9: Tomato, 10: Eggplant\n11: Garlic, 12: Cheese, 13: Pineapple, 14: Onion, 15: Caper")
                id=input("Select id's of ingredients:" ).split()
                id = [int(s) for s in id]
                self.pizza_list.append(Pizza("Custom",id))
            new = input("Do you want more pizzas (y/n)? ")
            ans = new.strip().lower()
           

        print (f"Pizza order {PizzaOrder.total_orders}'s summary:")
        for i in range(len(self.pizza_list)):
            print ("{}. {}".format(i+1, self.pizza_list[i]))
        return ""
    def __str__(self):
        return self.select_menu(self)





if __name__ == '__main__':
    PizzaOrder.total_orders = 0
    for i in range(3): # placing 3 pizza orders
        po = PizzaOrder()
        print(po)