from kor import Object, Text

invoiceSchema = Object(
    id="gpt_data_tagging",
    description=(
        "Given raw text, identify and extract following details in JSON format. Convert the given text to english language before extracting any details. Output should also be in english only."
    ),
    attributes=[
        Text(
            id="provider",
            description="Name of healthcare organization that offers medical services to patients. It could be hospital name, clinic name, laboratory name, nursing home etc. Dont include doctor name here. If you do not find any provider name, return 'Not found'",
            many=False,
        ),
        Text(
            id="doctor",
            description="Extract the name of the doctor who has provided the consultation or service. If you do not find any doctor name, return 'Not found'",
            many=False,
        ),
        Text(
            id="customer",
            description="Extract the name of the customer who has taken up the consultation or service. If you do not find any customer name, return 'Not found'",
            many=False,
        ),
        Text(
            id="age",
            description="Extract the age of the customer who has taken up the consultation or service. If you do not find any age, return 'Not found'",
            many=False,
        ),
        Text(
            id="gender",
            description="Extract the gender of the customer who has taken up the consultation or service. If you do not find any gender, return 'Not found' else return male or female only",
            many=False,
        ),
        Text(
            id="invoice",
            description="Extract the invoice number from the raw text. If you do not find any invoice number, return 'Not found'.",
            many=False,
        ),
        Text(
            id="date",
            description="Extract the invoice date from the raw text. Date format should be dd-mm-yyyy. If date year is incorrect, make date corrections as per current year. If you do not find any invoice date, return 'Not found'.",
            many=False,
        ),
        Text(
            id="amount",
            description="Extract the total bill amount from the raw text. If you do not find any amount, return 'Not found'. Total bill amount should be equal to the amount paid.",
            many=False,
        ),
        Text(
            id="degree",
            description="Extract the degree of the doctor providing the consultation or service. If you do not find any degree, return 'Not found'.",
            many=False,
        ),
        Text(
            id="speciality",
            description="Extract the speciality of the doctor providing the consultation or service. If you do not find any speciality, return 'Not found'.",
            many=False,
        ),
        Text(
            id="address",
            description="Extract the address of the service provider, it could be the hospital name, clinic, lab or nursing home. If you do not find any address, return 'Not found'.",
            many=False,
        ),
        Text(
            id="phone",
            description="Extract the contact number of the service provider or doctor. If service provider's phone number is mentioned extract that or else extract doctor's phone number. Make sure you are sure the phone number is either of the provider or the doctor ONLY. If you do not find any phone number for the provider or doctor, return 'Not found'.",
            many=False,
        ),
        Text(
            id="zipcode",
            description="Extract Indian pin codes of 6 digits of the service provider or doctor. Return a single list of string consisting of service provider's pincodes and doctor's pincode. If pincode is not mentioned return empty list.",
            many=True,
        ),
        Text(
            id="city",
            description="Extract the Indian city name from the document text. If city is not mentioned return 'Not found'.",
            many=False,
        ),
        Text(
            id="state",
            description="Extract the Indian state name from the document text. If state is not mentioned return 'Not found'.",
            many=False,
        ),
        Text(
            id="bill_items",
            description="Return a JSON of bill items mentioned in the document text along with the amount of that bill item. Correct the spelling of the bill item. The key should be the bill item and its value should be the price. Bill_items may be clubbed together in the input text like Blood Test/Urine test and have a single amount like 500. This means that the combined cost is 500. If no bill items is found return empty json.",
            many=False,
        ),
        Text(
            id="provider_category",
            description="Categorize the document into one of three categories: 'Hospital', 'Clinic' or 'Lab' or 'Doctor'. You must not use any other terms.",
            many=False,
        )
    ],
    many=False,
    examples = [
        [
            "maatoshree dental clinic\\ndr. siddant jajoo bds, mds\\nperiodontist & implantologist\\nshop no. 8, hari vitthal plaza\\nemail : siddhantjajoo@gmail.com\\nabove federal bank\\nweb : www.maatoshreedentalclinic.com\\nnear ahire gate, shivane\\npune - 23. @ 9765 41 9539\\nname\\nmera\\nupadlyay\\nreceipt\\naddress\\nno.\\n336\\nmob.\\ndate\\n28/3/23\\ntreatment\\n..\\namount\\nconsultation/root canal treatment\\n65001\\nmaatoshree dental clinic\\ndr. siddh/psd ez( 45)\\nregistration no. a 18609\\nshivano punc:411023 (03\\n10\\ntotal\\n6500-\\npagebreak\\n",
            {
                "provider": "Maatoshree Dental Clinic",
                "doctor": "Dr. Siddhant Jajoo",
                "customer": "Mera Upadhyay",
                "age": "Not found",
                "gender": "Not found",
                "invoice": "336",
                "date": "28-03-2023",
                "amount": "6500",
                "degree": "BDS, MDS",
                "speciality": "Periodontist & Implantologist",
                "address": "Shop no. 8, Hari Vitthal Plaza, above federal bank, near Ahire gate, Shivane, Pune- 23",
                "phone": "9258440141",
                "zipcode": [
                    "411023"
                ],
                "city": "Pune",
                "state": "Maharashtra",
                "bill_items": {
                    "consultation/root canal treatment": 6500
                },
                "provider_category": "Clinic"
            }
        ]
    ]
)