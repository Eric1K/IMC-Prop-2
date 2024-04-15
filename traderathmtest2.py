from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string
import numpy as np

#price, quantity

def __init__ (self):
    self.example_dict = {"AMETHYSTS": 10000, "STARFRUIT": 5000}
    self.amthhigh = 0
    self.amthlow = 99999999999999
class Trader:
    
    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

				# Orders to be placed on exchange matching engine 
        result = {}

        #we should use incorporate position
        for product in state.order_depths:
            if product == "AMETHYSTS":
              
              order_depth: OrderDepth = state.order_depths[product]
              orders: List[Order] = [] #ORDERS GO HERE
              
             
                              
              # #volatility = 1 + (self.amtthigh - self.amthlow)/(self.amthlow) #we'll use the day's high and low
              orderbook = sum(state.order_depths["AMETHYSTS"].buy_orders.values()) #total orders in the order book
              orderbook += sum(state.order_depths["AMETHYSTS"].sell_orders.values())

              # if orderbook == 0:
              #   spread = 0
              # else:                 
              #   spread = risktol * volatility * volatility + (2/risktol)*np.log(1+(risktol/orderbook))
              #   spread = spread / 2

              best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
              best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
              midprice = (int(best_ask) + int(best_bid))/2
              spread = int(best_bid) - int(best_ask) if int(best_bid) > int(best_ask) else int(best_ask) - int(best_bid)


              q = state.position.get('AMETHYSTS', 0)
              target_q = 10

              if q < target_q:
                  buy_price = midprice - spread
                  sell_price = midprice + spread + 1
              elif q > target_q:
                  buy_price = midprice - spread + 1
                  sell_price = midprice + spread
              else:
                  buy_price = midprice - spread
                  sell_price = midprice + spread
              
              #BUY
              if len(order_depth.sell_orders) != 0:
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]    
                orders.append(Order(product, sell_price, -best_ask_amount))    

              #SELL
              if len(order_depth.buy_orders) != 0:
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                orders.append(Order(product, buy_price, -best_bid_amount))

              # print("Acceptable price : " + str(acceptable_bid))
              # print("Acceptable ask : " + str(acceptable_ask))
              # acceptable_price = 10000  # Participant should calculate this value
              # print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))
      
              # if len(order_depth.sell_orders) != 0:
              #     best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
              #     if int(best_ask) <= 10000:
              #         print("BUY", str(-best_ask_amount) + "x", best_ask)
              #         orders.append(Order(product, best_ask, -best_ask_amount))
      
              # if len(order_depth.buy_orders) != 0:
              #     best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
              #     if int(best_bid) >= 10000:
              #         print("SELL", str(best_bid_amount) + "x", best_bid)
              #         orders.append(Order(product, best_bid, -best_bid_amount))

              
            result[product] = orders
    
		    # String value holding Trader state data required. 
				# It will be delivered as TradingState.traderData on next execution.
        traderData = "SAMPLE" 
        
				# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData