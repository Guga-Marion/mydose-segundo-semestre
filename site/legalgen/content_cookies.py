# -*- coding: utf-8 -*-
from blocks import h2, p, raw

UPDATED = {"pt":"24 de junho de 2024","en":"June 24, 2024","es":"24 de junio de 2024"}

def _toc(lang):
    T={"pt":["O que são Cookies?","Por que usamos Cookies?","Tipos de Cookies que Usamos","Como Controlar Cookies","Gerenciar Preferências"],
       "en":["What Are Cookies?","Why We Use Cookies","Types of Cookies We Use","How to Control Cookies","Manage Preferences"],
       "es":["¿Qué son las Cookies?","¿Por qué usamos Cookies?","Tipos de Cookies que Usamos","Cómo Controlar las Cookies","Gestionar Preferencias"]}
    return [("c%d"%(i+1),l) for i,l in enumerate(T[lang])]

def _btn(label, note):
    return ('<button type="button" class="btn-submit" style="max-width:260px" '
            'onclick="var n=this.nextElementSibling;n.style.display=n.style.display===\'block\'?\'none\':\'block\'">%s</button>'
            '<p class="m-priv" style="display:none;text-align:left;margin-top:12px;max-width:560px">%s</p>') % (label, note)

def build_pt():
    b=p("Esta Política de Cookies explica como a MyDose usa cookies e tecnologias similares para reconhecer você quando visita nosso site.", lead=True)
    b+=h2("O que são Cookies?","c1")
    b+=p("Cookies são pequenos arquivos de dados que são colocados no seu computador ou dispositivo móvel quando você visita um site. Os cookies são amplamente utilizados pelos proprietários de sites para fazer seus sites funcionarem, ou para trabalhar de forma mais eficiente, bem como para fornecer informações de relatórios.")
    b+=h2("Por que usamos Cookies?","c2")
    b+=p("Usamos cookies para várias razões: melhorar a funcionalidade do site, personalizar sua experiência, analisar como você usa nosso site e fornecer publicidade relevante.")
    b+=h2("Tipos de Cookies que Usamos","c3")
    b+=p("Usamos cookies essenciais (necessários para o funcionamento do site), cookies de desempenho (para analisar como você usa o site), cookies funcionais (para lembrar suas preferências) e cookies de marketing (para mostrar anúncios relevantes).")
    b+=h2("Como Controlar Cookies","c4")
    b+=p("Você pode controlar e/ou excluir cookies como desejar. Você pode excluir todos os cookies que já estão no seu computador e pode configurar a maioria dos navegadores para impedir que sejam colocados.")
    b+=h2("Gerenciar Preferências","c5")
    b+=p("Você pode gerenciar suas preferências de cookies a qualquer momento:")
    b+=raw(_btn("Configurar Cookies","Para gerenciar cookies, acesse as configurações de privacidade do seu navegador. Ali você pode aceitar, recusar ou excluir cookies. Se recusar, parte das funcionalidades do site pode ser comprometida."))
    return b

def build_en():
    b=p("This Cookie Policy explains how MyDose uses cookies and similar technologies to recognize you when you visit our website.", lead=True)
    b+=h2("What Are Cookies?","c1")
    b+=p("Cookies are small data files that are placed on your computer or mobile device when you visit a website. Cookies are widely used by website owners to make their websites work, or to work more efficiently, as well as to provide reporting information.")
    b+=h2("Why We Use Cookies","c2")
    b+=p("We use cookies for several reasons: to improve website functionality, personalize your experience, analyze how you use our site and deliver relevant advertising.")
    b+=h2("Types of Cookies We Use","c3")
    b+=p("We use essential cookies (necessary for the website to work), performance cookies (to analyze how you use the site), functional cookies (to remember your preferences) and marketing cookies (to show relevant ads).")
    b+=h2("How to Control Cookies","c4")
    b+=p("You can control and/or delete cookies as you wish. You can delete all cookies that are already on your computer and you can set most browsers to prevent them from being placed.")
    b+=h2("Manage Preferences","c5")
    b+=p("You can manage your cookie preferences at any time:")
    b+=raw(_btn("Configure Cookies","To manage cookies, go to your browser's privacy settings. There you can accept, refuse or delete cookies. If you refuse, some website functionality may be compromised."))
    return b

def build_es():
    b=p("Esta Política de Cookies explica cómo MyDose usa cookies y tecnologías similares para reconocerlo cuando visita nuestro sitio.", lead=True)
    b+=h2("¿Qué son las Cookies?","c1")
    b+=p("Las cookies son pequeños archivos de datos que se colocan en su computadora o dispositivo móvil cuando visita un sitio web. Las cookies son ampliamente utilizadas por los propietarios de sitios para que sus sitios funcionen, o para trabajar de forma más eficiente, así como para proporcionar información de informes.")
    b+=h2("¿Por qué usamos Cookies?","c2")
    b+=p("Usamos cookies por varias razones: mejorar la funcionalidad del sitio, personalizar su experiencia, analizar cómo usa nuestro sitio y ofrecer publicidad relevante.")
    b+=h2("Tipos de Cookies que Usamos","c3")
    b+=p("Usamos cookies esenciales (necesarias para el funcionamiento del sitio), cookies de rendimiento (para analizar cómo usa el sitio), cookies funcionales (para recordar sus preferencias) y cookies de marketing (para mostrar anuncios relevantes).")
    b+=h2("Cómo Controlar las Cookies","c4")
    b+=p("Puede controlar y/o eliminar las cookies como desee. Puede eliminar todas las cookies que ya están en su computadora y puede configurar la mayoría de los navegadores para impedir que se coloquen.")
    b+=h2("Gestionar Preferencias","c5")
    b+=p("Puede gestionar sus preferencias de cookies en cualquier momento:")
    b+=raw(_btn("Configurar Cookies","Para gestionar las cookies, acceda a la configuración de privacidad de su navegador. Allí puede aceptar, rechazar o eliminar cookies. Si las rechaza, parte de la funcionalidad del sitio puede verse comprometida."))
    return b

def content(lang):
    b={"pt":build_pt,"en":build_en,"es":build_es}[lang]()
    return UPDATED[lang], b, _toc(lang)
