def recommendproduct(product_id):
    import json
    import re
    import time
    import pandas as pd

    tstart = time.time()

    transactionsList = []
    # Reading transactions
    # with open("/Users/harpreetsingh/Downloads/transactions.txt") as f:
    with open("shorttran.csv") as f:
        for jsonObj in f:
            data = json.loads(jsonObj)
            transactionsList.append(data)
        
    f.close()

    tend = time.time()
    df =pd.DataFrame(transactionsList)
    itemListDf = df['itemList']

    #defining dictionary to keep products sold together with counts of how many times they were sold together. keeping key as one product and rest of products as values
    prodreldict= {}
    #iterating thru transaction rows and adding to dictionary
    for row in itemListDf:
        # iterating thru each product sold
        for prod in row:
            # generating dictionary to be added as value for each product
            allpr = {}
            for pr in row:
                if pr == prod:
                    continue
                allpr[pr['item']]=1 
                # {prod1:1, prod2:1}
            
            item_id = prod['item']
            if item_id in prodreldict:
                for _,prd in enumerate(allpr):
                    if prd in prodreldict[item_id]:
                        prodreldict[item_id][prd]+=1
                    else:
                        prodreldict[item_id][prd]=1
            else :
                prodreldict[prod['item']] = allpr
            
    #sorting only required dictionary key which matches product requested
    sorteddict ={}
    result =[]
    if product_id in prodreldict:
        sorteddict[product_id] = sorted(prodreldict[product_id].items(),key=lambda key1 : key1[1], reverse=True)
    else:
        # Need to enhance in case of no results from co-frequency logic. Need to lookup items sold together based on categories and finding max sold items in those categories. For now using dummy values
        sorteddict[product_id] = [("default_prod_id",1)]
    # print (sorteddict)
    # Reading product id and names
    prod_col_names =['prod_id','mch_code','prod_name']
    prod_names_df = pd.read_csv('/Users/harpreetsingh/Downloads/products.txt', sep='\t', names=prod_col_names)

    # Returning top 5 products as result array with lookup to product names
    resultlimit = 5
    i = 0
    for k in range(len(sorteddict[product_id])):
        recommendprod = sorteddict[product_id][k]
        recommendprodname = prod_names_df['prod_name'].loc[prod_names_df['prod_id']==recommendprod[0]].to_string(index=False) 
        if recommendprodname == "Series([], )":
            # Need to enhance in case of no results from co-frequency logic. Need to lookup items sold together based on categories and finding max sold items in those categories. For now using dummy values
            recommendprodname = "default_prod_name"
        result.append((recommendprod[0],recommendprodname))
        i += 1
        if i == resultlimit:
            break


    print("Recommendation for product ",product_id, " is product  with products id,name ", result  )
    tendfinal = time.time()
    # print("times taken to read", tend-tstart," time taken for parse", tendfinal -tend,"time taken for all:", tendfinal - tstart)

recommendproduct("prod1")
recommendproduct("prod2")
