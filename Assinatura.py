from PIL import Image, ImageDraw, ImageFont

def writeSignature(name, func, mail, ramal):
    config = {
        #'Outlook': 'client', #Web ou Client
        'Nome': name,
        'Work': func,
        'email': mail,
        'ramal': ramal
    }
    img = Image.open('Images//Madrecor Modelo Client.png')
    draw = ImageDraw.Draw(img)

    draw.text((225, 8), config['Nome'], font=ImageFont.truetype('Fontes//Rubik-Medium.ttf', size=40), fill='rgb(101, 179, 206)') #escrever na imagem
    draw.text((250, 57), config['Work'], font=ImageFont.truetype('Fontes//Rubik-Light.ttf', size=17), fill='rgb(99, 99, 99)')
    draw.text((250, 78), config['email']+'@madrecor.com.br', font=ImageFont.truetype('Fontes//Rubik-Light.ttf', size=17), fill='rgb(99, 99, 99)') 
    draw.text((315, 141),config['ramal'], font=ImageFont.truetype('Fontes//Rubik-Light.ttf', size=17), fill='rgb(99, 99, 99)') 
    img.save('Assinaturas/'+config['Nome']+' Client'+'.png') #Salvar imagem

    img = Image.open('Images//Madrecor Modelo Web.png')
    draw = ImageDraw.Draw(img)

    draw.text((142, 5),config['Nome'], font=ImageFont.truetype('Fontes//Rubik-Medium.ttf', size=20), fill='rgb(101, 179, 206)') #escrever na imagem
    draw.text((161, 34),config['Work'], font=ImageFont.truetype('Fontes//Rubik-Light.ttf', size=12), fill='rgb(99, 99, 99)')
    draw.text((161, 49),config['email']+'@madrecor.com.br', font=ImageFont.truetype('Fontes//Rubik-Light.ttf', size=12), fill='rgb(99, 99, 99)') 
    draw.text((201, 90),config['ramal'], font=ImageFont.truetype('Fontes//Rubik-Light.ttf', size=10), fill='rgb(99, 99, 99)') 

    img.save('Assinaturas/'+config['Nome']+' Web'+'.png') #Salvar imagem
