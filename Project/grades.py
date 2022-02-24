def flex_grades(data_flex):
  # print("dataall = ",data_flex)
  # print(" ")

  term = ""
  flex_box = ""
  text = """,{
            "type": "separator",
            "margin": "sm"
          }
        ]
      }"""

  for i in range(len(data_flex)):
    # print('data = ',data_flex[i])  
    semester = data_flex[i][5]
                  
    if term != semester : 

      if i > 0 :
        flex_box = flex_box + """%s %s %s %s"""% (flex_term,flex_course,flex_GPA,text)
        # print(flex_box)

      flex_term = """,{
          "type": "box",
          "layout": "vertical",
          "margin": "sm",
          "contents": [
            {
              "type": "text",
              "text": "Term %s/%s",
              "weight": "bold",
              "color": "#0C6BA1"
            }"""%(str(data_flex[i][5]),str(data_flex[i][6]))

      term = semester
      # print(term," / ",semester)
      flex_course = ''

    flex_course = flex_course + """,{
          "type": "box",
          "layout": "baseline",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "%s %s",
              "size": "sm",
              "flex": 10,
              "wrap": true
            },
            {
              "type": "text",
              "text": "(%s)"
            },
            {
              "type": "text",
              "text": "%s",
              "weight": "bold",
              "flex": 1
            }
          ]
        }"""%(str(data_flex[i][7]),str(data_flex[i][8]),str(data_flex[i][9]),str(data_flex[i][12]))

    flex_GPA = """,{
          "type": "box",
          "layout": "baseline",
          "spacing": "sm",
          "contents": [
           {
              "type": "text",
              "text": "CA = %s",
              "wrap": true,
              "weight": "bold",
              "style": "italic",
              "flex": 10
            },
            {
              "type": "text",
              "text": "CA = %s",
              "weight": "bold",
              "style": "italic",
              "flex": 7
            }
          ]
        },
        {
          "type": "box",
          "layout": "baseline",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "GPA = %s",
              "wrap": true,
              "weight": "bold",
              "style": "italic",
              "flex": 10
            },
            {
              "type": "text",
              "text": "GPAX = %s",
              "weight": "bold",
              "style": "italic",
              "flex": 7
            }
          ]
        }"""%(str(data_flex[i][10]),str(data_flex[i][11]),str(data_flex[i][13]),str(data_flex[i][14]))

  if flex_box != "" and flex_term != "" and flex_course != "" : 
    
    # print("end loop")
    textend = """,{
                "type": "separator",
                "margin": "sm"
              }
              ]
              }"""

    name =   """{
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "%s",
                  "size": "xl",
                  "weight": "bold",
                  "color": "#F9934b"
                },
                {
                  "type": "text",
                  "text": "%s%s %s",
                  "weight": "bold",
                  "color": "#00182E"
                },
                {
                  "type": "text",
                  "text": "Grades",
                  "color": "#aaaaaa"
                }
              ]
            },{
                "type": "separator",
                "margin": "sm"
            }"""%(str(data_flex[i][0]),str(data_flex[i][1]),str(data_flex[i][2]),str(data_flex[i][3]))

    result = """{
        "type": "bubble",
        "direction": "ltr",
        "hero": {
        "type": "image",
        "url": "https://sv1.picz.in.th/images/2022/02/23/rivaxQ.png",
        "aspectMode": "cover",
        "size": "full",
        "aspectRatio": "12:5"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [%s %s %s %s %s %s]
          }
        }"""%(name,flex_box , flex_term , flex_course , flex_GPA , textend)

    # result = flex_name + flex_box + flex_term + flex_course + flex_GPA + textend 
    # print("V\nV\nV\nV\nV\nV\nV\nV\n") 
    print(result)
    return result



























   
# {
#   "type": "bubble",
#   "direction": "ltr",
#   "body": {
#     "type": "box",
#     "layout": "vertical",
#     "contents": [
#       {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "text",
#             "text": "6131460",
#             "size": "xl",
#             "weight": "bold",
#             "color": "#FF7500"
#           },
#           {
#             "type": "text",
#             "text": "Mr.Swaddee Taweesuk",
#             "weight": "bold",
#             "color": "#00182E"
#           },
#           {
#             "type": "text",
#             "text": "Grades",
#             "color": "#aaaaaa"
#           }
#         ]
#       },
#       {
#         "type": "separator",
#         "margin": "sm"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "sm",
#         "contents": [
#           {
#             "type": "text",
#             "text": "Term 1/2561",
#             "weight": "bold",
#             "color": "#0C6BA1"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001201 Population",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001202 Internet programming",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001203 Internet of Things",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001204 Communicative English for Academic in Computer Technology",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3) "
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001205 Robotic",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001206 Software Engineer",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001207 Artificial Intelligence",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001208 Samena",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "CA  = 20",
#                 "wrap": true,
#                 "weight": "bold",
#                 "style": "italic",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "CA = 20",
#                 "weight": "bold",
#                 "style": "italic",
#                 "flex": 7
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "GPA = 4.00",
#                 "wrap": true,
#                 "weight": "bold",
#                 "style": "italic",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "GPAX = 4.00",
#                 "weight": "bold",
#                 "style": "italic",
#                 "flex": 7
#               }
#             ]
#           },
#           {
#             "type": "separator",
#             "margin": "sm"
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "sm",
#         "contents": [
#           {
#             "type": "text",
#             "text": "Term 2/2561",
#             "weight": "bold",
#             "color": "#0C6BA1"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001201 Population",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001202 Internet programming",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001203 Internet of Things",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "margin": "sm",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "spacing": "sm",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "001204 Communicative English for Academic , in Computer Technology",
#                     "size": "sm",
#                     "flex": 10,
#                     "wrap": true
#                   },
#                   {
#                     "type": "text",
#                     "text": "(3)"
#                   },
#                   {
#                     "type": "text",
#                     "text": "A",
#                     "weight": "bold",
#                     "flex": 1
#                   }
#                 ]
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001205 Robotic",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001206 Software Engineer",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001207 Artificial Intelligence",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001208 Samena",
#                 "size": "sm",
#                 "flex": 10,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "(3)"
#               },
#               {
#                 "type": "text",
#                 "text": "A",
#                 "weight": "bold",
#                 "flex": 1
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "CA  = 20",
#                 "wrap": true,
#                 "weight": "bold",
#                 "style": "italic",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "CA = 40",
#                 "weight": "bold",
#                 "style": "italic",
#                 "flex": 7
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "GPA  =  4.00",
#                 "wrap": true,
#                 "weight": "bold",
#                 "style": "italic",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "GPAX = 4.00",
#                 "weight": "bold",
#                 "style": "italic",
#                 "flex": 7
#               }
#             ]
#           },
#           {
#             "type": "separator",
#             "margin": "sm"
#           }
#         ]
#       }
#     ]
#   }
# }      