def contact():
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
                    "text": "สอบถามเพิ่มเติม",
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
                    "wrap": true,
                    "align": "start",
                    "text": "- เคาน์เตอร์งานทะเบีนนิสิต "
                },
                {
                    "type": "text",
                    "text": "โทร. 0-5596-8324"
                },
                {
                    "type": "text",
                    "text": " - หน่วยทะเบียนนิสิต"
                },
                {
                    "type": "text",
                    "text": "โทร. 0-5596-8314, 0-5596-8315, 0-5596-8300",
                    "wrap": true
                },
                {
                    "type": "text",
                    "text": "- หน่วยสนับสนุนการจัดการเรียน/สอน"
                },
                {
                    "type": "text",
                    "text": " โทร.0-5596-8312 (จัดตารางเรียน-สอน)",
                    "wrap": true
                },
                {
                    "type": "text",
                    "text": "โทร.0559683110 , 055968311 (คอมพิวเตอร์)",
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
    return result