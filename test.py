
from datetime import datetime

today_date = datetime.utcnow().date()

desired_time = datetime(today_date.year, today_date.month, today_date.day, 11, 30, 0)

##########################           epoch time in millisecond              #########################
t= int(desired_time.timestamp())*1000
yt=t-86400000
et=t-(86400000*8)

q="""db.order.find({"$or":[{"orderinfo.collectionid":1664348291191223,"$and":[{"orderinfo.createdtime":{"$gt":"""+str(yt)+"""}},{"orderinfo.createdtime":{"$lt":"""+str(t)+"""}}]},{"orderinfo.collectionid": 1666077346350774,"$and": [{ "orderinfo.createdtime":{ "$gt":"""+str(yt)+"""}},{"orderinfo.createdtime": {"$lt":"""+str(t)+"""}}]}]},{"_id": 1,"orderinfo.createdtime": 2,"orderinfo.updatedtime":3,"otherproperties.personID": 4,"otherproperties.friendlyAccountID": 5,"priceFacets.PV.PVAfterDiscount": 6,"priceFacets.CV.CVAfterDiscount": 7,"priceFacets.SB.SBAfterDiscount": 8,"math.fulfilmath.totalfulfilsale": 9,"math.tax": 10,"math.discount": 11,"math.totalsale": 12,"usertracking.firstname": 13,"usertracking.lastname": 14,"usertracking.usercontact.email": 15,"status": 16,"orderinfo.channel": 17,"orderinfo.storeid": 18,"otherproperties.orderSource":19}).skip(0).limit(0)"""

opd="""db.order.aggregate([{$match: { "orderinfo.collectionid" : { $in : [ NumberLong(1664348291191223) , NumberLong(1666077346350774) ]}, "orderinfo.storeid":  { $in : [ "407","404"] },  "orderinfo.createdtime": {$gte: """+str(yt)+""" , $lte:"""+str(t)+"""} }},  {$addFields: { "display_date_time" : { $dateToString: { format: "%Y:%m:%d,%H", date: {$toDate: "$orderinfo.createdtime" }, timezone: "-06:00" } } }}, {$group: { "_id" : "$display_date_time" , "count": { $sum : 1 }}},{$limit:10000}]);"""
oed="""db.order.aggregate([{$match: { "orderinfo.collectionid" : { $in : [ NumberLong(1664348291191223) , NumberLong(1666077346350774) ]}, "orderinfo.storeid":  { $in : [ "407","404"] },  "orderinfo.createdtime": {$gte: """+str(et)+""" , $lte:"""+str(t)+"""} }},  {$addFields: { "display_date_time" : { $dateToString: { format: "%Y:%m:%d", date: {$toDate: "$orderinfo.createdtime" }, timezone: "-06:00" } } }}, {$group: { "_id" : "$display_date_time" , "count": { $sum : 1 }}},{$limit:10000}]);"""


print(q)
print(opd)
print(oed)
