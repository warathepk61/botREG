def flex_regismenu():

    result = """{
        "type": "carousel",
        "contents": [
            {
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
                    "text": "การลงทะเบียนออนไลน์"
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
                    "label": "เตรียมพร้อมก่อนการลงทะเบียน",
                    "text": "เตรียมพร้อมก่อนการลงทะเบียน"
                    },
                    "style": "primary",
                    "margin": "xs",
                    "color": "#aaaaaa"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "ลืมรหัสผ่านเข้าระบบ",
                    "text": "ลืมรหัสผ่านเข้าระบบ"
                    },
                    "style": "primary",
                    "margin": "xs",
                    "color": "#aaaaaa"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "บัตรประจำตัวนิสิตหาย",
                    "text": "บัตรประจำตัวนิสิตหาย"
                    },
                    "style": "primary",
                    "margin": "xs",
                    "color": "#aaaaaa"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "เปลี่ยนแปลงข้อมูลส่วนตัว",
                    "text": "เปลี่ยนแปลงข้อมูลส่วนตัว"
                    },
                    "style": "primary",
                    "margin": "xs",
                    "color": "#aaaaaa"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "ไม่ได้ลงทะเบียนเรียน/ชำระเงิน",
                    "text": "ไม่ได้ลงทะเบียนเรียน/ชำระเงิน"
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
            }
        ]
        }"""
    print(result)
    return result


def flex_regisAnswer1() :
    result = """{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "เตรียมพร้อมก่อนการลงทะเบียน",
                "weight": "bold",
                "size": "lg",
                "align": "center",
                "wrap": true,
                "color": "#935CA3"
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "- ตรวจสอบกำหนดการลงทะเบียนตามประกาศปฏิทินมหาวิทยาลัย - ตรวจสอบการเปิดรายวิชาตามแผนหลักสูตรสาขาวิชา - ตรวจสอบภาระหนี้สินคงค้าง หากมีหนี้สินคงค้างนิสิตจะไม่สามารถลงทะเบียนเรียนในเทอมถัดไปได้  - พบอาจารย์ที่ปรึกษาเพื่อขอคำแนะนำการวางแผนการลงทะเบียน และขออนุมัติการลงทะเบียนเรียน - ทำการลงทำเบียนผ่านระบบทะเบียนออนไลน์ (www.reg.nu.ac.th) ที่เมนู “ลงทะเบียน” - ตรวจสอบผลการลงทะเบียน / ตารางเรียน ที่เมนู “ผลการลงทะเบียน”",
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
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "ไปที่ระบบลงทะเบียนออนไลน์",
                "uri": "https://reg.nu.ac.th"
                },
                "style": "primary"
            }
            ]
        },
        "styles": {
            "footer": {
            "separator": true
            }
        }
        }"""
    print(result)
    return result

def flex_regisAnswer2():
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
                    "text": "ลืมรหัสผ่านเข้าระบบ",
                    "align": "center",
                    "size": "lg",
                    "weight": "bold"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "นิสิตสามารถติดต่อขอรับรหัสผ่านที่กองบริการเทคโนโลยีสารสนเทศ (CITCOMS) โทร 05596-1524",
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
                "type": "button",
                "style": "primary",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "CALL",
                "text": "05596-1524"
                }
            },
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

def flex_regisAnswer3():
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
                    "text": "บัตรประจำตัวนิสิตหาย",
                    "align": "center",
                    "size": "lg",
                    "weight": "bold",
                    "color": "#5A9A70"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "ให้นิสิตดาวน์โหลดแบบฟอร์ม NU 2 ผ่านระบบทะเบียนออนไลน์ ที่เมนู “แบบฟอร์มขอทำบัตรนิสิต”และนำไปยื่นที่ธนาคารกสิกรไทย สาขา มหาวิทยาลัยนเรศวร เท่านั้น ธนาคารจะดำเนินการออกบัตรประจำตัวนิสิตให้ทันที",
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
                "type": "button",
                "style": "primary",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "ไปที่ระบบลงทะเบียนออนไลน์",
                "text": "https://reg.nu.ac.th"
                }
            },
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

def flex_regisAnswer4():
    result  = """{
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
                    "text": "เปลี่ยนแปลงข้อมูลส่วนตัว",
                    "align": "center",
                    "size": "lg",
                    "weight": "bold"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "นิสิตดาวน์โหลดแบบคำร้องทั่วไป (NU 18) และกรอกข้อมูลที่ต้องการเปลี่ยนแปลงให้ครบถ้วน แล้วยื่นที่เคาน์เตอร์งานทะเบียนนิสิตพร้อมหลักฐานการเปลี่ยนแปลงข้อมูล",
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
                "type": "button",
                "style": "primary",
                "height": "sm",
                "action": {
                "type": "uri",
                "label": "ดาวน์โหลดแบบฟอร์ม NU 18",
                "uri": "https://reg.nu.ac.th/registrar/e-form/NU18.pdf"
                }
            },
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

def flex_regisAnswer5():
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
                    "text": "ไม่ได้ลงทะเบียนเรียนหรือชำระเงิน",
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
                    "text": "ให้นิสิตกรอกแบบฟอร์ม NU 7 เพื่อขอคืนสภาพ และเสนอแบบฟอร์มผ่านคณะ จากนั้นนำแบบฟอร์มมายื่นที่งานทะเบียนนิสิต เพื่อดำเนินการลงทะเบียน และชำระเงินที่กองคลัง ในกรณีที่เกิน 5 สัปดาห์ ต้องให้อาจารย์ผู้สอนแต่ละรายวิชารับรองการเข้าชั้นเรียนด้วย",
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
                "type": "button",
                "style": "primary",
                "height": "sm",
                "action": {
                "type": "uri",
                "label": "ดาวน์โหลดแบบฟอร์ม NU 7",
                "uri": "https://reg.nu.ac.th/registrar/e-form/NU07.pdf"
                }
            },
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

def flex_regisAnswer6(): 
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
                    "text": "ช่องทางการติดต่อ",
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
                    "text": "กองบริการการศึกษา มหาวิทยาลัยนเรศวร 99 หมู่ 9 ตำบลท่าโพธิ์ อำเภอเมือง จังหวัดพิษณุโลก รหัสไปรษณีย์ 65000 เวลาทำการ: จันทร์ - ศุกร์ เวลา 8.30 - 16.30 น.",
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
                "type": "button",
                "action": {
                "type": "message",
                "label": "หน่วยสนับสนุนการเรียนการสอน โทร.",
                "text": "055-968300"
                },
                "style": "primary"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "หน่วยทะเบียนนิสิต โทร.",
                "text": "055-968314 , 055-968315"
                },
                "style": "primary"
            },
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