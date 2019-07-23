def buy_coffees(cash,cups=2):
    #去咖啡店
    print("去咖啡店")
    #告诉服务员要几杯咖啡
    cup_num = cups
    print("告诉服务员要",cup_num,"杯咖啡")
    #服务员告诉你要多少钱
    print("服务员告诉你要",cup_num*30,"钱")
    #你给服务员多少钱
    money = cash
    print("你给服务员",money,"钱")
    #服务员找零，给你咖啡
    print("服务员找零",money-cup_num*30,"，给你",cup_num,"杯咖啡")
# buy_coffees()
# # buy_coffees(100,2)
# # buy_coffees(200)
# # buy_coffees()
# # buy_coffees(1)
buy_coffees(200)
buy_coffees(1088888888888)
buy_coffees(6666666,88)
