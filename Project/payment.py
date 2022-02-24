def flex_paymentmenu():
    result = """{
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "weight": "bold",
                "size": "xl",
                "align": "center",
                "text": "การชำระเงินค่าธรรมเนียมการศึกษา",
                "wrap": true
            }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน",
                "text": "การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน"
                },
                "style": "primary",
                "margin": "xs",
                "color": "#aaaaaa"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "ช่องทางการชำระเงิน",
                "text": "ช่องทางการชำระเงิน"
                },
                "style": "primary",
                "margin": "xs",
                "color": "#aaaaaa"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "ตรวจสอบสถานะการชำระเงิน ",
                "text": "ตรวจสอบสถานะการชำระเงิน "
                },
                "style": "primary",
                "margin": "xs",
                "color": "#aaaaaa"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "ติดต่อ / contact",
                "text": "contact"
                },
                "style": "primary",
                "margin": "xs"
            }
            ]
        }
        }"""
    print(result)
    return result

def flex_paymentAnswer1():
    result = """{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน",
                    "align": "center",
                    "size": "lg",
                    "weight": "bold",
                    "wrap": true
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "นิสิตสามารถพิมพ์และชำระเงินค่าธรรมเนียมการศึกษาได้ตามกำหนดปฏิทินการศึกษาของมหาวิทยาลัย ",
                    "wrap": true,
                    "align": "start"
                },
                {
                    "type": "text",
                    "text": "(สัปดาห์ที่ 3 ของการเปิดภาคการศึกษา)",
                    "style": "italic",
                    "weight": "bold",
                    "wrap": true
                }
                ],
                "margin": "md"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "spacer",
                "size": "sm"
            }
            ],
            "flex": 0
        }
        }"""
    print(result)    
    return result

def flex_paymentAnswer2():
    result = """{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "ช่องทางการชำระเงิน",
                    "align": "center",
                    "size": "lg",
                    "weight": "bold",
                    "wrap": true
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "นิสิตสามารถชำระเงินค่าธรรมเนียมการศึกษาได้โดยผ่านเคาน์เตอร์ธนาคารหรือเคาน์เตอร์เซอร์วิสที่ระบุไว้ในใบแจ้งชำระเงิน หรือชำระผ่านระบบ QR Code โดยแสกนผ่าน Mobile Banking ของทุกธนาคาร",
                    "wrap": true,
                    "align": "start"
                }
                ],
                "margin": "md"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "spacer",
                "size": "sm"
            }
            ],
            "flex": 0
        }
        }"""
    print(result)
    return result

def flex_paymentAnswer3():
    result = """{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "ตรวจสอบสถานะการชำระเงิน และพิมพ์ใบเสร็จ",
                    "align": "center",
                    "size": "lg",
                    "weight": "bold",
                    "wrap": true
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "นิสิตสามารถตรวจสอบสถานการณ์ชำระเงิน และพิมพ์ใบเสร็จรับเงินออนไลน์ได้หลังจากที่ดำเนินการชำระเงินแล้วประมาณ 3 วันทำการ ผ่านทางระบบทะเบียนออนไลน์ได้ที่เมนู “ภาระหนี้สิน”  “พิมพ์ใบเสร็จออนไลน์” ",
                    "wrap": true,
                    "align": "start"
                },
                {
                    "type": "text",
                    "text": "หมายเหตุ : การพิมพ์ใบเสร็จรับเงินออนไลน์ฉบับจริง สามารถดำเนินได้เพียง 1 ครั้ง เท่านั้น  นิสิตควรพิมพ์หรือดาวน์โหลดไฟล์เก็บไว้ทันที",
                    "style": "italic",
                    "weight": "bold",
                    "wrap": true
                }
                ],
                "margin": "md"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "spacer",
                "size": "sm"
            },
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "ไปที่ระบบลงทะเบียนออนไลน์",
                "uri": "https://reg.nu.ac.th"
                },
                "style": "primary"
            }
            ],
            "flex": 0
        }
        }"""
    print(result)
    return result