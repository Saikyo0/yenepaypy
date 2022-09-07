import json
import requests
from signer import sign

class Client():
    def __init__(self,merchant_id) -> None:
        self.merchant_id = str(merchant_id)

    def payment_link(self, item_name, unit_price, quantity, item_id="", process="Express",
    expires_after="", delivery_fee="", handling_fee="", tax_1="", tax_2="", discount="",
    success_url="", ipn_url=""):
        url = ("https://www.yenepay.com/checkout/Home/Process/?"
               f"ItemName={item_name}&"
               f"ItemId={item_id}&"
               f"UnitPrice={'{:.2f}'.format(float(unit_price))}&"
               f"Quantity={quantity}&"
               f"Process={process}&"
               f"ExpiresAfter={expires_after}&"
               f"DeliveryFee={delivery_fee}&"
               f"HandlingFee={handling_fee}&"
               f"Tax1={tax_1}&"
               f"Tax2={tax_2}&"
               f"Discount={discount}&"
               f"SuccessUrl={success_url}&"
               f"IPNUrl={ipn_url}&"
               f"MerchantId={self.merchant_id}")
        return url

    def send_to(self, pemfile, amount, recieverid, authtoken, currency="ETB"):
        data_content = (f"ReceiverCode={recieverid}={'{:.2f}'.format(float(amount))}&" +
                        f"Amount={'{:.2f}'.format(float(amount))}&" +
                        f"Code={self.merchant_id}&" +
                        f"Currency={currency}")
        signature = sign(pemfile, data_content)
        API_BASE_URL = "https://endpoints.yenepay.com/api/client/send"
        headers = {"Authorization": "Bearer "+ authtoken,'content-type': 'application/json'}
        data_ = {"payerSignature": f"{signature}",
                "serviceProviderCode": "YP005",
                "msgToRecipients":"Your Money",
                "currency": "ETB",
                "totalPayment": '{:.2f}'.format(float(amount)),
                "recipients": [
                    { 
                    "customerCode": f"{recieverid}",
                    "amount": '{:.2f}'.format(float(amount))
                    }
                ]
            }
        response = requests.post(url=API_BASE_URL,headers=headers,data=str(data_))
        response = json.loads(response.content)
        receipt = response.get('order')
        result = response.get('paymentResult')
        if result.get("suceeded"):
            return f"Successfully Paid {receipt.get('recipient').get('name')} {receipt.get('grandTotal')}"
        else:
            return f"Error {result.get('errorMsg')}"
