
# YenePay Python API (Unofficial)

A simple and easily integrable yenepay library for your python code

![](https://yenepay.com/images/logo.png "")

help: https://community.yenepay.com/
## API Reference

### Client
Initiates a yenepay client, required for any of the other services of this library
https://community.yenepay.com/docs/getting-started/get-your-seller-merchant-code/
####
```
from yenepaypy.main import Client

client = Client(merchant_id = '...')

#on success creates a client instance with functions
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `merchant_id` | `string` | **Required**. Your Merchant id(customer code) |

# 
### Get Payment Link

This is the easiest and quickest way to accept a payment through YenePay. By generating a payment link from your YenePay account manager page, you will be able to share it to your customers via SMS, social media, viber or put the link on your website and allow your customers to pay you online. In order to be able to generate a payment link, you will need to register with YenePay and activate your merchant account. You can find more detail on how to register as a merchant on the How to register on YenePay article.

https://community.yenepay.com/docs/integration-guide/using-the-generate-payment-link-option-on-yenepay/

```
from yenepaypy.main import Client

client.payment_link(
	item_name = '...',
	unit_price = '...',
	quantity = '...'
  )
 
#on success returns a checkout link that any customer can pay through
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_name`      | `string` | **Required**. a name of the item you are requesting payment for or selling|
| `unit_price`      | `string` | **Required**. the unit price of the item in Ethiopian Birr currency |
| `quantity`      | `string` | **Required**. Quantity of the item to sell|
| `item_id`      | `string` | **Optional**. a unique identifier for the item |
| `expires_after`      | `string` | **Optional**. time until the link expires|
| `delivery_fee`      | `string` | **Optional**. the delivery fee of item to sell|
| `handling_fee`      | `string` | **Optional**. the handling fee on item |
| `tax_1`      | `string` | **Optional**. first tax of item to sell |
| `tax_2`      | `string` | **Optional**. secondary tax of item to sell |
| `discount`      | `string` | **Optional**. discount of item to fetch |
| `success_url`      | `string` | **Optional**. url to call on success|
| `ipn_url`      | `string` | **Optional**. ipn url of item to fetch on success |

# 
### Send Payment To User
Sends money directly asnd automatically to other users, if you have any problems with getting the values for this function, I suggest you read: https://community.yenepay.com/docs/integration-guide/using-our-api/

sdk core example:
https://github.com/YenePay/yenepay.sdk.core.client
####
```
from yenepaypy.main import Client

client = Client(merchant_id = '...')
authtoken = "..."
pem_file="..." 

result = client.send_to(
        pemfile = pem_file,
        authtoken = authtoken,
        amount = '...',
        recieverid = '...',
        payment_text = '...'
  )
    
#on success returns a string with the grand total and name of the reciever 
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pemfile `      | `string` | **Required**. signature key file location  |
| `authtoken`      | `string` | **Required**. Authoriztion Token string |
| `amount`      | `string` | **Required**. amount of money to be sent |
| `recieverid`      | `string` | **Required**. customer code of the reciever |
| `payment_text`      | `string` | **Optional**. text to be attached with the payment |
