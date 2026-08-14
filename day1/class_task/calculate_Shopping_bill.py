bill = int(input("Enter the total bill amount: "))
if(bill>0 and bill<=10000):
    discount =  (bill*(20/100))
    gst = (bill*(18/100))
    print("pruchase amount is:",bill    )
    print("discount amount is:",discount)
    print("GST amount is:",gst)
    print("Total bill amount is:",bill-discount+gst)
elif bill>5000:
    discount =  (bill*(10/100))
    gst = (bill*(18/100))
    print("pruchase amount is:",bill    )
    print("discount amount is:",discount)
    print("GST amount is:",gst)
    print("Total bill amount is:",bill-discount+gst)
else:
    discount = 0
    gst = (bill*(18/100))
    print("pruchase amount is:",bill    )
    print("discount amount is:",discount)
    print("GST amount is:",gst)
    print("Total bill amount is:",bill-discount+gst)
