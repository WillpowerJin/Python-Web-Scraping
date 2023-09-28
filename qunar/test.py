# Destination URL: https://m.flight.qunar.com/h5/flight/

import time


timestamp = round(time.time() * 1000)

ord_int_list = [ord(str(i)) for i in str(timestamp)[4:]]
ord_str_list = [str(i) for i in ord_int_list]
n_ord = "".join(ord_str_list)
print(n_ord)