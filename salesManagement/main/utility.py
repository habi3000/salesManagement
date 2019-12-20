from .models import feeprog,Statistics
def calcultate_min_selling(unitCost,feeProg):
    # Returns the minumin selling price based on the fee prog and the unit cost
    add = getattr(feeprog.objects.get(name__exact=feeProg), 'addfee')
    multiply = (1-getattr(feeprog.objects.get(name__exact=feeProg), 'mulfee')/100) # if the original value saved in DB is 10 multiply would equla 0.9 
    return (add+float(unitCost))/multiply

def calculate_selling_profit_percent(unitCost,feeProg,percent):
    # Returns the selling price that would result in percent% profit based on fee prog and percent
    add = getattr(feeprog.objects.get(name__exact=feeProg), 'addfee')
    multiply = 1-(getattr(feeprog.objects.get(name__exact=feeProg), 'mulfee')/100)
    return (add+float(unitCost))/(multiply-percent)

def calculate_profit_percent(unitCost,feeProg,sellingPrice):
    # Returns the profit percent based on the selling price, unit cost and fee prog
    add = getattr(feeprog.objects.get(name__exact=feeProg), 'addfee')
    multiply = 1-(getattr(feeprog.objects.get(name__exact=feeProg), 'mulfee')/100)
    res=((((float(sellingPrice)-add)*multiply)/float(unitCost))-1)*100
    return res

def queryset_to_jslist(queryset):
    # Takes in a quetyset and converys it to a java script list
    res='['
    for q in queryset:
        res=res+'"'+q.name+'"'+','
    res+=']'
    return res

def edit_statistics(name,value):
    # Edits a statistecs field value, either by addition or subtraction, takes in the name
    # and the value to add or sub
    stat=Statistics.objects.get(name__exact=name)
    stat.value+=value
    stat.save()

def new_statistics_value(name,value):
    # Changes the value of a statistics field, takes in the name and the new value
    stat=Statistics.objects.get(name__exact=name)
    stat.value=value
    stat.save()

def create_statistics(name,value):
    # Creates a new statistics field, takes in the value and name
    stat=Statistics()
    stat.name=name
    stat.value=value
    stat.save()